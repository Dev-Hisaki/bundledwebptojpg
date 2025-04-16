import os
import shutil
from pathlib import Path
from PIL import Image
from zipfile import ZipFile
from colorama import Fore, Style, init

init(autoreset=True)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def convert_images(input_path: Path, output_type: str, temp_folder: Path) -> int:
    count = 0
    for webp_file in input_path.glob("*.webp"):
        print(f"{Fore.CYAN}🔍 Mencari: {webp_file.name}")
        try:
            img = Image.open(webp_file)
            file_name = webp_file.stem
            output_file = temp_folder / f"{file_name}.{output_type.lower()}"

            if output_type == "jpg":
                img.convert("RGB").save(output_file, "JPEG")
            elif output_type == "png":
                img.save(output_file, "PNG")
            else:
                print(f"{Fore.RED}Tipe gambar tidak didukung: {output_type}")
                continue

            print(f"{Fore.GREEN}Berhasil mengonversi: {webp_file.name}")
            count += 1

        except Exception as e:
            print(
                f"{Fore.RED}Gagal mengonversi {webp_file.name}:\n   {Fore.YELLOW}{e}")
    return count


def zip_output(temp_folder: Path, output_zip_path: Path):
    with ZipFile(output_zip_path, 'w') as zipf:
        for file in temp_folder.glob("*"):
            zipf.write(file, file.name)
    print(f"{Fore.MAGENTA}\nFile ZIP berhasil dibuat: {output_zip_path}")


def main():
    while True:
        clear_screen()
        print(
            f"{Fore.CYAN}<=== WebP to JPG/PNG Converter by eepyneko feat. ChatGPT ===>\n")

        input_folder = input(
            "Masukkan path folder (tanpa tanda kutip): ").strip('"')
        output_type = input("Target image type (JPG/PNG): ").strip().lower()

        input_path = Path(input_folder)

        if not input_path.exists() or not input_path.is_dir():
            print(f"{Fore.RED}Folder tidak ditemukan. Pastikan path benar.")
            input("\nTekan Enter untuk melanjutkan...")
            continue

        if output_type not in ["jpg", "png"]:
            print(f"{Fore.RED}Format output hanya mendukung JPG atau PNG.")
            input("\nTekan Enter untuk melanjutkan...")
            continue

        folder_name = input_path.name
        temp_output_folder = Path(__file__).parent / "temp"
        output_zip_file = input_path.parent / f"{folder_name} - converted.zip"

        if temp_output_folder.exists():
            shutil.rmtree(temp_output_folder)
        temp_output_folder.mkdir(exist_ok=True)

        print(f"\n{Fore.BLUE}Memulai proses konversi file .webp...\n")
        total_converted = convert_images(
            input_path, output_type, temp_output_folder)

        if total_converted > 0:
            zip_output(temp_output_folder, output_zip_file)
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
