#ifndef ROLXU_LOG_H
#define ROXLU_LOG_H

extern "C" {
#  include <uv.h> 
}

#include <utils/Utils.h>
#include <iostream>
#include <string>
#include <fstream>
#include <vector>

#if defined(_WIN32) 
#  include <stdarg.h>
#endif

#if defined(__linux) 
#  include <stdarg.h>
#  include <stdio.h>
#endif

#define RX_LOG_NO_COLOR

#define RX_LOG_LEVEL_NONE 0 
#define RX_LOG_LEVEL_ERROR  1
#define RX_LOG_LEVEL_WARNING 2
#define RX_LOG_LEVEL_VERBOSE 3
#define RX_LOG_LEVEL_ALL 4

#if defined(_WIN32)
#  define ANSI_VERBOSE   "\x1b[32;1m"
#  define ANSI_WARNING   "\x1b[35;1m"
#  define ANSI_ERROR     "\x1b[31;1m"
#else 
#  define ANSI_VERBOSE   "\x1b[32m"
#  define ANSI_WARNING   "\x1b[35m"
#  define ANSI_ERROR     "\x1b[31m"
#endif

#if defined(_MSC_VER)
#  define RX_VERBOSE(fmt, ...) { rx_verbose(__LINE__, __FUNCSIG__, fmt, ##__VA_ARGS__); } 
#  define RX_WARNING(fmt, ...) { rx_warning(__LINE__, __FUNCSIG__, fmt, ##__VA_ARGS__); } 
#  define RX_ERROR(fmt, ...)   { rx_error(__LINE__, __FUNCSIG__, fmt, ##__VA_ARGS__); } 
#else                                                                             
#  define RX_VERBOSE(fmt, ...) { rx_verbose(__LINE__, __PRETTY_FUNCTION__, fmt, ##__VA_ARGS__); } 
#  define RX_WARNING(fmt, ...) { rx_warning(__LINE__, __PRETTY_FUNCTION__, fmt, ##__VA_ARGS__); } 
#  define RX_ERROR(fmt, ...)   { rx_error(__LINE__, __PRETTY_FUNCTION__, fmt, ##__VA_ARGS__); } 
#endif

#if !defined(RX_LOG_LEVEL)
#  define RX_LOG_LEVEL RX_LOG_LEVEL_VERBOSE
#endif

// unset log macros based on the -DRX_LOG_LEVEL preprocessor variable
#if RX_LOG_LEVEL == RX_LOG_LEVEL_VERBOSE
#  elif RX_LOG_LEVEL ==  RX_LOG_LEVEL_WARNING
#  undef RX_VERBOSE
#elif RX_LOG_LEVEL == RX_LOG_LEVEL_ERROR
#  undef RX_VERBOSE
#  undef RX_WARNING
#endif

#if RX_LOG_LEVEL == RX_LOG_LEVEL_NONE
#  undef RX_ERROR
#  undef RX_VERBOSE
#  undef RX_WARNING
#endif

// if not set anymore, define empties
#if !defined(RX_VERBOSE)
#  define RX_VERBOSE(fmt, ...) {}
#endif

#if !defined(RX_WARNING)
#  define RX_WARNING(fmt, ...) {}
#endif

#if !defined(RX_ERROR)
#  define RX_ERROR(fmt, ...) {}
#endif

extern "C" {

  typedef void(*roxlu_log_callback)(int level, void* user, int line, const char* function, const char* fmt, va_list args);

  extern roxlu_log_callback roxlu_log_cb;
  extern void* roxlu_log_user;
  extern int roxlu_log_level;

  void rx_log_set_callback(roxlu_log_callback cb, void* user);
  void rx_log_set_level(int level); 
  void rx_log_default_callback(int level, void* user, int line, const char* function, const char* fmt, va_list args); 

  void rx_verbose(int line, const char* function, const char* fmt, ...);
  void rx_warning(int line, const char* function, const char* fmt, ...);
  void rx_error(int line, const char* function, const char* fmt, ...);
} // extern C


struct LogMessage {
  std::string tty_message;
  std::string file_message;
  int level;
};

class Log {
 public:
  Log();
  ~Log();

  bool setup(std::string name, std::string path = "");  /* create a new log with the name `name` in dir `data/[path]/[name].log */
  void addMessage(LogMessage msg);                          /* gets called indirectly by RX_VERBOSE/RX_WARNING/RX_ERROR */

  void mini();                                              /* log minimal info, just the message */
  void maxi();                                              /* log maximum info */

  void logFunctionName(bool flag);                          /* log the function name of the caller */
  void logLineNumber(bool flag);                            /* log the line number of the caller */
  void logTime(bool flag);                                  /* log the timestamp */
  void logLevel(bool flag);                                 /* log [verbose], [warning], [error], etc.. */
                                                         
  void useColors(bool flag);                                /* enable/disable colors in the tty output */
  void writeToFile(bool flag);                              /* enable/disable writing to a log file */
  void writeToConsole(bool flag);                           /* enable/disable writing to the tty console */
                                                         
  void rotateLog();                                          /* when the file is bigger then max_file_size (in bytes), we rename the current file to somethigng like: [logname]-2013_04_03_16_33.log */
                                                         
 private:                                               
  bool createLogFile();                                
                                                         
 public:                                                
  bool write_function_name;                                 /* when true, we add the function name to the log lines */
  bool write_line_number;                                   /* when true, we add the line number where the log function was called */
  bool use_colors;                                          /* colorify the output to tty */
  bool write_to_file;                                       /* log messages to a file */
  bool write_to_console;                                    /* write to tty */
  bool write_time;                                          /* write the current time to a log file */
  bool write_log_level;                                     /* write [verbose], [warning], [error], etc.. */
                                                         
  std::string date_format;                                  /* strftime() date format */
  std::string log_file;                                     /* the path to the current log file */
  std::string log_name;                                     /* the name of this log. e.g. `roxlu` creates `roxlu.log` */
  std::string log_path;                                     /* the path name/dirname where we store the log (in the data path), e.g. `log/` */
  size_t max_file_size;                                     /* maximum filesize of the log; if the file gets bigger we rotate it */
    
  uv_loop_t* loop;
  uv_mutex_t mutex;
  uv_tty_t tty;
  std::ofstream ofs;
};

inline void Log::logFunctionName(bool flag) {
  write_function_name = flag;
}

inline void Log::logLineNumber(bool flag) {
  write_line_number = flag;
}

inline void Log::logTime(bool flag) {
  write_time = flag;
}

inline void Log::logLevel(bool flag) {
  write_log_level = flag;
}

inline void Log::useColors(bool flag) {
  use_colors = flag;
}

inline void Log::writeToConsole(bool flag) {
  write_to_console = flag;
}

inline void Log::writeToFile(bool flag) {
  write_to_file = flag;
}

#endif
