# Jul-31-2025
# main_frames.py

import os
import cv2 as cv
import numpy as np
from pathlib import Path

import cfg
from dir_support import reset_directory


"""
Изображения из папок _SPACE_DOMAIN и _FREQUENCY_DOMAIN 
используются для формирования объединенного изображения 
в папке _FRAMES. Эти объединенные изображения являются 
кадрами будущей GIF-анимации.
"""


def print_list(tag, any_list):
    print(f'\n{tag}')
    n = 0
    for item in any_list:
        print(f'{n}:\t {item}')
        n += 1


def main():

    # Init
    # ---------------------------------------------------------
    dir_space = Path.cwd() / '_SPACE_DOMAIN'
    dir_freq = Path.cwd() / '_FREQUENCY_DOMAIN'
    dir_frames = Path.cwd() / '_FRAMES'

    reset_directory(dir_frames)
    # ---------------------------------------------------------

    # ---------------------------------------------------------
    file_list_space = [f for f in os.listdir(dir_space) if os.path.isfile(os.path.join(dir_space, f))]
    file_list_space.sort()
    print_list('space', file_list_space)

    file_list_freq = [f for f in os.listdir(dir_freq) if os.path.isfile(os.path.join(dir_freq, f))]
    file_list_freq.sort()
    print_list('freq', file_list_freq)
    # ---------------------------------------------------------

    n_frames = len(file_list_space)

    for n in range(n_frames):
        image_space_name = dir_space / file_list_space[n]
        image_space = cv.imread(str(image_space_name))

        image_freq_name = dir_freq / file_list_freq[n]
        image_freq = cv.imread(str(image_freq_name))

        width = cfg.size_dft * 2 + cfg.space
        height = cfg.size_dft
        image_frame = np.zeros((height, width, 3), dtype=np.uint8)
        image_frame.fill(255)

        image_frame[:, 0:cfg.size_dft] = image_space
        image_frame[:, cfg.size_dft + cfg.space:2 * cfg.size_dft + cfg.space] = image_freq

        path_frame = dir_frames / str('frame_' + str(n) + '.png')
        cv.imwrite(str(path_frame), image_frame)


if __name__ == "__main__":
    main()
