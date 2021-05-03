#!/usr/bin/env python
# coding: utf-8

# ## Funciones trigonométricas

# In[1]:


from math import *
from numpy import *
# importar todas las funciones de pylab
from pylab import *

# importar el módulo pyplot
import matplotlib.pyplot as plt

t = arange(0.1, 20, 0.1)

y1 = sin(t)/t
y2 = sin(t)*exp(-t)
p1, p2 = plot(t, y1, t, y2)

# Texto en la gráfica en coordenadas (x,y)
texto1 = text(2, 0.6, r'$\frac{\sin(x)}{x}$', fontsize=20)
texto2 = text(13, 0.2, r'$\sin(x) \cdot e^{-x}$', fontsize=16)

# Añado una malla al gráfico
grid()

title('Representacion de dos funciones')
xlabel('Tiempo / s')
ylabel('Amplitud / cm')

show()

