#!/usr/bin/python

import numpy as np


def ray_segment_intersection(origin, direct, point1, point2):

    vect1 = origin - point1
    vect2 = point2 - point1
    vect3 = np.array((-origin[1], origin[0]))

    t1 = np.cross(vect2, vect1)/np.dot(vect2, vect3)
    t2 = np.dot(vect1, vect3)/np.dot(vect2, vect3)

    if t1 >= 0.0 and t2 >= 0.0 and t2 < 1.0:
        return True

    return False


def get_segments(x, y, i, j):
    segment1 = np.array([[x[i], y[j]],[x[i], y[j-1]]], dtype=np.float)
    segment2 = np.array([[x[i], y[j-1]],[x[i-1], y[j-1]]], dtype=np.float)
    segment3 = np.array([[x[i-1], y[j-1]],[x[i-1], y[j]]], dtype=np.float)
    segment4 = np.array([[x[i-1], y[j]],[x[i], y[j]]], dtype=np.float)

    return [segment1, segment2, segment3, segment4]


xmin = -10.0
xmax = 10.0
xres = 21

ymin = -30.0
ymax = 30.0
yres = 31

x = np.linspace(xmin, xmax, xres)
y = np.linspace(ymin, ymax, yres)

origin = np.array((0.1, 0.1), dtype=np.float)
direct = np.array((0.5, 1.0), dtype=np.float)

print origin

# find which box origin starts in
for i, xi in enumerate(x):
    if origin[0] < xi:
        break
x_start_index = i - 1

for j, yi in enumerate(y):
    if origin[1] < yi:
        break
y_start_index = j - 1

i = 0
while origin[0] > x[i]:
    i += 1

j = 0
while origin[1] > y[j]:
    j += 1

print i, j



for k in range(4):

    for index, segment in enumerate(get_segments(x, y, i, j)):

        segment_hit = ray_segment_intersection(origin, direct, segment[0,:], segment[1,:])

        if segment_hit:
            break


    print index


    if index == 0:
        i += 1
    elif index == 1:
        y -= 1
    elif index == 2:
        i -= 1
    elif index == 3:
        y += 1
    else:
        raise ValueError("oh nos!")








