
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from Random import RandomDist

# experiment parameters
Nmeas = 1
Nexp = 1000
sigma = 2


true = []
best = []

# instantiate Random class
random = RandomDist()

# Loop through different mu values 
# use function in random.py returns a random pesudo integer using normal distribution (Box-muller method)
for i in range(-100,100):
    mu_true = i/10.0
    for e in range(0, Nexp):
        mu_best = 0
        for m in range(0, Nmeas):
            # random pesudo number 
            x = float(random.normal(mu_true,sigma)) 
            mu_best += x

        mu_best = mu_best/Nmeas
   
        # append into array of mu values
        true.append(mu_true)
        best.append(mu_best)

# plotting 
plt.figure(figsize=(10,8))
plt.hist2d(true, best, bins=[50,150])
plt.colorbar()
plt.ylim(-10,10)
plt.xlim(-10,10)
plt.xlabel('$\\mu$ True', fontsize = 15)
plt.ylabel('$\\mu$ measured',fontsize = 15)
plt.title('Neyman Construction of Gaussian',fontsize = 15)
plt.savefig('Neyman_Gaussian.png')
plt.show()
  

