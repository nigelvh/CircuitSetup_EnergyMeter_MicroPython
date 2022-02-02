# Very simple test program using the atm90e32 libraries

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

def print_sensor_data(sensor):
	print('Voltage: {}Vrms'.format(sensor.line_voltageA), end='')
	print(', PeakV: {}Vp-p'.format(sensor.peak_voltageA), end='')
	print(', Freq: {}Hz'.format(sensor.frequency))
	
	print('Current RMS - T: {}A'.format(sensor.line_current_total), end='')
	print(', A: {}A'.format(sensor.line_currentA), end='')
	print(', B: {}A'.format(sensor.line_currentB), end='')
	print(', C: {}A'.format(sensor.line_currentC))

	print('Peak Current - A: {}A'.format(sensor.peak_currentA), end='')
	print(', B: {}A'.format(sensor.peak_currentB), end='')
	print(', C: {}A'.format(sensor.peak_currentC))
	
	print('Power Active - T: {}W'.format(sensor.active_power_total), end='')
	print(', A: {}W'.format(sensor.active_powerA), end='')
	print(', B: {}W'.format(sensor.active_powerB), end='')
	print(', C: {}W'.format(sensor.active_powerC))

	print('Power Reactive - T: {}W'.format(sensor.reactive_power_total), end='')
	print(', A: {}W'.format(sensor.reactive_powerA), end='')
	print(', B: {}W'.format(sensor.reactive_powerB), end='')
	print(', C: {}W'.format(sensor.reactive_powerC))

	print('Power Apparent - T: {}W'.format(sensor.apparent_power_total), end='')
	print(', A: {}W'.format(sensor.apparent_powerA), end='')
	print(', B: {}W'.format(sensor.apparent_powerB), end='')
	print(', C: {}W'.format(sensor.apparent_powerC))

	print('Power Factor - T: {}'.format(sensor.power_factor_total), end='')
	print(', A: {}'.format(sensor.power_factorA), end='')
	print(', B: {}'.format(sensor.power_factorB), end='')
	print(', C: {}'.format(sensor.power_factorC))

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

print_sensor_data(energy_sensor0)