## ESP32-S3-16MB Flash固件编译
### 1.安装编译环境
需要用**VirtualBox**下载安装[ubuntu-22.04.4-desktop-amd64.iso](https://releases.ubuntu.com/22.04/ubuntu-22.04.4-desktop-amd64.iso)
### 2. 安装ESP-IDF
```shell
$ git clone -b v4.4 --recursive https://github.com/espressif/esp-idf.git
cd esp-idf
source export.sh
```
**注意** 如果开启一个新的shell窗口需要执行````source export.sh````
### 3. 编译一个基础的micropython固件

````shell
git clone https://github.com/lvgl/lv_micropython.git -b release/v8
cd lv_micropython
git submodule update --init --recursive lib/lv_bindings
make -C mpy-cross
cd ports/esp32
make submodules
cd -
make -C ports/esp32 LV_CFLAGS="-DLV_COLOR_DEPTH=16 -DLV_COLOR_16_SWAP=1 -DMICROPY_ENABLE_FINALISER=1" BOARD=GENERIC_S3_SPIRAM

````

第三步编译过程不出意外，会出意外，解决方案:
按这个[PullRquest](https://github.com/lvgl/lv_binding_micropython/pull/243/files#diff-a83d385a7a3e9e5931ba0ea4e886753ed2496df54b96f2cbc736832f67ec042d)代码去修改相应文件即可编译通过


### 4.配置ESP_IDF项目
**需要在ubuntu桌面环境中运行shell**
````shell
cd lv_micropython/ports/esp32
idf.py set-target esp32s3
idf.py menuconfig
```` 
**修改以下选项:**

- Serial flasher config--->Flash SPI speed(80 MHz)
- Serial flasher config--->Flash Size(16 Mb)
- Partition Table--->Custom partition table,使用partitions.csv
- Component config--->ESP32-specific--->CPU frequency(240 MHz)
- 修改ports/esp32/partitions.csv文件如下:
    ````
      # Notes: the offset of the partition table itself is set in
        # $IDF_PATH/components/partition_table/Kconfig.projbuild.
        # Name,   Type, SubType, Offset,  Size, Flags
        nvs,      data, nvs,     0x9000,  0x6000,
        phy_init, data, phy,     0xf000,  0x1000,
        factory,  app,  factory,      ,       4M,
        vfs,      data, fat,          ,      10M,
    ````
### 5.将Lottie作为组件添加到ESP_IDF项目
- 下载rlottie
```shell
cd port/esp32
mkdir components
mkdir components/rlottie
cd components/rlottie
git clone https://github.com/Samsung/rlottie.git
```
- 创建如下目录结构
````
components/
└── rlottie
    └── rlottie
        ├── cmake
        ├── CMakeFiles
        ├── example
        ├── inc
        ├── licenses
        ├── packaging
        ├── src
        ├── test
        └── vs2019
````
- 在rlottie组件目录下新建一个CMakeList.txt
````
cmake_minimum_required(VERSION 3.5)

message("注册rlottie组件")
idf_component_register(SRCS ${SOURCES}
                    INCLUDE_DIRS "${CMAKE_CURRENT_LIST_DIR}/rlottie/inc"
                    )

set(LOTTIE_MODULE OFF)
set(LOTTIE_THREAD OFF)
set(BUILD_SHARED_LIBS OFF)
option(BUILD_TESTING OFF)

function(install)
endfunction()

function(export)
endfunction()

add_subdirectory(rlottie)
target_link_libraries(${COMPONENT_LIB} INTERFACE rlottie)
````

- 根据[Rlottie patch file](https://github.com/lvgl/lvgl/blob/master/env_support/esp/rlottie/0001-changes-to-compile-with-esp-idf.patch)修改components/rlottie/rlottie/下相应的几个文件

````
rlottie/CMakeList.txt
rlottie/src/vector/vimageloader.cpp
````
### 6.修改lv_conf.h头文件,支持矢量动画播放
````shell
cd lv_micropython/lib/lv_bindings
vim lv_conf.h
````
```text
/*Rlottie library, if available */
#define MICROPY_RLOTTIE 1 //开启动画功能
#ifdef MICROPY_RLOTTIE
    #define LV_USE_RLOTTIE 1
#else
    #define LV_USE_RLOTTIE 0
#endif
#define e LV_COLOR_SCREEN_TRANSP 1 //开启rolate功能
```
### 7.修改lvgl组件引用
```text
  #修改文件lv_micropython/lib/lv_bindings/lvgl/env_support/cmake/esp.cmake 添加REQUIRES
  idf_component_register(
    SRCS
    ${SOURCES}
    INCLUDE_DIRS
    ${LVGL_ROOT_DIR}
    ${LVGL_ROOT_DIR}/src
    ${LVGL_ROOT_DIR}/../
    REQUIRES
    main rlottie)
```
### 8.修改了lv_rlottie支持从整个文件中控制帧播放范围
[lv_rlottie.c](./lv_rlottie.c),[lv_rlottie.h](./lv_rlottie.h) 这个可以根据个人需求选择是否修改源文件
### 9.编译
```shell
make -C ports/esp32 LV_CFLAGS="-DLV_COLOR_DEPTH=16 -DLV_COLOR_16_SWAP=1 -DMICROPY_ENABLE_FINALISER=1" BOARD=GENERIC_S3_SPIRAM
//下载固件
ports/esp32/build_GENERIC_S3_SPIRAM/fireware.bin
```
