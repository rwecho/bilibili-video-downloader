# 下载 Bilibili 视频

这是一个使用 you-get 库下载 Bilibili 视频的 Python 项目。

[![Switch to English](https://img.shields.io/badge/lang-english-red.svg)](readme.md)


## 功能

- 下载单个 Bilibili 视频
- 支持输入视频 URL 或 BV 号
- 可选择下载视频质量
- 上传 `cookie.txt` 文件以下载高质量视频
- 清理下载目录中过期文件

## 使用前提

- 确保已安装 Python 3.6 或更高版本
- 安装 FFmpeg（you-get 依赖它来处理视频）

## 使用方法

1. 安装依赖:
   ```sh
   pip install -r requirements.txt
   ```
   注意该项目使用了 ffmpeg，因此需要安装 ffmpeg。

2. 运行 Streamlit 应用:
   ```sh
   streamlit run app.py
   ```

3. 按照提示输入视频 URL 或 BV 号

4. 选择下载质量

5. 等待下载完成

6. 可选：上传 `cookie.txt` 文件以下载高质量视频

## 注意事项

- 请确保您有权下载和使用相关视频内容
- 下载速度可能受到网络条件的影响
- 部分视频可能因版权限制无法下载
- 下载的文件将保存在脚本所在目录的 [downloads](./downloads/) 文件夹中
- 使用 [cleanup.py](./cleanup.py) 脚本清理下载目录中过期文件:
  ```sh
  python cleanup.py
  ```

## 开发容器

项目包含一个开发容器配置，使用 Visual Studio Code 和 Dev Containers 插件可以快速启动开发环境。

1. 打开项目文件夹
2. 按照提示使用 Dev Containers 启动开发环境

## 许可证

© 2024 Bilibili 视频下载器. 保留所有权利。