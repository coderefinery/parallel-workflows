# Parallelize using Slurm Array jobs

Slurm array jobs are jobs, that are run multiple times, with the same settings.
a slurm batch script with an array job looks something like:

```slurm
#!/bin/bash
#SBATCH --job-name=my_array_job
#SBATCH --array=2-100:2
#SBATCH --output=output_%A_%a.txt
#SBATCH --error=error_%A_%a.txt

# Your job commands go here
# You can use the environment variable SLURM_ARRAY_TASK_ID to get the current task ID
# load whatever modules or environments you need before running your actual command

# Example command: replace with your actual command
your_command --parameter $SLURM_ARRAY_TASK_ID
```

where `--array=2-100:2` creates 50 jobs numbered from 2 to 100 with a step size of 2
(the step size defaults to 1 if omitted). `%A` and `%a` in output and error indicate
the jobID and arrayID of the job respectively. The only difference in these jobs is the
environment variable `SLURM_ARRAY_TASK_ID` which is set to the array id of the job
and can be used to select what to calculate in this job.

We can use this variable to tell our program which element to use in this job, done in the above example by passing the `$SLURM_ARRAY_TASK_ID` as the parameter argument for the
program we run.

## Exercise 1

```{exercise} Parallel-2: Create a slurm script and run it.
For our example we will need to adapt the above script a bit.
First, we will need to run it for only four different values, as we only have four different
countries. Second, we need to start our array at 0 since python uses zero-based indexing
or we will need to adapt our code to change this.

Finally, we don't have any argument parsing, but need to provide the input parameter directly to the script as in `python long_code.py 1`

Build the sbatch script that we need to run the code for our 4 countries and run it on your cluster
```

````{solution} Solution: Parallel-2
Here is a script that should be able to run on your cluster:

```slurm
#!/bin/bash
#SBATCH --job-name=long_job
#SBATCH --array=0-3
#SBATCH --output=output_%A_%a.txt
#SBATCH --error=error_%A_%a.txt

# We assume, that python3 runs out of the box on your cluster, if not, you will have to
# add a command here that makes the python3 command available on your cluster

# Example command: replace with your actual command
python3 long_code.py $SLURM_ARRAY_TASK_ID
```

````

## More complex submission scripts

In many instances it is necessary to use parameters that are not simple integers, as
provided by `$SLURM_ARRAY_TASK_ID` or use multiple input parameters. To do this, you can
either adapt your code or generate more complex logic within the batch submission script
using bash commands. We will not go into the details of bash programming here, but if you
are familiar this can be a convenient way to achieve more complex input parameters.

In the next section we will show you an alternaive way to do this, which might be more
convenient as it uses the language you commonly use to achieve the goal.
