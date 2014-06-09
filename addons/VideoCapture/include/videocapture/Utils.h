#ifndef ROXLU_VIDEOCAPTURE_UTILS_H
#define ROXLU_VIDEOCAPTURE_UTILS_H

#include <string>
#include <videocapture/Types.h>

std::string rx_videocapture_pixel_format_to_string(VideoCaptureFormat fmt);
float rx_videocapture_rational_to_fps(VideoCaptureRational r);

#endif
