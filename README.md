# MarcAndreessen ASCII Image

Turn any photo into stylized American Standard Code for Information Interchange art — with animation, color, and custom character palettes.

## Overview

- Convert a portrait or photo into American Standard Code for Information Interchange art using a small, configurable CLI.
- Supports charset presets, custom charsets, animated rendering, and saving output.

## How it works

- Loads an Image with OpenCV, converts to Grayscale, scales to a user-specified width, maps pixel brightness to characters from a charset, and prints/saves the resulting lines.

## Quick start

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Put your image in the `assets/` folder (example: `assets/Marc.png`).

3. Run the converter:

```bash
python marc_ascii.py --image assets/Marc.png --width 120 --animate --speed 0.003 --save output/marc_ascii.txt
```

## Options

- `--image` / `-i`: Path to input image
- `--width` / `-w`: Output width in characters (default: 100)
- `--charset` / `-c`: Preset name (`default`, `detailed`, `simple`) or a custom charset string
- `--animate`: Print lines with a delay for progressive reveal
- `--speed`: Delay in seconds between lines when animating
- `--save` / `-s`: Save the result to a text file (e.g., `output/marc_ascii.txt`)
- `--color`: Colorize output (requires `colorama`)
- `--invert`: Flip dark/light mapping

## Notes

- The project uses OpenCV (`opencv-python`) to load and scale images (grayscale). The implementation previously mentioned Pillow; OpenCV is used here.
- Filenames on Windows are case-insensitive, but examples use `assets/Marc.png` — adjust to your actual filename.

## Tips

- Try wider widths for more detail, smaller widths for a bolder, blocky look.
- Use `--charset` with custom strings to create a unique style (list characters from darkest  lightest).

## Contributing

- Open an issue or PR to suggest new features (presets, progressive reveal modes, terminal auto-detection).

## Credits

- Simple personal project inspired by American Standard Code for Information Interchange portrait experiments.

## License

- MIT-style (add your own if desired).
