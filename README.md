# prusa-usb-andon
Code to control inexpensive USB relay boards to show the state of a Prusa Mini 3D Printer via an Andon (stack light).

## Hardware

### USB Relay Boards
The relay-control-code was original forked from Pavel-A's usb-relay-hid library; I maintain [a fork of that library](https://github.com/JeffersGlass/usb-relay-hid) which I've made more object-oriented and Pythonic. See that library for more details on intended USB relay-board targets, but in short: most of the "Programmable USB Relay" products from online vendors seem to be the same generic type. They often have a red silkmask on the PCB and blue relays from "SONGLE" (sometimes no-vender). They come in 5V, 12V, and 24V relay voltages.

### Andons
 

