# FFmpeg



全称  fast forward mpeg 用于处理音视频流媒体开源工具库

## 下载和配置软件

进入官网

```
https://ffmpeg.org/download.html
```

进入下载得到编译完成的软件，此时FFMPEG更新到了4.3

```
ffmpeg-4.3-win64-static
```

解压并放入软件专用文件夹即可，并在环境变量中添加如下，以便在任何目录中使用该软件

```shell
ffmpeg-4.3-win64-static/bin
```



安装验证

```shell
$ ffmpeg --version
```

查看是否安装完成；



## 简要开始

### 文档介绍

根目录下有三个文件夹和两个文档，其中LICENSE.txt为版权许可，README.txt为说明

```shell
LICENSE.txt
README.txt
bin/
doc/
presets/
```

bin文件夹中存在三个文件，其中ffmpeg.exe为编码工具，ffplay.exe为简易播放器，ffprobe.exe为视频信息查看工具；

```shell
ffmpeg.exe
ffplay.exe
ffprobe.exe
```

presets文件夹中存放预设

```shell
ffprobe.xsd
libvpx-1080p.ffpreset
libvpx-1080p50_60.ffpreset
libvpx-360p.ffpreset
libvpx-720p.ffpreset
libvpx-720p50_60.ffpreset
```

doc文件夹中为网页形式的详细软件文档，大多数操作细节可参考内容

```shell
bootstrap.min.css
default.css
developer.html
faq.html
fate.html
ffmpeg-all.html
ffmpeg-bitstream-filters.html
ffmpeg-codecs.html
ffmpeg-devices.html
ffmpeg-filters.html
ffmpeg-formats.html
ffmpeg-protocols.html
ffmpeg-resampler.html
ffmpeg-scaler.html
ffmpeg-utils.html
ffmpeg.html
ffplay-all.html
ffplay.html
ffprobe-all.html
ffprobe.html
general.html
git-howto.html
libavcodec.html
libavdevice.html
libavfilter.html
libavformat.html
libavutil.html
libswresample.html
libswscale.html
mailing-list-faq.html
nut.html
platform.html
style.min.css
```

FFMPEG采用LGPL和GPL混合版权许可，其实人可自由使用做软件且必须将其代码开放；

### 命令行帮助

```shell
$ ffmpeg -h
```

### 简易播放

```shell
$ ffplay example.mp4
$ ffplay example.mp3		#播放音频  方向键可进行前进和后退 F全屏  P和SPACE暂停   W 切换显示
```

按下ESC或者Q即可退出；

### 快速查看媒体信息

```SHELL
$ ffprobe MediaExample.mp4
ffprobe version 4.3 Copyright (c) 2007-2020 the FFmpeg developers
  built with gcc 9.3.1 (GCC) 20200621
  configuration: --enable-gpl --enable-version3 --enable-sdl2 --enable-fontconfig --enable-gnutls --enable-iconv --enable-libass --enable-libdav1d --enable-libbluray --enable-libfreetype --enable-libmp3lame --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenjpeg --enable-libopus --enable-libshine --enable-libsnappy --enable-libsoxr --enable-libsrt --enable-libtheora --enable-libtwolame --enable-libvpx --enable-libwavpack --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxml2 --enable-libzimg --enable-lzma --enable-zlib --enable-gmp --enable-libvidstab --enable-libvmaf --enable-libvorbis --enable-libvo-amrwbenc --enable-libmysofa --enable-libspeex --enable-libxvid --enable-libaom --enable-libgsm --disable-w32threads --enable-libmfx --enable-ffnvcodec --enable-cuda-llvm --enable-cuvid --enable-d3d11va --enable-nvenc --enable-nvdec --enable-dxva2 --enable-avisynth --enable-libopenmpt --enable-amf
  libavutil      56. 51.100 / 56. 51.100
  libavcodec     58. 91.100 / 58. 91.100
  libavformat    58. 45.100 / 58. 45.100
  libavdevice    58. 10.100 / 58. 10.100
  libavfilter     7. 85.100 /  7. 85.100
  libswscale      5.  7.100 /  5.  7.100
  libswresample   3.  7.100 /  3.  7.100
  libpostproc    55.  7.100 / 55.  7.100
Input #0, mov,mp4,m4a,3gp,3g2,mj2, from 'MediaExample.mp4':
  Metadata:
    major_brand     : isom
    minor_version   : 512
    compatible_brands: isomiso2avc1mp41
    encoder         : Lavf55.33.100
  Duration: 00:00:30.04, start: 0.000000, bitrate: 4470 kb/s
    Stream #0:0(und): Video: h264 (Main) (avc1 / 0x31637661), yuv420p(tv, bt709), 1920x1088, 4211 kb/s, 30 fps, 30 tbr, 90k tbn, 60 tbc (default)
    Metadata:
      handler_name    : VideoHandler
    Stream #0:1(eng): Audio: aac (LC) (mp4a / 0x6134706D), 44100 Hz, stereo, fltp, 256 kb/s (default)
    Metadata:
      handler_name    : SoundHandler

```

