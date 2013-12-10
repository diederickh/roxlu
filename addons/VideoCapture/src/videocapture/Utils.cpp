#include <math.h>
#include <videocapture/Utils.h>

std::string rx_videocapture_pixel_format_to_string(VideoCaptureFormat fmt) {
  switch(fmt) {
    case VIDEOCAPTURE_FMT_NONE:        return "VIDEOCAPTURE_FMT_NONE";         break;
    case VIDEOCAPTURE_FMT_UYVY422:     return "VIDEOCAPTURE_FMT_UYVY422";      break;
    case VIDEOCAPTURE_FMT_YUYV422:     return "VIDEOCAPTURE_FMT_YUYV422";      break;
    case VIDEOCAPTURE_FMT_YUV420P:     return "VIDEOCAPTURE_FMT_YUV420P";      break;
    case VIDEOCAPTURE_FMT_RGB24:       return "VIDEOCAPTURE_FMT_RGB24";        break;
    case VIDEOCAPTURE_FMT_JPEG_OPENML: return "VIDEOCAPTURE_FMT_JPEG_OPENML";  break;
    default:                           return "UNHANDLED PIXELFORMAT";         break;
  };
}

float rx_videocapture_rational_to_fps(VideoCaptureRational r) {
  double d = double(r.num) / double(r.den);
  double fps = 1.0 / d;
  float nearest = floorf(fps * 100 + 0.5) / 100;
  return nearest;
}


