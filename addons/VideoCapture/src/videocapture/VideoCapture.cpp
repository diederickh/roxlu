#include <videocapture/VideoCapture.h>

// Callback gets called by implementation
// --------------------------------------------------------------------------
void videocapture_process_frame_callback(void* pixels, size_t nbytes, void* user) {
  VideoCapture* c = static_cast<VideoCapture*>(user);
  assert(c->cb_frame);
  c->cb_frame(pixels, nbytes, c->cb_user);
}

// --------------------------------------------------------------------------

VideoCapture::VideoCapture(VideoCaptureImplementation imp) 
  :cb_user(NULL)
  ,cb_frame(NULL)
  ,cap(NULL)
  ,state(VideoCapture::STATE_NONE)
{

  // Create the capture implementation
  switch(imp) {
#if defined(_WIN32)
    case VIDEOCAPTURE_DIRECTSHOW:                 {  cap = new VideoCaptureDirectShow2();     break;     }
    case VIDEOCAPTURE_WINDOWS_MEDIA_FOUNDATION:   {  cap = new VideoCaptureMediaFoundation(); break;     }
#elif defined(__APPLE__)
    case VIDEOCAPTURE_AVFOUNDATION:               {  cap = new VideoCaptureMac();             break;     }
#elif defined(__linux)      
    case VIDEOCAPTURE_V4L2:                       {  cap = new VideoCaptureV4L2();            break;     }
#endif

    default: {
      printf("Unhandled VideoCaptureImplemtation type.\n");
      ::exit(EXIT_FAILURE);
    }
  }

  cap->setFrameCallback(videocapture_process_frame_callback, this);
}

VideoCapture::~VideoCapture() {

  if(cap) {
    cap->stopCapture();
    cap->closeDevice();
    delete cap;
    cap = NULL;
  }

  cb_user = NULL;
  cb_frame = NULL;
  state = VideoCapture::STATE_NONE;
}

bool VideoCapture::openDevice(int device, VideoCaptureSettings cfg,
                              videocapture_frame_callback frameCB,
                              void* user) 
{

  if(state == VideoCapture::STATE_OPENED) {
    printf("Cannot open the device because it's already opened, first close it.\n");
    return false;
  }
  else if(state == VideoCapture::STATE_CAPTURING) {
    printf("Cannot open the device because we're capturing, make sure to call stopCapture() and closeDevice() before openening it again.\n");
    return false;
  }

  settings = cfg;
  cb_frame = frameCB;
  cb_user = user;
  
  if(!cap->openDevice(device, cfg)) {
    printf("Error while trying to open the device.\n");
    return false;
  }

  state = VideoCapture::STATE_OPENED;
  return true;
}


bool VideoCapture::closeDevice() {

  if(!cap) {
    printf("Cannot close; did not allocate the capture implementation.\n");
    return false;
  }
  if(state == VideoCapture::STATE_NONE) {
    printf("Did not open the device yet so we cannot close it.\n");
    return false;
  }

  bool r = cap->closeDevice();
  cap->setState(VIDCAP_STATE_NONE);
  
  state = VideoCapture::STATE_NONE;
  return r;
}
