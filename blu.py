#!/usr/bin/python3

import serial
import obd
import time

def readFromELM(command):
  time.sleep(.05)
  connection = obd.OBD()
  fromELM = connection.query(command)
  #todo: figure out how to differ commands and convert speed to mph
  #print(command)
  print(fromELM.value.magnitude)
  magnitude = str(fromELM.value.magnitude)
  return magnitude;

#obd.logger.setLevel(obd.logging.DEBUG)
connection = obd.OBD()

while True:
  speed = obd.commands.SPEED
  rpm = obd.commands.RPM
  eng_temp = obd.commands.COOLANT_TEMP
  intake_temp = obd.commands.INTAKE_TEMP
  time.sleep(.05)
  if(connection.query(speed)):
    print(readFromELM(speed))       #data[0]
    print(readFromELM(rpm))        #data[1]
    print(readFromELM(eng_temp))    #data[2]
    print(readFromELM(intake_temp))



