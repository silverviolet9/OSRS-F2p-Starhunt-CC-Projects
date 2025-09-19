''' 
This program simulates star spawns and their variances and calculates and plots useful data.
This simulator is quite accurate, but may still need some fine tuning for complete accuracy. 
Note that generated data is not saved, only whatever graphs you save manually,
 and information you print to your terminal of course.
Every run instance we will produce all new data for the given number of worlds and waves.
It's expected you run this program at least several times to see varying results.

You are encouraged to adjust the number of waves and worlds which are represented by the
 variables "waves" and "worlds" respectively. Also, the height, "height", of the graph.
It's useful to know that there are 50 F2p worlds and 298 worlds total.
There are 108 waves in a week; 10,080 minutes per week / 93 minutes per wave.

Play around with the print statements to view additional relevant data.
The default graph uses star_averages, but you can set it to use star_spawns instead.
You will also want to adjust the height of the graph for better visuals.
For plotting star_averages, the number of worlds will affect the height needed for the graph.
For plotting star_spawns, the number of worlds and waves will affect the height needed.

Since it's producing the data, it is essentially assuming a recorded spawn time.
Therefore, 1-5 waves will produce data similar to what may be recorded and observed.
108 waves will demonstrate the Normal Distribution curve well enough, but you can do more.
Higher waves numbers will produce even clearer distribution curves, but will take longer to graph.
Default data simulation suggestion worlds=298, waves=108, height=26
Realistic data simulation suggestion worlds=49, waves=3, height=10
'''
import numpy as np
import matplotlib.pyplot as plt

# Change me
worlds = 298
waves = 108
height = 26

# If you want to reproduce the same data and graph each time.
# Generally leave this commented out to preserve the variation intended for each dataset.
#np.random.seed(42)


# Creates SEED or ANCHOR times for each world so that stars will be SOFT bounded by +-15 the seed.
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

# List of star spawns with their variances for 108 waves in each world.
star_spawns = []
count = 0
for wave in range(waves):
    for i in range(len(star_seeds)):
        ''' Variance creates the +-15 SOFT boundary around each seed time.
        The boundary is soft because normal distributions have loose boundaries and
         there's no code used to create hard boundaries between 0-45.
        This is in accordance with observations in game and may change over time with
         improved observed data that may indicate some kind of hard boundaries.
        '''
        # When no size argument is given to np.random.normal() it generates 1 number.
        variance = np.random.normal(loc=0, scale=5)
        spawn_variance = star_seeds[i] + variance
        # You can adjust the boundaries here to see the number and % of stars outside them.
        # < 7.5 and > 37.5 will show number of stars in the 3 standard deviations range in
        #  reference to the seeded normal distribution. 
        if spawn_variance < 7.5 or spawn_variance > 37.5:
            # Remove # on line below to see all out of bounds variances
            #print(spawn_variance)
            count += 1
        if len(star_spawns) == len(star_seeds):
            star_spawns[i].append(spawn_variance)
        else:
            # Create list of lists; list containing list of variances for each world.
            # Notice the averages DO NOT include the initial seed time. Very important.
            star_spawns.append([spawn_variance])

# See number of variances beyond 0-45 boundaries.    
print(f"Number of out of bounds variances: {count}")
percent = round(100*count / (waves * worlds), 2)
print(f"That is {percent}% of all star spawns.")

# Gives us a clean average for all data produced similar to how it would look in the Google Sheet averages.
star_averages = [round(sum(variances) / len(variances)) for variances in star_spawns]

# Remove # on print() lines to observe the two main lists.
#print(star_seeds)
#print(star_averages)
''' Notice how close the averages get to the SEED time if you managed to collect all poofs in a week.
You can play with the number of waves which in this case is essentially the number of poofs collected.
There will be a rough threshhold point on how many data points we need in order to "know" the SEED time. 
Even with only 2 data entries, the results are pretty remarkably close to the seed for many worlds.
Every data entry adds substantial progress towards finding the SEED time. 
Notice this is due to the properties of the normal distribution used for the variance, and from this we
can deduce that repeat number entries are a strong indicator you are close to the SEED time. 
'''

''' If you want to see the whole raw data list for the week, it's an eyesore but can be helpful to see.
Just try to ignore the np.float64 spam and trailing decimals. Use a small number of waves and worlds and 
look for square brackets indicating a list containing all the variances for a single world.
You can also plugin star_spawns in place of star_averages in the plt.hist() line of the Plot code below.
Rather than a nice looking average it will show the raw data plotted; which is every single star fall.
'''
#print(star_spawns)

# Plot
bins = np.arange(-20, 65) - 0.5
plt.hist(star_averages, bins=bins, edgecolor='black')
plt.xlabel("Time into Wave")
plt.ylabel("Number of star spawns")
plt.title(f"Distribution of star spawn averages over {waves} waves")
plt.grid(axis='y', linestyle='--')
plt.xticks(range(-20, 65, 5))
plt.xlim([-20, 65])
plt.yticks(range(0, height, 2))
plt.ylim([0, height])
plt.show()





''' TEST CODE FOR FREE MOVEMENT, DISTRIBUTION WAS TOO WIDE. Flattened distribution.
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

''' TESTED RANDINTS 15-30 THEN NORMAL VARIANCE BUT DISTRIBUTION WAS TOO NARROW.
import random
star_spawn = []
for _ in range(298):
    star_spawn.append(random.randint(15, 30))
'''
