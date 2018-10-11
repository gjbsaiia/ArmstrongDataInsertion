set OUT=%1.out
set HEX=%1.hex
set BIN=%1.bin

:: calculate checksum of the application
ielftool --fill 0xFF;0x08005000-checksum_end+3 --checksum ielftool_checksum:2,crc16,0x0;0x08005000-checksum_end+3 --verbose %OUT% %OUT%

:: generate additional ouput: hex
ielftool.exe --ihex --verbose %OUT% %HEX%

:: generate additional ouput: binary
ielftool.exe --bin --verbose %OUT% %BIN%

:: move transfer data
myJlink.py
