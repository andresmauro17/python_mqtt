# python mqtt  

This is a project to test in order to send and receive data from and to a mqtt broker using python paho library.

## 1.	Installation

-   To clone the repository 
-   To create a virtual enviroment
``` virtualenv -p $(which python3) . ```
-   To activate the virtual enviroment (WINDOWS)
``` source bin/activate ```
-   To install dependencies
``` pip install -r .requirements.txt ```
-   please locate prompt on scr folder
``` cd src ```
-   duplicate .env-example in order to set your own credentials
``` cp .env-example .env ```

## 1. run the services
-   To init the server listener
``` python listener.py ```
-   To init the server publisher
``` python publisher.py ```

