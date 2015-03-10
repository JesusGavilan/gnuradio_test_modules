INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_TESTING testing)

FIND_PATH(
    TESTING_INCLUDE_DIRS
    NAMES testing/api.h
    HINTS $ENV{TESTING_DIR}/include
        ${PC_TESTING_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    TESTING_LIBRARIES
    NAMES gnuradio-testing
    HINTS $ENV{TESTING_DIR}/lib
        ${PC_TESTING_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(TESTING DEFAULT_MSG TESTING_LIBRARIES TESTING_INCLUDE_DIRS)
MARK_AS_ADVANCED(TESTING_LIBRARIES TESTING_INCLUDE_DIRS)

