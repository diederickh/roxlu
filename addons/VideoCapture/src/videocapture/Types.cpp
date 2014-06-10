#include <stdio.h>
#include <videocapture/Types.h>

VideoCaptureSettings::VideoCaptureSettings() 
  :width(0)
  ,height(0)
  ,fps(0.0f)
  ,in_pixel_format(VIDEOCAPTURE_FMT_NONE)
  ,in_codec(VIDEOCAPTURE_FMT_NONE)
{
}

bool VideoCaptureSettings::validate() {
  bool result = true;

  if(in_pixel_format == VIDEOCAPTURE_FMT_NONE) {
    printf(ERR_VIDCAP_INVALID_IN_PIX_FMT);
    result = false;
  }

  if(width == 0) {
    printf(ERR_VIDCAP_INVALID_WIDTH);
    result = false;
  }

  if(height == 0) {
    printf(ERR_VIDCAP_INVALID_HEIGHT);
    result = false;
  }

  if(fps == 0.0f) {
    printf(ERR_VIDCAP_INVALID_FPS);
    result = false;
  }

  return result;
}

// ---------------------------------------------------------------------

VideoCaptureRational::VideoCaptureRational()
  :num(0.0)
  ,den(0.0)
{
}

void VideoCaptureRational::set(float n, float d) {
  num = n;
  den = d;
}
