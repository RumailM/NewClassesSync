import os
import csv
sheet = list(csv.reader(open("classes.csv")))

netid = sheet[1][1] #NetID
numrows = int(sheet[1][0])
user = " -e skip --username " + netid
down = " --download davs://newclasses.nyu.edu/dav/"
prefix = "duck"

for i in range(1,(numrows+1)):
	print("syncing "+ sheet[i][2])
	location = sheet[i][4]
	full = prefix + user + down + sheet[i][3] +'/ '+ location
	os.system(full)


	




