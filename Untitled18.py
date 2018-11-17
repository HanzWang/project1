
# coding: utf-8

# In[27]:


import math
def closest_point (p1,pspace):
    dist = [];
    for i in pspace:
        distance = math.sqrt((i[0]-p1[0])**2+(i[1]-p1[1])**2);
        dist.append(distance);
    close_point_index = dist.index(min(dist));
    return pspace[close_point_index]


# In[28]:


p1 = [1,2]
pspace = [[2,3],[4,5],[1,5]];

[a,b] = closest_point (p1,pspace)


# In[29]:


def step (target,initial,delta,w):
    if ((target[0]-initial[0]<10)&(target[1]-initial[1]<10)):
        new_p = initial;
    else:
        
        dist = math.sqrt((target[0]-initial[0])**2+(target[1]-initial[1])**2);
        if (dist < delta):
            new_p = target;
        else:
        #if ((target[0]>initial[0])&(target[1]>initial[1])):
            new_p = [initial[0]+((target[0]-initial[0])/(dist/(w*20))),initial[1]+((target[1]-initial[1])/(dist/(w*20)))];
        #if ((target[0]>initial[0])&(target[1]<initial[1])):
            #new_p = [initial[0]+((target[0]-initial[0])/(dist/(w*20))),initial[1]-((target[1]-initial[1])/(dist/(w*20)))];
        #if ((target[0]<initial[0])&(target[1]>initial[1])):
            #new_p = [initial[0]-((target[0]-initial[0])/(dist/(w*20))),initial[1]+((target[1]-initial[1])/(dist/(w*20)))];
        #if ((target[0]<initial[0])&(target[1]<initial[1])):
         #   new_p = [initial[0]-((target[0]-initial[0])/(dist/(w*20))),initial[1]-((target[1]-initial[1])/(dist/(w*20)))];
    return new_p


# In[117]:


target = [60,50];
initial = [80,100];
w = 1;
delta = 20*w;

[c,d] = step(target,initial,delta,w)


# In[118]:


c


# In[119]:


d


# In[120]:


import matplotlib.patches as patches
import matplotlib.pyplot as plt
rec = patches.Rectangle((5,5),30,50);


# In[134]:


from random import *

new_point = [200,400];
path = []
target = [700,500]
dist =200;
while (dist>75):
    x = randint(1,750);
    y = randint(1,500);
    print(x)
    print(y)
    new_point = step([x,y],new_point,delta,w);
    for i in path:
        if((x-i[0]<10)&(y-i[1]<10)):
            new_point = i;
    if (((new_point[0]<500)&(new_point[0]>400))&(new_point[1]>100)&(new_point[1]<200)):
        new_point = path[len(path)-1];
    path.append(new_point);
    dist = math.sqrt((target[0]-new_point[0])**2+(target[1]-new_point[1])**2);
    


# In[135]:


x = [];
y = [];
for i in path:
    x.append(i[0]);
    y.append(i[1]);


# In[145]:


plt.scatter(x,y)
#ax2 = im.add_subplot(111, aspect='equal')

for i in range(len(path)-1):
    cp = closest_point(path[i],path);
    plt.plot([path[i][0],cp[0]],[path[i][1],cp[1]],'k-');

plt.show()

