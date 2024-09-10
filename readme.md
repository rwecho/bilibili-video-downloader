# Bilibili Video Downloader

This is a Python project for downloading Bilibili videos using the you-get library.

[![Switch to Chinese](https://img.shields.io/badge/lang-中文-red.svg)](readme-zh.md)


## Features

- Download individual Bilibili videos
- Support input of video URL or BV number
- Option to select video quality
- Upload `cookie.txt` file to download high-quality videos
- Clean up expired files in the download directory

## Prerequisites

- Ensure Python 3.6 or higher is installed
- Install FFmpeg (you-get depends on it to process videos)

## Usage

1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

Note that this project uses ffmpeg, so you need to install ffmpeg.

2. Run the Streamlit app:

   ```
   streamlit run app.py
   ```

3. Follow the prompts to enter the video URL or BV number

4. Select the download quality

5. Wait for the download to complete

6. Optional: Upload cookie.txt file to download high-quality videos

## Notes

- Ensure you have the right to download and use the related video content
-  Download speed may be affected by network conditions
- Some videos may not be downloadable due to copyright restrictions
- Downloaded files will be saved in the downloads folder in the script directory
- Use the cleanup.py script to clean up expired files in the download directory:
   ```sh
   python cleanup.py
   ```

## Development Container

The project includes a development container configuration, which allows you to quickly start the development environment using Visual Studio Code and the Dev Containers extension.

1. Open the project folder
2. Follow the prompts to start the development environment using Dev Containers

## License

© 2024 Bilibili Video Downloader. All rights reserved.
