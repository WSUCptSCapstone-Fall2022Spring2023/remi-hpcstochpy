# Sprint 3 Report (1/9/2023 - 2/2/2023)

## What's New
 * First draft of MVP report completed
 * Ongoing implementation of Numba features into StochPy source code
 * Further research into potential application of Dask as well as how it works

## Work Summary
For Sprint 4, aside from keeping our documentation up-to-date, we have been working on implementing Numba features into StochPy to pursue our stated goals of optimizing and parallelizing the library. Progress is slow, however, as the StochPy codebase is labyrinthine, and there are numerous unusual errors that are difficult to debug. Still, progress is ongoing. Additionally, some StochPy source code has been partially retrofitted with Numba features, although it is currently in-progress and not operational, so it exists on the "numba-testing" GitHub branch. Additionally, we have uploaded some further study materials to the Sprint 4 folder from further study of Dask. 

## Unfinished Work
Unfinished work includes fully implementing Dask and Numba features into StochPy, along with conducting extensive testing and speedup analysis. As mentioned, this is hampered by the complexity of working within the StochPy codebase and numerous bugs caused by the smallest changes. For example, we have made attempts to integrate the Dask changes in the template example into the StochPy source code itself but are running into unusual simulation outputs and other bugs. Numba implementation into the StochPy source code is an ongoing process and faces similar errors. 

## Completed Issues
Here are links to the issues that we completed in this sprint:
* [Upload 1.18.23 Team Meeting Minutes](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/issues/58)
* [Upload 1.25.23 Team Meeting Minutes](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/issues/60)
* [Add Research Links](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/issues/66)
* [2/1/23 Team Meeting](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/issues/62)
* [2/2/23 Client Meeting](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/issues/63)
* [Submit the first deaft of MVP Project Report](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/issues/57)
* [Submit Sprint 4 Report Materials](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/issues/68)

 ## Incomplete Issues
There are some issues assigned to this sprint that remain incomplete, mostly due to implementation being ongoing. These issues are:
* [Use Dask to optimize StochPy doStochSim](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/issues/39)
* [Use Numba to optimize StochPy doStochSim](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/issues/44)
* [Perform speedup analysis after Numba/Dask optimization](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/issues/40)

## Code Files for Review
Much of this sprint has been dedicated to developing plans for organizational issues and deciding how best to complete the seemingly conflicting goals of the curriculum and the client, as such little code has been produced while we have adjusted our plans. The StochPy retrofitting/Numba implementation is ongoing.
* [Ongoing Numba Implementation](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/compare/main...numba-testing)
 
## Retrospective Summary
Here's what went well:
  * Collaborating with each other in a constructive and timely manner
  * Acquiring a better understanding of the technologies we are using (Dask, Numba)
  * Commencing modification of source code and actually implementing some Dask/Numba functionalities
 
Here's what we'd like to improve:
   * Increasing feature implementation speed
   * Considering the literature-heavy nature of our project, improve generation and tracking of research and development artifacts.
   * Considering the literature-heavy nature of our project, improve pace of producing testing results
  
Here are changes we plan to implement in the next sprint:
   * Ramping up implementation speed by enforcing stricter self-defined deadlines for Sprint issues
   * Ramping up implementation speed by directing additional resources to our most vital goal in the form of refactoring StochPy for use with Numba.
   * Keeping better track of "literature search"-esque activities for Sprint documentation purposes
