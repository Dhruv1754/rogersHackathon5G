import matplotlib.pyplot as plt
import csv

x1=[]
y1=[]

x2 = []
y2 = []

x3 = []
y3 = []

x4 = []
y4 = []

x5 = []
y5 = []

x6 = []
y6 = []

x7 = []
y7 = []

x8 = []
y8 = []

x9 = []
y9 = []

x10 = []
y10 = []

div = 300


with open('./ZonesDensity/z1.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for index, row in enumerate(plots): 
        if(index % div == 0):
            x1.append(int(row[0]))
            y1.append(int(row[1]))    

x1 = [thing/1000 for thing in x1]

with open('./ZonesDensity/z2.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for index, row in enumerate(plots): 
        if(index % div == 0):
            x2.append(int(row[0]))
            y2.append(int(row[1]))    

x2 = [thing/1000 for thing in x2]

with open('./ZonesDensity/z3.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for index, row in enumerate(plots): 
        if(index %div == 0):
            x3.append(int(row[0]))
            y3.append(int(row[1]))    

x3 = [thing/1000 for thing in x3]

with open('./ZonesDensity/z4.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for index, row in enumerate(plots): 
        if(index %div == 0):
            x4.append(int(row[0]))
            y4.append(int(row[1]))    

x4 = [thing/1000 for thing in x4]

with open('./ZonesDensity/z5.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for index, row in enumerate(plots): 
        if(index %div == 0):
            x5.append(int(row[0]))
            y5.append(int(row[1]))    

x5 = [thing/1000 for thing in x5]

with open('./ZonesDensity/z6.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for index, row in enumerate(plots): 
        if(index %div == 0):
            x6.append(int(row[0]))
            y6.append(int(row[1]))    

x6 = [thing/1000 for thing in x6]

with open('./ZonesDensity/z7.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for index, row in enumerate(plots): 
        if(index %div == 0):
            x7.append(int(row[0]))
            y7.append(int(row[1]))    

x7 = [thing/1000 for thing in x7]

with open('./ZonesDensity/z8.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for index, row in enumerate(plots): 
        if(index % div== 0):
            x8.append(int(row[0]))
            y8.append(int(row[1]))    

x8 = [thing/1000 for thing in x8]

with open('./ZonesDensity/z9.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for index, row in enumerate(plots): 
        if(index %div == 0):
            x9.append(int(row[0]))
            y9.append(int(row[1]))    

x9 = [thing/1000 for thing in x9]

with open('./ZonesDensity/z10.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for index, row in enumerate(plots): 
        if(index % div == 0):
            x10.append(int(row[0]))
            y10.append(int(row[1]))    

x10 = [thing/1000 for thing in x10]


plt.plot(x1,y1, label = "zone 1",  marker='o')
plt.plot(x2,y2, label = "zone 2",  marker='o')
plt.plot(x3,y3, label = "zone 3",  marker='o')
plt.plot(x4,y4, label = "zone 4",  marker='o')
plt.plot(x5,y5, label = "zone 5",  marker='o')
plt.plot(x6,y6, label = "zone 6",  marker='o')
plt.plot(x7,y7, label = "zone 7",  marker='o')
plt.plot(x8,y8, label = "zone 8",  marker='o')
plt.plot(x9,y9, label = "zone 9",  marker='o')
plt.plot(x10,y10, label = "zone 10",  marker='o')


plt.xlim(left = 22, right = 34)

plt.title('Density of All Occupied Zones 1-10 Versus Time')

plt.xlabel('Time')
plt.ylabel('Density Zone')

plt.grid(which = 'both')

plt.legend()
plt.show()

