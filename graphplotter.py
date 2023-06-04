#Install matplotlib
import matplotlib.pyplot as plt

x1=[2,4,6]
y1=[1,5,8]
x2=[5,6,2]
y2=[1,3,6]
plt.plot(x1,y1,label='Line 1')
plt.plot(x2,y2,label='Line 2')
plt.xlabel('X-AXIS')
plt.ylabel('Y-AXIS')
plt.title("Graph")

plt.legend()

plt.show()