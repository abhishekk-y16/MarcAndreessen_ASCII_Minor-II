import cv2
import os
import numpy as np


def load_image(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Image not found: {path}")
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError(f"Unable to load image (unsupported format?): {path}")
    return img


def scale_image(img, new_width):
    # `img` is a numpy 2D array (grayscale)
    h, w = img.shape
    aspect_ratio = h / w
    new_height = max(1, int(aspect_ratio * new_width * 0.55))
    resized = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)
    return resized


def map_pixels_to_ascii(img, charset, invert=False):
    # `img` expected to be a 2D numpy array (grayscale)
    charset_list = list(charset)
    if invert:
        charset_list = charset_list[::-1]
    n = len(charset_list)
    # normalize pixels to indices in charset
    indices = (img.astype(np.float32) / 255.0 * (n - 1)).astype(int)
    lines = ["".join(charset_list[idx] for idx in row) for row in indices]
    return lines


def image_to_ascii(path, width=100, charset=None, invert=False):
    if charset is None:
        charset = "@#%*+=-:. "
    img = load_image(path)
    img = scale_image(img, width)
    lines = map_pixels_to_ascii(img, charset, invert=invert)
    return lines


def save_ascii(lines, out_path):
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
