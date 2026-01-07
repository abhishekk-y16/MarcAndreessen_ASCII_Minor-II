import argparse
import time
import sys
import os
from utils import image_to_ascii, save_ascii

try:
    from colorama import init, Fore, Style
    init()
    COLORAMA_AVAILABLE = True
except Exception:
    COLORAMA_AVAILABLE = False


CHARSET_PRESETS = {
    "default": "@#%*+=-:. ",
    "detailed": "@#%$&8WMBD0QXYmwqpdbkhao*+;:,. ",
    "simple": "@#%.*: "
}


def render_ascii(lines, animate=False, speed=0.002, colorize=False):
    if colorize and not COLORAMA_AVAILABLE:
        print("colorama not installed; continuing without color.")
        colorize = False

    if not animate:
        for L in lines:
            print(L)
        return

    # Animate by printing lines with a small delay.
    delay = max(0.0, float(speed))
    for line in lines:
        if colorize:
            # a very simple color gradient based on character density
            print(Fore.GREEN + line + Style.RESET_ALL)
        else:
            print(line)
        sys.stdout.flush()
        time.sleep(delay)


def choose_charset(name_or_chars):
    if name_or_chars in CHARSET_PRESETS:
        return CHARSET_PRESETS[name_or_chars]
    if len(name_or_chars) >= 2:
        return name_or_chars
    return CHARSET_PRESETS["default"]


def main():
    p = argparse.ArgumentParser(description="Convert an image to American Standard Code for Information Interchange art (Marc Andreessen Edition)")
    p.add_argument("--image", "-i", help="Path to input image (e.g., assets/Marc.png)")
    p.add_argument("--width", "-w", type=int, default=100, help="Output Width in Characters")
    p.add_argument("--charset", "-c", default="default", help="Charset preset name or custom string")
    p.add_argument("--animate", action="store_true", help="Animate rendering line-by-line")
    p.add_argument("--speed", type=float, default=0.002, help="Delay (seconds) between lines when animating")
    p.add_argument("--save", "-s", help="Save final ASCII art to a text file (path)")
    p.add_argument("--color", action="store_true", help="Colorize output if colorama is available")
    p.add_argument("--invert", action="store_true", help="Invert shading mapping")

    args = p.parse_args()

    if not args.image:
        args.image = input("Path to image (relative to project): ").strip()

    if not os.path.exists(args.image):
        print(f"Image not found: {args.image}")
        return

    charset = choose_charset(args.charset)
    lines = image_to_ascii(args.image, width=args.width, charset=charset, invert=args.invert)

    render_ascii(lines, animate=args.animate, speed=args.speed, colorize=args.color)

    if args.save:
        save_ascii(lines, args.save)
        print(f"Saved ASCII art to {args.save}")


if __name__ == "__main__":
    main()
