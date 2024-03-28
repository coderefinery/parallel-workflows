# Conclusions and recommendations

- Use scheduler based parallelisation for embarassingly parallel problems
- Adapt your code to allow it to use input parameters that can be read from the command line
- Potentially build collection methods to re-combine the individual results of the parallel executions
- Use system calls from your language to submit jobs to avoid complex bash coding if you are not that familiar with bash
- Keep code and input variables separate, to allow reusability of code, avoid unintentional errors and keep better track of individual runs
