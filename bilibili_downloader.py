import os
import subprocess

def download_video(url, cookies_path=None):
    output_dir = os.path.join(os.getcwd(), 'downloads')
    os.makedirs(output_dir, exist_ok=True)
    
    cmd = ['you-get', '-o', output_dir]
    if cookies_path and os.path.exists(cookies_path):
        cmd.extend(['--cookies', cookies_path])
    cmd.append(url)
    
    subprocess.run(cmd)

def main():
    url = input("请输入Bilibili视频URL或BV号: ")
    if not url.startswith('http'):
        url = f'https://www.bilibili.com/video/{url}'
    
    cookies_path = input("请输入cookies文件路径（如果没有，直接按回车）: ").strip()
    
    print("开始下载视频...")
    download_video(url, cookies_path)
    
    print("下载完成！")

if __name__ == "__main__":
    main()