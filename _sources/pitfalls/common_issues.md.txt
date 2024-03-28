# Common issues

By running several computations in parallel we place a few more constraints on what we can
or cannot do, resulting in concurrency issues. In a non parallel situation we commonly
do not need to pay attention to what the resources are accessed by the code. This is different
when the code runs in parallel. There are also additional considerations as to overheads
which need to be taken into consideration.

## Concurrency issues

Let's take the following piece of code:

`````{tabs}

   ````{group-tab} Python
    ```{literalinclude} /code/python/basic_example.py
        :language: python
    ```

   ````

   ````{group-tab} R
    ```{literalinclude} /code/r/basic_example.r
        :language: R
    ```

   ````

`````

which we have identified as embarassingly parallel code and converted to the following:

`````{tabs}

   ````{group-tab} Python
    ```{literalinclude} /code/python/basic_parallelized.py
        :language: python
    ```

   ````

   ````{group-tab} R
    ```{literalinclude} /code/r/basic_parallelized.r
        :language: R
    ```

   ````

`````

Our `append_result` function either creates the results file, if it does not exist yet, or, if
it does, it reads in the result array. We run this function several times via an `sarray` job.
This can work fine. However, it can also lead to errors, and worst case invalid results.
The problem arises because we don't know the point in time at which the result file is opened
and written to. Likely some jobs will fail with an error thrown, when two processes try to
simultaneously write to the same file, or that some try to read from the file while it is
written to. More inconvenient could be suspiciously missing results in the results file, due to
two reads of the file, which leads to conflicting writes, where one result is simply lost.
Or, we could end up with an entirely corrupt file, when two jobs write simultaneously and the
filesystem doesn't complain about it...

So, an important thing to keep in mind is to have the parallelized code really be independent
of other instances. In most cases this means, using index specific output files and having a
"collection script" that combines the data after the jobs are complete. This can even be done with slurm internal methods:

```slurm
#!/bin/bash
#SBATCH --job-name=collection_job
#SBATCH --dependency=afterok:your_array_job_id

# run your collection script
python collection.py
```

The above case would then become something like:

Calculation script:

`````{tabs}

   ````{group-tab} Python
    ```{literalinclude} /code/python/basic_parallelized_non_conflict.py
       :language: python
    ```

   ````

   ````{group-tab} R
    ```{literalinclude} /code/r/basic_parallelized_non_conflict.r
        :language: R
    ```

   ````

`````

Submission:

`````{tabs}

   ````{group-tab} Python
    ```{literalinclude} /code/slurm/submit_parallel_py.sh
        :language: slurm
    ```

   ````

   ````{group-tab} R
    ```{literalinclude} /code/slurm/submit_parallel_r.sh
        :language: slurm
    ```

   ````

`````

CollectionScript:

`````{tabs}

   ````{group-tab} Python
    ```{literalinclude} /code/python/collection.py
        :language: python
    ```

   ````

   ````{group-tab} R
    ```{literalinclude} /code/r/collection.r
        :language: R
    ```

   ````

`````

Submission for collection:

`````{tabs}

   ````{group-tab} Python
    ```{literalinclude} /code/slurm/collection_py.sh
        :language: slurm
    ```

   ````

   ````{group-tab} R
    ```{literalinclude} /code/slurm/collection_r.sh
        :language: slurm
    ```

   ````

`````

While the above example might be a bit artificial, we once had a user, who had a more complex
workflow, which needed to call scripts from several languages, and used files to communicate
between the different runs. However, these temporary files were the same for all runs, which
lead to results that were completely unreliable. The user was lucky that some of the runs
actually errored out with a very strange error and they had to re-run all of their runs as
none were reliable. And these things can even be hidden within some libraries, which expect to
only be used in one process at a time and e.g. write some temporary files to home folders.
