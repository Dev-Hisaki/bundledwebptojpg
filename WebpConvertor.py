import os
import shutil
from pathlib import Path
from PIL import Image
from zipfile import ZipFile
from colorama import Fore, Style, init

init(autoreset=True)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def process_files(input_path: Path, output_type: str, export_folder: Path) -> tuple[int, list[Path]]:
    count = 0
    existing_files = []

    for source_file in input_path.glob("*"):
        # Skip directories
        if source_file.is_dir():
            continue

        # Skip non-image files
        if source_file.suffix.lower() not in ['.webp', '.jpg', '.jpeg', '.png']:
            print(f"{Fore.YELLOW}Skipping non-image file: {source_file.name}")
            continue

        # Handle existing JPG/PNG files
        if source_file.suffix.lower() in ['.jpg', '.jpeg', '.png']:
            print(
                f"{Fore.CYAN}Found existing image: {source_file.name} (will include in ZIP)")
            existing_files.append(source_file)
            continue

        # Process WebP files
        try:
            print(f"{Fore.CYAN}Converting: {source_file.name}")
            img = Image.open(source_file)
            file_name = source_file.stem
            output_file = export_folder / f"{file_name}.{output_type.lower()}"

            if output_type.lower() == "jpg":
                img.convert("RGB").save(output_file, "JPEG")
            elif output_type.lower() == "png":
                img.save(output_file, "PNG")
            else:
                print(f"{Fore.RED}Unsupported output type: {output_type}")
                continue

            print(f"{Fore.GREEN}Successfully converted: {source_file.name}")
            count += 1

        except Exception as e:
            print(
                f"{Fore.RED}Failed to process {source_file.name}:\n   {Fore.YELLOW}{e}")

    return count, existing_files


def zip_output(export_folder: Path, output_zip_path: Path, existing_files: list[Path]):
    with ZipFile(output_zip_path, 'w') as zipf:
        # Add converted files
        for file in export_folder.glob("*"):
            if file.suffix.lower() in ['.jpg', '.jpeg', '.png']:
                zipf.write(file, file.name)

        # Add existing files
        for file in existing_files:
            zipf.write(file, file.name)

    print(f"{Fore.MAGENTA}\nZIP file created successfully: {output_zip_path}")


def get_user_input() -> tuple[Path, str]:
    input_folder = input(
        "Masukkan path folder (tanpa tanda kutip): ").strip('"')
    output_type = input("Target image type (JPG/PNG): ").strip().lower()
    return Path(input_folder), output_type


def main():
    script_dir = Path(__file__).parent
    export_folder = script_dir / "export"
    export_folder.mkdir(exist_ok=True)

    while True:
        clear_screen()
        print(f"{Fore.CYAN}<=== WebP to JPG/PNG Converter ===>\n")
        print(f"{Fore.YELLOW}Output will be saved to: {export_folder}\n")

        input_folder = input(
            "Enter folder path containing files (without quotes): ").strip('"')
        output_type = input(
            "Target image type for WebP files (JPG/PNG): ").strip().lower()

        input_path = Path(input_folder)

        if not input_path.exists() or not input_path.is_dir():
            print(f"{Fore.RED}Folder not found. Please check the path.")
            input("\nPress Enter to continue...")
            continue

        if output_type not in ["jpg", "png"]:
            print(f"{Fore.RED}Output format only supports JPG or PNG.")
            input("\nPress Enter to continue...")
            continue

        folder_name = input_path.name
        output_zip_file = export_folder / f"{folder_name}.zip"

        print(f"\n{Fore.BLUE}Starting file processing...\n")
        total_converted, existing_files = process_files(
            input_path, output_type, export_folder)

        if total_converted > 0 or existing_files:
            zip_output(export_folder, output_zip_file, existing_files)
        else:
            print(f"{Fore.YELLOW}⚠️ No convertible image files found.")

        # Clean up converted files (leave existing files untouched)
        for file in export_folder.glob(f"*.{output_type.lower()}"):
            file.unlink()
        print(f"{Fore.YELLOW}Converted files deleted from the export folder.")

        repeat = input(
            f"\n{Style.BRIGHT}Convert more files? (y/n): ").strip().lower()
        if repeat != 'y':
            break

    print(f"\n{Fore.BLUE}👋 Conversion complete. Thank you for using this converter!")
    print(f"Export folder: {Fore.CYAN}{export_folder}{Style.RESET_ALL}\n")


if __name__ == "__main__":
    main()
