
import matplotlib.pyplot as plt

# simple plots 1D

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]


# plot
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()

# simple plots 2D

z =[[0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0]]

# plot
fig, ax = plt.subplots()
ax.imshow(z)
plt.show()

# other version

x =[[0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4]]

y =[[0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2],
    [3, 3, 3, 3, 3],
    [4, 4, 4, 4, 4]]

z =[[0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0]]


# plot
fig, ax = plt.subplots()
ax.pcolormesh(x, y, z)
plt.show()

x =[[0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4]]

y =[[0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2],
    [3, 3, 3, 3, 3],
    [4, 4, 4, 4, 4]]

z =[[0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0]]

# plot  
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.scatter(x, y, z)
plt.show()



# simple plots 1D

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# plot
fig, ax = plt.subplots(figsize=(6,6))
ax.plot(x, y, 'o-', color='blue', label='somthing here')
plt.legend()
plt.title('Masked and NaN data')
plt.grid(True)
plt.xlim(0,50)
plt.ylim(0, 50)
plt.xlabel('xlabel', fontsize=18)
plt.ylabel('ylabel', fontsize=16)
plt.show()