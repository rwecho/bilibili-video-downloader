from downloader import download_video

def main():
    url = input("请输入Bilibili视频URL或BV号: ")
    if not url.startswith('http'):
        url = f'https://www.bilibili.com/video/{url}'
    
    print("开始下载视频...")
    download_video(url)
    
    print("下载完成！")

if __name__ == "__main__":
    main()