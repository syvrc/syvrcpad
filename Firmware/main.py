import os
import board
import digitalio
import busio
import displayio
import terminalio
import rotaryio
import time

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from adafruit_display_text import label
from adafruit_ssd1306 import SSD1306_I2C

keyboard = KMKKeyboard()
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.row_pins = (board.GP0, board.GP1, board.GP2, board.GP3)
keyboard.col_pins = (board.GP4, board.GP5, board.GP6)

displayio.release_displays()
i2c = busio.I2C(board.GP5, board.GP4) 
display = SSD1306_I2C(128, 32, i2c)
splash = displayio.Group()
text_area = label.Label(terminalio.FONT, text="XIAO MACROPAD", x=0, y=10)
splash.append(text_area)
display.show(splash)

keymap = [
    lambda: open_app("Visual Studio Code"),    # k00
    lambda: open_app("Discord"),               # k01
    lambda: open_app("WhatsApp"),              # k02
    lambda: open_app("Spotify"),               # k10
    lambda: open_app("Safari"),                # k11
    lambda: open_app("Slack"),                 # k12
    lambda: open_app("Terminal"),              # k20
    lambda: open_app("Notes"),                 # k21
    lambda: open_app("Calendar"),              # k22
    lambda: open_app("System Preferences"),    # k30
    lambda: open_app("Music"),                 # k31
    lambda: open_app("Photos"),                # k32 (encoder switch)
]

keyboard.keymap = [[keymap[i] for i in range(12)]]

keyboard.modules.append(EncoderHandler())

keyboard.modules[-1].encoder_pins = ((board.GP7, board.GP8),)
keyboard.modules[-1].encoder_direction_flips = (False,)
keyboard.modules[-1].rotate_callbacks = (
    lambda direction: open_app("Volume Up") if direction else open_app("Volume Down"),
)

while True:
    keyboard.go()