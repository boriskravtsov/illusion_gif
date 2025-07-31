# Jul-31-2025
# calc_magnitude.py

import cv2 as cv
import numpy as np

import cfg


def calc_magnitude(image):

    # Get Image Data
    # ---------------------------------------------------------
    # image = np.invert(image)    # black background

    image_height, image_width = image.shape
    # ---------------------------------------------------------

    # Copy image to array_dft (left-top corner).
    # ---------------------------------------------------------
    width_dft = cfg.size_dft
    height_dft = cfg.size_dft

    array_dft = np.zeros((height_dft, width_dft), dtype=np.float32)

    # изображение в левом верхнем углу
    x0 = 0
    y0 = 0
    array_dft[y0:y0 + image_height, x0:x0 + image_width] = image[0::, 0::]
    # ---------------------------------------------------------

    # Image DFT - Discrete Fourier Transform.
    # ---------------------------------------------------------
    dft = cv.dft(array_dft, flags=cv.DFT_COMPLEX_OUTPUT)
    # ---------------------------------------------------------

    # Shift DFT, origin DFT in center.
    # ---------------------------------------------------------
    dft_shift = np.fft.fftshift(dft)

    re_shift = dft_shift[:, :, 0]
    im_shift = dft_shift[:, :, 1]
    # -------------------------------------------------------------

    # Magnitude shift
    # -------------------------------------------------------------
    magn_shift = cv.magnitude(re_shift, im_shift)

    magn_shift_norm = np.zeros(cfg.dsize_dft, dtype=np.float32)
    cv.normalize(magn_shift, magn_shift_norm, 0, 255, cv.NORM_MINMAX)
    # -------------------------------------------------------------

    return magn_shift_norm
