# Jul-31-2025
# main_arrow_in.py

import cv2 as cv
import numpy as np
from pathlib import Path

from dir_support import reset_directory
from calc_magnitude import calc_magnitude
from draw_magnitude import draw_magnitude
import cfg


"""
В папках _SPACE_DOMAIN и _FREQUENCY_DOMAIN создаются 
изображения стрелы из которых в дальнейшем будут созданы
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

    x_left  = x0 - cfg.arrow_shaft_half
    x_right = x0 + cfg.arrow_shaft_half
    # ---------------------------------------------------------

    for n in range(cfg.arrow_head):

        yl_up   = y0 - n
        yl_down = y0 + n
        xl = x_left   - n
        xr = x_right  + n

        if n == 0:
            color = cfg.maraschino
        else:
            color = cfg.white

        image[yl_up,   xl] = color
        image[yl_down, xl] = color
        image[yl_up,   xr] = color
        image[yl_down, xr] = color

    # path_image = '_SPACE_DOMAIN/image_orig.png'
    # cv.imwrite(path_image, image)

    image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    magn = calc_magnitude(image_gray)
    draw_magnitude('magn_in', magn)

    zoom_factor = cfg.size_dft / cfg.image_size
    zoomed_image = cv.resize(image,
                             None,
                             fx=zoom_factor, fy=zoom_factor,
                             interpolation=cv.INTER_NEAREST)

    path_image = '_SPACE_DOMAIN/arrow_in.png'
    cv.imwrite(path_image, zoomed_image)


if __name__ == "__main__":
    main()
