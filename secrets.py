# Wi-Fi credentials of your home/IOT network:
WIFI_SSID="SSID"
WIFI_PSK='PASSWORD'

'''
Please use values below to translate used port to GPIO port number:
D0=16
D1=5
D2=4
D3=0
D4=2
D5=14
D6=12
D7=13
D8=15
'''

# GPIO port connected to reed sensor
GPIO=314

# MQTT credentials
MQTT_HOST = 'X.X.X.X'
MQTT_PORT = 1883
MQTT_USER = 'USER'
MQTT_PASS = 'PASSWORD'
MQTT_CLIENT_ID = '24f527a8-64c3-4ac1-9f57-d35910b3b848'
MQTT_TOPIC = 'TOPIC'
ringing = 'ringing'   # Your prefered payload when ringing
standby = 'standby'   # Your prefered payload when in standby
