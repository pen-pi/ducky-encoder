#!/usr/bin/env python2

import sys
from Scancodes import *  
import time 

class HIDReport:
   # https://gist.github.com/rmed/0d11b7225b3b772bb0dd89108ee93df0
   # http://www.freebsddiary.org/APC/usb_hid_usages.php

   def __init__():
      pass
   def setShift():
      pass
   def setCTRL():
      pass

def stringToReport():
   pass
   

def createReport():
   pass

def stringToReport(string):
   with open('/dev/hidg0', 'rb+') as fd:
      #fd.write(report.encode())
      for char in string:
         if char == '\n':
            continue
         if char in shiftedLetters:
            fd.write((SHIFT+NULL_CHAR+scancodes[char]+NULL_CHAR*5).encode())

         else:
            fd.write((NULL_CHAR*2+scancodes[char]+NULL_CHAR*5).encode())
         fd.write((NULL_CHAR*8).encode())
def keyCombo(string):
   with open('/dev/hidg0', 'rb+') as fd:
      #fd.write(report.encode())
      for char in string:
         if char == '\n':
            continue
         if char in shiftedLetters:
            fd.write((SHIFT+NULL_CHAR+scancodes[char]+NULL_CHAR*5).encode())

         else:
            fd.write((NULL_CHAR*2+scancodes[char]+NULL_CHAR*5).encode())
         fd.write((NULL_CHAR*8).encode())
      fd.close()


def displayHelp():
   print("Ducky Encoder for PenPi using Python 2.7")
   print("")
   print("Usage:")
   print("      ./ducky-encoder.py <ducky script>")
   print("")


def isInt(s):
   try: 
      int(s)
      return True
   except ValueError:
      return False



def processLine(line):
   toks = line.split(None, 1)
   if len(toks) >= 2:
      command, arguments = toks
      if arguments[len(arguments)-1] == '\n':
         arguments = arguments[0:len(arguments)-1] # removing the \n at the end
   else:
      command = toks[0]
      arguments = ''

   if command == "REM":
      print "Comment: ", arguments

   elif command == "DEFAULT_DELAY" or command == "DEFAULTDELAY":
      if isInt(arguments):
         # TODO set default delay to int
         print("TODO: set default value to "+arguments)
      else:
         sys.exit("Error line "+str(lineNUmb)+": argument of DEFAULT_DELAY has to be integer")

   elif command == "DELAY":
      #print("DELAY")
      if isInt(arguments):

         time.sleep(int(arguments)/1000.0)
      else:
         return False

   elif command == "STRING":
      stringToReport(arguments)

   elif command == "WINDOWS" or command == "GUI":
      argLen = len(arguments) 
      if argLen >= 2:
         sys.exit("Error in line "+str(lineNUmb)+". GUI can only have one CHAR as argument.")
      elif argLen == 0:
         with open('/dev/hidg0', 'rb+') as fd:
            fd.write((GUI+NULL_CHAR+NULL_CHAR*6).encode())
            fd.close()
      elif argLen == 1:
         with open('/dev/hidg0', 'rb+') as fd:
            fd.write((GUI+NULL_CHAR+scancodes[arguments]+NULL_CHAR*5).encode())
            fd.close()
      else:
         return False

   elif command == "MENU" or command == "APP":
      pass

   elif command == "SHIFT":
      pass

   elif command == "ALT":
      pass

   elif command == "CONTROL" or command == "CTRL":
      pass

   elif command == "DOWNARROW" or command == "DOWN":
      pass
   elif command == "LEFTARROW" or command == "LEFT":
      pass
   elif command == "RIGHTARROW" or command == "RIGHT":
      pass
   elif command == "UPARROW" or command == "UP":
      pass

   elif command == "BREAK" or command == "PAUSE":
      pass

   elif command == "CAPSLOCK":
      pass
   elif command == "DELETE":
      pass
   elif command == "END":
      pass
   elif command == "ESC" or command == "ESCAPE":
      pass
   elif command == "HOME":
      pass
   elif command == "INSERT":
      pass
   elif command == "NUMLOCK":
      pass
   elif command == "PAGEUP":
      pass
   elif command == "PAGEDOWN":
      pass
   elif command == "PRINTSCREEN":
      pass
   elif command == "SCROLLLOCK":
      pass
   elif command == "SPACE":
      pass
   elif command == "TAB":
      pass
   elif command == "ENTER":
      pass
   elif command == "REPEAT":
      pass
   else:
      print command
      return False
   return True




print chr(8)



print "length", len(sys.argv)
for arg in sys.argv:
   print arg



filename = sys.argv[1]

try:
   script = open(filename, "r")
except:
   sys.exit("Error: Can not open file")

lastLine = ""
for lineNUmb, line in enumerate(script, start=1):

   if not processLine(line):
      sys.exit("Error: Line " + str(lineNUmb) + ": Command not recognized\nQuiting now")
   else:
      lastLine = line
