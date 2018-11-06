# This is script that run when device boot up (or wake from sleep.)
from secrets import *    # Load credentials
import network   # Import WLAN library
import webrepl
from time import sleep

sta_if = network.WLAN(network.STA_IF) # Initialize STA mode (to connect to a network)
ap_if = network.WLAN(network.AP_IF) # Initialize AP mode (to turn it off)
ap_if.active(False) # Turn off AP mode
if not sta_if.isconnected():
    print('Connecting to network: %s' % (WIFI_SSID))
    sta_if.active(True)
    sta_if.connect(WIFI_SSID, WIFI_PSK)             # Connect to predefined Wi-Fi network
    while not sta_if.isconnected():
        pass
sleep(3)                # I don't totally recall why I put this sleep here
print('Network Configuration:', sta_if.ifconfig())

