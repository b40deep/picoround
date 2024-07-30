# installation:

-   flash the firmware onto the device. The firmware comes with pre-built libraries for the display and some fonts.
-   copy the `tft-config.py` and `tft-buttons.py` from `examples\tft-configs` folder onto the root of the Pico. The config is for display and the buttons is for handling input. You can alternatively ignore the buttons one and initialise your own GPIO buttons inside your code. setting up buttons inside the `tft-buttons.py` file is done like this `self.right = Pin(22, Pin.IN, Pin.PULL_DOWN)` and calling them inside your code is like this

```
import tft_buttons
buttons = tft_buttons.Buttons()
right_flipper = buttons.right
# in main loop, check value
if right_flipper.value() == 1:
# do something
```

-   need an `env`? probably not.

# todo

# things I've learnt

-   `tft = tft_config.config(tft_config.TALL)` initialises the screen in its proper top-to-bottom order and `tft = tft_config.config(tft_config.WIDE, options=gc9a01.WRAP_V)` makes it display sideways (wide orientation). not yet sure what the `options=gc9a01.WRAP_V` does.
-   `gc9a01_mpy-main\docs\_sources\gc9a01.rst.txt` has functions and their explanations, might be handy.
