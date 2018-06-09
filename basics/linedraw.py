#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Note:  enumerate is a type, not a function, as
it returns instances of the enumerate type
"""
import matplotlib.pyplot as plt
import numpy as np

def makeline(m, b):
    def line(x):
        """line function"""
        return m*x + b
    return line

domain = np.arange(-10, 10, 0.1)

plt.figure()

colors = ['red','orange','blue','green','black']
for idx, slope in enumerate(range(-4, 1)):
    f = makeline(slope, 10)
    y = f(domain)
    plt.plot(domain, y, color = colors[idx])

colors = ['green', 'blue', 'orange', 'red', 'black']
for idx, slope in enumerate(range(1, 5)):
    f = makeline(slope, 10)
    y = f(domain)
    plt.plot(domain, y, color = colors[idx])
    
plt.xlabel("Domain")
plt.title("Plotting Lines")
plt.grid()
