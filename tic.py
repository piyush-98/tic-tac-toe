
# coding: utf-8

# In[4]:


def conditions():
    flag=0
    
    for v in l:
        if (set(v))=={1} or (set(v))=={2}:
            flag=1
    if(flag==0):
        col_l=zip(*l)
        for r in col_l:
            if (set(v))=={1} or (set(v))=={2}:
                flag=1
    if(flag==0):
        col_l=zip(*l)
        for r in col_l:
            if (set(r))=={1} or (set(r))=={2}:
                flag=1
    if(flag==0):
        import numpy as np
        dia_l=(np.diag(l))
        dia_r=(np.diag(l[::-1])[::-1])
        if(set(dia_l))=={1} or (set(dia_r))=={1} or (set(dia_l))=={2} or (set(dia_r))=={2}:
            flag=1
    if(flag==0):
        count=0
        for w in l:
            if 0 in w:
                count=count+1
        if(count==0):
            flag=2
    return flag
def tictac():
    
    flag=0
    print('first user: \n')
    n=int(input())
    if n<3:
        l[0][n]=1
    elif n<6:
        l[1][n%3]=1
    else:
        l[2][n%3]=1
        
    for s in l:
        for t in s:
            print(t,end=' ')
        print('\n')
    flag=conditions()
    if(flag):
        if(flag==1):
            print('user 1 is the winner')
        else:
            print('the game is a draw')
    else:
        print('second user: \n')
        n1=int(input())
        if n1<3:
            l[0][n1]=2
        elif n1<6:
            l[1][n1%3]=2
        else:
            l[2][n1%3]=2
        for s in l:
            for t in s:
                print(t,end=' ')
            print('\n')
        flag=conditions()
        if(flag):
            if(flag==1):
                print('user 2 is the winner')
            else:
                print('the game is a draw')
        else:
            tictac()           

l=[]
for i in range(0,3):
    l.append([])
    l[i]=[0]*3
#print(l)
l1=[[0,1,2],[3,4,5],[6,7,8]]
print("welcome to the game \n the user should enter the pos as shown")
for q in l1:
    for z in q:
        print(z,end=' ')
    print('\n')
    
tictac()


# In[ ]:




# In[ ]:



