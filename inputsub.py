import evdev
from evdev import UInput, InputDevice, categorize, ecodes

devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
for device in devices:
    #print(device.path, device.name, device.info, device.phys, device.capabilities())
    if device.name == "ETPS/2 Elantech Touchpad" :
        target = device

print(target)
ui = UInput.from_device(target, name='touchpad-device')

#print(evdev.list_devices())
target.grab()

for event in target.read_loop():
    print(categorize(event))
    ui.write(event.type, event.code, event.value)    
