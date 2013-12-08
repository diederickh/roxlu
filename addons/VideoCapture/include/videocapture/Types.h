#ifndef ROXLU_VIDEOCAPTURE_TYPES_H
#define ROXLU_VIDEOCAPTURE_TYPES_H

#define ERR_VIDCAP_INVALID_WIDTH "Invalid VideoCaptureSettings.width\n"
#define ERR_VIDCAP_INVALID_HEIGHT "Invalid VideoCaptureSettings.height\n"
#define ERR_VIDCAP_INVALID_IN_PIX_FMT "Invalid VideoCaptureSettings.in_pixel_format\n"
#define ERR_VIDCAP_INVALID_FPS "Invalid VideoCaptureSettings.fps\n"

#include <stdlib.h>
#include <stdio.h>

typedef void(*videocapture_frame_cb)(void* pixels, size_t nbytes, void* user); /* the callback function that gets called by the implementation with video data */

// The VideoCapture add supports multiple capture implementations, these are used together
// with the VideoCapture() constructor where you tell what capture implementation you want
// to use. For each platform we select a default implementation
enum VideoCaptureImplementation {
  VIDEOCAPTURE_DIRECTSHOW,                   // Windows - DEFAULT - Use the DirectShow samplegrabber
  VIDEOCAPTURE_WINDOWS_MEDIA_FOUNDATION,     // Windows -         - Use the Windows Media Foundation grabber
  VIDEOCAPTURE_AVFOUNDATION,                 // Mac     - DEFAULT - Use the AVFoundation grabber
  VIDEOCAPTURE_V4L2                          // Linux   - DEFAULT - Use the Video4Linux sample grabber
};

enum VideoCapturePixelFormat {
  VIDEOCAPTURE_FMT_NONE,
  VIDEOCAPTURE_FMT_UYVY422,
  VIDEOCAPTURE_FMT_YUYV422,
  VIDEOCAPTURE_FMT_YUV420P,
  VIDEOCAPTURE_FMT_YUV444P,
  VIDEOCAPTURE_FMT_YUV444P16LE,
  VIDEOCAPTURE_FMT_YUV444P10LE,
  VIDEOCAPTURE_FMT_YUV422P16LE,
  VIDEOCAPTURE_FMT_YUV422P10LE,
  VIDEOCAPTURE_FMT_RGB24,
  VIDEOCAPTURE_FMT_ARGB,
  VIDEOCAPTURE_FMT_BGRA,
  VIDEOCAPTURE_FMT_RGB555BE,
  VIDEOCAPTURE_FMT_RGB555LE,
  VIDEOCAPTURE_FMT_RGB565BE,
  VIDEOCAPTURE_FMT_RGB565LE
};

// VideoCaptureSize represents the capture width/height a device can use to capture (most devices support multiple sizes)
struct VideoCaptureSize {
  VideoCaptureSize();
  int width;
  int height;

  bool operator<(const VideoCaptureSize& o) const {
    return width < o.width && height < o.height;
  }

  bool operator==(const VideoCaptureSize& o) const {
    return width == o.width && height == o.height;
  }

};

struct VideoCaptureRational {
  VideoCaptureRational();
  void set(float n, float d);
  double num;
  double den;
};

// VideoCaptureCapability represent the capabilities that a capture device supports. 
struct VideoCaptureCapability {
  VideoCaptureCapability();
  int index;                                       /* default to -1, but can be used by the implementation to reference an internal index */
  VideoCaptureSize size;
  VideoCaptureRational framerate;
  VideoCapturePixelFormat pixel_format;
};

// Used to filter capabilities on pixel formats
struct VideoCaptureCapabilityFindPixelFormat {
  VideoCaptureCapabilityFindPixelFormat(VideoCapturePixelFormat fmt):fmt(fmt){}
  bool operator()(const VideoCaptureCapability& c) { return c.pixel_format == fmt; } 
  VideoCapturePixelFormat fmt;
};


// Used to filter capabilites on size
struct VideoCaptureCapabilityFindSize {
  VideoCaptureCapabilityFindSize(int w, int h):w(w),h(h){}
  bool operator()(const VideoCaptureCapability& c) { return c.size.width == w && c.size.height == h; } 
  int w;
  int h;
};

// find FPS, 2 decimal significance
struct VideoCaptureCapabilityFindFrameRate {
  VideoCaptureCapabilityFindFrameRate(double fps):fps(fps) {}
  bool operator()(const VideoCaptureCapability& c) { 
    double c_fps = 1.0 / (double(c.framerate.num)/double(c.framerate.den));
    float c_fps_corr = 0;
    char buf[512];
    sprintf(buf, "%2.02f", c_fps);
    sscanf(buf, "%f", &c_fps_corr);
    return c_fps_corr == fps;
  } 
  double fps;
};

// The VideoCaptureSettings are used to open a capture device
struct VideoCaptureSettings {
  VideoCaptureSettings();
  bool validate();                             /* returns true when all member has been correctly set */

  int width;                                   /* the width you want to capture in */ 
  int height;                                  /* the height you want to capture in */
  float fps;                                   /* the framerate you want to capture in, must  2 digit accurate, e.g. 30.00, 29.97, 20.00 etc... */
  VideoCapturePixelFormat in_pixel_format;     /* the pixel format you want to receive you're data in.. this must be supported */
};

// -----------------------------------

inline VideoCaptureSize::VideoCaptureSize()
              :width(0)
              ,height(0)
{
}

inline VideoCaptureCapability::VideoCaptureCapability() 
                              :index(-1)
{
}

#endif
