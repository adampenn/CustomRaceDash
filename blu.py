#!/usr/bin/python3

import serial
import obd

#obd.logger.setLevel(obd.logging.DEBUG)
connection = obd.OBD()

while True:
  speed = obd.commands.SPEED
  RPM = obd.commands.RPM

  if(connection.query(speed)):
    sval = connection.query(speed)
    print(sval.value)
  if(connection.query(RPM)):
    rval = connection.query(RPM)
    print(rval.value)

