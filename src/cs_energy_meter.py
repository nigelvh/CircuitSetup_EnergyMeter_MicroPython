from atm90e32_ctl import atm90e32_ctl

class cs_energy_meter:

	def __init__(self, spiLink, numBoards=1, csPins=[5, 4, 0, 16, 27, 17, 2, 21, 13, 22, 14, 25, 15, 26]):
		self._spiLink = spiLink
		self._numBoards = numBoards
		self._csPins = csPins
		self.sensor = [False, False, False, False, False, False, False]
	
	def init_board(self, boardNum, lineFreq=4231, voltChannels=1, voltGain=[7305], currentGain=[11131, 11131, 11131, 11131, 11131, 11131], pgaGain=0):
		if boardNum < 1 or boardNum > 7: raise ValueError("boardNum must be between 1 to 7 inclusive.")
		if lineFreq != 4231 and lineFreq != 135: raise ValueError("lineFreq must be 4231 (60Hz) or 135 (50Hz).")
		if voltChannels < 1 or voltChannels > 2: raise ValueError("voltChannels must be between 1 and 2 inclusive.")
		if voltChannels != len(voltGain): raise ValueError("voltGain length does not match voltChannels.")
		if len(currentGain) != 6: raise ValueError("currentGain list does not contain 6 channels.")
		if pgaGain != 0 and pgaGain != 21 and pgaGain != 42: raise ValueError("pgaGain must be 0 (1x), 21 (2x), or 42 (4x).")
		
		sensorNumA = (boardNum - 1) * 2
		sensorNumB = sensorNumA + 1
		
		if voltChannels==2:
			sensorBVolt = voltGain[1]
		else:
			sensorBVolt = voltGain[0]
		
		self.sensor.insert(sensorNumA, atm90e32_ctl(lineFreq, pgaGain, voltGain[0], currentGain[0], currentGain[1], currentGain[2], self._csPins[sensorNumA], self._spiLink))
		self.sensor.insert(sensorNumB, atm90e32_ctl(lineFreq, pgaGain, sensorBVolt, currentGain[3], currentGain[4], currentGain[5], self._csPins[sensorNumB], self._spiLink))

	def get_voltage(self, boardNum):
		if boardNum < 1 or boardNum > 7: raise ValueError("boardNum must be between 1 to 7 inclusive.")

		sensorNumA = (boardNum - 1) * 2
		sensorNumB = sensorNumA + 1
		
		return [self.sensor[sensorNumA].line_voltageA, self.sensor[sensorNumB].line_voltageA]

	def get_current(self, boardNum):
		if boardNum < 1 or boardNum > 7: raise ValueError("boardNum must be between 1 to 7 inclusive.")

		sensorNumA = (boardNum - 1) * 2
		sensorNumB = sensorNumA + 1
		
		return [self.sensor[sensorNumA].line_currentA, self.sensor[sensorNumA].line_currentB, self.sensor[sensorNumA].line_currentC, self.sensor[sensorNumB].line_currentA, self.sensor[sensorNumB].line_currentB, self.sensor[sensorNumB].line_currentC]

	def get_frequency(self, boardNum):
		if boardNum < 1 or boardNum > 7: raise ValueError("boardNum must be between 1 to 7 inclusive.")

		sensorNumA = (boardNum - 1) * 2
		sensorNumB = sensorNumA + 1
		
		return [self.sensor[sensorNumA].frequency, self.sensor[sensorNumB].frequency]
	
	def get_power_factor(self, boardNum):
		if boardNum < 1 or boardNum > 7: raise ValueError("boardNum must be between 1 to 7 inclusive.")

		sensorNumA = (boardNum - 1) * 2
		sensorNumB = sensorNumA + 1
		
		return [self.sensor[sensorNumA].power_factorA, self.sensor[sensorNumA].power_factorB, self.sensor[sensorNumA].power_factorC, self.sensor[sensorNumB].power_factorA, self.sensor[sensorNumB].power_factorB, self.sensor[sensorNumB].power_factorC]
		