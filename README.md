# rfm69-python

# Ported to Micropython by Arko at EMFCAMP 2016 - Habville

A library to control HopeRF RFM69-series radio modules through SPI and
GPIO. This is designed for use on a pyboard.

Written for use with the [ukhas.net](http://ukhas.net) project.

## Requirements
* Only currently tested on MicroPython v1.8.3

## Datasheets
* [RFM69W](http://www.hoperf.com/upload/rf/RFM69W-V1.3.pdf)
* [Semtech SX1231](https://www.semtech.com/images/datasheet/sx1231.pdf)
    (the underlying RF chip, which much of the RFM69 datasheet is lifted
    from)

## Prior Art
* [rfm69-python](https://github.com/russss/rfm69-python)
* [ukhasnet-rfm69](https://github.com/UKHASnet/ukhasnet-rfm69)
* [UKHASNetPiGateway](https://github.com/dbrooke/UKHASNetPiGateway) (in
  C/Wiring)
* [ukhasnet LPC810 node](https://github.com/jamescoxon/LPC810)
* [Python code for the beaglebone black](https://github.com/wcalvert/rfm69-python)
