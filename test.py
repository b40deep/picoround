"""
hershey.py
==========
.. figure:: /_static/hershey.png
  :align: center

  Hershey vector font demo

Demo program that draws greetings on display cycling thru hershey fonts and colors.
"""

import random
import utime
import gc9a01
import tft_config
import tft_buttons

buttons = tft_buttons.Buttons()

left_flipper = buttons.left
right_flipper = buttons.right

tft = tft_config.config(tft_config.TALL, options=gc9a01.WRAP_V)

# Load several frozen fonts from flash

# import greeks
import italicc      # kawa large
import italiccs     # kawa notbad
import meteo        # kawa comic sans normal
import romanc       # kawa
import romancs      # notnice
import romand       # comic sans bold
import romanp       # comic sans caps, kawa
import romans       # comic sans thin
import scriptc      # kawa
import scripts      # kawa thin


def cycle(p):
    """return the next item in a list"""
    try:
        len(p)
    except TypeError:
        cache = []
        for i in p:
            yield i
            cache.append(i)

        p = cache
    while p:
        yield from p


# Create a cycle of colors
# COLORS = cycle([0xe000, 0xece0, 0xe7e0, 0x5e0, 0x00d3, 0x7030])
# 0xe000 red, 0xece0 orange, 0xe7e0 yellow, 0x5e0 green, 0x00d3 blue, 0x7030 purple
COLORS = cycle([0xece0])

# List Hershey fonts
# FONT = [greeks, italicc, italiccs, meteo, romanc, romancs, romand, romanp, romans, scriptc, scripts]
FONT = [ romanc]

# Create a cycle of tuples consisting of a FONT[] and the HEIGHT of the next FONT[] in the cycle
FONTS = cycle([
    (font, FONT[(i + 1) % len(FONT)].HEIGHT)
        for i, font in enumerate(FONT)])

# Greetings
GREETING = [
    "Ahoy", "Buenos Dias", 
    "How Are You",
    "Gyebale ko", "Nkulamusizza",
    'Yo!']

# Create a cycle of tuples consisting of a list of words from a GREETING, the number of spaces+1
# in the that GREETING, and the number of spaces+1 in the next GREETING of the cycle
GREETINGS = cycle([
    (greeting.split(), greeting.count(' ')+1, GREETING[(i + 1) % len(GREETING)].count(' ')+1)
        for i, greeting in enumerate(GREETING)])


def main():
    """Scroll greetings on the display cycling thru Hershey fonts and colors"""

    tft.init()
    tft.fill(gc9a01.BLACK)

    height = tft.height()
    print(f"screen height: {type(height)} {height}")
    # height = 500   # want to see if i can make a `longer` screen to enable proper scrolling
    width = tft.width()

    # Set up scrolling area
    tfa = tft_config.TFA
    bfa = tft_config.BFA
    tft.vscrdef(tfa, height, bfa)

    scroll = 0
    to_scroll = 0

    while True:

        # if we have scrolled high enough for the next greeting
        if to_scroll == 0:
            font = next(FONTS)                              # get the next font
            greeting = next(GREETINGS)                      # get the next greeting
            color = next(COLORS)                            # get the next color
            lines = greeting[2]                             # number of lines in the greeting
            to_scroll = lines * font[1] + 8                 # number of rows to scroll

            # draw each line of the greeting
            for i, word in enumerate(greeting[0][::-1]):
                word_len = tft.draw_len(font[0], word)                          # width in pixels
                col = 0 if word_len > width else (width//2 - word_len//2)       # column to center
                row = (scroll + height - ((i + 1) * font[0].HEIGHT) % height)   # row to draw
                tft.draw(font[0], word, col, row, color)                        # draw the word
                tft.hline(20,40, 20, color)

        if left_flipper.value() == 1:
            print('left')
            tft.fill_rect(0, scroll, width, 1, gc9a01.BLACK)    # clear the top line
            tft.vscsad(scroll-tfa)                              # scroll the display
            scroll = (scroll-1) % height                        # update the scroll position
            to_scroll += 1                                      # update rows left to scroll
            utime.sleep(0.02)                                   # stop and smell the roses
        if right_flipper.value() == 1:
            print('right')
            tft.fill_rect(0, scroll, width, 1, gc9a01.BLACK)    # clear the top line
            tft.vscsad(scroll+tfa)                              # scroll the display
            scroll = (scroll+1) % height                        # update the scroll position
            to_scroll -= 1                                      # update rows left to scroll
            utime.sleep(0.02)                                   # stop and smell the roses


main()
