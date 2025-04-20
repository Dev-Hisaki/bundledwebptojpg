import os
import shutil
from pathlib import Path
from PIL import Image
from zipfile import ZipFile
from colorama import Fore, Style, init

init(autoreset=True)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def is_supported_format(fmt: str) -> bool:
    return fmt.lower() in ["jpg", "png"]


def create_temp_folder(temp_folder: Path):
    if temp_folder.exists():
        shutil.rmtree(temp_folder)
    temp_folder.mkdir(exist_ok=True)


def convert_images(input_path: Path, output_type: str, temp_folder: Path) -> int:
    count = 0
    for webp_file in input_path.glob("*.webp"):
        print(f"{Fore.CYAN}🔍 Mencari: {webp_file.name}")
        try:
            img = Image.open(webp_file)
            file_name = webp_file.stem
            output_file = temp_folder / f"{file_name}.{output_type}"

            if output_type == "jpg":
                img.convert("RGB").save(output_file, "JPEG")
            else:  # png
                img.save(output_file, "PNG")

            print(f"{Fore.GREEN}Berhasil mengonversi: {webp_file.name}")
            count += 1

        except Exception as e:
            print(
                f"{Fore.RED}Gagal mengonversi {webp_file.name}:\n   {Fore.YELLOW}{e}")
    return count


def zip_output(temp_folder: Path, output_zip_path: Path, original_folder: Path):
    with ZipFile(output_zip_path, 'w') as zipf:
        # File hasil konversi
        for file in temp_folder.glob("*"):
            zipf.write(file, file.name)
        # File asli selain .webp
        for file in original_folder.glob("*"):
            if file.suffix.lower() != ".webp":
                zipf.write(file, file.name)
    print(f"{Fore.MAGENTA}\nFile ZIP berhasil dibuat: {output_zip_path}")


def get_user_input() -> tuple[Path, str]:
    input_folder = input(
        "Masukkan path folder (tanpa tanda kutip): ").strip('"')
    output_type = input("Target image type (JPG/PNG): ").strip().lower()
    return Path(input_folder), output_type


def main():
    while True:
        clear_screen()
        print(
            f"{Fore.CYAN}<=== WebP to JPG/PNG Converter by eepyneko feat. ChatGPT ===>\n")

        input_path, output_type = get_user_input()

        if not input_path.exists() or not input_path.is_dir():
            print(f"{Fore.RED}Folder tidak ditemukan. Pastikan path benar.")
            input("\nTekan Enter untuk melanjutkan...")
            continue

        if not is_supported_format(output_type):
            print(f"{Fore.RED}Format output hanya mendukung JPG atau PNG.")
            input("\nTekan Enter untuk melanjutkan...")
            continue

        folder_name = input_path.name
        temp_output_folder = Path(__file__).parent / "temp"
        output_zip_file = input_path.parent / f"{folder_name} - converted.zip"

        create_temp_folder(temp_output_folder)

        print(f"\n{Fore.BLUE}Memulai proses konversi file .webp...\n")
        total_converted = convert_images(
            input_path, output_type, temp_output_folder)

        if total_converted > 0:
            zip_output(temp_output_folder, output_zip_file, input_path)
        else:
            print(f"{Fore.YELLOW}⚠️  Tidak ada file .webp yang berhasil dikonversi.")

        shutil.rmtree(temp_output_folder)

        ulang = input(
            f"\n{Style.BRIGHT}Ulang program? (y/n): ").strip().lower()
        if ulang != 'y':
            break

    print(
        f"\n{Fore.BLUE}👋 Program selesai. Terima kasih telah menggunakan converter ini!\n")


if __name__ == "__main__":
    main()
