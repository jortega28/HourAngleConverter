#This small program will convert Hour angles to degrees and radians
import sys
import decimal

def main():
    HA = getHA()
    hour = float(HA[0:2])
    min = float(HA[3:5])
    sec = float(HA[6:11])
    degrees = float(0)
    degrees = degrees+(hour*15.0)
    mod = min/60.0
    degrees = degrees+(mod*15.0)
    mod = sec/3600.0
    degrees = degrees+(mod*15.0)
    print("In degrees:\n" + str(degrees))
    radians = 0.0
    degtoradmod = 0.01745329252
    radians = radians+(degrees*degtoradmod)
    print("In radians:\n" + str(radians))

def getHA():
    print("When entering your hour angle please enter it in the following format 00:00:00.00\nDon't forget to include the zeros, for example use 04 rather than just 4")
    HA = raw_input("Enter your HA below:\n")
    if len(HA) != 11:
        sys.exit("Incorrect hour angle format! Should be in the following format 00:00:00.00")
    return HA

main()