#  Mushroom calculator disktop widget

A cute, hand-drawn, mushroom-themed desktop calculator widget — built pixel by pixel and coded from scratch with PyQt5.

mushcalc isn't your typical calculator. It's a frameless, transparent, draggable desktop widget shaped like a little pixel-art mushroom with its own hand-illustrated face and button set, designed to sit on your desktop like a fun little accessory rather than a boring system app.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![PyQt5](https://img.shields.io/badge/PyQt5-GUI-green)
![Piskel](https://img.shields.io/badge/Art-Piskel-pink)

---

##  Features

- **Fully custom pixel art** — every visual element (the mushroom body, face, and all 15–16 calculator buttons) was individually hand-drawn as separate PNG assets, no icon packs or stock graphics used.
- **Transparent, frameless window** — the widget has no title bar or background, so only the mushroom shape is visible on the desktop.
- **Draggable anywhere** — click and drag the widget to reposition it anywhere on your screen.
- **Hover feedback** — buttons respond to mouse hover with a smooth opacity change (down to 0.6), styled using QSS.
- **Hand-positioned layout** — instead of a standard grid layout, every button's position was manually set using custom geometry so the buttons could be arranged to fit organically within the mushroom's shape.
- **Working calculator logic** — supports standard operations (`+`, `−`, `×`, `÷`), with dedicated logic for digit/operator input, clearing, and evaluating results.
- **Packaged as a standalone `.exe`** — built with PyInstaller so it can run without needing Python installed.

---

##  Design & Art Process

All artwork was designed and drawn in **[Piskel](https://www.piskelapp.com/)**, a browser-based pixel art editor.

- The mushroom body (in a soft purple and cream color palette) and its face were drawn as the base background image.
- Each of the calculator's buttons — numbers, operators, clear, and equals — was drawn as its own separate PNG sprite, giving full control over how each button looks and behaves individually.
- The final assets were exported as `.png` files with transparency, ready to be layered into the PyQt5 interface.

---

##  Tech Stack

| Layer | Tool/Library |
|---|---|
| Art & Assets | Piskel (pixel art editor) |
| GUI Framework | PyQt5 (`QtWidgets`) |
| Styling | QSS (Qt Style Sheets) for hover effects |
| Packaging | PyInstaller (`.exe` build) |
| Language | Python 3 |

---

##  How It Works

**Main file:** `mushcalc.py`

- **Window setup:** Built on `QMainWindow`, with `Qt.FramelessWindowHint` and `Qt.WindowStaysOnTopHint` to remove the title bar and keep the widget floating above other windows, plus `Qt.WA_TranslucentBackground` so only the mushroom artwork itself is visible — no rectangular window edges.
- **Background art:** The mushroom illustration is loaded as a `QLabel` with a `QPixmap`, scaled to fill the window (`setScaledContents(True)`), acting as the base layer everything else sits on top of.
- **Layout:** Rather than using PyQt5's grid layout system, all 16 buttons (0–9, +, −, ×, ÷, Clear, Equals) are individually placed using `setGeometry()` with hand-tuned coordinates, allowing each one to sit exactly where it needed to on the mushroom's irregular pixel-art shape.
- **Buttons as icons:** Each button uses `QPushButton` with a `QIcon` set to its own pre-drawn PNG (e.g. `1button.png`, `+button.png`), rather than plain text — so every key looks hand-illustrated rather than like a default widget.
- **Hover effect:** A `QGraphicsOpacityEffect` is attached to every button, starting at full opacity (`1.0`). Custom `enterEvent`/`leaveEvent` handlers drop the opacity to `0.6` on hover and restore it on mouse-leave, giving a soft, responsive feel without extra animation libraries.
- **Display:** A `QLineEdit` acts as the calculator's screen, styled via QSS with a soft rounded-corner look that matches the mushroom's color palette.
- **Button logic:**
  - Digit and operator buttons share a single `button_clicked()` function — each button stores its own value as a Qt property (`setProperty("value", ...)`), so one function can read `sender().property("value")` and append it to the display.
  - **Clear** has its own dedicated `clear_button()` function that resets the display.
  - **Equals** has its own dedicated `equal_button()` function that evaluates the expression in the display using Python's `eval()`, with a try/except so invalid expressions show a friendly `Error:` message instead of crashing.
- **Dragging:** `mousePressEvent()` and `mouseMoveEvent()` are overridden to calculate the offset between the mouse and window position, letting the whole widget be dragged freely around the desktop like a sticky note.
- **PyInstaller compatibility:** A `resourcepath()` helper function checks for `sys._MEIPASS` (the temp folder PyInstaller uses at runtime) so that all image assets load correctly whether the app is run from source or from the packaged `.exe`.

---

## 📦 Installation & Usage

### Run from source
```bash
git clone https://github.com/yourusername/mushcalc.git
cd mushcalc
pip install PyQt5
python mushcalc.py
```
Make sure the `templates/` folder (containing the background mushroom image and all button PNGs) sits in the same directory as `mushcalc.py`.

### Run the standalone executable
A pre-built `.exe` version is available (built using PyInstaller), so you can run MushCalc without installing Python or any dependencies.

---

##  Preview

<img width="500" height="600" alt="image" src="https://github.com/user-attachments/assets/a84e5f9e-ea4e-43ab-9e07-af9c0cb7cacf" />


---

## What I Learned / Challenges

- Positioning 15+ individually drawn buttons to sit naturally within an irregular, non-rectangular pixel-art shape — grid layouts didn't give enough control, so manual geometry placement was the better fit.
- Implementing smooth hover feedback using QSS opacity changes.
- Making a fully transparent, frameless, and draggable window work smoothly in PyQt5.
- Packaging a GUI app with custom assets into a distributable `.exe` using PyInstaller.

---

##  License

This project is open for personal and educational use. Feel free to explore the code, but please credit the original artwork if reused.

---
