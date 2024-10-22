#! /usr/bin/env python
import os
import sys
import time
import smbus
import numpy as np

from imusensor.MPU9250 import MPU9250
from imusensor.filters import kalman 

address = 0x69
bus = smbus.SMBus(1)
imu = MPU9250.MPU9250(bus, address)
imu.begin()
imu.caliberateAccelerometer()
imu.caliberateMagPrecise()
imu.saveCalibDataToFile("/home/comlab/calibrated.json")
# imu.loadCalibDataFromFile("calibrated.json")

# while True:
#     imu.readSensor()
#     imu.computeOrientation()
#     print(imu.roll//1, imu.pitch//1, imu.yaw//1)
#     time.sleep(0.1)

# sensorfusion = kalman.Kalman()
# imu.readSensor()
# imu.computeOrientation()
# sensorfusion.roll = imu.roll
# sensorfusion.pitch = imu.pitch
# sensorfusion.yaw = imu.yaw

# count = 0
# currTime = time.time()                 
# while True:
#     imu.readSensor()
#     imu.computeOrientation()
#     newTime = time.time()
#     dt = newTime - currTime
#     currTime = newTime
#     sensorfusion.computeAndUpdateRollPitchYaw(imu.AccelVals[0], imu.AccelVals[1], imu.AccelVals[2], imu.GyroVals[0], imu.GyroVals[1], imu.GyroVals[2], imu.MagVals[0], imu.MagVals[1], imu.MagVals[2], dt)
#     # print(abs(imu.yaw//1), abs(sensorfusion.yaw//1))
#     print(sensorfusion.roll//1,sensorfusion.pitch//1,abs(sensorfusion.yaw//1-180))
#     time.sleep(0.05)