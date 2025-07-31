# Jul-31-2025
# main_distance.py

import cv2 as cv
import numpy as np
from pathlib import Path

from dir_support import reset_directory
from calc_magnitude import calc_magnitude
from draw_magnitude import draw_magnitude
import cfg


"""
В папках _SPACE_DOMAIN и _FREQUENCY_DOMAIN создаются 
изображения из которых в дальнейшем будут созданы
кадры GIF-анимации.
"""

def main():

    # Init
    # ---------------------------------------------------------
    dir_space = Path.cwd() / '_SPACE_DOMAIN'
    dir_freq = Path.cwd() / '_FREQUENCY_DOMAIN'
    reset_directory(dir_space)
    reset_directory(dir_freq)
    # ---------------------------------------------------------

    # ---------------------------------------------------------
    shape = (cfg.height_image, cfg.width_image, 3)
    image = np.zeros(shape, dtype=np.uint8)

    x0 = cfg.width_image // 2
    y0 = cfg.height_image // 2

    x_left  = x0 - 11
    x_right = x0 + 11
    # ---------------------------------------------------------

    for n in range(3):

        image.fill(0)

        xl = x_left  + 3 * n
        xr = x_right - 3 * n

        image[y0, xl] = cfg.maraschino
        image[y0, xr] = cfg.maraschino

        # path_image = '_SPACE_DOMAIN/image_orig_' + str(n) + '.png'
        # cv.imwrite(path_image, image)

        image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        magn = calc_magnitude(image_gray)
        draw_magnitude('freq_' + str(n), magn)

        zoom_factor = cfg.size_dft / cfg.image_size
        zoomed_image = cv.resize(image,
                                 None,
                                 fx=zoom_factor, fy=zoom_factor,
                                 interpolation=cv.INTER_NEAREST)

        path_image = '_SPACE_DOMAIN/image_' + str(n) + '.png'
        cv.imwrite(path_image, zoomed_image)



if __name__ == "__main__":
    main()
