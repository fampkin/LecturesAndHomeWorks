import matplotlib.pyplot as plt
import matplotlib.patches as patches
fig = plt.figure()
ax = fig.add_subplot(111)
x = [0, 1, 3 ,4]
y = [0, 2, 4 ,6]
points = [[0, 0], [1, 2], [3, 4], [4 ,6]]
# ax.set_xlim(10)
# ax.set_ylim(10)
ax.add_patch(patches.Polygon(points, fill = False))
plt.show()