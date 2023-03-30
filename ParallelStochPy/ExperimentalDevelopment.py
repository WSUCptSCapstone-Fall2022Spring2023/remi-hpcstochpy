import numpy as np
from numba import njit
import time

# Parameter Values
prey = 6
predator = 3
alpha = 10
gamma = 1
mu = 1
beta = 0.45
delta = 0.1
K_prey = 10
K_predator = 15
end_time = 100

@njit
def Simulation(t : np.array, preyc : np.array, predc : np.array) -> None:
    #simulation
    while t[-1] < end_time:

        #get current count of prey and predator
        Prey = preyc[-1]
        Predator = predc[-1]

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

        #add new timestep
        t = np.append(t, t[-1] + tau)

        #determine reaction
        random_number = np.random.uniform(0,1)
        random_reaction = random_number*rates_sum

        if(random_reaction < rates[0]):
            preyc = np.append(preyc, preyc[-1] - 1)
            predc = np.append(predc, predc[-1])
        elif(random_reaction > rates[0] and random_reaction < rates[0] + rates[1]):
            preyc = np.append(preyc, preyc[-1] + 1)
            predc = np.append(predc, predc[-1])
        elif(random_reaction > rates[0] + rates[1] and random_reaction < rates[0] + rates[1] + rates[2]):
            predc = np.append(predc, predc[-1] + 1)
            preyc = np.append(preyc, preyc[-1])
        elif(random_reaction > rates[0] + rates[1] + rates[2] and random_reaction < rates[0] + rates[1] + rates[2] + rates[3]):
            predc = np.append(predc, predc[-1] - 1)
            preyc = np.append(preyc, preyc[-1])
        elif(random_reaction > rates[0] + rates[1] + rates[2] + rates[3]):
            predc = np.append(predc, predc[-1] + 1)
            preyc = np.append(preyc, preyc[-1])

    # print(t[-1])
    # print(preyc[-1])
    # print(predc[-1])
    print("Simulated")

start = time.time()
for i in range(500):
    Simulation(np.array(0), np.array(prey), np.array(predator))
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