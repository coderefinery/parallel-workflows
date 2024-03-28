# Concepts

## Embarassingly parallel code

Embarassingly parallel code is code that essentially runs the same functionality
for a large variety of input parameters, where each step does not depend on anything
other than the input data.
Here are two types of situations in pseudo-code that show embarassinlgy parallel execution:

```
data = load_and_preprocess_data

for i in 1,2,3,...,n do:
   res[i] = calculate(data[i])

```

or

```
parameters = [ 1,2,3,4,5,6 ]
res = []

for value in parameters:
   res.append(calculate(value))
```

The first being a pipeline applied to every datapoint in some input data, the second a cassical
parameter sweep for a model. Essentially you are running the same type of computation for each
entry of a set of data.
This is the type of code that can easily be parallelized on a scheduler level.

## Parallel execution pitfalls

Here are a couple of issues that can be causing your code to fail or produce invalid data:

- Interfering temporary files
  - Make sure that whenever you create temporary files in your jobs, those files have a name that
    is unique to the jobID and (if applicable) array ID of the job. Otherwise you can easily end up
    trying to load data from another run, or corrupt a file by writing to it from two processes
- Indexing (only applicable for array jobs):
  - The indexes of slurm array jobs by default start with 1 not 0 (which many coding languages use
    as first index of an array)

## Size of jobs

In general, jobs should not be too short on a cluster. There is always an overhead in scheduling
tasks, and if jobs of an array job are too short, this overhead can result in a waste of resources.
If you have code that runs in a second but needs to be run millions of times, try to batch executions
into batches, such that each individual job takes 10-60 minutes. This way, the overhead of starting
and scheduling the jobs is reduced significantly.
