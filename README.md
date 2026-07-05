# Home-Automation-version-2.0

## Project Overview:-

- This project demonstrates a Wi-Fi-based Home Automation System using an ESP32 microcontroller. The system allows users to know Temperature & humidiity in home directly from a mobile phone over Wi-Fi.

- The ESP32 acts as a web server, providing a simple control interface accessible through any smartphone browser.

---

## Features:-

- To know Temperature & humidity using a mobile phone
- Wi-Fi connectivity through ESP32✅💯
- Supports multiple user's devices
- Low-cost
- easy to build
- Expandable for IoT applications

## Components Required:-

- ESP32 Development Board (or ESP32 cam module)
- Wi-Fi Network(ESP,darkking--password)
- Mobile Phone
- Power Supply (6V)
- Connecting Wires
- DHT11 or DHT22 temperature/humidity sensor

## Hardware connection:-
- connect GPIO-4  ---> DHT11 DATA pin
- connect ESP32-GND --> DHT11 GND pin
- connect ESP32-3.3V --> DHT11 VCC pin
- connect ESP32-RX pin --> TTl adaptor-TX pin
- connect ESP32-TX pin --> TTl adaptor-RX pin
- connect ESP32-5V pin --> TTl adaptor-5V pin
- connect ESP32-GND pin --> TTl adaptor-GND pin
- connect TTL adaptor --> PC
  
## Installation:-

- Open the project in Arduino IDE.
- Install Thimcker-AI ESP32 CAM  board support.
- Uploard speed is 115,200
- select port as COM-7
- Connect ESp32 to PC via USB cable (or)TTL adaptor
- compile and Upload code to ESP32
- Power the ESP32 and connect your mobile phone to the same Wi-Fi network.
- Open the ESP32 IP address in a browser and Know the temperature and humidity around you.


## Working:-

-compile and upload esp32 code from arduino app
- when ESP32 connect to wifi ,then it generate IP address like(it is mine---->192.168.137.89)
- run python using command like--> python app.py
- open index.html in chrome
- when the ip address enter into browser on pc or mobile---> which it connect to same wifi as ESP32 connected
- then you can see the user interface.

## Testing:-

- check is it Front code is ok or not
- check is the values are loaded or not
- check for modifications

## My Experience:-
- Detailed explanation and my rectified mistakes:-
- https://homeautomationesp32.blogspot.com/2026/07/smart-sensor.html

## Licence:-

This project is licenced under the MIT License.
- see the [LICENSE](LICENSE) file.

---

## About the Developer:-

- **Name:** Venkata Manohar Reddy M
- **Email:** manoharmuli18@gmail.com
- **GitHub:** https://github.com/manoharmuli18-tech
- **LinkedIn:** https://www.linkedin.com/in/muli-manohar-57134a408
- **Portfolio:** https://manoharmuli18-tech.github.io/portifolio/
- **status:-** open to collaboration & freelance automation gigs!

---
---
## Acknowlegments:-
Thanks to the maker community and open source projects for inspiration.
