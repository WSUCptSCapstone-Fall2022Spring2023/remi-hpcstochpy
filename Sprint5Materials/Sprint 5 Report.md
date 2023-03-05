# Sprint 5 Report (2/3/2023 - 3/2/2023)

## What's New
 * Second draft of MVP report completed
 * Completion of solution architecting
 * Ongoing implementation of Numba features into StochPy source code

## Work Summary
For Sprint 5, aside from keeping our documentation up-to-date, we have continued to work on implementing Numba features into StochPy. Progress is continuing steadily but slowly, as our planning and analysis activities are completed, but we still continue to face difficult implementation challenges with Numba. We're continuing to put work into integrating Numba functions into StochPy, but there is the looming concern that Numba implementation would be impossible to achieve for StochPy--in which case, we'd fall back to our Dask version and refining it. Still, as already stated, we're committing fully to getting Numba to work, and our current implementation progress can be seen in the numba-testing class. 

## Unfinished Work
Unfinished work includes fully implementing Dask and Numba features into StochPy, along with conducting speedup testing on StochPy once this is completed. As mentioned, the implementation is hampered by the complexity of working within the StochPy codebase and numerous bugs caused by the smallest changes, along with errors that are nearly impossible to deduce the cause of. The StochPy library continues to throw many errors as we try to implement Numba functionality into it, but we still continue to work towards it. 

## Completed Issues
Here are links to the issues that we completed in this sprint:
* [2/9/23 Team Meeting](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/issues/70)
* [2/16/23 Client Meeting](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/issues/71)
* [2/16/23 Team Meeting](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/issues/72)
* [2/21/23 Mentor Meeting](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/issues/73)
* [2/23/23 Team Meeting](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/issues/74)
* [3/2/23 Client Meeting](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/issues/75)
* [3/2/23 Team Meeting](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/issues/76)
* [Prepare and submit the second draft of the MVP Project Report](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/issues/93)
* [Prepare and submit Sprint 5 Report Materials](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/issues/96)

 ## Incomplete Issues
There are some issues assigned to this sprint that remain incomplete, mostly due to implementation being ongoing. These issues are:
* [Use Dask to optimize StochPy doStochSim](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/issues/39)*
* [Use Numba to optimize StochPy doStochSim](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/issues/44)
* [Perform speedup analysis after Numba/Dask optimization](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/issues/40)

\* While we have a working Dask version, we are working on getting it directly integrated into StochPy. So, it remains as an "incomplete" issue.

## Code Files for Review
Much of this sprint has been dedicated to developing plans for implementation details, along with some limited implementation. The StochPy retrofitting/Numba implementation is ongoing, as can be seen below:
* [Ongoing Numba Implementation](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/compare/main...numba-testing)
 
## Retrospective Summary
Here's what went well:
  * Acquiring a better understanding of the technologies we are using (Dask, Numba)
  * Communicating with our faculty mentor to clarify expectations and acquire work
 
Here's what we'd like to improve:
   * Accelerating implementation speed
   * Communicating with team members and setting clear work expectations
  
Here are changes we plan to implement in the next sprint:
   * Ramping up implementation speed by enforcing stricter self-defined deadlines for Sprint issues and directing additional resources to our most vital goal in the form of refactoring StochPy for use with Numba
   * More frequent communication, 