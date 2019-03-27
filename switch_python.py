#!/bin/python3.6
import os
import subprocess
import getopt
import sys

#rep = int(input("Quel Jour ? "))
#week(rep)

def week(i):
        switcher={
                0:'Sunday',
                1:'Monday',
                2:'Tuesday',
                3:'Wednesday',
                4:'Thursday',
                5:'Friday',
                6:'Saturday'
             }
        print(switcher.get(i,"Invalid day of week"))

week(sys.argv[1])