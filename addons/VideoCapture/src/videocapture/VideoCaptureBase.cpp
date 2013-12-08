#include <videocapture/VideoCaptureBase.h>
#include <videocapture/Utils.h>
#include <algorithm>


// TESTING FOR SUPPORTED CAPABILITES
// --------------------------------------------------------------------------------------
bool VideoCaptureBase::isPixelFormatSupported(int device, VideoCapturePixelFormat fmt) {
  std::vector<VideoCaptureCapability> caps = getCapabilities(device);
  return std::find_if(caps.begin(), caps.end(), VideoCaptureCapabilityFindPixelFormat(fmt)) != caps.end();
}

bool VideoCaptureBase::isSizeSupported(int device, int width, int height) {
  std::vector<VideoCaptureCapability> caps = getCapabilities(device);
  return std::find_if(caps.begin(), caps.end(), VideoCaptureCapabilityFindSize(width, height)) != caps.end();
}

bool VideoCaptureBase::isFrameRateSupported(int device, double fps) {
  std::vector<VideoCaptureCapability> caps = getCapabilities(device);
  return std::find_if(caps.begin(), caps.end(), VideoCaptureCapabilityFindFrameRate(fps)) != caps.end();
}

std::vector<VideoCaptureSize> VideoCaptureBase::getSupportedSizes(int device) {
  std::vector<VideoCaptureSize> result;
  std::vector<VideoCaptureCapability> caps = getCapabilities(device);
 
  for(std::vector<VideoCaptureCapability>::iterator it = caps.begin(); it != caps.end(); ++it) {
    VideoCaptureCapability& cap = *it;
    std::vector<VideoCaptureSize>::iterator it_found = std::find(result.begin(), result.end(), cap.size);
    if(it_found == result.end()) {
      result.push_back(cap.size);
    }
  }
 
  return result;
}

std::vector<VideoCapturePixelFormat> VideoCaptureBase::getSupportedPixelFormats(int device, int width, int height) {
  std::vector<VideoCapturePixelFormat> result;
  std::vector<VideoCaptureCapability> caps = getCapabilities(device);
 
  for(std::vector<VideoCaptureCapability>::iterator it = caps.begin(); it != caps.end(); ++it) {
    VideoCaptureCapability& cap = *it;
    if(cap.size.width == width && cap.size.height == height) {
      std::vector<VideoCapturePixelFormat>::iterator it_found = std::find(result.begin(), result.end(), cap.pixel_format);
      if(it_found == result.end()) {
        result.push_back(cap.pixel_format);
      }
    }
  }
 
  return result;
}

std::vector<VideoCaptureRational> VideoCaptureBase::getSupportedFrameRates(int device, int width, int height, VideoCapturePixelFormat fmt) {
  std::vector<VideoCaptureCapability> caps;
  std::vector<VideoCaptureRational> result;

  for(std::vector<VideoCaptureCapability>::iterator it = caps.begin(); it != caps.end(); ++it) {
    VideoCaptureCapability& cap = *it;
    if(cap.size.width == width && cap.size.height == height && cap.pixel_format == fmt) {
      result.push_back(cap.framerate);
    }
  }

  return result;  
}

bool VideoCaptureBase::getBestMatchingCapability(int device, 
                                                 VideoCaptureSettings cfg, 
                                                 VideoCaptureCapability& result) 
{
  std::vector<VideoCaptureCapability> caps = getCapabilities(device);
  for(std::vector<VideoCaptureCapability>::iterator it = caps.begin(); it != caps.end(); ++it) {
    VideoCaptureCapability& cap = *it;
    if(cfg.width == cap.size.width 
       && cfg.height == cap.size.height
       && cfg.in_pixel_format == cap.pixel_format) 
      {
        float cap_fps = rx_videocapture_rational_to_fps(cap.framerate);
        if(cap_fps == cfg.fps) {
          result = cap;
          return true;
        }
      }
  }
  return false;
}


