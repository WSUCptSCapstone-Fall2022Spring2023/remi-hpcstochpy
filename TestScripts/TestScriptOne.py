import stochpy
import time

smod = stochpy.SSA()
start_time = time.time()
smod.DoStochSim(trajectories=1, end=1000000, mode='steps', use_jit=True)
end_time = time.time()
print("StochSim time: ", end_time - start_time, " seconds")
