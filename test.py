import os
from pathlib import Path

os.system('cls' if os.name == 'nt' else 'clear')

print("<=== Webp to JPG converter by eepyneko ===>")

try:
    # Input path
    inputFolder = Path(__file__).parent
    print(f"Path: {inputFolder}")
except:
    print("Failed")
finally:
    print("Done")
