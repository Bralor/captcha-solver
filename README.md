### Captcha solver

---

Library for the captcha image generation and recognition.

<br>

#### Installation

---

Run command:
```
$ pip install -e .
```

<br>

#### Image generation

---

First thing first, you need to generate content of captcha image.

You can create a single string:
```
>>> from src.content_creator import CaptchaContentGenerator as ccg
>>> single = ccg(length=5, samples=1, numbers=True, lowercase=True, uppercase=True)
>>> single
1aD3x
```
... or a batch:
```
>>> from src.content_creator import CaptchaContentGenerator as ccg
>>> samples = ccg(length=5, samples=4, numbers=True, lowercase=True, uppercase=True)
>>> samples
XpXJs, 3YUFp, FyNmg, xqujI
```

... then you can generate **PNG** files:
```
>>> from src.captcha_generator import DatasetGenerator as dg
>>> images = dg(x=180, y=50, content=samples)

INFO: Setting up the resolution (180x50),
INFO: do not forget to specify argument FOLDER,

>>> images.folder = "images"

INFO: Creating the output folder 'images',

>>> image.create_images()

INFO: Images have been saved into the folder 'images'.
```

<br>

#### Project layout

---

```
/captcha
  ├─README.md
  ├─requirements.txt
  └─csolver
     ├─generator.py
     ├─solver.py
     ├─tests/
     └─data/
```

<br>

