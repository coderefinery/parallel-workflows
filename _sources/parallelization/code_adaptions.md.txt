# Code Adaptions

Even in an embarassingly parallel situation we will have to make a couple of adaptions to the code
in order to be able to run parallel executions of our code.

## Updating the code to obtain input parameters

First off, we will need to allow the programm to receive input parameters that define which element(s)
of the data have to be computed by this instance.

So from this:

```
data = load_and_preprocess_data

for i in 1,2,3,...,n do:
   res[i] = calculate(data[i])

save(res)

```

We need to create something like:

```
i = input_arg

data = load_and_preprocess_data(i)
res = calculate(data)

save res as res_i
```

## Collection script

Since we are now producing multiple individual results, we will have to collect them and put them together
into our actual result. This highly depends on your result data, but in general it will take the form of

```
res = [] of length n
for i in 1,2,3...n do:
   res[i] = load(res_i)

save(res)
```

## Exercise 1

````{exercise} Parallel-1: Make the script accept an input index
Our example is a very simple code which extracts cities for a country from a list of
cities with their countries and writes a list of these cities.
The data for the cities for this example are provided in the {download}`cities.csv </code/cities.csv>` file.
The code itself is provided {download}`here </code/python/long_code.py>`:
```{literalinclude} /code/python/long_code.py
    :language: python
```

Adapt the code, such that it takes an integer input and generates one country list
for each integer input. In this instance, the order of execution is not important
as one list per country will be produced.

````

````{solution} Solution: Parallel-1
The simplest solution is to use `sys.argv` taking in the first argument and converting
it to an integer. You can also use more elaborate input parsers (see for example
[this lecture about argument parsing](https://aaltoscicomp.github.io/python-for-scicomp/scripts/#parsing-command-line-arguments-with-argparse))

```{literalinclude} /code/python/long_code_for_index.py
    :language: python
    :emphasize-lines: 1, 30-37
```

````
