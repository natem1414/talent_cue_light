Talent Cue Light README

Setup
install tcp_rx_dmx_draw.py
chmod +x tcp_rx_dmx_draw.py

Install Open Lighting Architecture (OLA) for DMX
sudo apt update
sudo apt upgrade
sudo apt-get install ola-python

sudo nano /etc/ola/ola-opendmx.conf
enabled = false

sudo nano /etc/ola/ola-usbdmx.conf
enabled = true

sudo nano /etc/ola/ola-ftdidmx.conf
enabled = true

sudo nano /etc/ola/ola-usbserial.conf
enabled = false

systemctl restart olad.service

Goto
http://IP_ADDRESS:9090/ola.html

For a USB DMX device with a FTDI chip:
Amazon: https://a.co/d/8b6Quaq

Check FTDI is loaded and running
Plugins>FTDI USB DMX

Add Universe:
Home>Add Universe
Universe ID: 1
Universe Name: Anything
Device: FT232R USB UART with serial number :XXXXXXXX

Run tcp_rx_dmx_draw.py
python3 tcp_rx_dmx_draw.py
