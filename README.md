# EternalZerp

This script generates random data and writes it to hard drives and storage devices on Linux systems. 
It is intended for educational purposes only and should NOT be run on any system that contains important data. Use it at your own risk.

# Requirements
Python 3.x
Linux operating system (tested on Ubuntu 20.04 LTS)

# Usage
1. python3 random_data_writer.py
- If the script generates a random number that is not zero, it will print "OK, Good" and exit.
- If the script generates a random number that is zero, it will start writing random data to all files starting with 'sd' or 'nv' in the /dev/ directory. 
- This could take a long time depending on the size of the hard drives and storage devices connected to your system.

# Notes
- The amount of data written to each file is fixed at 4096 bytes.
- This script has only been tested on Ubuntu 20.04 LTS, so it may not work on other Linux distributions.
- The script requires root privileges to access the /dev/ directory and write to the files. You may need to run it as root using the sudo command.


