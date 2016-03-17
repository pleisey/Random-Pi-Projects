import max7219.led as led
import string

device = led.sevensegment()
message='f b00b5'
current_position = 8

device.clear()

for letter in message:
	print letter
	device.letter(deviceId=0, position=current_position, char=letter)
	current_position -= 1