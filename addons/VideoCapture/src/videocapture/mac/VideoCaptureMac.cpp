#include <videocapture/mac/VideoCaptureMac.h>

VideoCaptureMac::VideoCaptureMac()
  :cap(NULL)
{
  cap = avf_alloc();
  if(!cap) {
    printf(ERR_CAP_MAC_CANNOT_ALLOC);
  }
}

VideoCaptureMac::~VideoCaptureMac() {
  printf("added a VideoCaptureAVFoundation::dealloc + make sure that all is dealloc'd\n");
  avf_dealloc(cap);
}

int VideoCaptureMac::listDevices() {
  return avf_list_devices(cap);
}

bool VideoCaptureMac::openDevice(int device, VideoCaptureSettings cfg) {
  if(!cfg.validate()) {
    return false;
  }
  return avf_open_device(cap, device, cfg);
}

bool VideoCaptureMac::closeDevice() {
  return avf_close_device(cap);
}

bool VideoCaptureMac::startCapture() {
  return avf_start_capture(cap);
}

bool VideoCaptureMac::stopCapture() {
  return avf_stop_capture(cap);
}

void VideoCaptureMac::update() {
}

void VideoCaptureMac::setFrameCallback(videocapture_frame_cb frameCB, void* user) {
  avf_set_frame_callback(cap, frameCB, user);
}

std::vector<VideoCaptureCapability> VideoCaptureMac::getCapabilities(int device) {
  return avf_get_capabilities(cap, device);
}


