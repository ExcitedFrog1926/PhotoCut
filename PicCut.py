from PIL import Image
import os
from scan_photo import getFileName
#将图片填充为正方形
def fill_image(image):
    width,height = image.size
    #选取长和宽中较大值作为新图片的边长
    new_image_length = width if width > height else height
    #生成新白底图片
    new_image = Image.new(image.mode,(new_image_length,new_image_length),color="white")
    #原图居中贴在新图上
    if width > height :
         new_image.paste(image,(0,int((new_image_length - height) / 2)))
    else:
         new_image.paste(image,(int((new_image_length - width) / 2),0))
    return new_image
#切图
def cut_image(image):
    width,height = image.size
    item_width = int(width / 3)
    box_list = []
    for i in range(0,3):
        for j in range(0,3):
            box = (j * item_width,i * item_width,(j + 1) * item_width,(i + 1) * item_width)
            box_list.append(box)
    image_list = [image.crop(box)for box in box_list]
    return image_list
#保存
def save_images(image_list):
    index = 1
    #检查目标文件是否存在
    if(os.path.isdir('result') == 0):
        os.mkdir('result')
    #输出文件，并在控制台显示进度
    for image in image_list:
        image.save('./result/Pic' + str(index) + '.png','PNG')
        print(str(index * 10) + '% done')
        index += 1

if __name__ == '__main__':
    path= '.\\'
    file_path = str(path) + '\\' + str(getFileName(path))
    image = Image.open(file_path)
    image = fill_image(image)
    image_list = cut_image(image)
    save_images(image_list)
    print('100% done')