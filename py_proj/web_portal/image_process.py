#coding=utf-8
from conf import *
import os
from myLog import log
from subprocess import call
from PIL import Image, ImageEnhance, ImageDraw, ImageFont



def composeStyle_0(imagePath, mainTitle, subTitle):
    log.info("Enter composeStyle_0")
    log.info("----"+imagePath)
    log.info("----"+mainTitle)
    log.info("----"+subTitle)

    text2img(mainTitle)
    res="out.png"
    return res

#Color Names
#The ImageColor module supports the following string formats:
#
#Hexadecimal color specifiers, given as #rgb or #rrggbb. For example, #ff0000 specifies pure red.
#RGB functions, given as rgb(red, green, blue) where the color values are integers in the range 0 to 255. Alternatively, the color values can be given as three percentages (0% to 100%). For example, rgb(255,0,0) and rgb(100%,0%,0%) both specify pure red.
#Hue-Saturation-Lightness (HSL) functions, given as hsl(hue, saturation%, lightness%) where hue is the color given as an angle between 0 and 360 (red=0, green=120, blue=240), saturation is a value between 0% and 100% (gray=0%, full color=100%), and lightness is a value between 0% and 100% (black=0%, normal=50%, white=100%). For example, hsl(0,100%,50%) is pure red.
#Common HTML color names. The ImageColor module provides some 140 standard color names, based on the colors supported by the X Window system and most web browsers. color names are case insensitive. For example, red and Red both specify pure red.
#

def text2img(text, font="simsun.ttc", font_color="Black", font_size=36, font_face=0):
    font = ImageFont.truetype(font, font_size, font_face)
    #多行文字处理
    text = text[:-1].split('\n')
    print text
    mark_width = 0
    for  i in range(len(text)):
        (width, height) = font.getsize(text[i])
        if mark_width < width:
            mark_width = width
    mark_height = height * len(text)

    pad = 8 
    (mark_width,mark_height) = (mark_width + pad*2, mark_height + pad*2)
    #生成水印图片
    mark = Image.new('RGBA', (mark_width,mark_height))
    draw = ImageDraw.ImageDraw(mark, "RGBA")
    draw.setfont(font)
    for i in range(len(text)):
        (width, height) = font.getsize(text[i])
        draw.text((0 + pad, i*height), text[i], fill=font_color)
    return mark


def calc_offset(im, mark, position):
    """计算偏移值"""

    try:
        if im.mode != 'RGBA':
            im = im.convert('RGBA')
        if im.size[0] < mark.size[0] or im.size[1] < mark.size[1]:
            print "The mark image size is larger size than original image file."
            return False

        #设置水印位置
        if position == 'left_top':
            x = 0
            y = 0
        elif position == 'left_bottom':
            x = 0
            y = im.size[1] - mark.size[1]
        elif position == 'right_top':
            x = im.size[0] - mark.size[0]
            y = 0
        elif position == 'right_bottom':
            x = im.size[0] - mark.size[0]
            y = im.size[1] - mark.size[1]
        else:
            x = (im.size[0] - mark.size[0]) / 2
            y = (im.size[1] - mark.size[1]) / 2
        return (x,y)
    except Exception as e:
        print ">>>>>>>>>>> WaterMark EXCEPTION:  " + str(e)
        return False


def draw_text_on_img(img, text, x, y, font="simsun.ttc", font_color="Black", font_size=36, font_face = 0):
    """在图片上加入文字"""
    font = ImageFont.truetype(font, font_size, font_face)
    #多行文字处理
    text = text[:-1].split('\n')
    print text
    mark_width = 0
    for  i in range(len(text)):
        (width, height) = font.getsize(text[i])
        if mark_width < width:
            mark_width = width
    mark_height = height * len(text)

    pad = 8 
    (mark_width,mark_height) = (mark_width + pad*2, mark_height + pad*2)
    #生成水印图片
    draw = ImageDraw.ImageDraw(img, "RGBA")
    draw.setfont(font)
    for i in range(len(text)):
        (width, height) = font.getsize(text[i])
        draw.text((0 + pad + x, i*height + y), text[i], fill=font_color)
    return img


#@font-face{font-family:"PingFang-SC";font-weight:100;src:local("PingFang SC Thin")}
#@font-face{font-family:"PingFang-SC";font-weight:300;src:local("PingFang SC Light")}
#@font-face{font-family:"PingFang-SC";font-weight:400;src:local("PingFang SC Regular")}
#@font-face{font-family:"PingFang-SC";font-weight:500;src:local("PingFang SC Medium")}
#@font-face{font-family:"PingFang-SC";font-weight:700;src:local("PingFang SC Semibold")}
#@font-face{font-family:"PingFang-SC";font-weight:800;src:local("PingFang SC Heavy")}

def composeStyle_0(imagePath, mainTitle, subTitle):
    log.info("Enter composeStyle_0")
    log.info("----"+imagePath)
    log.info("----"+mainTitle)
    log.info("----"+subTitle)

    res="out.png"

    composite(imagePath, mainTitle, res)

    return res


def composite(img_path, text, out_path, font="PingFant.ttc", font_color="white", font_size=36, font_face=0, position="center"):

    font = os.path.join(FONT_ABS_FOLDER, font)

    im = Image.open(img_path)
    mark = text2img(text, font, font_color, font_size, font_face) 

    (x,y)= calc_offset(im, mark, position)
    image = draw_text_on_img(im, text, x, y, font, font_color, font_size, font_face)

    if image:
        image.save(out_path)
        #image.show()
    else:
        log.error("Image save failed")


def main():
    P = r"C:\Users\Administrator\code_projs\PY_projs\web_portal\tmp"

    t1 = os.path.join(P, "text.txt")
    p1 = os.path.join(P, "2_0.jpg")
    f1 = os.path.join(P, "msyh.ttf")
    f2 = os.path.join(P, "PingFang.ttc")

    out = os.path.join(P, "out.png")

    text = open(t1).read().decode('utf-8')
    # print text
    im = Image.open(p1)
    mark = text2img(text, font=f2, font_color="white", font_size=36)
    #mark.show()
    (x,y)= calc_offset(im, mark, 'center')
    image = draw_text_on_img(im, text, x, y, font=f2, font_color="white", font_size=36, font_face = 0)

    if image:
        image.save(out)
        image.show()
    else:
        log.error("Image save failed")

if __name__ == '__main__':
    main()
