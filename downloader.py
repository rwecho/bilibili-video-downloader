import os
import subprocess
import logging
import json
import shlex

# 配置日志
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class VideoDownloader:
    def __init__(self, output_dir='downloads', cookies_path='cookie.txt'):
        self.output_dir = os.path.join(os.getcwd(), output_dir)
        self.cookies_path = cookies_path
        os.makedirs(self.output_dir, exist_ok=True)
        logging.info(f"初始化下载器，输出目录: {self.output_dir}")

    def _run_command(self, cmd):
        logging.debug(f"执行命令: {' '.join(map(shlex.quote, cmd))}")
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            return result.stdout, None
        except subprocess.CalledProcessError as e:
            logging.error(f"命令执行失败: {e}")
            return None, e.stderr

    def _get_video_info(self, url):
        cmd = ['you-get', '--json', url]
        if os.path.exists(self.cookies_path):
            cmd.extend(['--cookies', self.cookies_path])
        
        stdout, stderr = self._run_command(cmd)
        if stdout:
            try:
                return json.loads(stdout)
            except json.JSONDecodeError as e:
                logging.error(f"JSON 解析失败: {e}")
                return None
        else:
            logging.error(f"获取视频信息失败: {stderr}")
            return None

    def _download_single_video(self, url):
        video_info = self._get_video_info(url)
        if not video_info:
            return None, "无法获取视频信息"

        streams = video_info.get('streams', {})
        if not streams:
            return None, "无可用的视频流"

        best_quality = max(streams.keys(), key=lambda x: int(x.split('x')[0]) if 'x' in x else 0)
        logging.info(f"选择最高分辨率: {best_quality}")

        cmd = ['you-get', '-o', self.output_dir, '--debug', url]
        if os.path.exists(self.cookies_path):
            cmd.extend(['--cookies', self.cookies_path])
        
        stdout, stderr = self._run_command(cmd)
        if stdout:
            title = video_info['title']
            ext = video_info['streams'][best_quality]['container']
            filename = f"{title}.{ext}"
            file_path = os.path.join(self.output_dir, filename)
            logging.info(f"标题: {title}, 扩展名: {ext}")
            logging.info(f"成功下载文件: {file_path}")
            return file_path, None
        else:
            return None, stderr

    def download_videos(self, urls):
        logging.info(f"开始下载 {len(urls)} 个视频")
        results = []
        for url in urls:
            logging.info(f"开始处理: {url}")
            file_path, error = self._download_single_video(url)
            results.append((file_path, error))
        
        logging.info(f"下载完成，共 {len(results)} 个结果")
        return results

def download_videos(urls, cookies_path='cookie.txt'):
    logging.info(f"开始下载视频，共 {len(urls)} 个 URL")
    downloader = VideoDownloader(cookies_path=cookies_path)
    return downloader.download_videos(urls)