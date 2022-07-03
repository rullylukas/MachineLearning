# Humidity-and-temperature-sensors-for-monitoring-plants-iot-project
Project for the course Introduction to Applied IoT, Summer 2022

**Name:** Johannes Eriksson; **Student** credentials: je224bk

# Short project overview
This project is aimed to construct a simple iot device with 2 sensors for placement besides your plant that monitors the temperature and air humidity around the plant aswell as the humidity in the plants soil in order to se when you need to water your plant. 

**Approxiamtion of time needed for the project:**

Around one hour


# Objective
**Reasons for choosing the project:**
The reason i choose this project is that i some plants in my home and have the habit of sometimes forgetting to water them in time before they start to wither so being able to the when i should water the plants will probably help them thrive. 

**Purposes of the project:**
The purpose of this project is firstly to learn about the Inter of things, how to build a iot device and connect it to a platform to visualize its data. And secondly to monitor my plants to see when i need to water them.

**Insights gained by doing the project:**
The project is able to give insights in basic concepts of IOT, programming and electric circuits. 

# Material
Component | Purpose of | Bought at | Price 
-| -| -| -
ESP32 DEVKIT V1 DOIT | A microcontroller used for data collection, data transfer, and data analysis. | sizable.se | 94 sek 
Capacitive soil moisture sensor | A sensor that mesures the humidity in soil  | amazon.se | 72 sek
DHT11 | A sensor used for mesuring the humidity in the air asweel as the temperature | sizable.se | 28 sek
40x jumper wires Male/Male | Wires for connecting the different components | sizable.se | 24 sek
Breadboard 400 points | A board used to easy connect the sensors without soldering | sizable.se | 34 sek
Micro USB cable*

\* USB cable was already in possession and free.

![material](https://user-images.githubusercontent.com/108582271/177007654-dc706edb-46cb-425e-a652-3f34982a3d64.jpg)
Figure 1: Components used for the project

All components are shown in Figure 1. From left to right:
* Breadboard
* ESP32 DEVKIT V1 DOIT
* Capacitive soil moisture sensor. With its wires beneath it
* DHT11
* Jumper wires

# Computer setup
**Setting up the IDE:**

The first step to set up the ESP32 is by first connecting the device to a computer and then downloading the the latest hardware driver available. The link i used https://www.silabs.com/documents/public/software/CP210x_Windows_Drivers.zip

The next step is to update the firmware of the ESP32. This is done by donwloading this file https://micropython.org/resources/firmware/esp32-20220117-v1.18.bin to your computer and on this website https://nabucasa.github.io/esp-web-flasher/ connect your development board by choosing 460800 Baud in the top right corner and pressing connect. You then press erase to delete the files on the board so that you then can enter aoffset of 100 and in "choose file" select the downloaded file and then press "Program".(It takes a while and during this time don’t disconnect your board from the USB cable)

The next thing to do is to download and install Node js (Windows download link https://nodejs.org/en/) and choose a IDE for the project and i choose work in Atom.io (Windows download link https://atom.io/). Then add the Pymakr plugin to Atom by going to File >> Settings >> Install and Look for Pymakr and Install it. (It takes a while; wait until shows it is successfully installed)

You are now ready to run your code on the development board. In order to uppload the code you need to open the Pymakr plugin that you find at the bottom and go into its setting and choose global settings. Enter the device com port into the Device address (list) field (which can be found in the device manager) and remove the check box selection from Safe-boot before upload. Go back and press Connect device in Pymakr and choose your COM port to connect to your board. Now you just need to press Upload project to device in order to run your code on the board.

# Putting everything together
The setup of the device and the wiring is shown in a circuit diagram in Figure 3. Note that i could not find the exact same microcontroller that i used but it has the same amount of pins on each side, so the diagram shows in what spot you to put the wires. I also could not find the exact soil moisture senor but this one has the exact same wiring.

![Screenshot 2022-07-03 153746](https://user-images.githubusercontent.com/108582271/177042312-ed59c1e5-c0c5-4794-9272-6547b3453352.jpg)

Figure 2: Wiring of the components

The EPS32 is put on in right side of the breadboard so the left side pins of the microcontroller can be used. It is powerd by a micro USB cable either connected to a power supply or to a computer. The Vin pin is connected to the breadboards power supply line to give power to the senors and the GND pin is conneced to the GND line. 

Both sensors have a GND pin that is also connected to the breadboards GND line VCC that is connected to the breadboards power supply line. Then each have one data transfer pin, since the capacitive soil moisture sensor is a analog senor then the data pin is wired to a ADC (Analogue to Digital Converter)  pin in this case GPIO36 and DHT11 is connected to GPIO14.

# Chosen platform
The platform i choose for this project is Adafruit since it is a free cloud service that seemed to fit my project with what it has to offer. It is able to easily visualize your data in real-time online in their dashboard where you can choose if you want to see it in a diagram, as a Gauge or any other form. It also offers the opportunity to analyse the data online in simple ways by going to the feeds.

![Screenshot 2022-07-03 161432](https://user-images.githubusercontent.com/108582271/177043837-c7ffd412-ce5b-40e6-ada5-160e3ae2873e.jpg)
FIgure 3: The dashboard page on Adafruit

# The code



