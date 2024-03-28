# Motivation

```{objectives}
- Get poptions how to run workflows in parallel.
- Structuring workflows to avoid repeating already executed steps
- Pitfalls and problems occuring in workflows
```

## Why parallelize at all

While the actual processing speeds of processors hasn't increased that much over the last decade (~3.6 Ghz i~ 2010 vs 4.1 Ghz in 2020)
the number of cores has increased a ot ( from max 6 (most machines having 2) to up to 64 (with most having ~6)). This is particularily
true if we look at clusters, where the number of machines and thus available cores has risen a lot, while the single core speed hasn't
improved that much.
In addition, the amount of data we are processing nowadays, often requires us to repeat the same pocesses multiple times for each data
point (e.g. in pre-processing). And while many libraries have inherent parallelization mechanisms for several types of mathematical
processes that does not cover re-application of the same process unless we use in-language parallelization techniques.
