/* RayTracer */

#include <math.h>
#include <stdio.h>
#include <time.h>

#define EPSILON 0.00000001
#define CROSS(dest,v1,v2) \
          dest[0]=v1[1]*v2[2]-v1[2]*v2[1]; \
          dest[1]=v1[2]*v2[0]-v1[0]*v2[2]; \
          dest[2]=v1[0]*v2[1]-v1[1]*v2[0];
#define DOT(v1,v2) (v1[0]*v2[0]+v1[1]*v2[1]+v1[2]*v2[2])
#define SUB(dest,v1,v2) \
          dest[0]=v1[0]-v2[0]; \
          dest[1]=v1[1]-v2[1]; \
          dest[2]=v1[2]-v2[2];

int intersect_triangle(double orig[3], double dir[3],
               double vert0[3], double vert1[3], double vert2[3],
               double *t, double *u, double *v);

int main(){

    double ray_origin[3], ray_direction[3];
    double vert0[3], vert1[3], vert2[3];
    double t = 0.0, u = 0.0, v = 0.0;
    int n, i;
    int value;

    ray_origin[0] = 0.0;
    ray_origin[1] = 0.0;
    ray_origin[2] = 1.0;

    ray_direction[0] = 1.0;
    ray_direction[1] = 0.0;
    ray_direction[2] = 0.0;

    vert0[0] = 1.2;
    vert0[1] = 1.0;
    vert0[2] = 0.0;

    vert1[0] = 1.2;
    vert1[1] = -1.0;
    vert1[2] = 0.0;

    vert2[0] = 1.2;
    vert2[1] = 0.0;
    vert2[2] = 2.0;

    n = 100000000;

    clock_t begin = clock();

    for (i = 0; i <= n; i++){
        value = intersect_triangle(ray_origin, ray_direction, vert0, vert1, vert2, &t, &u, &v);
    }

    clock_t end = clock();

    double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;

    printf("n = %d\n", n);
    printf("time = %f\n", time_spent);

    return 0;
}

int intersect_triangle(double orig[3], double dir[3],
               double vert0[3], double vert1[3], double vert2[3],
               double *t, double *u, double *v)
{
   double edge1[3], edge2[3], tvec[3], pvec[3], qvec[3];
   double det, inv_det;

   /* find vectors for two edges sharing vert0 */
   SUB(edge1, vert1, vert0);
   SUB(edge2, vert2, vert0);

   /* begin calculating determinant - also used to calculate U parameter */
   CROSS(pvec, dir, edge2);

   /* if determinant is near zero, ray lies in plane of triangle */
   det = DOT(edge1, pvec);

   if (det > -EPSILON && det < EPSILON)
     return 0;
   inv_det = 1.0 / det;

   /* calculate distance from vert0 to ray origin */
   SUB(tvec, orig, vert0);

   /* calculate U parameter and test bounds */
   *u = DOT(tvec, pvec) * inv_det;
   if (*u < 0.0 || *u > 1.0)
     return 0;

   /* prepare to test V parameter */
   CROSS(qvec, tvec, edge1);

   /* calculate V parameter and test bounds */
   *v = DOT(dir, qvec) * inv_det;
   if (*v < 0.0 || *u + *v > 1.0)
     return 0;

   /* calculate t, ray intersects triangle */
   *t = DOT(edge2, qvec) * inv_det;

   return 1;
}

