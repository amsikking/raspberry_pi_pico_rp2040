# raspberry_pi_pico_rp2040
Quick start guide: Raspberry Pi Pico RP2040 microcontroller with MicroPython
## Quick start:
- To get MicroPython running on the Pico -> with the Pico USB unplugged, hold down the 'BOOTSEL' button on the board and then plug it in to the computer. This should boot the Pico into a special
mode and it should now appear as drive called 'RPI-RP2' (like a USB memory stick).
- Get the latest pre-built binary 'firmware.uf2' file from the Raspberry Pi Pico website: https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html.
  - A version of the .uf2 file is included here for convenience 'RPI_PICO-20231005-v1.21.0.uf2'.
- Drag and drop the .uf2 file onto the RPI-RP2 drive to install MicroPython (this handles all the heavy lifting and the Pico should now boot ready to go).
- Get the Raspberry Pi backed open source 'Thonny' Python/MicroPython IDE (https://thonny.org/) and install
it or simply use the 'Portable variant'. Toggle Thonny into MicroPython mode, select the (connected) Pico
and start developing and running code directly on the Pico!
- Try the 'led_toggle.py' example in this repo to get started!
## Details:
- The Pico comes in regular and wireless (+ W) variants, either with or without soldered pins. I opted for 
the regular with pins, part: RASPBERRY PI PICO H RP2040 SC0917
- It's nice to have a breakout board with some status LED's and screw terminals for connections. I tried
this one which seems fine: Freenove FNK0081 (https://github.com/Freenove/Freenove_Breakout_Board_for_Raspberry_Pi_Pico)
- For more info on programming the Pico with MicroPython, start with 'raspberry-pi-pico-python-sdk.pdf'
(a version included here for convenience) and look here: https://docs.micropython.org/en/latest/rp2/quickref.html
- For more technical info on the Pico board and rp2040 chip see 'pico-datasheet.pdf' and 'rp2040-datasheet.pdf' 
(versions included here for convenience).
- For more about MicroPython start here: https://docs.micropython.org/en/latest/library/index.html
