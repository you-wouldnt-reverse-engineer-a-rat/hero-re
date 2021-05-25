#!/bin/bash

sigrok-cli -i ../la_captures/g305_sigrok_pulseview/startup.sr -P spi:miso=MISO:mosi=MOSI:clk=SCLK:cs=CS:cpol=1:cpha=1 -A spi=mosi-data > startup-mosi
sed -i -e 's/spi-1: //g' startup-mosi
