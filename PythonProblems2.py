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

from algorithms import evolve_sequence

# This function will help us model a single generation of a single sequence.
# Here, clonal reproduction will occur

from algorithms import evolve_generation

# Then we have the entry point function. We provide the parameters for the simulation: Initial sequence, number of
# generations and mutation probabilities.
# This code is built on the previously mentioned functions.

from algorithms import evolve_generations

# now we can run a simulation using a random DNA sequence and evolve three generations. We will use evolve_sequence from
# algorithms and pass the verbose = true parameter.

from algorithms import random_sequence

import skbio

sequence = random_sequence(skbio.DNA, 50)

sequences = evolve_generations(sequence, 3, 0.1, 0.05, 0.1, True)

# sequences will contain the the child sequence from the last generation. We also note that we will only have sequences
# from the last generation. Not the ancestral sequence, since this models a real world application.

# Lets take a look at the following:

print(len(sequences))

print(sequences[0])

print(sequences[-1])

# In our simulation each, each sequence is derived from exactly one sequence from the previous generation, and the
# evolution traces back to the ancestral sequence that we provided. This means that are final sequences are all
# homologous. Our goal now, is to reconstruct the phylogeny given only the last generation of sequences. We will use the
# fact that we know the previous phylogeny to evaluate our performance.

















