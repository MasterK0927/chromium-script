import os
import glob

from PIL import Image
from config import sizes

CHROMIUM_PATH_TWO = "/home/keshav/broswer/src/brave/app/theme/brave/android/res_brave_base"
CHROMIUM_PATH_THREE = "/home/keshav/broswer/src/brave/app/theme/brave/android/res_brave_beta_base"
CHROMIUM_PATH_FOUR = "/home/keshav/broswer/src/brave/app/theme/brave/android/res_brave_default_base"
CHROMIUM_PATH_ONE = "/home/keshav/broswer/src/brave/app/theme/brave/android/res_brave_nightly_base"
BROWSER_NAME = "Ping Browser"
EXTENSIONS = ['grd', 'grdp']

def replace_file_with_text(name, str_a, str_b):
    txt = ""
    with open(name, "r", encoding="utf8") as f:
        txt = f.read()
        txt = txt.replace(str_a, str_b)
    with open(name, "w", encoding="utf8") as f:
        f.write(txt)

if not os.path.isdir('out'):
    os.mkdir('out')

image = Image.open('LOGO-removebg-preview.png')

for size in sizes:
    temp = image.copy()
    temp.thumbnail((size['res'],size['res']))
    temp.save(f"out/{size['name']}")
    source_path = f"{os.getcwd()}/out/{size['name']}"
    source_path_two = f"{os.getcwd()}/out2/{size['name']}"
    source_path_three = f"{os.getcwd()}/out3/{size['name']}"
    source_path_four = f"{os.getcwd()}/out4/{size['name']}"
    
    destination_path = f"{CHROMIUM_PATH_ONE}/{size['parent']}/{size['name']}"
    destination_path_two = f"{CHROMIUM_PATH_TWO}/{size['parent']}/{size['name']}"
    destination_path_three = f"{CHROMIUM_PATH_THREE}/{size['parent']}/{size['name']}"
    destination_path_four = f"{CHROMIUM_PATH_FOUR}/{size['parent']}/{size['name']}"
    try:
        os.replace(source_path, destination_path)
        os.replace(source_path_two, destination_path_two)
        os.replace(source_path_three, destination_path_three)
        os.replace(source_path_four, destination_path_four)
        print("File moved successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

for ext in EXTENSIONS:
    for name in glob.glob(f"{CHROMIUM_PATH_ONE}/src/chrome/app/*.{ext}"):
        replace_file_with_text(name, "Chromium", BROWSER_NAME)
    
    for name in glob.glob(f"{CHROMIUM_PATH_ONE}/src/components/*.{ext}"):
        replace_file_with_text(name, "Chromium", BROWSER_NAME)

