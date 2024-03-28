Pitfalls when parallelising code
================================

.. warning::

   This is under construction.  The schedule is not final, please see
   the planning HackMD (not linked here, check on CodeRefinery chat)
   for the current planning. 

.. admonition:: Course instance in April 2024

   You can follow the dates this course is given on the `course page
   <https://scicomp.aalto.fi/training/scip/workflows-2023/>`__.
   Dates are not yet known and registration is not yet open, though.

This part of the lesson will highlight common issues arising when parallelising 
embarassingly parallel problems. We will discuss both issues that can arise when 
running the same code multiple times at the same time as well as issues that arise 
from excessive parallelisation. 

.. prereq::

   * Basic HPC usage course (if you don't have, many of the things we
     talk about won't make sense, but you might pick up something
     anyway).
   * A bit of experience using a HPC cluster (technically optional,
     but will allow you to engage with the material at a deeper
     level).
   * Access to some HPC computer cluster to do most exercises.
     (Slurm-based, but most are these days).  (If you don't have, you
     can't do all exercises - but still might learn something!)


.. csv-table::
   :widths: auto
   :delim: ;

   10 min ; :doc:`common_issues`
   

.. toctree::
   :maxdepth: 1
   :caption: The lesson

   common_issues

