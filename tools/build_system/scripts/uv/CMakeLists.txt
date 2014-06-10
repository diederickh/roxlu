cmake_minimum_required(VERSION 2.8)

# 2014.02.02 - Created to able to have 32/64, debug/release, vs2012/vs2010 builds
# CMakeListst.txt file which creates a shared library 
# for libuv. This is easily adjusted to create a static library too

set(bd ${CMAKE_CURRENT_LIST_DIR})
set(sd ${bd}/src)
set(id ${bd}/include)

set(libuv_sources
  ${sd}/fs-poll.c
  ${sd}/inet.c
  ${sd}/queue.h
  ${sd}/uv-common.c
  ${sd}/uv-common.h
  ${sd}/version.c
)

# headers that will be installed
set(libuv_headers
  ${id}/uv.h
  ${id}/uv-errno.h
)

# OS libraries to link with
set(libuv_libs "")

# preprocessor defs
set(libuv_defs "") 

set(libuv_inc_dirs ${bd}/include ${bd}/src)

if(WIN32)
  
  list(APPEND libuv_headers
    ${id}/uv-win.h
    ${id}/tree.h
    ${id}/stdint-msvc2008.h
    )

  list(APPEND libuv_defs
    "-DWIN32_LEAN_AND_MEAN"
    "-D_WIN32_WINNT=0x0600"
    "-D_CRT_SECURE_NO_DEPRECATE"
    "-D_CRT_NONSTDC_NO_DEPRECATE"
    "-DWIN32"
    "-DBUILDING_UV_SHARED=1"
    )

  if(CMAKE_BUILD_TYPE STREQUAL "Debug")
    list(APPEND libuv_defs "-DNDEBUG")
  endif()

  list(APPEND libuv_inc_dirs ${sd}/win)

  list(APPEND libuv_libs 
    ws2_32.lib
    psapi.lib
    iphlpapi.lib
    shell32.lib
    )

  list(APPEND libuv_sources
    ${sd}/win/async.c 
    ${sd}/win/atomicops-inl.h 
    ${sd}/win/core.c 
    ${sd}/win/dl.c 
    ${sd}/win/error.c 
    ${sd}/win/fs-event.c 
    ${sd}/win/fs.c 
    ${sd}/win/getaddrinfo.c 
    ${sd}/win/handle.c 
    ${sd}/win/handle-inl.h 
    ${sd}/win/internal.h 
    ${sd}/win/loop-watcher.c 
    ${sd}/win/pipe.c 
    ${sd}/win/poll.c 
    ${sd}/win/process-stdio.c 
    ${sd}/win/process.c 
    ${sd}/win/req.c 
    ${sd}/win/req-inl.h 
    ${sd}/win/signal.c 
    ${sd}/win/stream.c 
    ${sd}/win/stream-inl.h 
    ${sd}/win/tcp.c 
    ${sd}/win/thread.c 
    ${sd}/win/threadpool.c 
    ${sd}/win/timer.c 
    ${sd}/win/tty.c 
    ${sd}/win/udp.c 
    ${sd}/win/util.c 
    ${sd}/win/winapi.c 
    ${sd}/win/winapi.h 
    ${sd}/win/winsock.c 
    ${sd}/win/winsock.h
    )
endif()

if(UNIX)

  list(APPEND libuv_inc_dirs ${bd}/src/unix)

  list(APPEND libuv_sources
    ${sd}/unix/async.c 
    ${sd}/unix/atomic-ops.h 
    ${sd}/unix/core.c 
    ${sd}/unix/dl.c 
    ${sd}/unix/fs.c 
    ${sd}/unix/getaddrinfo.c 
    ${sd}/unix/internal.h 
    ${sd}/unix/loop-watcher.c 
    ${sd}/unix/loop.c 
    ${sd}/unix/pipe.c 
    ${sd}/unix/poll.c 
    ${sd}/unix/process.c 
    ${sd}/unix/signal.c 
    ${sd}/unix/spinlock.h 
    ${sd}/unix/stream.c 
    ${sd}/unix/tcp.c 
    ${sd}/unix/thread.c 
    ${sd}/unix/threadpool.c 
    ${sd}/unix/timer.c 
    ${sd}/unix/tty.c 
    ${sd}/unix/udp.c
    )
endif()

if(APPLE)
  list(APPEND libuv_defs "-D_DARWIN_USE_64_BIT_INODE=1")
  list(APPEND libuv_sources
    ${sd}/unix/darwin.c 
    ${sd}/unix/darwin-proctitle.c 
    ${sd}/unix/fsevents.c 
    ${sd}/unix/kqueue.c 
    ${sd}/unix/proctitle.c
    )
endif()

add_definitions(${libuv_defs})
include_directories(${libuv_inc_dirs})
add_library(libuv SHARED ${libuv_sources})
target_link_libraries(libuv ${libuv_libs})

install(TARGETS libuv ARCHIVE DESTINATION lib)
install(FILES ${libuv_headers} DESTINATION include)
install(TARGETS libuv RUNTIME DESTINATION bin)