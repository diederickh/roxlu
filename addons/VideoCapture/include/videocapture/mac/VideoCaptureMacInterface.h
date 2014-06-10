/*

 Thin C-wrapper between OBJ-C and C++

 */

#ifndef ROXLU_VIDEOCAPTURE_MAC_C_INTERFACE_H
#define ROXLU_VIDEOCAPTURE_MAC_C_INTERFACE_H

#include <vector>

void* avf_alloc();
void avf_dealloc(void* cap);
int avf_list_devices(void* cap);
int avf_open_device(void* cap, int device, VideoCaptureSettings cfg);
int avf_close_device(void* cap);
int avf_start_capture(void* cap);
int avf_stop_capture(void* cap);
void avf_update(void* cap);
void avf_set_frame_callback(void* cap, videocapture_frame_cb frameCB, void* user);
std::vector<VideoCaptureCapability> avf_get_capabilities(void* cap, int device);

#endif
