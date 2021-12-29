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

First thing first, you need to generate images:
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

