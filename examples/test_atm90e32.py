# Very simple test program using the atm90e32 libraries
# Currently no error checking, not reading all available values, etc.

from atm90e32_spi import atm90e32_spi
from atm90e32_ctl import atm90e32_ctl
import utime

# CALIBRATION SETTINGS
linefreq = 4231  # 4231 for 60 Hz, 135 for 50 Hz
pgagain = 0  # 0 is default for CircuitSetup Energy Meter Board, 21 (2x), 42 (4x)
ugain = 7305  # 7305 - 9v AC Transformer - Jameco 157041

igainA = 8650  # 30A/1V SCT-013-030: 8650
igainB = 8650  # 20A/25mA SCT-006: 11131
igainC = 8650  # 50A/1V SCT-013-050: 15420

spiConn = atm90e32_spi()
energy_sensor0 = atm90e32_ctl(linefreq, pgagain, ugain, igainA, igainB, igainC, 5, spiConn)
#energy_sensor1 = atm90e32_ctl(linefreq, pgagain, ugain, igainA, igainB, igainC, 4, spiConn)
#energy_sensor2 = atm90e32_ctl(linefreq, pgagain, ugain, igainA, igainB, igainC, 0, spiConn)
#energy_sensor3 = atm90e32_ctl(linefreq, pgagain, ugain, igainA, igainB, igainC, 16, spiConn)
#energy_sensor4 = atm90e32_ctl(linefreq, pgagain, ugain, igainA, igainB, igainC, 27, spiConn)
#energy_sensor5 = atm90e32_ctl(linefreq, pgagain, ugain, igainA, igainB, igainC, 17, spiConn)
#energy_sensor6 = atm90e32_ctl(linefreq, pgagain, ugain, igainA, igainB, igainC, 2, spiConn)
#energy_sensor7 = atm90e32_ctl(linefreq, pgagain, ugain, igainA, igainB, igainC, 21, spiConn)
#energy_sensor8 = atm90e32_ctl(linefreq, pgagain, ugain, igainA, igainB, igainC, 13, spiConn)
#energy_sensor9 = atm90e32_ctl(linefreq, pgagain, ugain, igainA, igainB, igainC, 22, spiConn)

print('Sensor0 Voltage: {}V'.format(energy_sensor0.line_voltageA))
#print('Sensor1 Voltage: {}V'.format(energy_sensor1.line_voltageA))
#print('Sensor2 Voltage: {}V'.format(energy_sensor2.line_voltageA))
#print('Sensor3 Voltage: {}V'.format(energy_sensor3.line_voltageA))
#print('Sensor4 Voltage: {}V'.format(energy_sensor4.line_voltageA))
#print('Sensor5 Voltage: {}V'.format(energy_sensor5.line_voltageA))
#print('Sensor6 Voltage: {}V'.format(energy_sensor6.line_voltageA))
#print('Sensor7 Voltage: {}V'.format(energy_sensor7.line_voltageA))
#print('Sensor8 Voltage: {}V'.format(energy_sensor8.line_voltageA))
#print('Sensor9 Voltage: {}V'.format(energy_sensor9.line_voltageA))