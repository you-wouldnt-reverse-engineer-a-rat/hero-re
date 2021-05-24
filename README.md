# hero-re

Reverse engineering of the HERO sensor used by Logitech mice

## Pin Configuration

![g305-hero](assets/g305-hero.png)

Pin no. | Funcion | Type | Description
:---: | :---: | :---: | :---:
1 | GND | ? |
2 | VDD | Power | Sensor power input
3 | GND | Power |
4 | GND | ? |
5 | IR LED K | LED drive | IR LED Cathode
6 | GND | ? |
7 | NC | NC |
8 | GND | ? |
9 | NC | NC |
10 | GND | ? |
11 | NC | NC |
12 | GND | ? |
13 | NC | NC |
14 | NC | NC |
15 | GND | Power |
16 | DEC | Power | External decoupling for internal 1.7V
17 | SCLK | SPI |
18 | MISO | SPI | also used as motion/wake up pin
19 | MOSI | SPI |
20 | CS | SPI |

