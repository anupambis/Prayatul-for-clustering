# -*- coding: utf-8 -*-
"""PrayatulClusterNoteBook.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10nwaUDrJ7YuIPUIUltd_XmR549uSnGkJ

### Prayatul Matrix for direct comparison of clustering algorithms                                                          
  Source codes demo version 1.0                                                                      
                                                                                                  
  Developed in Python 3
"""

import numpy as np

"""### Prayatul Matrix Generation
The generatePrayatulMatrixCluster function takes three inputs
 1) G : Ground truth labels of all test samples in the dataset
 2) P : Predicted labels obtained with primary algorithm
 3) Q : Predicted labels obtained with alternative algorithm
"""

def generatePrayatulMatrixCluster( G,P,Q ):
    D = np.array([[0,0], [0,0]])
    n=len(G)
    count=0
    for i in range(n):
        for j in range(i+1,n): 
            count+=1
            if P[i]==P[j] and Q[i]==Q[j] and G[i]==G[j]:
                D[0][0]+=1
            elif P[i]==P[j] and Q[i]!=Q[j] and G[i]==G[j]:
                D[0][1]+=1
            elif P[i]!=P[j] and Q[i]==Q[j] and G[i]==G[j]:
                D[1][0]+=1
            elif P[i]!=P[j] and Q[i]!=Q[j] and G[i]==G[j]:
                D[1][1]+=1  
            elif P[i]!=P[j] and Q[i]!=Q[j] and G[i]!=G[j]:
                D[0][0]+=1
            elif P[i]!=P[j] and Q[i]==Q[j] and G[i]!=G[j]:
                D[0][1]+=1
            elif P[i]==P[j] and Q[i]!=Q[j] and G[i]!=G[j]:
                D[1][0]+=1
            elif P[i]==P[j] and Q[i]==Q[j] and G[i]!=G[j]:
                D[1][1]+=1       
    print('count=', count)
    return D

"""### Scores based on Prayatul Matrix
The getScore function takes a prayatul matrix as input and return five scores
"""

def getScores(D):
    BR=D[0][0]
    RW=D[0][1]
    WR=D[1][0]
    BW=D[1][1]
    k=0.0001  # k is a very small quantity added to the denominator to avoid x/0 situation
    if RW==0 and WR==0:
        sigmaC=(RW-WR)/(RW+WR+k)
    else:
        sigmaC=(RW-WR)/(RW+WR)
    alpha=(BR+RW-BW)/(BR+RW+WR+BW)    
    if BR==0 and RW==0 and WR==0:
        xiC=(BR+RW)/(BR+RW+WR+k)
        xiE=(BR+RW-WR)/(BR+RW+WR+k)
    else:
        xiC=(BR+RW)/(BR+RW+WR)
        xiE=(BR+RW-WR)/(BR+RW+WR)    
    phiE=(BR+RW-WR)/(BR+RW+WR+BW)
    return sigmaC, alpha, xiC, xiE, phiE

# Example 1
G=[1,1,0,0,1]
P=[1,1,0,0,1]
Q=[0,0,1,1,0]
# Q=[1,1,0,0,1]

# Example 2
# # Ground truth labels for test all samples
# G=[1,1,1,0,0,0,1,0,0,1,1,0,1,1,0,1,1,1,0,1]

# # Predicted labels for all test samples obtained with primary algorithm, whose performance is to be compared
# P=[1,1,1,0,1,0,1,1,0,0,1,0,1,0,0,1,1,1,1,1]

# # Predicted labels for all test samples obtained with alternative algorithm with whom the primary algorithm is to be compared
# Q=[1,0,1,0,1,1,0,1,0,1,0,1,1,1,0,0,1,0,0,1]


D=generatePrayatulMatrixCluster(G,P,Q)
# Display Prayatul Matrix D
print(D)

sigmaC, alpha, xiC, xiE, phiE = getScores(D)
# Display Scores obatained based on the Prayatul Matrix prepared for two ML algorithms 
print(sigmaC, alpha, xiC, xiE, phiE)