
# coding: utf-8

# In[343]:


import random
import numpy as np
import copy
import matplotlib.pyplot as plt
import array as arr
import time


# In[191]:


W=6;
L=6;
n=W*L*12;
S=np.zeros((n,3));
Pe=0.1;
a1=A[1];
s1=[5,4,2];
s1n=[5,5,4];

s2=[5,4,2];


# In[7]:


#1a


# In[8]:


for i in range(n):
    S[i][0]=i//(L*12);
    S[i][1]=(i//(12))%6;
    S[i][2]=i%12;


# In[9]:


#1b


# In[10]:


A=['Stay','FL','FS','FR','BL','BS','BR'];


# In[11]:


#1c


# In[318]:


# Since there are too many states, we mainly focus on the change in h where there are only situation of changing 1 ,2 and 0
# We first testing the distance between tow states
def probsa(Pe,s1,a1,s1n):
    if np.sqrt(abs(s1n[0]-s1[0])**2+abs(s1n[1]-s1[1])**2)>1:
        psa=0;
    elif a1==A[0]:
        psa=1;
    elif s1[2]-s1n[2] == -2 or s1[2]-s1n[2] == 10: # 2 units change in h determination also need help from action 
        if (a1 == A[1]) or (a1 == A[4]):
            psa = 0;
        else:
            psa=Pe;
    elif s1[2]-s1n[2] == 2 or s1[2]-s1n[2] == -10:
        if a1 == A[4] or a1 == A[6]:
            psa = 0;
        else:
            psa=Pe;
    elif abs(s1[2]-s1n[2])==1 or abs(s1[2]-s1n[2])==11 : #Due to the clock 0=12 issue, we need to cover some speicial case
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


# In[199]:


probsa(Pe,s1,a1,s1n)


# In[200]:


s1n


# In[201]:


probsa(0,[2,0,0],'FL',[2,1,11])


# In[25]:


#1d


# In[122]:


def nextstate(Pe,s1,a1):
    s1n = copy.deepcopy(s1);
    if a1==A[0]:
        s1n=s1n;
    else:
        r=random.uniform(0, 1);# We first random number to simulate the error rate, and then consider next transition
        if r<Pe:
            s1n[2]=(s1n[2]-1) % 12;
        elif Pe<=r<2*Pe:
            s1n[2]=(s1n[2]+1) % 12;
        if a1==A[1] or a1==A[2] or a1==A[3]: # All the possible transication 
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
            s1n[2]=(s1n[2]-1) % 12;
        elif a1==A[3] or a1==A[6]:
            s1n[2]=(s1n[2]+1) % 12;
            

        if s1n[0]>5:
            s1n[0]=s1n[0]-1;
        if s1n[0]<0:
            s1n[0]=s1n[0]+1;
        if s1n[1]>5:
            s1n[1]=s1n[1]-1;
        if s1n[1]<0:
            s1n[1]=s1n[1]+1;
    return s1n


# In[38]:


#2


# In[220]:


R=np.array([[-100,-100,-100,-100,-100,-100],
            [-100,   0,   0,   0,   0,-100],
            [-100,   0, -10, -10, -10,-100],
            [-100,   0,   0,   0,   1,-100],
            [-100,   0, -10, -10, -10,-100],
            [-100,-100,-100,-100,-100,-100]]);
# In order to match the graph given in homework, we need to adjust the matrix oder since array is in form (x,y) and first line is 0 row


# In[41]:


#3a


# In[268]:


pi0=[[['FL' for a in range(12)]for b in range(6)]for c in range(6)]


# #3b

# In[351]:


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


# In[352]:


route(pi0,[1,4,6],0)


# In[125]:


#3D


# In[319]:


def evalpolicy (policy,discount):
    v = np.zeros((6,6,12));
    x = np.ones((6,6,12))
    while (np.amax(x)>0.01):
        v_old = copy.deepcopy(v);
        for i in range(6):
            for y in range(6):
                for u in range(12):
                    nx = nextstate(0,[i,y,u],policy[i][y][u])
                    v[i,y,u] = probsa(0,[i,y,u],policy[i][y][u],nextstate(0,[i,y,u],policy[i][y][u]))*(R[nx[0],nx[1]]+discount*v[i,y,u])
                    #print ([i,y,u],nextstate(0,[i,y,u],policy[i,y]),probsa(0,[i,y,u],policy[i,y],nextstate(0,[i,y,u],policy[i,y])),R[i,y])
                    # Using the formula from class, and sum through all possible states
                    # In fact, since we assume pe=0. We can use one state, since under specific action, the probility is always 1
                    #print("\n")
                    
                    x = v-v_old;
    return v
        
        
    


# In[339]:


evalpolicy(pi0,0.9)


# In[214]:


#3f


# In[334]:


def policyiteration (statevalue,discount):
    op_po = [[['' for a in range(12)] for b in range(6)] for c in range(6)]
    v = np.zeros((6,6,12));
    for i in range(6):
            for y in range(6):
                for u in range(12):
                    vmax = 0
                    for k in A:
                        nx = nextstate(0,[i,y,u],k)
                        v[i,y,u] = probsa(0,[i,y,u],k,nx)*(R[nx[0],nx[1]]+discount*statevalue[i,y,u])
                        if abs(v[i,y,u]) >= abs(vmax):
                            vmax = v[i,y,u];
                            op_po[i][y][u] = k
    return op_po


# In[335]:


initial = np.zeros((6,6,12));
policyiteration (initial,0.9)


# In[ ]:


##3g


# In[346]:


t0 = time.time()


# In[340]:


def interateprocess (discount):
    pi_prac=[[['FR' for a in range(12)]for b in range(6)]for c in range(6)]
    pi_op=[[['FL' for a in range(12)]for b in range(6)]for c in range(6)]
    while (pi_op != pi_prac):
        pi_prac = pi_op
        value = evalpolicy(pi_prac,discount);
        pi_op = policyiteration (value, discount)
    return pi_op
    


# In[341]:


optimal = interateprocess(0.9)


# In[ ]:


##3h


# In[342]:


route(optimal,[1,4,6],0)


# In[347]:


t1 = time.time()


# In[348]:


##3i


# In[349]:


print 'function vers1 takes %f' %(t1-t0)


# In[ ]:


##5a


# In[353]:


route(pi0,[1,4,6],0.25)


# In[ ]:


##5b


# In[368]:


def evalpolicype (pe,policy,discount):
    v = np.zeros((6,6,12));
    x = np.ones((6,6,12))
    while (np.amax(x)>0.01):
        v_old = copy.deepcopy(v);
        for i in range(6):
            for y in range(6):
                for u in range(12):
                    for a in range(100):
                        output = []
                        ref = []
                        nx = nextstate(pe,[i,y,u],policy[i][y][u])
                        recof = [nx[0],nx[1]]
                        if nx not in output:
                            output.append(nx)
                            ref.append(ref)
                    print(output)
                    for c in range(3):
                        v[i,y,u] = v[i,y,u]+probsa(pe,[i,y,u],policy[i][y][u],output[c])*(R[ref[c]]+discount*v[i,y,u])

                    
                    x = v-v_old;
    return v
        


# In[369]:


def interateprocesspe (discount,pe):
    pi_prac=[[['FR' for a in range(12)]for b in range(6)]for c in range(6)]
    pi_op=[[['FL' for a in range(12)]for b in range(6)]for c in range(6)]
    while (pi_op != pi_prac):
        pi_prac = pi_op
        value = evalpolicype (pe,pi_prac,discount);
        pi_op = policyiteration (value, discount)
    return pi_op


# In[370]:


interateprocesspe (0.9,0.25)

