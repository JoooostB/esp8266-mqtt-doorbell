# Load credentials
from secrets import *
import machine as m
from umqtt.simple import MQTTClient
from time import sleep

def main():
    led = m.Pin(2, m.Pin.OUT)
    sleep(3)
    led.value(1)
    sensor = m.Pin(GPIO, m.Pin.IN, m.Pin.PULL_UP)
    while True:
        onchange(sensor)    # When sensor state changes
        mqtt_conn()
        if sensor.value() == 0:
            mqtt_pub(ringing)
            led.value(0)
            sleep(5)
            led.value(1)
            mqtt_pub(standby)
        else:
            mqtt_pub(standby)

def onchange(sensor):
    current = sensor.value()
    active = 0
    while active < 5:    # 5ms because the electromagnet is triggered very short
        if sensor.value() != current:
            active += 1
        else:
            active = 0
        sleep(0.001)

def mqtt_conn():
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_HOST, user=MQTT_USER, password=MQTT_PASS, port=MQTT_PORT)
    client.connect()
    return client

def mqtt_pub(payload):
    client = mqtt_conn()
    client.publish(topic=MQTT_TOPIC, msg=payload)
    client.disconnect()

main()
