# Sprint 3 Report (11/10/2022 - 12/9/2022)

## What's New
 * Prototype project report finalized
 * Ongoing implementation of Numba features into StochPy source code
 * Dask applied to StochPy test script, basic parallelization achieved

## Work Summary
For Sprint 2, aside from keeping our documentation up-to-date, we have been working on implementing Dask and Numba features into StochPy to pursue our stated goals of optimizing and parallelizing the library. Progress is slow, however, as the StochPy codebase is labyrinthine, and there are numerous unusual errors that are difficult to debug. Still, progress is ongoing, and we already have a functioning parallelized example with the "Upload Dask Template example". Additionally, some StochPy source code has been partially retrofitted with Numba features, although it is currently in-progress and not operational, so it exists on the "numba-testing" GitHub branch. Additionally, we have uploaded some case study materials to the Sprint 2 folder. 

## Unfinished Work
Unfinished work includes fully implementing Dask and Numba features into StochPy, along with conducting extensive testing and speedup analysis. As mentioned, this is hampered by the complexity of working within the StochPy codebase and numerous bugs caused by the smallest changes. For example, we have made attempts to integrate the Dask changes in the template example into the StochPy source code itself but are running into unusual simulation outputs and other bugs. Numba implementation into the StochPy source code is an ongoing process and faces similar errors. 

## Completed Issues
Here are links to the issues that we completed in this sprint:
* [Upload Dask Template example](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/issues/47)
* [Finish Sprint 3 documentation](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/issues/54)
* [Upload Case Studies folder missing from Sprint 2](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/issues/51)
* [Complete prototype project report](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/issues/41)
* [Create class presentation materials](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/issues/42)
* [Upload 12.2 client meeting minutes](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/issues/50)
* [Upload meeting minutes from 11.7.2022](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/issues/45)
* [Create client prototype demo materials](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/issues/43)

 ## Incomplete Issues
There are some issues assigned to this sprint that remain incomplete, mostly due to implementation being ongoing. These issues are:
* [Use Dask to optimize StochPy doStochSim](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/issues/39)
* [Use Numba to optimize StochPy doStochSim](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/issues/44)
* [Perform speedup analysis after Numba/Dask optimization](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/issues/40)

## Code Files for Review
There are some code files for review regarding a preliminary application of Dask and ongoing Numba implementation. Note that the plan is for the added Dask lines to the script to eventually be integrated into the StochPy source code, as soon as the errors associated with doing so are dealt with. The StochPy retrofitting/Numba implementation is ongoing. 
* [Dask-ified Scripts](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/pull/48/files)
* [Ongoing Numba Implementation](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/compare/main...numba-testing)
 
## Retrospective Summary
Here's what went well:
  * Collaborating with each other in a constructive and timely manner
  * Acquiring a better understanding of the technologies we are using (Dask, Numba)
  * Commencing modification of source code and actually implementing some Dask/Numba functionalities
 
Here's what we'd like to improve:
   * Increasing feature implementation speed
   * Considering the literature-heavy nature of our project, improve pace of producing testing results
  
Here are changes we plan to implement in the next sprint:
   * Ramping up implementation speed by enforcing stricter self-defined deadlines for Sprint issues
   * Keeping better track of "literature search"-esque activities for Sprint documentation purposes

