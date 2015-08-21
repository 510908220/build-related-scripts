# -*- coding: utf-8 -*-

import os
from PIL import Image

import config
game_dir = os.path.join(config.STRIFE_DIR, "game")
game_ui_dir = os.path.join(game_dir, "ui")
atlas_file = os.path.join(game_ui_dir, "elements.atlas")

total_size = 0


def is_image_size_nice(image_path):
	img = Image.open(image_path)
	w, h = img.size
	global total_size
	if w <= 64 and h <= 64:
		total_size += w * h
		return True
	return False


def get_images(dir_path):
	fit_images = []
	for parent, dir_names, file_names in os.walk(dir_path):
		for file_name in file_names:
			file_path = os.path.join(parent, file_name)
			if 'generated_files' not in file_path and ".tga" in file_path and is_image_size_nice(file_path):
				file_path = file_path.replace(game_dir, "")
				file_path = file_path.replace("\\", "/")
				fit_images.append(file_path)
	return fit_images


def get_atlas_size():
	width = 1024
	height = total_size / width

	mod = height % 1024

	if mod > 0:
		height = height - mod + 1024
	return width, height * 2


def main():
	images = get_images(game_ui_dir)
	header = '''<atlas maxwidth="{width}" maxheight="{height}">\n'''.format(width=get_atlas_size()[0],
	                                                                        height=get_atlas_size()[1])
	body = ""
	for image in images:
		texture = '''<texture name="{name}" path="{path}" requiredmips="1" padding="10"/>'''.format(name=image,
		                                                                                           path=image)
		body += (texture + "\n")
	footer = "</atlas>"

	with open(atlas_file, "w") as f:
		f.write(header + body + footer)


if __name__ == "__main__":
	main()
