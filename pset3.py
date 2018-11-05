
# coding: utf-8

# In[121]:


import numpy as np
from __future__ import division
import math
import matplotlib.pyplot as plt

def next_truth (x,y,w1,w2,degree,t):
    import random
    nw1 = random.randint(-5,5)/100;
    nw2 = random.randint(-5,5)/100;
    
    error = 50*2*np.pi/60;
    next_degree = ((w2+error*nw2)*t*20)/(85*(w1+error*nw1)/((w2+error*nw2)-(w1+error*nw1)+0.0000000001));
    dist = (w1+w2)*t*20/2;
    x_new = x + dist*math.sin(degree+next_degree);
    y_new = y + dist*math.cos(degree+next_degree);
    print(degree,next_degree,nw1,nw2,degree+next_degree,w1+error*nw1,x_new)
    
    return x_new, y_new, degree+next_degree


# In[122]:


[x1,y1,d1] = next_truth (1,1,20,20,90,1)


# In[124]:


x = [];
y = [];

w1 = 50*2*np.pi/60;
w2 = 50*2*np.pi/60
x1 = 51;
y1 = 51;
d1 = 0;
for i in range(1,500):
    [x2,y2,d2] = next_truth(x1,y1,w1,w2,d1,0.1);
    x.append(x1);
    y.append(y1);
    x1 = x2;
    y1 = y2;
    d1 = d2;
    
plt.axis([0, 750, 0, 500])
plt.plot(x,y)
plt.show()


# In[145]:


# Observation generation

def ob_gen(x,y,d):
    
    front = (500-y)/math.cos(d);
    right = (750-x)/math.cos(d);
    new_d = d;
    
    return front,right,d


# In[103]:


# Time update

def time_update (x,y,w1,w2,degree,t,x_cov,y_cov,d_cov):
    F = np.zeros((3,3));
    F[0][0] = 1;
    F[0][1] = 0;
    F[0][2] = 0;
    F[1][0] = (-(w1+w2)/2)*math.sin(degree)*t;
    F[1][1] = 1;
    F[1][2] = 0;
    F[2][0] = ((w1+w2)/2)*math.cos(degree)*t;
    F[2][1] = 1;
    F[2][2] = 1;
    
    W = np.zeros((3,2));
    W[0,0] = t/2;
    W[0,1] = t/2;
    W[1,0] = math.cos(degree)*t*20/2;
    W[1,1] = math.cos(degree)*t*20/2;
    W[2,0] = math.sin(degree)*t*20/2;
    W[2,1] = math.sin(degree)*t*20/2;
    
    dist = (w1+w2)*t*20/2;
    error = 50*2*np.pi/60;
    [d_new,x_new,y_new] = np.matrix(F)*[[degree],[x],[y]];
    cov = np.matrix.transpose(np.matrix(F)*[[d_cov],[x_cov],[y_cov]])*np.matrix.transpose(F) + [1,1,1];
    d_cov = cov[0,0];
    x_cov = cov[0,1];
    y_cov = cov[0,2];
    return d_new,x_new,y_new, d_cov,x_cov,y_cov;
    
    


# In[104]:


x = [];
y = [];

cov2 = []
w1 = 50*2*np.pi/60;
w2 = 50*2*np.pi/60
x1 = 51;
y1 = 51;
d1 = 0;
d_cov1 = 0;
x_cov1 = 0;
y_cov1 = 0;
for i in range(1,500):
    [d2,x2,y2,dcov2,xcov2,ycov2] = time_update(x1,y1,w1,w2,d1,0.1,x_cov1,y_cov1,d_cov1);
    x.append(x1);
    y.append(y1);
    x1 = x2;
    y1 = y2;
    d1 = d2;
    d_cov1 = dcov2;
    x_cov1 = xcov2;
    y_cov1 = ycov2;


# In[118]:


# Observation update

def obs_update (x_cov,y_cov,degree):
    
    H = np.zeros((3,3));
    H[0][0] = 0;
    H[0][0] = 1/math.cos(degree);
    H[0][0] = 0;
    H[0][0] = 1/math.sin(degree);
    H[0][0] = 0;
    H[0][0] = 0;
    H[0][0] = 0;
    H[0][0] = 0;
    H[0][0] = 1;
    
    nxcov = np.matrix.transpose(np.matrix(H)*[[x_cov],[y_cov],[degree]])*np.matrix.transpose(H)
    d_covn = nxcov[0,2];
    x_covn = nxcov[0,1];
    y_covn = nxcov[0,0];
    
    return d_covn, x_covn, y_covn
    


# In[120]:


obs_update(2,2,10)

