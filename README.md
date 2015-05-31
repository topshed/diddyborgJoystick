# diddyborgJoystick

Client-server Python code to allow a [DiddyBorg] (https://www.piborg.org/diddyborg) robot to be controlled using a Joystick connected to another Pi, via wifi. Any joystick with simple switch contacts will work, but the cheap and robust [Zippyy ball handle] (http://shop.pimoroni.com/products/zippyy-ball-handle-joystick) is recommended.  

### borg.py

This runs on the Raspberry Pi installed in the diddyborg. It assumes that the Pi is connected to the same wifi network as the controlling Pi.

### control.py

This runs on the Pi connected to the Joystick. It assumes that the Pi is connected to the same wifi network as the Diddyborg Pi.

The code is set for the following joystick axis connections:

* Right motion - pin 12
* Left motion - pin 13
* Forward motion - pin 15
* Backwards motion - pin 11

However you can select which GPIO pins are used with the Joystick and modify the code accordingly. The code also assumes you have a bi-colour led connected to pins 7 (for red = stopped) and 18 (for green - in motion) to provide a visual indicator of activity. 


See this [entry on my blog]  (http://richardhayler.blogspot.com/2015/05/diddyborg-with-joystick-control.html) for more information.