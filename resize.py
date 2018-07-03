__author__ = 'Jacob Zhou'

from PIL import Image
import os
from scan_photo import getFileName


def save_image(image):
	if(os.path.isdir('result') == 0):
		os.mkdir('result')
		image.save('./result/Pic' + '.png', 'PNG')


if __name__ == '__main__':
    path = '.\\'
    file_path = str(path) + '\\' + str(getFileName(path))
    image = Image.open(file_path)
    image = image.resize((480,360))
    save_image(image)
