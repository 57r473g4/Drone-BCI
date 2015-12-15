from dronekit import *
from dronedirect import DroneDirect

SIM = False
running = True

print "connecting to drone..."
if SIM:
    vehicle = connect('tcp:127.0.0.1:5760', wait_ready=True)
else:
    vehicle = connect('0.0.0.0:14550', wait_ready=True) # connecting from GCS
    #vehicle = connect('udpout:127.0.0.1:14560', wait_ready=True) #connecting from onboard solo


dd = DroneDirect(vehicle)
dd.take_control()

if SIM:
    #arm and takeoff drone - DO NOT USE THIS ON A REAL DRONE ONLY IN SIMULATION
    if vehicle.armed == False:
        # Don't let the user try to arm until autopilot is ready
        print " Waiting for vehicle to initialise..."
        while not vehicle.is_armable:
            time.sleep(1)
        vehicle.armed   = True
        print 'Vehicle Armed'
    dd.takeoff()

try:
    while running:
        dd.enable_fence(alt_floor=50, alt_ceiling=100 , radius=10)
        dd.translate(x=1)

finally:
    dd.release()
