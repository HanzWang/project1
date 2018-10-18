
# coding: utf-8

# In[325]:


import matplotlib.pyplot as plt
import random
import numpy as np
import time


# In[297]:


W=6;
L=6;
n=W*L*12;
S=np.zeros((n,3));
Pe=0.1;

s0=[1,3,5];
s1=[5,4,2];
s1n=[5,5,4];

s2=[5,4,2];


# In[298]:


#1a


# In[299]:


for i in range(n):
    S[i][0]=int(i//(L*12));
    S[i][1]=int((i//(12))%6);
    S[i][2]=int(i%12);


# In[300]:


#### 1b


# In[301]:


A=['ST','FL','FS','FR','BL','BS','BR'];
a1=A[1];


# In[302]:


#1c


# In[303]:


def probsa(Pe,s1,a1,s1n):
    global psa
    if np.sqrt(abs(s1n[0]-s1[0])**2+abs(s1n[1]-s1[1])**2)>1:
        psa=0;
    elif a1==A[0]:
        psa=1;
    elif (s1[2]-s1n[2])==2 or (s1[2]-s1n[2])==-10:
        if a1==A[1] or a1==A[4]:
            psa=Pe;
        else:
            psa=0;
    elif (s1n[2]-s1[2])==2 or (s1n[2]-s1[2])==-10:
        if a1==A[3] or a1==A[6]:
            psa=Pe;
        else:
            psa=0;
    elif abs(s1[2]-s1n[2])==1:
        if a1==A[1] or a1==A[3] or a1==A[4] or a1==A[6]:
            psa=1-2*Pe;
        elif a1==A[2] or a1==A[5]:
            psa=Pe;       
    elif abs(s1[2]-s1n[2])==0:
        if a1==A[1] or a1==A[3] or a1==A[4] or a1==A[6]:
            psa=Pe;
        elif a1==A[2] or a1==A[5]:
            psa=1-2*Pe;
    else:
        psa=0;
    return psa


# In[304]:


probsa(Pe,s1,a1,s1n)


# In[305]:


#1d


# In[306]:


def nextstate(Pe,s1,a1):
    s1n=s1.copy();
    if a1==A[0]:
        s1n=s1n;
    else:
        r=random.uniform(0, 1);
        if r<Pe:
            s1n[2]=s1n[2]-1;
        elif Pe<=r<2*Pe:
            s1n[2]=s1n[2]+1;
        if a1==A[1] or a1==A[2] or a1==A[3]:
            if s1n[2]==11 or s1n[2]==0 or s1n[2]==1:
                s1n[1]=s1n[1]+1;
            elif s1n[2]==2 or s1n[2]==3 or s1n[2]==4:
                s1n[0]=s1n[0]+1;
            elif s1n[2]==5 or s1n[2]==6 or s1n[2]==7:
                s1n[1]=s1n[1]-1;
            elif s1n[2]==8 or s1n[2]==9 or s1n[2]==10:
                s1n[0]=s1n[0]-1;
        elif a1==A[4] or a1==A[5] or a1==A[6]:
            if s1n[2]==11 or s1n[2]==0 or s1n[2]==1:
                s1n[1]=s1n[1]-1;
            elif s1n[2]==2 or s1n[2]==3 or s1n[2]==4:
                s1n[0]=s1n[0]-1;
            elif s1n[2]==5 or s1n[2]==6 or s1n[2]==7:
                s1n[1]=s1n[1]+1;
            elif s1n[2]==8 or s1n[2]==9 or s1n[2]==10:
                s1n[0]=s1n[0]+1;
                
        if a1==A[1] or a1==A[4]:
            s1n[2]=s1n[2]-1;
        elif a1==A[3] or a1==A[6]:
            s1n[2]=s1n[2]+1;
            
        if s1n[2]>11:
            s1n[2]=s1n[2]-12;
        if s1n[0]>5:
            s1n[0]=s1n[0]-1;
        if s1n[0]<0:
            s1n[0]=s1n[0]+1;
        if s1n[1]>5:
            s1n[1]=s1n[1]-1;
        if s1n[1]<0:
            s1n[1]=s1n[1]+1;
    return s1n


# In[307]:


for i in range(50):
    s1n=nextstate(Pe,s1,a1);
    print(s1n);


# In[308]:


def nextallstates(s1,a1):
    s1n=np.zeros((3,3));
    
    s1n[0]=s1;
    s1n[1]=s1;
    s1n[2]=s1;
    if a1==A[0]:
        s1n[0]=s1;
    else:
        s1n[1][2]=s1[2]-1;
        s1n[2][2]=s1[2]+1;
        for i in range(3):
            if a1==A[1] or a1==A[2] or a1==A[3]:
                if s1n[i][2]==11 or s1n[i][2]==0 or s1n[i][2]==1:
                    s1n[i][1]=s1n[i][1]+1;
                elif s1n[i][2]==2 or s1n[i][2]==3 or s1n[i][2]==4:
                    s1n[i][0]=s1n[i][0]+1;
                elif s1n[i][2]==5 or s1n[i][2]==6 or s1n[i][2]==7:
                    s1n[i][1]=s1n[i][1]-1;
                elif s1n[i][2]==8 or s1n[i][2]==9 or s1n[i][2]==10:
                    s1n[i][0]=s1n[i][0]-1;
            elif a1==A[4] or a1==A[5] or a1==A[6]:
                if s1n[i][2]==11 or s1n[i][2]==0 or s1n[i][2]==1:
                    s1n[i][1]=s1n[i][1]-1;
                elif s1n[i][2]==2 or s1n[i][2]==3 or s1n[i][2]==4:
                    s1n[i][0]=s1n[i][0]-1;
                elif s1n[i][2]==5 or s1n[i][2]==6 or s1n[i][2]==7:
                    s1n[i][1]=s1n[i][1]+1;
                elif s1n[i][2]==8 or s1n[i][2]==9 or s1n[i][2]==10:
                    s1n[i][0]=s1n[i][0]+1;

            if a1==A[1] or a1==A[4]:
                s1n[i][2]=s1n[i][2]-1;
            elif a1==A[3] or a1==A[6]:
                s1n[i][2]=s1n[i][2]+1;

            if s1n[i][2]>11:
                s1n[i][2]=s1n[i][2]-12;
            if s1n[i][0]>5:
                s1n[i][0]=s1n[i][0]-1;
            if s1n[i][0]<0:
                s1n[i][0]=s1n[i][0]+1;
            if s1n[i][1]>5:
                s1n[i][1]=s1n[i][1]-1;
            if s1n[i][1]<0:
                s1n[i][1]=s1n[i][1]+1;
    print(s1n[0][0])
    if s1n[0][0]==s1n[1][0]==s1n[2][0] and s1n[0][1]==s1n[1][1]==s1n[2][1] and s1n[0][2]==s1n[1][2]==s1n[2][2]:
        s1n = np.delete(s1n, (2), axis=0)
        s1n = np.delete(s1n, (1), axis=0)
    elif s1n[0][0]==s1n[1][0] and s1n[0][1]==s1n[1][1] and s1n[0][2]==s1n[1][2]:
        s1n = np.delete(s1n, (0), axis=0)
    elif s1n[2][0]==s1n[1][0] and s1n[2][1]==s1n[1][1] and s1n[2][2]==s1n[1][2]:
        s1n = np.delete(s1n, (1), axis=0)
    elif s1n[0][0]==s1n[2][0] and s1n[0][1]==s1n[2][1] and s1n[0][2]==s1n[2][2]:
        s1n = np.delete(s1n, (0), axis=0)

    return s1n


# In[309]:


nextallstates([0,0,0],A[0])


# In[310]:


s1n


# In[311]:


#2


# In[312]:



R=np.array([[-100,-100,-100,-100,-100,-100],
            [-100,   0,   0,   0,   0,-100],
            [-100,   0, -10, -10, -10,-100],
            [-100,   0,   0,   0,   1,-100],
            [-100,   0, -10, -10, -10,-100],
            [-100,-100,-100,-100,-100,-100]]);


# In[313]:


R[s2[0]][s2[1]]


# In[314]:


#3a


# In[315]:


pi0=np.array([['FS','FS','FS','FS','FS','FS'],
              ['FS','FS','FS','FS','FS','FS'],
              ['FS','FS','FS','FS','FS','FS'],
              ['FS','FS','FS','FS','FS','FS'],
              ['FS','FS','FS','FS','FS','FS'],
              ['FS','FS','FS','FS','FS','FS']]);


# In[316]:


pi0


# #3b

# In[317]:


def route(policy,s0,Pe):
    npolicy=sum(len(x) for x in policy);
    path=np.zeros((npolicy,3));
    for i in range(npolicy):
        path[i]=s0;
        s0=nextstate(Pe,s0,pi0[s0[0],s0[1]]);
    path[i]=s0;  
    return path


# In[318]:


path=route(pi0,s0,Pe);


# In[319]:


path


# In[320]:


#4a


# In[326]:


def value_iteration(S,reward,Pe,theta,A):
    pi=[[['' for a in range(12)]for b in range(6)]for c in range(6)]
    V = np.zeros((6,6,12));
    Va= np.zeros(7);
#    pi= np.zeros((6,6,12));
    while True:

        delta=0;
        for i in range(432):
            Vtem=V[int(S[i][0]),int(S[i][1]),int(S[i][2])];
            n=0;
            Va= np.zeros(7);
            for a in A:
                Va[n]=0;
                Sn=nextallstates(S[i],a);
                for sn in Sn:
                    Va[n]=Va[n]+probsa(Pe,S[i],a,sn)*(reward[int(sn[0]),int(sn[1])]+0.9*V[int(sn[0]),int(sn[1]),int(sn[2])]);
                n=n+1;
            V[int(S[i][0]),int(S[i][1]),int(S[i][2])]=max(Va);
            print(pi[int(S[i][0])][int(S[i][1])][int(S[i][2])])
            pi[int(S[i][0])][int(S[i][1])][int(S[i][2])]=A[np.where(Va==max(Va))[0][0]];
            delta = max(delta, np.abs(Vtem - V[int(S[i][0]),int(S[i][1]),int(S[i][2])]));
           # print(delta)
        if delta<theta:
            break
    return pi, V


# In[327]:


t1 = time.time()
theta=0.05
Pe=0
[pi4,V4]=value_iteration(S,R,Pe,theta,A);
t2 = time.time()


# In[328]:


t2-t1


# In[285]:


def route (policy,s0,pe):
    curstate = s0;
    path = np.zeros((100,3));
    for i in range(100) :
        act = policy[curstate[0]][curstate[1]][curstate[2]];
        n_state = nextstate(pe,curstate,act);
        path[i,:] = n_state;
        plt.plot([curstate[0],n_state[0]],[curstate[1],n_state[1]],'ro-');
        curstate = n_state;
    plt.xlim(0,5)
    plt.ylim(0,5)
    plt.show();
    return path


# In[329]:


route(pi4,[4,4,6],0.1)

