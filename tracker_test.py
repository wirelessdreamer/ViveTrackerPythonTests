#!/usr/bin/python
import usb.core
import usb.util
import sys

dev = usb.core.find(idVendor=0x28de, idProduct=0x2022)
print dev
if dev is None:
	raise ValueError("Vive Tracker not found")

print "Found Vive Tracker"

if dev.is_kernel_driver_active(0):
    try:
            dev.detach_kernel_driver(0)
            dev.detach_kernel_driver(1)
            dev.detach_kernel_driver(2)

            print "kernel driver detached"
    except usb.core.USBError as e:
            sys.exit("Could not detach kernel driver: %s" % str(e))
else:
    print "no kernel driver attached"

try:
    dev.set_configuration()
    dev.reset()
except usb.core.USBError as e:
    sys.exit("Could not set configuration: %s" % str(e))

try:
    usb.util.claim_interface(device, 0)
    usb.util.claim_interface(device, 1)
    usb.util.claim_interface(device, 2)
    print "claimed device"
except:
    sys.exit("Could not claim the device")


