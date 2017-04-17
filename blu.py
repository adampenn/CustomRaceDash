#!/usr/bin/python3

import obd

connection = obd.OBD()

while True:
  speed = obd.commands.SPEED

  response = connection.query(speed)

  print(response.value) # returns unit-bearing values thanks to Pint
  print(response.value.to("mph")) # user-friendly unit conversions
