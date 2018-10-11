#!python
import pylink
import sys
import os

def main():
	serial_no = "158001796"
	chip_name = "STM32F103RE"
	path = "test.txt"
	sampleData = readData(path)
	print("data transferred")
	jlink = pylink.JLink()
	jlink.open(serial_no)
	print("jlink open")
	jlink.connect(chip_name, verbose=True)
	print("connected")
	wroteBytes = jlink.memory_write(addr=0x08060000, data=sampleData, nbits=32)
	#0x0807FFFF
	print(str(wroteBytes)+" of data written")
	jlink.reset()

def readData(path):
	with open(path, "r") as file:
		lines = file.readlines()
	file.close()
	data = []
	for line in lines:
		splitted = line.split("\n")[0]
		data += splitted.split(' ')
	floatData = []
	for each in data:
		try:
			floatData.append(int(each))
		except ValueError:
			i = 0
	return floatData

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
