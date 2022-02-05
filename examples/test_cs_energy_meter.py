# Very simple test program using the cs_energy_meter library

from atm90e32_spi import atm90e32_spi
from cs_energy_meter import cs_energy_meter
import utime

numBoards = 2
spiConn = atm90e32_spi()
energyMeter = cs_energy_meter(spiConn, numBoards)

energyMeter.init_board(1, currentGain=[11131, 11131, 15420, 9260, 9260, 9260]) # Init board with custom current gain values
energyMeter.init_board(2) # Init board with default current gain values

print('Board 1: ', end='')
print(energyMeter.get_current(1))
print('Board 2: ', end='')
print(energyMeter.get_current(2))
print('\n')
