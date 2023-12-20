import machine

led = machine.Pin("LED", machine.Pin.OUT)

while True:
    led.toggle()
    input('hit enter to toggle LED (exit: CTRL + c)')
