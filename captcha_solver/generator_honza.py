import random
import uuid
import json
import string
import os
import shutil
import itertools

import random
from PIL import Image
from PIL import ImageFilter
from PIL.ImageDraw import Draw
from PIL.ImageFont import truetype

# pip install captcha - https://github.com/lepture/captcha
from captcha.image import ImageCaptcha

DATA_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data')
DEFAULT_FONTS = [os.path.join(DATA_DIR, 'DroidSansMono.ttf')]

print(DEFAULT_FONTS)

table =  []
for i in range( 256 ):
    table.append( i * 1.97 )

class MyImageCaptcha(ImageCaptcha):

    @staticmethod
    def create_noise_curve(image, color):
        w, h = image.size
        x1 = random.randint(0, int(w / 5))
        x2 = random.randint(w - int(w / 5), w)
        y1 = random.randint(int(h / 5), h - int(h / 5))
        y2 = random.randint(y1, h - int(h / 5))
        points = [x1, y1, x2, y2]
        end = random.randint(160, 200)
        start = random.randint(0, 20)
        Draw(image).arc(points, start, end, fill=color)
        return image

    @staticmethod
    def create_noise_dots(image, color, width=3, number=50):
        draw = Draw(image)
        w, h = image.size
        while number:
            x1 = random.randint(0, w)
            y1 = random.randint(0, h)
            draw.line(((x1, y1), (x1 - 1, y1 - 1)), fill=color, width=width)
            number -= 1
        return image

    def create_captcha_image(self, chars, color, background):
        image = Image.new('RGB', (self._width, self._height), background)
        draw = Draw(image)

        def _draw_character(c):
            font = random.choice(self.truefonts)
            w, h = draw.textsize(c, font=font)

            dx = random.randint(2, 4)
            dy = random.randint(2, 6)
            im = Image.new('RGBA', (w + dx, h + dy))
            Draw(im).text((dx, dy), c, font=font, fill=color)

            # rotate
            im = im.crop(im.getbbox())
            im = im.rotate(random.uniform(-30, 30), Image.BILINEAR, expand=1)

            # warp
            dx = w * random.uniform(0.1, 0.3)
            dy = h * random.uniform(0.2, 0.3)
            x1 = int(random.uniform(-dx, dx))
            y1 = int(random.uniform(-dy, dy))
            x2 = int(random.uniform(-dx, dx))
            y2 = int(random.uniform(-dy, dy))
            w2 = w + abs(x1) + abs(x2)
            h2 = h + abs(y1) + abs(y2)
            data = (
                x1, y1,
                -x1, h2 - y2,
                w2 + x2, h2 + y2,
                w2 - x2, -y1,
            )
            # im = im.resize((w2, h2))
            # im = im.transform((w, h), Image.QUAD, data)
            return im

        images = []
        for c in chars:
            if random.random() > 0.5:
                images.append(_draw_character(" "))
            images.append(_draw_character(c))

        text_width = sum([im.size[0] for im in images])

        width = max(text_width, self._width)
        image = image.resize((width, self._height))

        average = int(text_width / len(chars))
        rand = int(0.25 * average)
        offset = int(average * 0.1)

        for im in images:
            w, h = im.size
            mask = im.convert('L').point(table)
            image.paste(im, (offset, int((self._height - h) / 2)), mask)
            offset = offset + w + random.randint(-rand, 0)

        if width > self._width:
            image = image.resize((self._width, self._height))

        return image


    def generate_image(self, chars):
        background = (255, 255, 255)
        color = (128, 128, 128)

        im = self.create_captcha_image(chars, color, background)
        self.create_noise_dots(im, color)
        self.create_noise_curve(im, color)
        # im = im.filter(ImageFilter.SMOOTH)
        return im

def random_color(start, end, opacity=None):
    red = random.randint(start, end)
    green = random.randint(start, end)
    blue = random.randint(start, end)
    if opacity is None:
        return (red, green, blue)
    return (red, green, blue, opacity)


def get_choices():
    choices = [
        (True, map(str, range(5))),
        (False, string.ascii_lowercase),
        (False, string.ascii_uppercase),
        ]
    return tuple([i for is_selected, subset in choices for i in subset if is_selected])

def _generate_captcha(img_dir, num_per_image, n, width, height, choices):

    # if os.path.exists(img_dir):
    #     shutil.rmtree(img_dir)

    image = MyImageCaptcha(width=width, height=height)

    print('generating %s epoches of captchas in %s' % (n, img_dir))
    for _ in range(n):
        for i in itertools.permutations(choices, num_per_image):

            captcha = ''.join(i)
            # if not os.path.exists(img_dir + '/' + captcha):
            #     os.makedirs(img_dir + '/' + captcha)
            # fn = os.path.join(img_dir, '%s/%s.png' % (captcha, uuid.uuid4()))
            fn = os.path.join(img_dir, '%s_%s.png' % (captcha, uuid.uuid4()))
            image.write(captcha, fn)

        if n < 20:
            print('A epoche finished')

def generate_dataset():

    choices = get_choices()

    width = 180
    height = 50
    num_per_image = 5
    n_epoch = 1

    # meta info
    meta = {
        'num_per_image': num_per_image,
        'label_size': len(choices),
        'label_choices': ''.join(choices),
        'n_epoch': n_epoch,
        'width': width,
        'height': height,
    }


    _generate_captcha('test', num_per_image, n_epoch, width, height, choices=choices)


class CaptchaContentGenerator:
    """
    Generate captcha characters from the number, lowercase and uppercase
    letters.
    """

    def __init__(self, numbers: bool, lowercase: bool, uppercase: bool):
        self.numbers = numbers
        self.lowercase = lowercase
        self.uppercase = uppercase

    def collect_numbers(self) -> str:
        """
        Return a string of all numbers.

        :return: the string of numbers.
        :rtype: str

        :Example:
        >>> numbers = CaptchaContentGenerator.collect_numbers()
        >>> numbers
        '0123456789'
        """
        return string.digits if self.numbers else ""

    def collect_lowercase(self) -> str:
        """
        Return a string of all lowercase letters.

        :return: the string of lowercase letters.
        :rtype: str

        :Example:
        >>> lowercases = CaptchaContentGenerator.collect_lowercase()
        >>> lowercases
        'abcdefghijklmnopqrstuvwxyz'
        """
        return string.ascii_lowercase if self.lowercase else ""

    def collect_uppercase(self) -> str:
        """
        Return a string of all uppercase letters.

        :return: the string of uppercase letters.
        :rtype: str

        :Example:
        >>> uppercases = CaptchaContentGenerator.collect_uppercase()
        >>> uppercases
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        """
        return string.ascii_uppercase if self.uppercase else ""

    def create_content(self):
        """
        Return a string of 5 characters from the given numbers, lowercase
        and uppercase letters.

        :return: the string of 5 characters
        :rtype: str

        :Example:
        >>> content = CaptchaContentGenerator.create_content()
        >>> content
        '1a3Bp'
        """
        chars_collection: str = "".join(
            (
                self.collect_numbers(),
                self.collect_lowercase(),
                self.collect_uppercase()
            )
        )

        return "".join(random.choices(chars_collection, k=5))


if __name__ == '__main__':
    generate_dataset()
