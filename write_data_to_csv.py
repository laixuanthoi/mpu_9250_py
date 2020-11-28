import csv

num_sample = 1000
count = 0
prev_x= 0
prev_y= 0 
prev_z = 0
with open('zzz.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    while True:
        imu.readSensor()    
        # imu.computeOrientation()
        # print("roll: {0} ; pitch : {1} ; yaw : {2}: temp: {3}".format(imu.roll, imu.pitch, imu.yaw, imu.Temp))
        x, y, z = imu.MagVals
        int_x,int_y,int_z = int(x), int(y), int(z)
        if int_x != prev_x and int_y != prev_y and int_z!= prev_z:
            prev_x = int_x
            prev_y = int_y
            prev_z = int_z
            employee_writer.writerow([x,y,z])
            count += 1
            print(imu.MagVals, count)
        if count > num_sample:
            break
        time.sleep(0.01)