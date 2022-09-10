import paho.mqtt.client as mqtt
from termcolor import colored #lib for colors on temrinal
from threading import Thread # we need to use multithread task
import sys

print(colored("bienbenidos al chat", "red"))
nombre = input("hola dime tu nombre: ")

nombre = nombre.capitalize()

def on_connect(client, userdata, flags, rc):
    print("conectado con exito")
    client.subscribe("andresmauro17/feeds/remote-data")
    client.publish("andresmauro17/feeds/remote-data", nombre + "se ha unido al chat")

def on_message(client, userdata, msg):
    print(msg.payload)

cliente = mqtt.Client()
cliente.on_connect = on_connect
cliente.on_message = on_message

cliente.username_pw_set("andresmauro17", "aab24fb96c304778b2ffa42cda92396b")
cliente.connect('io.adafruit.com', 1883, 60)

while True:
    a_enviar = input("escribe mensaje ->")
    a_enviar = nombre + "dice: " + a_enviar
    cliente.publish("andresmauro17/feeds/remote-data", a_enviar)
    cliente.loop()

sys.exit(0)