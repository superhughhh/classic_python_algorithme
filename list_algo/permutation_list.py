# -*- coding: UTF-8 -*-
# this algo allows to create a list that regroup all the permutation of a given list
import itertools


# Exemple d'utilisation
l = [1,2,3,4]
permutations = itertools.permutations(l)
L = list(permutations)
print ("Les listes obtenues en échangeant les termes de la liste l:\n", L)