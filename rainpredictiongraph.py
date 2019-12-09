import numpy
import matplotlib.pyplot as plt
x=numpy.array([87.833,78.1,65.133,45.56]).reshape(-1,1)
y=[2011,2012,2015,2016]

plt.figure()
plt.title('prediction of rainfall')
plt.xlabel('years')
plt.ylabel('rain fall')
plt.plot(x,y,'ko')
plt.grid(True)
plt.show()
