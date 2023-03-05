import time
import stochpy

# times a simple simulation
smod = stochpy.SSA()
start_time = time.time()
smod.DoStochSim(trajectories=1, end=1000000, mode='steps')
end_time = time.time()
print("StochSim time: ", end_time - start_time, " seconds")