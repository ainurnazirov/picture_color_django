from django.shortcuts import render
from .forms import ImageForm
import os
from PIL import Image, ImageColor
from picture_color_django.settings import MEDIA_ROOT


def number_total(image, color):
    white = 0
    black = 0
    count = 0
    for pixel in image.getdata():
        if pixel == (0, 0, 0):
            black += 1
        elif pixel == (255, 255, 255):
            white += 1
        elif pixel[:-1] == color:
            count += 1
    return white, black, count


def number(image):
    white = 0
    black = 0
    for pixel in image.getdata():
        if pixel == (0, 0, 0):
            black += 1
        elif pixel == (255, 255, 255):
            white += 1
    return white, black


def check_colors(img, color):
    img = str(img)[13:]
    image = Image.open(os.path.join(MEDIA_ROOT) + img, 'r')
    print(type(color))
    # if not color.startswith('#'):
    #     color = '#' + color
    print(color)
    color = ImageColor.getcolor(color, "RGB")
    print(image.getpixel((25, 45))[:-1])
    print(type(image.getpixel((25, 45))))
    print(color)
    print(color)

    if (0, 0, 0) != color:
        if (255, 255, 255) != color:
            white, black, count = number_total(image, color)
        else:
            white, black = number(image)
            count = white
    else:
        white, black = number(image)
        count = black

    return white, black, count


def index(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            w, b, c = check_colors(img_obj.image.url, img_obj.color)
            return render(request, 'picture_color\index.html',
                          {'form': form, 'img_obj': img_obj, 'w': w, 'b': b, 'c': c})
    else:
        form = ImageForm()
    return render(request, 'picture_color\index.html', {'form': form})
