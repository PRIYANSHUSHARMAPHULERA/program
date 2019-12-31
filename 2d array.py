import numpy as np
import matplotlib.pyplot as plt
x_train =np.array([
    [158,64],
    [171,86],
    [183,84],
    [191,80],
    [155,49],
    [163,59],
    [180,67],
    [158,54],
    [170,67]
])
y_train=['male','male','male','male','female','female','female','female','female']
plt.figure()
plt.title('human height and weight by sex')
plt.xlabel('height in cm')
plt.ylabel('weight in kg')

for i,x in enumerate(x_train):
    plt.scatter(x[0],x[1],c='k',marker='x' if y_train[i]=='male' else 'D')
plt.grid(True)
plt.show()
