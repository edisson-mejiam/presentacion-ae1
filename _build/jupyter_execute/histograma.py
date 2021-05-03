#!/usr/bin/env python
# coding: utf-8

# ## Histogramas

# In[1]:


# importar todas las funciones de pylab
from pylab import *

# importar el módulo pyplot
import matplotlib.pyplot as plt

from pylab import *      # importar todas las funciones de pylab
# Importamos el módulo de numeros aleatorios de numpy
from numpy import random

# utilizo la función randn() del modulo random para generar
# un array de números aleatorios con distribución normal
nums = random.randn(200)  # array con 200 números aleatorios

# generamos el histograma
h = hist(nums)
hist(nums, bins=20)


# In[ ]:




