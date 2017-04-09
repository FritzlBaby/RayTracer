#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

def ray_segment_intersection(origin, direct, point1, point2):

    vect1 = origin - point1
    vect2 = point2 - point1
    vect3 = np.array((-direct[1], direct[0]))

    t1 = np.cross(vect2, vect1)/np.dot(vect2, vect3)
    t2 = np.dot(vect1, vect3)/np.dot(vect2, vect3)

    if t1 >= 0.0 and t2 >= 0.0 and t2 < 1.0:
        return True

    return False


def get_segment(x, y, i, j, segment):
    if segment == 0:
        return np.array([[x[i], y[j]],[x[i], y[j-1]]], dtype=np.float)
    elif segment == 1:
        return np.array([[x[i], y[j-1]],[x[i-1], y[j-1]]], dtype=np.float)
    elif segment == 2:
        return np.array([[x[i-1], y[j-1]],[x[i-1], y[j]]], dtype=np.float)
    elif segment == 3:
        return np.array([[x[i-1], y[j]],[x[i], y[j]]], dtype=np.float)
    else:
        raise ValueError("0 < segment < 3")


xmin = -3.0
xmax = 3.0
xres = 7

ymin = -4.0
ymax = 4.0
yres = 9

x = np.linspace(xmin, xmax, xres)
y = np.linspace(ymin, ymax, yres)

origin = np.array((0.25, 0.25), dtype=np.float)
direct = np.array((0.5, 1.0), dtype=np.float)

# find which box origin starts in
i = 0
while origin[0] > x[i]:
    i += 1

j = 0
while origin[1] > y[j]:
    j += 1

check_boxes = [(i,j)]

next_segments = [0, 1, 2, 3]


for k in range(5):
    segment_hit = False
    for segment in next_segments:
        if segment_hit:
            continue

        current_segment = get_segment(x, y, i, j, segment)

        p1 = current_segment[0,:]
        p2 = current_segment[1,:]

        segment_hit =  ray_segment_intersection(origin, direct, p1, p2)

        if segment_hit:
            print "Segment ", segment, " hit"

            if segment == 0:
                print "hit right hand side, i + 1"
                i += 1
                next_segments = [0, 1, 3]

            elif segment == 1:
                print "hit bottom side, j - 1"
                j += -1
                next_segments = [0, 1, 2]

            elif segment == 2:
                print "hit left hand side, i - 1"
                i += -1
                next_segments = [1, 2, 3]

            elif segment == 3:
                print "hit top side, j + 1"
                j += 1
                next_segments = [0, 2, 3]

            check_boxes.append((i,j))

print check_boxes

end = origin + 5*direct

ax = plt.figure().gca()


plt.plot([origin[0], end[0]], [origin[1], end[1]], "kx-", ms=5)

ax.set_xticks(x)
ax.set_yticks(y)
plt.axis([-6, 6, -6, 6])
plt.grid()
plt.show()




