import numpy as np
import matplotlib.pyplot as plt

# Create first wave spawns for all worlds, make sure they are >= 0 to avoid possible fatal errors on startup.
while True:
    valid = True
    star_spawn = np.random.normal(loc=22.5, scale=7.5, size=298)
    for spawn in star_spawn:
        if spawn < 0:
            valid = False
            break
    if valid:
        break

# 108 waves in a week, 10,080 minutes per week / 93.
waves = 108
# List of averages of variances over 108 waves for each world.
star_averages = []
for wave in range(waves):
    for i in range(len(star_spawn)):
        variance = round(np.random.normal(loc=0, scale=5))
        spawn_variance = star_spawn[i] + variance
        if len(star_averages) == len(star_spawn):
            star_averages[i].append(spawn_variance)
        else:
            star_averages.append([spawn_variance])

star_averages = [round(sum(variances) / len(variances)) for variances in star_averages]
#print(star_averages)

# Plot
bins = np.arange(-10, 55) - 0.5
plt.hist(star_averages, bins=bins, edgecolor='black')
plt.xlabel("Time into Wave")
plt.ylabel("Number of star spawns")
plt.title(f"Distribution of star spawn averages {waves}")
plt.grid(axis='y', linestyle='--')
plt.xticks(range(-10, 55, 5))
plt.xlim([-10, 55])
plt.yticks(range(0, 26, 2))
plt.ylim([0, 26])
plt.show()



''' TEST CODE FOR FREE MOVEMENT, DISTRIBUTION WAS TOO WIDE. Binary boundaries, either too much or too little.
star_spawn_list = list(map(round, star_spawn))
star_spawn_list = [round(spawn) for spawn in star_spawn]


for _ in range(108):
    for i in range(len(star_spawn_list)):
        while True:
            variance = round(np.random.normal(loc=0, scale=5))
            next_spawn = star_spawn_list[i] + variance
            if next_spawn >= 0 and next_spawn <= 45:
                break
        star_spawn_list[i] += variance
'''

''' TESTED RANDINTS 15-30 THEN NORMAL VARIANCE BUT DISTRIBUTION WAS TOO NARROW
import random
star_spawn = []
for _ in range(298):
    star_spawn.append(random.randint(15, 30))
'''
