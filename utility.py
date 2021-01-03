import os
from pathlib import Path
path = "./dataset/"
def rename(folder_name):
	folder_list = []
	new_path = Path(path + folder_name)
	for image_folder in new_path.glob("*"):
		for folder in (image_folder).glob("*.jpg"):
			new_image_name = "dataset\\" + folder_name + "\\" + (str(image_folder)).split("\\")[-1] + "\\" + (str(image_folder)).split("\\")[-1] + " " + str(folder).split("\\")[-1]
			os.rename(folder, new_image_name)

if __name__ == '__main__':
	dirs = ["training", "validation"]
	for folder in dirs:
		rename(folder)
