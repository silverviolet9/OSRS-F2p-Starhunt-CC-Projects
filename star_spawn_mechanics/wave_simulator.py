''' 
Wave generator simulates star spawns and variances and calculates and plots the averages.
It's fairly accurate but still likely needs tuning to improve accuracy. 
Note that generated data is not saved, only whatever charts you save manually,
 and information you print to your terminal of course.
Every run instance we will produce all new data for the given number of worlds and waves.

You are encouraged to adjust the number of waves and worlds which are represented by the
 variables "waves" and "worlds" respectively. Also, the height, "height", of the graph.
Play around with the print statements to view additional relevant data.

Default data simulation suggestion worlds=298, waves=108, height=26
Realistic data simulation suggestion worlds=49, waves=3, height=10
You may want to edit the worlds, 49 F2p worlds (excluding PVP). 298 is total number of servers.
108 waves in a week, 10,080 minutes per week / 93 minutes per wave.
Since it's producing the data that is essentially assuming a recorded spawn time.
You may want to edit this number to simulate a more realistic number of data entries.
You can adjust the height for better visuals if needed.
'''
import numpy as np
import matplotlib.pyplot as plt

# Change me
worlds = 298
waves = 108
height = 26

# Creates SEED or ANCHOR times for each world that stars will be SOFT bounded by.
# THIS IS NOT THE FIRST WAVE.
while True:
    valid = True
    # Star seeds is a list of float numbers generated randomly according to normal distribution parameters.
    # loc is the mean, scale is the standard deviation, size is the number of worlds in this case.
    star_seeds = np.random.normal(loc=22.5, scale=7.5, size=worlds)
    for spawn in star_seeds:
        if spawn < 0 or spawn > 45:
            valid = False
            break
    if valid:
        break

# List of averages of variances over 108 waves for each world.
star_spawns = []
count = 0
for wave in range(waves):
    for i in range(len(star_seeds)):
        # When no size argument is given to np.random.normal() it generates 1 number.
        variance = np.random.normal(loc=0, scale=5)
        spawn_variance = star_seeds[i] + variance
        if spawn_variance < 0 or spawn_variance > 45:
            # Remove # on line below to see all out of bounds variances
            #print(spawn_variance)
            count += 1
        if len(star_spawns) == len(star_seeds):
            star_spawns[i].append(spawn_variance)
        else:
            # Create list of lists; list of each world, list of variances in each world.
            # Notice the averages DO NOT include the initial seed time. Very important.
            star_spawns.append([spawn_variance])

# See number of variances beyond boundaries to gauge viability of idea.     
print(f"Number of out of bounds variances: {count}")
percent = round(100*count / (waves * worlds), 2)
print(f"That is {percent}% of all star spawns.")

# Gives us a clean average for all data produced similar to how it would look in the Google Sheet averages.
star_averages = [round(sum(variances) / len(variances)) for variances in star_spawns]

# Remove # on print() lines to observe the two main lists.
#print(star_seeds)
#print(star_averages)
''' Notice how close the averages get to the SEED time if you managed to collect all poofs in a week.
You can play with the number of waves which in this case is essentially number of poofs collected.
There will be a rough threshhold point on how many data points we need to "know" the SEED time. 
Even with only 2 data entries the results are pretty remarkably close for many worlds.
Every further data entry adds substantial progress towards finding the SEED time. 
Notice this is due to the properties of the normal distribution of the variance, and from this we
can deduce that repeat number entries are a strong indicator you are close to the SEED time. 
'''

# If you want to see the whole raw data list for the week, it's an eyesore but can be helpful to see.
# Just try to ignore the np.float64 spam and trailing decimals. Use small # of waves and worlds and 
#  look for square brackets indicating a list containing all the variances for a single world.
#print(star_spawns)

# Plot
bins = np.arange(-10, 55) - 0.5
plt.hist(star_averages, bins=bins, edgecolor='black')
plt.xlabel("Time into Wave")
plt.ylabel("Number of star spawns")
plt.title(f"Distribution of star spawn averages over {waves} waves")
plt.grid(axis='y', linestyle='--')
plt.xticks(range(-10, 55, 5))
plt.xlim([-10, 55])
plt.yticks(range(0, height, 2))
plt.ylim([0, height])
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
