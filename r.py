"""from matplotlib import pyplot as plt
import numpy as np

# Generate 100 random data points along 3 dimensions
x, y, scale = np.random.randn(3, 100)
fig, ax = plt.subplots()

# Map each onto a scatterplot we'll create with Matplotlib
ax.scatter(x=x, y=y, c=scale, s=np.abs(scale)*500)
ax.set(title="Some random data, created with JupyterLab!")
plt.show()
import numpy as np
A=np.array([[4,78],[7,8]])
B=np.array([[4,6],[7,8]])
C=np.array([[9,18],[11,12]])
result1=(A+B)+C
result2=A+(B*C)
if np.array_equal(result1,result2):
    print("s")
else:
        print("y") """


def bhrat():
      c = int(input("enter the number:"))
      r = int(input("enter the number:"))
      x =c+r
      print(x)


bhrat()
      