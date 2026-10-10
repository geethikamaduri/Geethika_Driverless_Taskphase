import csv
import math
cones = []
with open('cones.csv','r') as file:
    reader = csv.DictReader(file)
    for row in reader:
       cone_data = {
           'cone_id' : row['cone_id'],
           'x' : float(row['x']),
           'y' : float(row['y']),
           'colour' : row['colour'].lower()
        }
       cones.append(cone_data)
sorted_cones = sorted(cones,key = lambda p: p['x']**2 + p['y']**2)
blue_cones = []
yellow_cones = []
for cone in sorted_cones:
    if cone['colour'] == 'blue':
        blue_cones.append(cone)
    elif cone['colour'] == 'yellow':
        yellow_cones.append(cone)
fieldnames = ['cone_id','x','y','colour']
with open('blue_cones.csv','w',newline='') as file:
    writer = csv.DictWriter(file,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(blue_cones)
with open('yellow_cones.csv','w',newline='') as file:
    writer = csv.DictWriter(file,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(yellow_cones)
centreline_points = []
for blue in blue_cones:
    closest_yellow = None
    shortest_distance = float('inf')
    for yellow in yellow_cones:
        dist = (blue['x']-yellow['x'])**2 + (blue['y']-yellow['y'])**2
        if dist < shortest_distance:
            shortest_distance = dist
            closest_yellow = yellow
    if closest_yellow is not None:
        mid_x = (blue['x'] + closest_yellow['x'])/2.0
        mid_y = (blue['y'] + closest_yellow['y'])/2.0
        centreline_points.append({
            'blue_id' : blue['cone_id'],
            'yellow_id' : closest_yellow['cone_id'],
            'x' : mid_x,
            'y' : mid_y
        })
centreline_headers = ['blue_id','yellow_id','x','y']
with open('centreline.csv','w',newline='') as file:
    writer = csv.DictWriter(file, fieldnames=centreline_headers) 
    writer.writeheader() 
    writer.writerows(centreline_points)         