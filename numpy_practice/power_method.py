# coding: utf-8

A = np.array([.3,.6,.1]
[.5,.2,.3]
[.4,.1,.5])
import numpy as np
A = np.array([.3,.6,.1]
[.5,.2,.3]
[.4,.1,.5])
A = np.array([[.3,.6.1],[.5,.2,.3],[.4,.1,.5]])
A = np.array([[.3,.6,.1],[.5,.2,.3],[.4,.1,.5]])
v = np.array([.25,.5,.25])
for i in range of (0,25):
for i in range(0,25):
    v_prime = v*A
    v = v_prime
    
v
v*A
np.shape(v)
v = np.array([1/3,1/3,1/3])
np.shape(v)
np.shape(v')
np.shape(v.T)
A 
A * v
v = np.array([1/3,1/3,1/3])
A.dot(v)
A.dot(v)
A @ v
for i in range(0,25):
    v_prime = A @ v
    v = v_prime
    
v
v = np.array([.5,.25,.25])
for i in range(0,25):
    v_prime = A @ v
    v = v_prime
    
v
import matplotlib.pyplot as plt
delta = np.array()
delta = np.array([])
v = np.array([.5,.3,.2])
for i in range(0,25):
    v_prime = A @ v
    delta.append(v - v_prime)
    v = v_prime
    
for i in range(0,25):
    v_prime = A @ v
    delta.append([v - v_prime])
    v = v_prime
    
for i in range(0,25):
    v_prime = A @ v
    np.append(delta, [v - v_prime])
    v = v_prime
    
v
delta
print(delta)
delta = []
for i in range(0,25):
    v_prime = A @ v
    np.append(delta, np.norm(v - v_prime))
    v = v_prime
    
for i in range(0,25):
    v_prime = A @ v
    np.append(delta, np.linalg.norm(v - v_prime))
    v = v_prime
    
v
delta
print(delta)
for i in range(0,25):
    v_prime = A @ v
    delta.append( np.linalg.norm(v - v_prime))
    v = v_prime
    
v =
v
delta
v = np.array([.5,.25,.25])
delta = []
for i in range(0,25):
    v_prime = A @ v
    delta.append( np.linalg.norm(v - v_prime))
    v = v_prime
    
v
delta
delta = np.array(delta)
x = linspace(0,25,25)
x = np.linspace(0,25,25)
plt.plot(x,delta)
plt.show()
get_ipython().run_cell_magic('save', '', '')
get_ipython().run_line_magic('save', '')
get_ipython().run_line_magic('save', 'power_method')
get_ipython().run_line_magic('savepower_method', '')
get_ipython().run_line_magic('save', "'power_method'")
get_ipython().run_line_magic('save', '"power_method"')
get_ipython().run_line_magic('save', '-r power_method')
get_ipython().run_line_magic('save', '-f power_method')
get_ipython().run_line_magic('save', '-f power_method 0-65')
