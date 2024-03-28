# Parallelize via a script

We have now seen how to parallelize code using array jobs. This is convenient, if you have
a situation, where your script just walks over some integer values (or indices in an array)
and you can just use the index provided by the slurm array as input index to your script.
Often however, this is not possible, as we want to e.g. scan a (non-integer) space of parameters or need textual input parameters.

This could be achieved, by e.g. adding the values of the parameters to the script and reference them by index.

However, at the same time, we want our code to be re-usable and don't want to put the
actual values within our code base, since this would force us to always edit the code files
of our project and will make it more likely that errors are introduced in the code itself.
So an alternative approach to touching our code base is to create packages that can parse
multiple or non integer input parameters.

Here is a simple piece of code that combines a Name with a numbe rand writes it to a
file with a given name, where all elements are given as command line arguments.

`````{tabs}

   ````{group-tab} Python
    ```{literalinclude} /code/python/scan_code.py
        :language: python
    ```
   ````

   ````{group-tab} R
    ```{literalinclude} /code/r/scan_code.r
        :language: R
    ```

   ````
`````

Lets say we want to run this with the following input parameter sets:

- File1, Joe, 1.23
- File2, Jane, 23.5
- File3, Doe. 11.5

we can do this in bash, but an easier way is to use the language we work in and build a general purpose submission script like this:

```{literalinclude} /code/slurm/submission.sh
    :language: slurm
```

This submission script again takes three input parameters and runs the python script with
these three input parameters. We can now build a small piece of code that stars our
submissions:

`````{tabs}

   ````{group-tab} Python
    ```{literalinclude} /code/python/submission.py
        :language: python
    ```
    You can run this code by running `python3 submission.py` and it will submit the
    submission.sh file to the slurm scheduler for each of your options.
   ````

   ````{group-tab} R
    ```{literalinclude} /code/r/submission.r
        :language: R
    ```
    You can run this code by running `Rscript submission.r` and it will submit the
    submission.sh file to the slurm scheduler for each of your options.
   ````
`````

This way, we have separated the input parameters from the code itself.
The main things you have to take care of when doing this are:

- Make sure, that no two output files have the same name. This is particularily important, if you determine the output file name not by an explicit provided file name but e.g. from the input parameters.
- Be careful when using floating numbers as input parameters, as the values actually supplied can be different (due to rounding and string representation) than the numbers you intend to be providing. This should be very small differences, but depending on your problem this can have a huge impact.

You can of course also make more complex submission scripts using nested loops (e.g. if values depend on each other).
