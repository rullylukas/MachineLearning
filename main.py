
# Importing libraries for the project.
import time
from machine import Pin, ADC
import machine
import random
import dht
import network
from network import WLAN
import micropython
import ubinascii
from mqtt import MQTTClient

# Variables
time_period = 60 * 15
air_max_value = 2733.0
Water_max_value = 911.0
range = air_max_value - Water_max_value


# Wireless network
ssid = "Network name"
password = "Network password"
sta_if = network.WLAN(network.STA_IF)


# Adafruit IO (AIO) configuration
AIO_SERVER = "io.adafruit.com"
AIO_PORT = 1883
AIO_USER = "JohannesE"
AIO_KEY = "aio_KJWh30EXR4GPLTRCuExHiPBxbT2N"
AIO_CLIENT_ID = ubinascii.hexlify(machine.unique_id())
AIO_HUM_FEED = "JohannesE/feeds/monitoring-plant.air-moisture"
AIO_TEMP_FEED = "JohannesE/feeds/monitoring-plant.temperature"
AIO_SOILHUM_FEED = "JohannesE/feeds/monitoring-plant.soil-moisture"

#Locate the pins
sensor = dht.DHT11(Pin(14))
time.sleep(2)
adc = ADC(Pin(36))
adc.atten(ADC.ATTN_11DB)




# Function that gets the data from the pins and sends it to adafruit
def send_sensor_data():
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        time.sleep(2)
        soilhum = adc.read()

        print('Temperature: %3.1f C' %temp)
        print('Humidity: %3.1f %%' %hum)
        print("Soil humidity: %3.1f T" %soilhum)

        percent = ((float(soilhum) - Water_max_value) / (float(range))) * 100
        reverse_percent = 100.0 - percent

        print("Soil humidity percentage:  %3.1f %%" %reverse_percent)

        print("Publishing: {0} to {1} ... ".format(temp, AIO_TEMP_FEED), end='')
        try:
            client.publish(topic=AIO_TEMP_FEED, msg=str(temp))
            print("Done")
        except Exception as e:
            print("Failed")

        print("Publishing: {0} to {1} ... ".format(hum, AIO_HUM_FEED), end='')
        try:
            client.publish(topic=AIO_HUM_FEED, msg=str(hum))
            print("Done")
        except Exception as e:
            print("Failed")

        print("Publishing: {0} to {1} ... ".format(reverse_percent, AIO_SOILHUM_FEED), end='')
        try:
            client.publish(topic=AIO_SOILHUM_FEED, msg=str(reverse_percent))
            print("Done")
        except Exception as e:
            print("Failed")

        time.sleep(time_period)
    except OSError as e:
      print('Failed to read sensor.')



# Function that resets the device.
def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()

#Function that connects the device to WiFi.
def do_connect():
    import network
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())


do_connect()

# Use the MQTT protocol to connect to Adafruit IO
client = MQTTClient(AIO_CLIENT_ID, AIO_SERVER, AIO_PORT, AIO_USER, AIO_KEY)
try:
    client.connect()
except OSError as e:
    print("Restarting...")
    time.sleep(20)
    restart_and_reconnect()


while True:
    try:
        send_sensor_data()
    except OSError as e: # If an exception is thrown
        client.disconnect()
        client = None
        sta_if.disconnect()
        sta_if = None
        print("Disconnected from Adafruit IO.")
        print("Restarting...")
        time.sleep(20)
        restart_and_reconnect()
