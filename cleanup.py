import os
import time
import logging
from datetime import datetime, timedelta

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def cleanup_downloads(directory='downloads', days=5):
    """
    清理指定目录中超过指定天数的文件
    """
    now = time.time()
    cutoff = now - (days * 86400)  # 86400 秒 = 1 天

    cleaned_count = 0
    total_count = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            total_count += 1
            file_path = os.path.join(root, file)
            if os.path.getmtime(file_path) < cutoff:
                os.remove(file_path)
                logging.info(f"已删除文件: {file_path}")
                cleaned_count += 1

    logging.info(f"清理完成。共检查 {total_count} 个文件，删除了 {cleaned_count} 个文件。")

if __name__ == "__main__":
    downloads_dir = os.path.join(os.getcwd(), 'downloads')
    cleanup_downloads(downloads_dir)