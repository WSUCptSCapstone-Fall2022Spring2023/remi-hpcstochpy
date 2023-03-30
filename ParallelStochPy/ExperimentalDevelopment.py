import numpy
import random
from numba import njit
from dask import delayed

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

@delayed
def Simulation(t, preyc, predc) -> None:
    #simulation
    while t[-1] < end_time:

        #get current count of prey and predator
        Prey = preyc[-1]
        Predator = predc[-1]

        #calculate rates for events
        rates = [Prey*Predator*beta, Prey*alpha*(1-(Prey/K_prey)),
                Predator*Prey*delta*(1-(Predator/K_predator)),
                Predator*gamma*(1-(Predator/K_predator)), Predator*mu*(1-(Predator/K_predator))]
        
        #sum of rates for determining tau
        rates_sum = sum(rates)

        #determine tau
        if(rates_sum == 0):
            break
        tau = numpy.random.exponential(scale=1/rates_sum)

        #add new timestep
        t.append(t[-1] + tau)

        #determine reaction
        random_number = random.uniform(0,1)
        random_reaction = random_number*rates_sum

        if(random_reaction < rates[0]):
            preyc.append(preyc[-1] - 1)
            predc.append(predc[-1])
        elif(random_reaction > rates[0] and random_reaction < rates[0] + rates[1]):
            preyc.append(preyc[-1] + 1)
            predc.append(predc[-1])
        elif(random_reaction > rates[0] + rates[1] and random_reaction < rates[0] + rates[1] + rates[2]):
            predc.append(predc[-1] + 1)
            preyc.append(preyc[-1])
        elif(random_reaction > rates[0] + rates[1] + rates[2] and random_reaction < rates[0] + rates[1] + rates[2] + rates[3]):
            predc.append(predc[-1] - 1)
            preyc.append(preyc[-1])
        elif(random_reaction > rates[0] + rates[1] + rates[2] + rates[3]):
            predc.append(predc[-1] + 1)
            preyc.append(preyc[-1])

    print(t[-1])
    print(preyc[-1])
    print(predc[-1])

x = Simulation([0], [prey], [predator])
for i in range(1000):
    x = x + Simulation([0], [prey], [predator])
    print("simulated")
x.compute()









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