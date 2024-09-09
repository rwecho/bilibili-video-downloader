# 下载 Bilibili 视频

这是一个使用 you-get 库下载Bilibili视频的Python项目。

## 功能

- 下载单个Bilibili视频
- 支持输入视频URL或BV号
- 可选择下载视频质量

## 使用前提

- 确保已安装 Python 3.6 或更高版本
- 安装 FFmpeg（you-get 依赖它来处理视频）

## 使用方法

1. 安装依赖:
   ```
   pip install -r requirements.txt
   ```

2. 运行脚本:
   ```
   python bilibili_downloader.py
   ```

3. 按照提示输入视频URL或BV号

4. 选择下载质量

5. 等待下载完成

## 注意事项

- 请确保您有权下载和使用相关视频内容
- 下载速度可能受到网络条件的影响
- 部分视频可能因版权限制无法下载
- 下载的文件将保存在脚本所在目录的 'downloads' 文件夹中

