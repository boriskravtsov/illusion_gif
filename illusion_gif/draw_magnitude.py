# Jul-31-2025
# draw_magnitude.py

import sys
import os
import cv2 as cv
import cfg


def draw_magnitude(tag, magnitude):

    # Save Magnitude in file as grayscale.
    # ---------------------------------------------------------
    magnitude_gray_path = '_FREQUENCY_DOMAIN/' + tag + '_gray.png'
    result = cv.imwrite(magnitude_gray_path, magnitude)

    if not result:
        print('Magnitude is not saved')
        sys.exit(1)
    # ---------------------------------------------------------

    # Convert Magnitude to ColorMap.
    # ---------------------------------------------------------
    if os.path.exists(magnitude_gray_path):

        magnitude_gray = cv.imread(magnitude_gray_path, cv.IMREAD_GRAYSCALE)

        os.remove(magnitude_gray_path)

        if cfg.colormap == 'HOT':
            magnitude_color_path = '_FREQUENCY_DOMAIN/' + tag + '.png'
            magnitude_color = cv.applyColorMap(magnitude_gray, cv.COLORMAP_HOT)

            # Set 1-pixel border to black
            magnitude_color[0, :, :] = 0  # top row
            magnitude_color[-1, :, :] = 0  # bottom row
            magnitude_color[:, 0, :] = 0  # left column
            magnitude_color[:, -1, :] = 0  # right column

            cv.imwrite(magnitude_color_path, magnitude_color)

        if cfg.colormap == 'HSV':
            magnitude_color_path = '_FREQUENCY_DOMAIN/' + tag + '.png'
            magnitude_color = cv.applyColorMap(magnitude_gray, cv.COLORMAP_HSV)

            # Set 1-pixel border to black
            magnitude_color[0, :, :] = 0  # top row
            magnitude_color[-1, :, :] = 0  # bottom row
            magnitude_color[:, 0, :] = 0  # left column
            magnitude_color[:, -1, :] = 0  # right column

            cv.imwrite(magnitude_color_path, magnitude_color)

        if cfg.colormap == 'JET':
            magnitude_color_path = '_FREQUENCY_DOMAIN/' + tag + '.png'
            magnitude_color = cv.applyColorMap(magnitude_gray, cv.COLORMAP_JET)

            # Set 1-pixel border to black
            magnitude_color[0, :, :] = 0  # top row
            magnitude_color[-1, :, :] = 0  # bottom row
            magnitude_color[:, 0, :] = 0  # left column
            magnitude_color[:, -1, :] = 0  # right column

            cv.imwrite(magnitude_color_path, magnitude_color)
    else:
        print("draw_magnitude(): The file does not exist")
        sys.exit(1)
    # ---------------------------------------------------------
