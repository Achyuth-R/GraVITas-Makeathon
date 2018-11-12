import picamera
import RPi.GPIO as IO
IO.setmode(IO.BOARD)
IO.setup(40,IO.OUT)
IO.output(40,1)
IO.setup(38,IO.OUT)
IO.output(38,1)    
cam = picamera.PiCamera()
for i in xrange(1,51):
	cam.capture( '%d.jpg' %i)

