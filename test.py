import math

import matplotlib.pyplot as plt

stars = []
with open('C:\\Users\\lukas\\Downloads\\bsc5(1).dat\\bsc5.dat', 'r') as fi:
    for line in fi.readlines():
        name = line[4:14]

        try:
            mag = float(line[102:107])

            # Right ascension (hrs, mins, secs), equinox J2000, epoch 2000.0
            ra_hrs, ra_min, ra_sec = [float(x) for x in (line[60:62], line[62:64], line[64:66])]
            # Declination (hrs, mins, secs), equinox J2000, epoch 2000.0
            dec_deg, dec_min, dec_sec = [float(x) for x in (line[68:71], line[71:73], line[73:75])]
            # Convert both RA and declination to radians
            ra = math.radians((ra_hrs + ra_min/60 + ra_sec/3600) * 15.)
            dec = math.radians(dec_deg + dec_min/60 + dec_sec/3600)
            # Create a new Star object and add it to the list of stars
            stars.append((mag, ra, dec))
        except ValueError:
            # some stars do not have magnitudes: ignore these entries
            continue

list = []

for s in stars:
    list.append((math.cos(s[2])*math.cos(s[1]), math.cos(s[2])*math.sin(s[1]), math.sin(s[2])))

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(projection='3d')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

with open('moin.txt', 'w') as f:
    f.write(str(list))

print(list)

plt.show()