import numpy as np
from numba import njit
import dask
import time

# Parameter Values
prey = 60
predator = 30
alpha = 10
gamma = 1
mu = 1
beta = 0.45
delta = 0.1
K_prey = 100
K_predator = 150
end_time = 100

def Simulation(t, Prey, Predator) -> None:
    #simulation
    while t < end_time:

        #calculate rates for events
        rates = np.array([Prey*Predator*beta, Prey*alpha*(1-(Prey/K_prey)),
                Predator*Prey*delta*(1-(Predator/K_predator)),
                Predator*gamma*(1-(Predator/K_predator)), Predator*mu*(1-(Predator/K_predator))])
        
        #sum of rates for determining tau
        rates_sum = np.sum(rates)

        #determine tau
        if(rates_sum == 0):
            break

        tau = np.random.exponential(scale=1/rates_sum)

        #update timestep
        t += tau

        #determine reaction
        random_number = np.random.uniform(0,1)
        random_reaction = random_number*rates_sum

        #handle reaction
        if(random_reaction < rates[0]):
            Prey -= 1
        elif(random_reaction > rates[0] and random_reaction < rates[0] + rates[1]):
            Prey += 1
        elif(random_reaction > rates[0] + rates[1] and random_reaction < rates[0] + rates[1] + rates[2]):
            Predator += 1
        elif(random_reaction > rates[0] + rates[1] + rates[2] and random_reaction < rates[0] + rates[1] + rates[2] + rates[3]):
            Predator -= 1
        elif(random_reaction > rates[0] + rates[1] + rates[2] + rates[3]):
            Predator += 1
    
    #print(t, Prey, Predator)

start = time.time()
for i in range(1000000):
    Simulation(0, prey, predator)
    print("Simulation %i of %i complete" % (i+1, 1000000))
end = time.time()
print(end - start)

#reactions for reference
# # Prey Reactions
# R1:
# 	prey > $pool
# 	prey*predator*beta

# R2:
# 	$pool > prey
# 	prey*alpha*(1-(prey/K_prey))

# # Predator Reactions (from consumption of prey)
	
# R3:
# 	$pool > predator
# 	predator*prey*delta*(1-(predator/K_predator))

# # Predator Reactions (from intrinsic birth/death rates)

# R4:
#     predator > $pool
#     predator*gamma*(1-(predator/K_predator))

# R5:
#     $pool > predator
#     predator*mu*(1-(predator/K_predator))