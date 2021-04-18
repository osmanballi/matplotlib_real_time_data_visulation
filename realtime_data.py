import csv
import random 
import time

x_value = 0
y1_value = 100
y2_value = 100

fieldnames = ["x_value","y1_value","y2_value"]

with open('data.csv',"w") as csv_file:
    csv_writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
    csv_writer.writeheader()

while True:
    with open("data.csv","a") as csv_file:
        csv_writer=csv.DictWriter(csv_file,fieldnames=fieldnames)

        info = {
            "x_value" : x_value,
            "y1_value" : y1_value,
            "y2_value" : y2_value
        }

        csv_writer.writerow(info)
        print(x_value, y1_value, y2_value)

        x_value += 1
        y1_value = y1_value + random.randint(-5,5)
        y2_value = y2_value + random.randint(-5,5)
        
    time.sleep(1)


