import evdev
from evdev import UInput, InputDevice

mouse = InputDevice('/dev/input/event16')
keybd = '/dev/input/event5'

ui1 = UInput.from_device(mouse, keybd, name='keyboard-mouse-device')
ui1.capabilities(verbose=True).keys()

ui2 = UInput.from_device('/dev/input/event6', name='touchpad-device')
ui2.capabilities(verbose=True).keys()

print(evdev.list_devices())

devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
for device in devices:
    print(device.path, device.name, device.info, device.phys, device.capabilities())
