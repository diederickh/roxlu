/*

  PI                      - the value of pi
  HALF_PI                 - value of (pi * 0.5)
  TWO_PI                  - the value of 2 * pi
  FOUR_PI                 - four times pi
  DEG_TO_RAD              - convert degrees to radians
  RAD_TO_DEG              - convert radians to degrees
  MIN(a,b)                - get the lowest value
  MAX(a,b)                - get the biggest value
  CLAMP(val, min, max)    - make sure a value stays between min and max
  ABS(x)                  - get absolute value (-10 become 10)
  IS_ZERO(f)              - use epsilon value to check if a float is zero or almost zero

  rx_fast_sqrt(v)         - faster but a bit less accurate sqrt function

 */


#ifndef ROXLU_MATH_UTILS_H
#define ROXLU_MATH_UTILS_H

#ifndef PI
#  define PI 3.14159265358979323846
#endif

#ifndef TWO_PI
#  define TWO_PI 6.28318530717958647693
#endif

#ifndef FOUR_PI
#  define FOUR_PI 12.56637061435917295385
#endif

#ifndef HALF_PI
#  define HALF_PI 1.57079632679489661923
#endif

#ifndef DEG_TO_RAD
#  define DEG_TO_RAD (PI/180.0)
#endif

#ifndef RAD_TO_DEG
#  define RAD_TO_DEG (180.0/PI)
#endif

#ifndef MIN
#  define MIN(x,y) (((x) < (y)) ? (x) : (y))
#endif

#ifndef MAX
#  define MAX(x,y) (((x) > (y)) ? (x) : (y))
#endif

#ifndef CLAMP
#  define CLAMP(val,min,max) (MAX(MIN(val,max),min))
#endif

#ifndef ABS
#  define ABS(x) (((x) < 0) ? -(x) : (x))
#endif

#ifndef IS_ZERO
#  define EPSILON 0.000001
#  define IS_ZERO(f) (fabs(f) < EPSILON)        
#endif

// as described in: "From Quaternion to Matrix and Back", J.M.P. van Waveren, 27th feb. 2005, id software
static float rx_fast_sqrt(float x) {
  long i; 
  float y, r; 
  y = x * 0.5f; 
  i = *(long *)( &x ); 
  i = 0x5f3759df - ( i >> 1 ); 
  r = *(float *)( &i ); 
  r = r * ( 1.5f - r * r * y ); 
  return r; 
}

#endif
