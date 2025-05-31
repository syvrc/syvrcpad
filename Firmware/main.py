import board
import displayio
import busio
import terminalio
import time

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from adafruit_display_text import label
from adafruit_ssd1306 import SSD1306_I2C

keyboard = KMKKeyboard()

keyboard.row_pins = (board.GP0, board.GP1, board.GP2)  
keyboard.col_pins = (board.GP3, board.GP4, board.GP5, board.GP6)  
keyboard.diode_orientation = DiodeOrientation.COL2ROW

displayio.release_displays()
i2c = busio.I2C(board.GP4, board.GP5)  

display = SSD1306_I2C(128, 32, i2c)
splash = displayio.Group()
text_area = label.Label(terminalio.FONT, text="XIAO MACROPAD", x=0, y=10)
splash.append(text_area)
display.show(splash)

encoder = EncoderHandler()
encoder.encoder_pins = ((board.GP10, board.GP11),)  
encoder.rotate_callbacks = (
    lambda direction: print("Volume Up" if direction else "Volume Down"),
)
keyboard.modules.append(encoder)

keyboard.keymap = [
    [
        KC.A, KC.B, KC.C, KC.D,    # S1, S2, S3, Rotary switch
        KC.E, KC.F, KC.G, KC.H,    # S5, S6, S7, S8
        KC.I, KC.J, KC.K, KC.L     # S9, S10, S11, S12
    ]
]

if __name__ == '__main__':
    while True:
        keyboard.go()
