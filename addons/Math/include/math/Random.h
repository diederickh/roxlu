#ifndef ROXLU_RANDOMH
#define ROXLU_RANDOMH

// random: source openFrameworks + stackoverflow
#include <stdlib.h>
#include <math/Vec3.h>
#include <math/Vec2.h>

#if __APPLE__
#  include <sys/time.h>
#  include <unistd.h>
#endif

static void rx_init_random() {
#if defined(__APPLE__)
  struct timeval tv;
  gettimeofday(&tv, 0);
  long int n = (tv.tv_sec ^ tv.tv_usec) ^ getpid();
  srand(n);
#elif ROXLU_PLATFORM == ROXLU_WINDOWS
  srand(GetTickCount());
#else
#error initRandom cannot execute on this operating system
#endif
}

static void rx_init_random(int val) {
  srand((long) val);
}

static float rx_random(float max) {
  return max * rand() / (RAND_MAX + 1.0f);
}

static float rx_random(float x, float y) {
  float high = 0;
  float low = 0;
  float result = 0;
	
  high = std::max<float>(x,y);
  low = std::min<float>(x,y);
  result = low + ((high-low) * rand()/(RAND_MAX + 1.0));
  return result;
}

static float rx_randomf() {
  float rand_num = 0;
  rand_num = (rand()/(RAND_MAX + 1.0)) * 2.0 - 1.0;
  return rand_num;
}

static float rx_randomuf() {
  float rand_num = 0;
  rand_num = rand()/(RAND_MAX + 1.0);
  return rand_num;
}

static roxlu::Vec3 rx_random_vec3() {
  roxlu::Vec3 r;
  float phi = rx_random(3.1415f * 2.0f);
  float costheta = rx_random(-1.0f, 1.0f);

  float rho = sqrt(1.0f - costheta * costheta);
  r.x = rho * cos(phi);
  r.y = rho * sin(phi);
  r.z = costheta;
  return r;
}

static roxlu::Vec2 rx_random_vec2() {
  roxlu::Vec2 r;
  float phi = rx_random(3.1415f * 2.0f);
  float costheta = rx_random(-1.0f, 1.0f);
  float rho = sqrt(1.0f - costheta * costheta);
  r.x = rho * cos(phi);
  r.y = rho * sin(phi);
  return r;
}

#endif
