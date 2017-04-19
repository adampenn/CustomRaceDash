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
    value = "S" + str(sval.value.magnitude)
    print(value)

