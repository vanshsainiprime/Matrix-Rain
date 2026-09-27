# Matrix Rain

A fun little Matrix-style terminal rain animation made with Python.
I made this as a **fun activity **. :D

---

## Preview

![Matrix Rain Preview](image.png)

---

## Features

- Matrix-style falling rain animation
- 100+ different symbols
- Random patterns
- Binary and hexadecimal patterns
- Different falling speeds
- Different trail lengths
- Bright leading characters
- Fading trails
- Random colors
- Glitch effects
- Dynamic patterns
- Fullscreen mode
- Hidden terminal menubar
- Automatic terminal restoration when exiting
- No external Python packages required

---

## Requirements

This project is made for **Linux**.

### You need

- Python 3
- XFCE Terminal
- `wmctrl`

The animation itself does not require any Python packages.

### Check Python

```bash
python3 --version


### Check wmctrl

```bash
wmctrl -V
```

If `wmctrl` is not installed:

```bash
sudo apt update
sudo apt install wmctrl
```

---

## Download

There are two ways to get the project.

### Download ZIP

1. Open the repository on GitHub.
2. Click **Code**.
3. Click **Download ZIP**.
4. Extract the ZIP file.
5. Open a terminal in the extracted folder.

Then check the files:

```bash
ls
```

You should see:

```text
matrix-rain.py
README.md
```

### Clone with Git

If Git is installed, run:

```bash
git clone https://github.com/vanshsainiprime/Matrix-Rain.git
```

Then:

```bash
cd Matrix-Rain
```

Check the files:

```bash
ls
```

---

## Install Requirements

If you do not have `wmctrl`:

```bash
sudo apt update
sudo apt install wmctrl
```

That's all.

There are no Python packages to install.

---

## Run

Inside the project folder, run:

```bash
python3 matrix-rain.py
```

The Matrix Rain animation should start in the terminal.

---

## Stop

To stop the animation, press:

```text
Ctrl + C
```

The animation will stop and the terminal will automatically restore itself.

---

## Optional: Create the `matrix` Command

You can also make it possible to launch the animation by simply typing:

```bash
matrix
```

First, make the script executable:

```bash
chmod +x matrix-rain.py
```

Then copy it to `/usr/local/bin`:

```bash
sudo cp matrix-rain.py /usr/local/bin/matrix
```

Now you can run it from anywhere:

```bash
matrix
```

To stop it:

```text
Ctrl + C
```

### Remove the `matrix` command

If you want to remove the optional command:

```bash
sudo rm /usr/local/bin/matrix
```

This will not delete the project folder.

---

## Customization

You can edit `matrix-rain.py` and experiment with things like:

* Falling speed
* Trail length
* Animation FPS
* Symbols
* Colors
* Glitch effects
* Patterns
* Symbol density
* Brightness

For example:

```python
FPS = 50
```

Change the value and experiment with different animation speeds.

---

## Why I Made This

There isn't really a serious purpose behind this project.
I made it as a **fun activity**.

---

## Built With

* Python 3
* ANSI escape sequences
* XFCE Terminal
* X11
* `wmctrl`

---

## Project Structure

```text
Matrix-Rain/
│
├── matrix-rain.py
├── README.md
└── image.png
```

---

## Compatibility

This project is primarily designed for:

* Linux
* XFCE
* X11
* XFCE Terminal

Some features may behave differently on other desktop environments or terminal emulators.

---

## Note

This is a small project made mainly for **fun and experimentation**.
Have fun with it!
