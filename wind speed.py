from gpiozero import Button
import math
import time
import statistics 

#Variables
wind_count = 0 #counts how many half rotations 
radius_cm = 9.0 #radius of aneometers (cm)
wind_interval = 5  #how often to report speed (seconds)  
CM_IN_A_KM = 100000.0
SECS_IN_AN_HOUR = 3600

ADJUSTMENT = 1.18 

#lists

store_speeds = []

def spin():
    global wind_count
    wind_count = wind_count + 1
#    print("spin" + str(wind_count))


def calculate_speed(time_sec):
    global wind_count
    circumference_cm = (2* math.pi) * radius_cm
    rotations = wind_count /2.0
    
    dist_km = (circumference_cm * rotations)/ CM_IN_A_KM 
    
    km_per_sec = dist_km/time_sec
    km_per_hour = km_per_sec * SECS_IN_AN_HOUR

    return km_per_hour * ADJUSTMENT 


def reset_wind():
    global wind_count
    wind_count = 0

wind_speed_sensor = Button(5) 
wind_speed_sensor.when_pressed = spin
#changes when there is a new high speed (wind gust) 
maxspeed = 0
while True:
    start_time = time.time()
    while time.time() - start_time <= wind_interval:
        reset_wind()
        time.sleep(wind_interval)
        final_speed = calculate_speed(wind_interval)
        store_speeds.append(final_speed)
    if max(store_speeds)>maxspeed:
        maxspeed = max(store_speeds) 
#wind gust is max speed which changes when there is a new "max" or high speed
    wind_gust = maxspeed 
    wind_speed = statistics.mean(store_speeds)   
    print(wind_speed,"kmh", wind_gust,"kmh")
    store_speeds.clear()  
      
