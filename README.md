# ArmstrongDataInsertion
Suite of code to generate, insert, and run data to test Armstrong system
## Process
  - execute dataGeneration.py, enter parameters
  - dataGeneration generates data for a function in floats, writeHex.c repackages floats into uint32_t so they can be 
  written to memory
  - this data is stored in test.txt, and a graphic of the function is display to ensure accuracy
  - when Armstrong device is programmed, post-build script is called by IAR, nested here is my writeData.bat script
  - this script copies fresh data from the network mounted folder, and executes myJlink.py
  - myJlink.py writes data to specified vacant memory
  - I reprogrammed the Armstrong device to then read from that address for data instead of from its sensors
This process allows for flexible and thorough testing of the Armstong waveform display, algorithms, and system 
response - all without relying on sensor conditions.
