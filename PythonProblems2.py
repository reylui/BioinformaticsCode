# Python Problems 2
# Luis J. Ramirez
# In this assignment, we work on phylogenitic reconstruction problems that are presented by Dr. Greg Caporaso.

# Before we can reconstruct a phylogenetic tree from a DNA sequence, we must first simulate the process of evolution
# for a DNA sequence.
# We are going to use a python function to model a sequence evolution, then we will run that function to simulate
# multiple generations of evolution.

import numpy as np
import seaborn as sns
import random
from IPython.core import page

# First we take a look at the function that is going to help us model this DNA sequence evolution.
# This is were most of the modeling takes place.

from BioinformaticsCode.algorithms import evolve_sequence

# This function will help us model a single generation of a single sequence.
# Here, clonal reproduction will occur

from BioinformaticsCode.algorithms import evolve_generation

# Then we have the entry point function. We provide the parameters for the simulation: Initial sequence, number of
# generations and mutation probabilities.
# This code is built on the previously mentioned functions.

from BioinformaticsCode.algorithms import evolve_generations













