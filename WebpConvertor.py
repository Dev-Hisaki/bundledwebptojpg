import os
import shutil
from glob import glob
from PIL import Image
from pathlib import Path
from zipfile import ZipFile

os.system('cls' if os.name == 'nt' else 'clear')
print("<=== Webp to JPG converter by eepyneko ===>")

try:
    input_folder = input("Masukan path folder (without quotes): ")
    input_type = input("Target image type")
    folder_name = os.path.basename(input_folder)
except (TypeError, ValueError) as e:
    print(f"Error: {e}")

temp_output_folder = fr"{Path(__file__).parent}\temp"
output_zip_file = Path(input_folder).parent / f"{folder_name} - converted.zip"

os.makedirs(temp_output_folder, exist_ok=True)

for webp_file in glob(os.path.join(input_folder, "*.webp")):
    try:
        img = Image.open(webp_file)
        file_name = os.path.splitext(os.path.basename(webp_file))[0]

        # Simpan sebagai JPG
        img.save(os.path.join(temp_output_folder,
                 f"{file_name}.jpg"), "JPEG")

        # Simpan sebagai PNG
        # img.save(os.path.join(temp_output_folder, f"{file_name}.png"), "PNG")

        print(f"Berhasil mengonversi {webp_file}")
    except Exception as e:
        print(f"Gagal mengonversi {webp_file}: {e}")

with ZipFile(output_zip_file, 'w') as zipf:
    for root, dirs, files in os.walk(temp_output_folder):
        for file in files:
            file_path = os.path.join(root, file)
            zipf.write(file_path, os.path.relpath(
                file_path, temp_output_folder))

print(f"Hasil konversi disimpan dalam file ZIP: {output_zip_file}")

# Bersihkan folder sementara (opsional)
shutil.rmtree(temp_output_folder)