// LOGGING SUPPORTED CAPABILITIES 
// --------------------------------------------------------------------------------------
void VideoCaptureBase::printSupportedFrameRates(int device, 
                                                int width, 
                                                int height,
                                                VideoCapturePixelFormat fmt) 
{

  std::vector<VideoCaptureRational> rates = getSupportedFrameRates(device, width, height, fmt);
  if(!rates.size()) {
    printf("No supported framerates for: %dx%d.\n", width, height);
    return;
  }

  printf("Supported framerate for device: %d and size: %dx%d\n", device, width, height); 
  printf("--------------------------------------------------------------------\n");
  for(std::vector<VideoCaptureRational>::iterator it = rates.begin(); it != rates.end(); ++it) {
    VideoCaptureRational r = *it;
    double fps = 1.0 / (double(r.num) / double(r.den));
    printf("\t %02.02f fps\'n", fps); 
  }

}

void VideoCaptureBase::printSupportedPixelFormats(int device, int width, int height) {

  std::vector<VideoCapturePixelFormat> formats = getSupportedPixelFormats(device, width, height);
  if(!formats.size()) {
    printf("No supported pixel formats for: %dx%d\n", width, height);
    return;
  }

  printf("Supported pixel formats for device: %d and size: %dx%d\n", device, width, height);
  printf("--------------------------------------------------------------------\n");
  for(std::vector<VideoCapturePixelFormat>::iterator it = formats.begin(); it != formats.end(); ++it) {
    VideoCapturePixelFormat f = *it;
    std::string fmt_name = rx_videocapture_pixel_format_to_string(f);
    printf("\t%s\n", fmt_name.c_str());
  }
}

void VideoCaptureBase::printSupportedSizes(int device) { 

  std::vector<VideoCaptureSize> sizes = getSupportedSizes(device);
  if(!sizes.size()) {
    printf("No supported sizes found.\n");
    return;
  }

  printf("Supported sizes for device: %d\n", device);
  printf("--------------------------------------------------------------------\n");
  for(std::vector<VideoCaptureSize>::iterator it = sizes.begin(); it != sizes.end(); ++it) {
    VideoCaptureSize& s = *it;
    printf("\t%dx%d\n", s.width, s.height);
  }
}

void VideoCaptureBase::printSupportedPixelFormats(int device) {

  std::vector<VideoCaptureCapability> caps = getCapabilities(device);
  if(!caps.size()) {
    printf("No capabilities found for device: %d\n", device);
    return;
  }

  printf("Supported pixel formats for device: %d\n", device);
  printf("--------------------------------------------------------------------\n");

  std::set<VideoCapturePixelFormat> unique_fmts;
  for(std::vector<VideoCaptureCapability>::iterator it = caps.begin();
      it != caps.end();
      ++it)
    {
      VideoCaptureCapability cap = *it;
      unique_fmts.insert(cap.pixel_format);
    }

  for(std::set<VideoCapturePixelFormat>::iterator it = unique_fmts.begin();
      it != unique_fmts.end();
      ++it) 
    {
     
      VideoCapturePixelFormat pix_fmt = *it;
      printf("\t%s\n", rx_videocapture_pixel_format_to_string(pix_fmt).c_str());
    }
}

void VideoCaptureBase::printCapabilities(int device) {

  std::vector<VideoCaptureCapability> caps = getCapabilities(device);
  if(!caps.size()) {
    printf("No capabilities found for device: %d\n", device);
    return;
  }

  int last_width = 0;
  int last_height = 0;
  VideoCapturePixelFormat last_pix_fmt = VIDEOCAPTURE_FMT_NONE;
  
  for(std::vector<VideoCaptureCapability>::iterator it = caps.begin();
      it != caps.end();
      ++it)
    {
      VideoCaptureCapability cap = *it;
      if(cap.size.width != last_width 
         || cap.size.height != last_height 
         || cap.pixel_format != last_pix_fmt) 
        {
          printf("\n");
          printf("%s, %dx%d\n", 
                     rx_videocapture_pixel_format_to_string(cap.pixel_format).c_str(),
                     cap.size.width,
                     cap.size.height);
          printf("--------------------------------------------------------------------\n");
          last_width = cap.size.width;
          last_height = cap.size.height;
          last_pix_fmt = cap.pixel_format;
      }
      
      VideoCaptureRational r = cap.framerate;
      double fps = 1.0 / (double(r.num) / double(r.den));
      printf("\tFPS %2.02f \n", fps);
    }
}