可见视频采用了H264编码格式，avc1封装，采用了yuv420p颜色空间，1920x1088像素，比特率4211kb/s，帧率30

音频采用了acc格式，LC规格，mp4a封装，采用率44100 Hz，立体声，比特率256 kb/s

## 格式转换

### 介绍

视频文件的后缀通常能判断为其封装格式，各类组织和公司都制定了很多标准，用于将视频和音频字幕等都放在一个容器内封装起来；其中有些兼容有些不兼容，不兼容时需要改变编码才能转换，通常我们采用兼容性好的封装方式和编码进行视频的转换方式；

| 视频封装方法                                        | 视频文件格式               |
| --------------------------------------------------- | -------------------------- |
| AVI                                                 | AVI                        |
| WMV                                                 | WMV                        |
| MPEG-1/MPEG-2/MPEG-4 (moving picture experts group) | MPG/MPEG/VOB/DAT/3GP   MP4 |
| Matroska                                            | MKV                        |
| Real Video                                          | RM/RMVB                    |
| Quick Time File Format (Apple Inc.)                 | MOV                        |
| Flash Video                                         | FLV                        |

MKV最为开放但是体积大，AVI较老，MOV为苹果公司制定，MP4为最流行；

### 视频封装转换

```shell
$ ffmpeg.exe -i MediaExample.mp4 MediaExample.mkv
# 这里将MP4封装 转换为 MKV封装
# -i 为 输入缩写
```

## 编码转换

### 音视频编码

#### 介绍

ffmpeg支持很多编码格式，可以查看，基本具有上百种；

```shell
$ ffmpeg -codecs
```

常用视频网站使用的时H264视频编码+AAC音频编码；

当然还有 WebM封装，VP8视频编码+Voribis音频编码 ，谷歌youtube就使用这个方案；仅仅为了避免版权问题；

还有一套完全开源的编码方案：OGG封装 ， Theora视频编码 + Vorbis音频编码 ；无专利问题；

如需要制作超过1080P的2K 4K视频 还需要使用其他编码；

#### 音频转码

```shell
$ ffmpeg -i example.flac -acodec libmp3lame -ar 44100 -ab 320k -ac 2 output.mp3
#这里将flac音频转为mp3    输入example.flac  输出output.mp3
# -i 为 输入缩写
#-acodec    a为audio音频缩写   codec为编码器   指定了 libmp3lame编码 就是mp3  若不输入则自动根据输出文件判断编码
# -ar 44100 a为audio音频缩写  r为采样率  常用 44100Hz或48000Hz
# -ab 320  a为audio音频缩写  b为比特率   指定比特率320kb/s
# -ac 2 c为channel  这里设置声道数   
```









### 视频压制





### 码率控制模式

 





