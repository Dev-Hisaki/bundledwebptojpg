# WebP Image Converter

A Python utility that converts WebP images to JPG or PNG format, while preserving existing JPG/PNG files. All output is packaged into a convenient ZIP file.

## Features

- 🖼️ Convert WebP images to JPG or PNG format
- 📦 Automatic ZIP packaging of all images (converted + existing)
- 🔄 Preserves existing JPG/PNG files in the source folder
- 🎨 Colorful console interface with status indicators
- 🗂️ Organized output in dedicated export folder
- ♻️ Automatic cleanup of temporary converted files
- 🔁 Batch processing with repeat conversion option

## Requirements

- Python 3.10 or higher (uses type hints with `tuple[...]` syntax)
- Pillow (PIL) library
- colorama library

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/webp-converter.git
cd webp-converter
```

### 2. Install Dependencies

Install the required Python packages using pip:

```bash
pip install Pillow colorama
```

Or if you're using Python 3 specifically:

```bash
pip3 install Pillow colorama
```

### Using Requirements File

Create a `requirements.txt` file with:
```
Pillow>=10.0.0
colorama>=0.4.6
```

Then install:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Program

```bash
python webp_converter.py
```

Or on some systems:
```bash
python3 webp_converter.py
```

### Step-by-Step Guide

1. **Enter folder path**: Provide the path to the folder containing your images
   - You can drag and drop the folder or paste the path
   - No need to add quotes around the path

2. **Choose output format**: Select either JPG or PNG for WebP conversion
   - Type `jpg` for JPEG format
   - Type `png` for PNG format

3. **Processing**: The program will:
   - Convert all WebP files to your chosen format
   - Include existing JPG/PNG files without conversion
   - Package everything into a ZIP file
   - Clean up temporary converted files

4. **Repeat or Exit**: Choose whether to convert another folder

### Supported Image Formats

**Input formats:**
- `.webp` (will be converted)
- `.jpg`, `.jpeg` (included as-is in ZIP)
- `.png` (included as-is in ZIP)

**Output formats for WebP conversion:**
- `JPG` (JPEG format, RGB color mode)
- `PNG` (PNG format, preserves transparency)

### Example Workflow

```
Enter folder path: C:\Users\YourName\Pictures\MyWebPImages
Target image type: jpg

Processing...
Converting: image1.webp ✓
Found existing image: photo.jpg (will include in ZIP) ✓
Converting: image2.webp ✓

ZIP file created: export/MyWebPImages.zip

Convert more files? (y/n): n
```

## Output

- All ZIP files are saved in an `export` folder created in the same directory as the script
- ZIP files are named after the source folder
- The ZIP contains:
  - All converted WebP images (in JPG or PNG format)
  - All existing JPG/PNG images from the source folder
- Temporary converted files are automatically deleted after ZIP creation

## File Processing Logic

The program handles files as follows:

| File Type | Action |
|-----------|--------|
| `.webp` | Converted to JPG/PNG and added to ZIP |
| `.jpg`, `.jpeg`, `.png` | Copied directly to ZIP (no conversion) |
| Other files | Skipped with a warning message |
| Directories | Ignored |

## Color-Coded Messages

The program uses colored output for better readability:

- 🔵 **Blue**: Process start messages
- 🟢 **Green**: Successful conversions
- 🟡 **Yellow**: Warnings and information
- 🔴 **Red**: Errors
- 🟣 **Magenta**: ZIP creation success
- 🔵 **Cyan**: File discoveries and program title

## Error Handling

The program includes error handling for:
- Invalid folder paths
- Unsupported output formats
- Corrupted or unreadable image files
- File system permissions issues

## Notes

- WebP files are automatically converted to RGB mode when saving as JPG
- PNG conversion preserves transparency from WebP files
- The program clears the screen between operations for a cleaner interface
- Temporary converted files in the export folder are deleted after ZIP creation
- Original source files are never modified or deleted

## Troubleshooting

**"ModuleNotFoundError: No module named 'PIL'"**
- Install Pillow: `pip install Pillow`

**"ModuleNotFoundError: No module named 'colorama'"**
- Install colorama: `pip install colorama`

**"Folder not found. Please check the path."**
- Verify the folder path exists
- Use absolute paths or correct relative paths
- Remove any surrounding quotes from the path

**"Output format only supports JPG or PNG"**
- Enter either `jpg` or `png` (case-insensitive)
- Do not include the dot (`.`) before the format

**Python version error with type hints**
- This program requires Python 3.10 or higher
- Update Python: [python.org/downloads](https://www.python.org/downloads/)

## System Requirements

- **Operating System**: Windows, macOS, or Linux
- **Python Version**: 3.10 or higher
- **Disk Space**: Sufficient space for temporary files and ZIP output

## License

This project is open source and available under the MIT License.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.
