import time
import board
import busio
import adafruit_adxl34x as adxl
import matplotlib.pyplot as plt
from datetime import datetime as dt

log_start_time = dt.now().isoformat()
starttime = time.time()
runtime = 5

i2c = busio.I2C(board.SCL, board.SDA)
accelerometer = adxl.ADXL345(i2c)
accelerometer.data_rate = adxl.DataRate.RATE_1600_HZ 

datfile_name = log_start_time + ".csv"
datfile = open(datfile_name,"a")

#datfile.write(log_start_time + "\n")

x = []
y = []
z = []
while True:
    x_val,y_val,z_val = accelerometer.acceleration
    datfile.write(str(x_val)+","+str(y_val)+","+str(z_val)+"\n")
    x.append(x_val)
    y.append(y_val)
    z.append(z_val)
    if time.time() >= starttime + runtime:
        break

#log_end_time = dt.now().isoformat()  
#datfile.write(log_end_time)
datfile.close()

plt.plot(x,linewidth=0.5,label='x')
plt.plot(y,linewidth=0.5,label='y')
plt.plot(z,linewidth=0.5,label='z')
plt.legend(loc="upper right")
plt.ylabel(r"Acceleration $(m/s^2)$")
plt.show()

    
