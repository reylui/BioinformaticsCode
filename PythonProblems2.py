# Python Problems 2
# Luis J. Ramirez
# In this assignment, we work on phylogenitic reconstruction problems that are presented by Dr. Greg Caporaso.

# Before we can reconstruct a phylogenetic tree from a DNA sequence, we must first simulate the process of evolution
# for a DNA sequence.
# We are going to use a python function to model a sequence evolution, then we will run that function to simulate
# multiple generations of evolution.

import pylab as p
import numpy as np
import seaborn as sns
import random
from IPython.core import page
page.page = print


# First we take a look at the function that is going to help us model this DNA sequence evolution.
# This is were most of the modeling takes place.

from BioinformaticsCode.algorithms import evolve_sequence

# This function will help us model a single generation of a single sequence.
# Here, clonal reproduction will occur

from BioinformaticsCode.algorithms import evolve_generation

# Then we have the entry point function. We provide the parameters for the simulation: Initial sequence, number of
# generations and mutation probabilities.
# This code is built on the previously mentioned functions.

from BioinformaticsCode.algorithms  import evolve_generations

# now we can run a simulation using a random DNA sequence and evolve three generations. We will use evolve_sequence from
# algorithms and pass the verbose = true parameter.

from BioinformaticsCode.algorithms  import random_sequence

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

# Now we are going to simulate 10 generations of sequences. We will randomly select some of the sequences for the
# remainder of this code. We are setting the indel probability to 0.0. This means we wont have to align the selected
# This saves us some runtime.

from skbio.alignment import global_pairwise_align_nucleotide
from BioinformaticsCode.algorithms import progressive_msa
from functools import partial

indel_probability = 0.0

sequences = evolve_generations(sequence, 10, .03, 0.0, 0.1, False)

sequences = random.sample(sequences, 25)

if indel_probability == 0:
    sequences_aligned = sequences
else:
    gpa = partial(global_pairwise_align_nucleotide, True)
    sequences_aligned = progressive_msa(sequences, pairwise_aligner=gpa)


# While the simulations are strong for comparing algorithms, they can often be misleading. This is because we simplify ,
# the evolutionary process. In practice a combination of real data and simulated data can help/

# Now we start to compute phylogenetic trees, we're going to need a way to visualize them. the ete3 python package can
# help us do this. We will configure TreeStyle to define the way trees work.

import ete3
ts = ete3.TreeStyle()
ts.show_leaf_name = True
ts.scale = 250
ts.branch_vertical_margin = 15

# We can apply this tree style to a random tree as follows.

t = ete3.Tree()
t.populate(10)
t.render("%%inline", tree_style=ts)

# distance based methods to phylogenetic reconstruction

# for the next approach, we will rely on computing the distances between the sequences.

# We will use dissimilarity distance between two objects x and y. Literature on this can be found online, for now
# we are going to show the code.

from skbio import DistanceMatrix

dm = DistanceMatrix([[0.0, 1.0, 2.0],
                     [1.0, 0.0, 3.0],
                     [2.0, 3.0, 0.0]],
                    ids=['a', 'b', 'c'])

_ = dm.plot(cmap ='Greens')

# We will use the scikit-bio to create a skbio.distancematrix object. These objects can be viewed as heatmaps.

from BioinformaticsCode.algorithms import kmer_distance
kmer_dm = DistanceMatrix.from_iterable(sequences, metric=kmer_distance, key='id')
_ = kmer_dm.plot(cmap='Greens', title='3mer distances between sequences')

kmer_dm.plot


















