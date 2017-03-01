from appJar import gui

# function called by pressing the buttons
app=gui()
app.setGeometry("1000x700")
app.setFont(20)
app.addMeter("RPM")
app.addMeter("MPH")
app.addScale("scale")
app.go()

while True:
  app.setMeter("RPM", app.getScale("scale"), text=None)
  
