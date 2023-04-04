# Sprint 6 Report (3/3/2023 - 4/2/2023)

## What's New
 * Completed a Numba stochastic simulation implementation
 * Concluded unfeasibility of Dask implementation
 * Touched base with Dr. Lofgren about project progress, future planning 

## Work Summary
For Sprint 6, aside from keeping our documentation up-to-date, we have generally reached a conclusion on the state of a Numba implementation for StochPy and a Dask implementation for StochPy. For Numba, while we have completed implementing Numba functionality into StochPy, specifically the parts relating to stochastic simulation functionality, the overall runtime has increased by a factor of three, owing to incompatibilities (one of which being that Numba lacks a key random seed feature used by StochPy) in the StochPy forcing Numba to run in a less-efficient mode. We have concluded that attempting to get Numba to fully work with StochPy is not possible, especially considering the remaining time in this semester and the sheer difficulty of working within the StochPy codebase. Additionally, we have found that Dask is also not practical for a StochPy rewrite either, since it also has some incompatibilities with how StochPy performs its simulations. Our client, Dr. Lofgren, has been notified of this, and accepts our results for this foray into parallelizing StochPy, and has also directed us to pursue other alternatives with our remaining time. As such, our team has begun the process of creating a rewrite of StochPy limited solely to the stochastic simulation functionality, and some limited simulation files have already been created for this.

## Unfinished Work
Unfinished work includes preparing our poster presentations for the demo day, along with preparing all associated documentation and materials for final submissions and transfer to Dr. Lofgren. In addition, there are more additions that can be made to our limited rewrite of StochPy. 

## Completed Issues
Here are links to the issues that we completed in this sprint:
* [3/9/23 Client Meeting](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/issues/78)
* [3/21/23 Mentor Meeting](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/issues/79)
* [3/30/23 Team Meeting](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/issues/82)
* [3/9/23 Team Meeting](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/issues/77)
* [3/23/23 Team Meeting](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/issues/80)
* [3/31/23 Client Meeting](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/issues/81)
* [Prepare and submit the third draft of the MVP Project Report](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/issues/94)
* [Prepare and submit Sprint 6 Report Materials](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/issues/97)
* [Use Numba to optimize StochPy doStochSim](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/issues/44)
* [Use Dask to optimize StochPy doStochSim](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/issues/39)
* [Perform speedup analysis after Numba/Dask optimization](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/issues/40)

 ## Incomplete Issues
No issues pertaining to Sprint 6 remain incomplete. All that remains are the aforementioned presentation materials, documentation, and other miscellanea. 

## Code Files for Review
* [Completed Numba Implementation](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/compare/main...numba-testing)
* [Experimental Work on New Library](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/pull/114/files)
 
## Retrospective Summary
Here's what went well:
  * Acquiring a better understanding of the technologies we are using (Dask, Numba)
  * Acquiring a better understanding of StochPy
  * Communicating our work and efforts to our client
 
Here's what we'd like to improve:
   * Accelerate implementation speed
   * Improve quality and production rate of deliverables in a satisfactory timeframe
  
Here are changes we plan to implement in the next sprint:
   * Ramping up implementation speed by enforcing stricter self-defined deadlines for Sprint issues
   * Dedicate more time and attention to working on deliverables, along with working with the team for them