import sys
import paho.mqtt.client
import ast
import time
import os
from dotenv import load_dotenv

def on_connect(client, userdata, flags, rc):
    print('conected, sending data ... ')

def on_publish(mosq, obj, mid):
    print("mid: " + str(mid))

def main():
    load_dotenv(dotenv_path='.env')
    client = paho.mqtt.client.Client()
    client.on_connect = on_connect
    client.on_publish = on_publish
    client.username_pw_set(os.getenv('BROKER_USERNAME'), os.getenv('BROKER_PASSWORD'))
    client.connect(host=os.getenv('BROKER_HOST'),port=int(os.getenv('BROKER_PORT')))
    temp = 2
    while(True):        
        print("Temperature: ", temp,"°C")
        print("--------------------------------------")
        client.publish(os.getenv('BROKER_TOPIC'), str(temp))
        time.sleep(3)
        if (temp < 8 ):
            temp = temp + 1
        else:
            temp = 2
        client.loop()

if __name__ == "__main__":
    main()

sys.exit(0)
