# Sprint 4 Report (1/9/2023 - 2/2/2023)

## What's New
 * First draft of MVP report completed
 * Ongoing implementation of Numba features into StochPy source code
 * Continued research into potential application of Dask as well as how it works

## Work Summary
For Sprint 4, aside from keeping our documentation up-to-date, we have been continuing our work on implementing Numba features into StochPy. Progress is continuing steadily but slowly, as we continue to face several unusual errors that are complicated to debug as Numba features are implemented. Moreover, we are also generating design materials to create a skeleton of our approach to integrating Numba into StochPy. In summary, progress is ongoing. Additionally, some StochPy source code has been partially retrofitted with Numba features, although it is currently not operational, so it exists on the "numba-testing" GitHub branch. Finally, we have uploaded some study materials that were used in studying Dask to the text file in the Sprint 4 folder.

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
* [Use Dask to optimize StochPy doStochSim](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/issues/39)*
* [Use Numba to optimize StochPy doStochSim](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/issues/44)
* [Perform speedup analysis after Numba/Dask optimization](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/issues/40)

\*Though we have technically implemented speedup using Dask via the script files mentioned in Sprint 3, we are still researching and experimenting with how we might be able to better integrate it into StochPy, so we are leaving the issue up for now. 

## Code Files for Review
Much of this sprint has been dedicated to developing plans for organizational issues and deciding how best to complete the seemingly conflicting goals of the curriculum and the client. As such, little code has been produced while we are adjusting our plans. The StochPy retrofitting/Numba implementation is ongoing, as can be seen below:
* [Ongoing Numba Implementation](https://github.com/WSUCptSCapstone-Fall2022Spring2023/remi-hpcstochpy/compare/main...numba-testing)
 
## Retrospective Summary
Here's what went well:
  * Acquiring a better understanding of the technologies we are using (Dask, Numba)
  * Collaborating with each other in a constructive and timely manner
 
Here's what we'd like to improve:
   * Increasing feature implementation speed 
   * Considering the literature-heavy nature of our project, improve generation and tracking of research and development artifacts, along with improving the pace of producing testing results
  
Here are changes we plan to implement in the next sprint:
   * Ramping up implementation speed by enforcing stricter self-defined deadlines for Sprint issues and directing additional resources to our most vital goal in the form of refactoring StochPy for use with Numba
   * Keeping better track of "literature search"-esque activities for Sprint documentation and accountability purposes
   * Improving team communication by enforcing weekly meetings, delineating expected tasks for each week, and holding fellow team members accountable through generating tangible work artifacts
