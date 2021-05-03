#!/usr/bin/env python
# coding: utf-8

# ## Gráficas de funciones en jupyter

# Existe una gran variedad de módulos para hacer gráficos de todo tipo con Python, pero el estándar de facto en ciencia es matplotlib. Se trata de un paquete grande y relativamente complejo que entre otros contiene dos módulos principales, pyplot y pylab.
# 
# pyplot ofrece una interfaz fácil para crear gráficos fácilmente, automatizando la creación de figuras y ejes automáticamente cuando hace un gráfico. Por otra parte, pylab combina la funcionalida de pyplot para hacer gráficos con funcionalidad de numpy para hacer cálculos con arrays usando un único espacio de nombres muy parecido a Matlab.

# In[1]:


# importar todas las funciones de pylab
from pylab import *

# importar el módulo pyplot
import matplotlib.pyplot as plt

from pylab import *      # importar todas las funciones de pylab
def f1(x):
    y = sin(x)
    return y

def f2(x):
    y = sin(x) + sin(5.0*x)
    return y


def f3(x):
    y = sin(x) * exp(-x/10.)
    return y

# array de valores a representar
x = linspace(0, 10*pi, 800)

p1, p2, p3 = plot(x, f1(x), x, f2(x), x, f3(x))

# Añado leyenda, tamaño de letra 10, en esquina superior derecha
legend(('Funcion 1', 'Funcion 2', 'Funcion 3'),
prop = {'size': 10}, loc='upper right')

xlabel('Tiempo / s')
ylabel('Amplitud / cm')
title('Representacion de tres funciones')

# Creo una figura (ventana), pero indico el tamaño (x,y) en pulgadas


show()


# In[ ]:





# 
# ```{toctree}
# :hidden:
# :titlesonly:
# 
# 
# recta
# funciones trigonométricas
# histograma
# ```
# 
