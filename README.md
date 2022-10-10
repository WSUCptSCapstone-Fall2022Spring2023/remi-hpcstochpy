# Simulation Library Optimization and Parallelization of Stochastic Simulation Code for Computational Epidemiology

## Project Summary

### Parallelizing the StochPy stochastic simulation library to facilitate the activities of the Washington State University Resistance Epidemiology Modeling Initiative (REMI)

REMI conducts simulations modeling epidemics, particularly in smaller populations and focused on the beginning and end of epidemics. Such models can help with preventing and containing present and future epidemics and as such are of great utility. Most of the major tools for disease modeling in the field are deterministic, which function well for large population sizes. However, since the REMI lab focuses most of their research around smaller populations, a stochastic modeling tool is preferred, as stochastic models are superior for use in small populations [1]. Unfortunately, the tools for such modeling methods are not as highly developed as would be ideal for a research field as important as epidemiology. 

The shortcoming of StochPy is that the stochastic simulation algorithm is slow, especially when trying to perform large computations with upwards of 10 million groups of simulations. As such, our aim is to create an optimized and parallelized fork of the StochPy library. This library is used by REMI to conduct stochastic simulations in computational chemistry, physics, epidemiology, and ecology. The stochastic simulation algorithm is also embarrassingly parallel, which means that if the codebase were refactored to run the simulations on many cores at once, the amount of time for a job to complete would be drastically reduced [2].

(Please refer to the project report for citation references.)

## Installation

### Prerequisites

	Python 2.6+ or Python 3.4+
	NumPy 1.x+
	SciPy
	Matplotlib (optional)
	libsbml (optional)
	libxml2 (optional)
	mpmath (optional)

### Add-ons

(None.)

### Installation Steps

Install StochPy and dependencies with PIP using the following command (in your StochPy Python virtual environment):

pip install scipy matplotlib python-libsbml jedi==0.17.2 ipython stochpy

If you are using Anaconda, create a custom conda environment for StochPy, for example:

conda create -n "stochpy39" -c sbmlteam python=3.9 pip scipy matplotlib sympy ipython

Activate your new environment, install StochPy (only required once per environment) and start ipython.

conda activate stochpy39
pip install stochpy
ipython

Linux/MAC OS/Cygwin from source.

In the directory where you downloaded/cloned the StochPy source, for example, the git main branch:

sudo python setup.py install

## Functionality
To run the application, the user will create a .psc file, storing the specifics of the simulation to be run. The user will then use the following commands to do necessary operations.
Run ipython and import stochpy:
import stochpy
smod = stochpy.SSA() 
See command list for additional functionality

## Known Problems

Slow speeds at high volume simulations.

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## Additional Documentation

Documentation: https://stochpy.sourceforge.net/html/userguide.html 
Team Repo: https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy 
Original StochPy Repo: https://github.com/SystemsBioinformatics/stochpy 

## License

License: https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/blob/main/LICENSE

## Command List
### Basic Simulation with the Direct method
smod.DoStochSim(IsTrackPropensities=True)
smod.data_stochsim.simulation_endtime
smod.data_stochsim.simulation_timesteps
smod.GetWaitingtimes()
smod.PrintWaitingtimesMeans()
### Do some Plotting
smod.PlotSpeciesTimeSeries()
smod.PlotWaitingtimesDistributions()
smod.PlotPropensitiesTimeSeries()
### Write data to a text file
smod.Export2File()
smod.Export2File(analysis='distribution')
smod.Export2File(analysis='distribution',datatype='species')
smod.Export2File(analysis='mean',datatype='species')
smod.Export2File(analysis='std',datatype='species')
smod.Export2File(analysis='autocorrelation',datatype='species')
### Show the means from the data of 3-th trajectory
smod.DoStochSim(trajectories=3) # multiple trajectories
smod.data_stochsim.simulation_trajectory
smod.PrintSpeciesMeans()
smod.PrintSpeciesStandardDeviations()
### Switch to data from trajectory 1 and show the means of each species
smod.GetTrajectoryData(1)
smod.PrintSpeciesMeans()
smod.PrintSpeciesStandardDeviations()
### Do one long simulation
smod.DoStochSim(trajectories=1,end=1000000,mode='steps')
smod.PrintSpeciesMeans()
smod.PrintSpeciesStandardDeviations()
### Plot the PDF for different bin sizes
smod.PlotSpeciesDistributions()
smod.PlotSpeciesDistributions(bin_size=5)  # larger bin size
smod.PlotSpeciesDistributions(bin_size=10) # again a larger bin size
smod.Export2File(analysis='distribution',datatype='species')
### Usage of the Reload Function: Ksyn = 20, kdeg = 0.2
smod.ChangeParameter('Ksyn',20.0)
smod.ChangeParameter('Kdeg',0.2)
smod.DoStochSim()
smod.PrintSpeciesMeans()   # should be ~Ksyn/Kdeg
### Use another model to show the Interpolation features
smod.Model('dsmts-001-01.xml.psc')
smod.DoStochSim(trajectories=1000,end=50,mode='time')
smod.GetRegularGrid(npoints=51)
smod.PlotAverageSpeciesTimeSeries()
smod.PrintAverageSpeciesTimeSeries()
smod.Export2File(datatype='species',analysis='timeseries',IsAverage=True)
### Test each method for different models:
smod.Model('Autoreg.psc')
smod.DoStochSim(trajectories=1,end=1000,mode='steps')
smod.Method('NextReactionMethod')
smod.DoStochSim(trajectories=1,end=1000,mode='steps')
smod.data_stochsim.species
smod.PlotWaitingtimesDistributions()
smod.Method('FirstReactionMethod')
smod.DoStochSim(trajectories=1,end=1000,mode='steps')
smod.Method('TauLeaping')
smod.DoStochSim(trajectories=1,end=1000,mode='steps')
smod.Model('DecayingDimerizing.psc')
smod.DoStochSim(method = 'Direct',trajectories=1,end=50,mode='time')
smod.DoStochSim(method = 'NextReactionMethod',trajectories=1,end=50,mode='time')
smod.DoStochSim(method = 'FirstReactionMethod',trajectories=1,end=50,mode='time')
smod.PlotWaitingtimesDistributions()
smod.DoStochSim(method = 'TauLeaping',trajectories=1,end=50,mode='time',epsilon=0.03)  # Should outperform all other implementations
smod.PlotSpeciesTimeSeries()
#smod.PlotWaitingtimesDistributions()   # Should give an error
smod.Model('chain500.psc')
smod.DoStochSim(method = 'Direct',trajectories=1,end=10000,mode='steps')
smod.DoStochSim(method = 'NextReactionMethod',trajectories=1,end=10000,mode='steps') # should outperform the direct method and all other implementations
### Use the Next Reaction Method to test a model with a time event
smod.Model('dsmts-003-03.xml.psc')
smod.DoStochSim(method = 'NextReactionMethod')
smod.DoTestsuite()
### Use the First Reaction method to test a model with a concentration event
smod.Model('dsmts-003-04.xml.psc')
smod.DoStochSim(method = 'FirstReactionMethod')
smod.DoTestsuite()
### Volume Models
smod.Model('dsmts-001-11.xml.psc')
smod.DoStochSim(method = 'Direct',trajectories=1000,end=50,mode ='time')
smod.PrintAverageSpeciesTimeSeries()


