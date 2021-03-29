import sys
import paho.mqtt.client
import os
import json
from dotenv import load_dotenv

def on_connect(client, userdata, flags, rc):
    print('conecting, waiting for data.....')
    client.subscribe(topic=os.getenv('BROKER_TOPIC'), qos=2)

def on_message(client, userdata, message):
    print("--------------------------")
    print('topic: ', message.topic)
    var = str(message.payload.decode('utf-8'))
    print('payload: ', message.payload )
    try:
        # CON STRING DUMPS AND LOADS
        data = json.dumps(var)
        data = json.loads(data)
        print(data)
    except Exception as e:
        print(e)
    print('qos: ', message.qos)

def main():
    load_dotenv(dotenv_path='.env')
    client = paho.mqtt.client.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set(os.getenv('BROKER_USERNAME'), os.getenv('BROKER_PASSWORD'))
    client.connect(host=os.getenv('BROKER_HOST'),port=int(os.getenv('BROKER_PORT')))
    client.loop_forever()

if __name__ == '__main__':
    main()

sys.exit(0)