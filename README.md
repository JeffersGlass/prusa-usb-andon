# prusa-usb-andon
Code to control inexpensive USB relay boards to show the state of a Prusa Mini 3D Printer via an Andon (stack light).

## Hardware

### USB Relay Boards
The relay-control-code was original forked from Pavel-A's usb-relay-hid library; I maintain [a fork of that library](https://github.com/JeffersGlass/usb-relay-hid) which I've made more object-oriented and Pythonic. See that library for more details on intended USB relay-board targets, but in short: most of the ["Programmable USB Relay"](https://www.aliexpress.com/wholesale?catId=0&initiative_id=SB_20200829101410&origin=y&SearchText=usb+relay+control) products from online vendors seem to be the same generic type. They often have a red silkmask on the PCB and blue relays from "SONGLE" (sometimes no-vender). They come in 5V, 12V, and 24V relay voltages.

### Andons	
There are a variety of cheap Andons available from online vendors these days. I hesitate to call them "stack lights" since most of them donts actually stack - rather, they are a single internal PCB with multiple levels of SMD LEDs, which a multicolor plastic shell that slides over them to provide color indication. However, if you're looking for these online, [seaching "stack lights" on online vendor sites](https://www.aliexpress.com/wholesale?catId=0&initiative_id=SB_20200829101432&origin=y&SearchText=stack+light) is the way to go. 

You may wish to think about your control voltage vs. your Andon voltage when purchasing a USB Relay Board and an Andon - having them be the same voltage simplifies power supply wiring, though this is not required.


