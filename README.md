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

First thing first, you need to generate content of captcha image:
```
$ python
>>> from captcha_solver.generator_honza import CaptchaContentGenerator as ccg
>>> sample_1 = ccg(length=5, numbers=True, lowercase=True, uppercase=True)
>>> sample_2 = ccg(length=6, numbers=True, lowercase=True, uppercase=True)
>>> sample_1
'1aD3x'
>>> sample_2
'aSDR3t'
```

```
$ python
>>> from generator import Generate_images, read_image
>>> images = Generate_images(...)
Images saved to the folder /root/src/images.
>>> read_image("path/to/image")
captcha: 1aD34
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

