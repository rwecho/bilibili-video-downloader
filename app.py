import streamlit as st
from downloader import download_videos
import os
import base64  # 添加这行导入语句
import logging
import tempfile
from moviepy.editor import VideoFileClip, concatenate_videoclips

# 配置日志
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# 设置页面配置
st.set_page_config(
    page_title="Bilibili 视频下载器",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.example.com/help',
        'Report a bug': "https://www.example.com/bug",
        'About': "# Bilibili 视频下载器\n这是一个简单的 Bilibili 视频下载工具。"
    }
)

# 确保下载目录存在
downloads_dir = os.path.join(os.getcwd(), 'downloads')
os.makedirs(downloads_dir, exist_ok=True)

# 添加自定义 CSS
st.markdown("""
<style>
    .reportview-container {
        background: #f0f2f6
    }
    .main .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    h1 {
        color: #1f77b4;
    }
</style>
""", unsafe_allow_html=True)

# 添加页面头部
st.markdown("""
<div style="background-color:#1f77b4;padding:10px;border-radius:10px">
    <h1 style="color:white;text-align:center;">Bilibili 视频下载器</h1>
    <p style="color:white;text-align:center;">轻松下载您喜爱的 Bilibili 视频</p>
</div>
""", unsafe_allow_html=True)

# 添加 SEO 相关的元标签
st.markdown("""
<!-- SEO Meta Tags -->
<meta name="description" content="Bilibili Video Downloader - 轻松下载您喜爱的 Bilibili 视频 | Easily download your favorite Bilibili videos">
<meta name="keywords" content="Bilibili, 视频下载, 在线工具, video downloader, online tool, 哔哩哔哩, bilibili downloader">
<meta name="author" content="rwecho">
""", unsafe_allow_html=True)

st.title("Bilibili 视频下载器")

cookies_path = ''
urls = st.text_area("请输入Bilibili视频URL或BV号（每行一个）:")

if st.button("下载视频"):
    if urls:
        url_list = [url.strip() for url in urls.split('\n') if url.strip()]
        url_list = [f"https://www.bilibili.com/video/{url}" if not url.startswith('http') else url for url in url_list]
        
        st.info("开始下载视频...")
        
        results = download_videos(url_list, cookies_path)
        
        for i, (file_path, error) in enumerate(results):
            if file_path and not error:
                dir_path = os.path.dirname(file_path)
                base_name = os.path.splitext(os.path.basename(file_path))[0]
                video_parts = sorted([f for f in os.listdir(dir_path) if f.startswith(base_name) and f.endswith('.mp4')])
                
                if len(video_parts) > 1:
                    merged_file_path = os.path.join(dir_path, f"{base_name}_merged.mp4")
                    merge_video_parts([os.path.join(dir_path, part) for part in video_parts], merged_file_path)
                    file_path = merged_file_path
                    st.success(f"视频片段已合并：{os.path.basename(file_path)}")

            if file_path:
                file_name = os.path.basename(file_path)
                short_name = file_name
            else:
                short_name = f"视频{i+1}"

            if error:
                st.error(f"{short_name} 下载失败")
                if st.button(f"查看错误信息 ({short_name})", key=f"error_{i}"):
                    st.error(f"错误详情：\n{error}")
                logging.error(f"下载错误: {error}")
            elif file_path:
                st.success(f"{short_name} 下载完成！")
                # After the download process
                st.subheader("Downloaded Files:")
                for file in os.listdir(downloads_dir):
                    st.text(file)
                if os.path.exists(file_path):
                    with open(file_path, "rb") as file:
                        st.download_button(
                            label=f"下载 {short_name}",
                            data=file,
                            file_name=os.path.basename(file_path),
                            mime="video/mp4",
                            key=f"download_{i}"
                        )
                else:

                    st.error(f"文件不存在: {file_path}")
            else:
                st.warning(f"{short_name} 下载完成，但无法生成下载链接。")
                logging.warning("无法生成下载链接")
    else:
        st.warning("请输入有效的URL或BV号。")

st.markdown("---")

# 添加 cookie.txt 文件上传功能
uploaded_file = st.file_uploader("上传 cookie.txt 文件（可选）", type="txt")
if uploaded_file is not None:
    # 创建一个临时文件来保存上传的 cookie.txt
    with tempfile.NamedTemporaryFile(delete=False, suffix='.txt') as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        cookies_path = tmp_file.name
    st.success("cookie.txt 文件上传成功！")
else:
    cookies_path = 'cookie.txt'  # 默认路径
st.text("注意：上传 cookie.txt 文件可以帮助下载高质量视频。")

# 清理临时文件
if 'cookies_path' in locals() and cookies_path != 'cookie.txt':
    os.unlink(cookies_path)

# 添加页脚
st.markdown("""
<div style="background-color:#1f77b4;padding:10px;border-radius:10px;margin-top:20px">
    <p style="color:white;text-align:center;">© 2024 Bilibili 视频下载器. 保留所有权利。</p>
</div>
""", unsafe_allow_html=True)

def merge_video_parts(video_parts, output_path):
    clips = [VideoFileClip(part) for part in video_parts]
    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile(output_path)
    for clip in clips:
        clip.close()
