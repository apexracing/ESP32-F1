## 项目简介

### 硬件设备
![这是图片](https://www.waveshare.net/photo/development-board/ESP32-S3-Touch-LCD-1.28-B/ESP32-S3-Touch-LCD-1.28-B-1.jpg)
>开发板详细资料 [ESP32-S3-Touch-LCD-1.28](https://www.waveshare.net/wiki/ESP32-S3-Touch-LCD-1.28)
### 固件编译
>- 目录[fireware](./fireware)下已经存放编译好的固件，用[flash_download_tool_3.9.5](https://www.espressif.com/sites/default/files/tools/flash_download_tool_3.9.5.zip)烧录固件
>- 固件编译步骤可查看[README.md](./fireware/README.md)
### 运行项目
>- 下载软件[Thonny](https://objects.githubusercontent.com/github-production-release-asset-2e65be/163728962/ac488763-b0bb-4412-9dec-757bde673849?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=releaseassetproduction%2F20240531%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240531T100214Z&X-Amz-Expires=300&X-Amz-Signature=4bdeef57906a6cdbc2b380348c2df3219d4b4620098a0d72873a712a3b0679ac&X-Amz-SignedHeaders=host&actor_id=69035246&key_id=0&repo_id=163728962&response-content-disposition=attachment%3B%20filename%3Dthonny-4.1.4.exe&response-content-type=application%2Foctet-stream)
>- 上传项目代码[main](./main)里的所有目录及文件到ESP32设备上，运行test.py文件测试
### UI开发
>- SquareLine Studio是比较好用，可惜商业收费，所以使用NXP开发的[GUI Guider](https://www.nxp.com/webapp/sps/download/preDownload.jsp)
>- 用GUI Guider打开[UI项目](./nxp_gui)即可进行UI编辑
### 动画制作
>adobe Illustrator 2024 绘制矢量图后，用 https://app.lottiefiles.com/ 制作关键帧，导出json格式动画