#!/usr/bin/python3

# Griffin Saiia

import sys
import os
import matplotlib.pyplot as plt
import numpy as np
import struct
import tkinter
import subprocess

def main():
	line = input("Name of dataset: ")
	binPath = "/samba/mountedFolder/"+line+"Bin.txt"
	txtPath = "/samba/mountedFolder/"+line+".txt"
	line = input("Enter a freq: ")
	freq = int(line)
	line = input("Enter an amp: ")
	amp = int(line)
	data = genData(freq, amp)
	writeLog(binPath, txtPath, data)
	plot(data[0], data[1], freq, amp)
	# display the plot
	plt.show()

def genData(freq, amp):
	fs = 50.0 # sample rate
	numSamples = 2*60*fs # 2 min * 60 s/min * 50 samples/second
	x = np.arange(numSamples)
	y = [ ((amp * np.sin(2*np.pi*freq*(i/fs))) + 2.0) for i in x]
	samples = [x, y]
	return samples

def plot(x, y, freq, amp):
	x1 = []
	y1 = []
	# plot first 50 points
	i = 0
	while(i < 100):
		x1.append(x[i])
		y1.append(y[i])
		i += 1
	plt.stem(x1,y1, 'r', bottom=2)
	plt.plot(x1, y1)
	# label the axes
	plt.ylabel("y")
	plt.xlabel("x")
	# set the title
	plt.title("Sample Data: Freq "+str(freq)+", Amp "+str(amp))

def writeLog(binPath, txtPath, data):
	i = 0
	with open(txtPath, "w+") as file:
		for y in data[1]:
			yIn = toString(y)
			file.write(yIn+"_")
			i += 1
		file.write("\n")
	file.close()
	print(str(i)+" data points\n")
	command = "./writeHex.o"
	output = subprocess.check_output(command, shell = True)
	print(output)

def toString(num):
	return '%.2f' % num

# to run it from command line
if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("")
		print('Interrupted')
		try:
			sys.exit(0)
		except SystemExit:
			os._exit(0)
