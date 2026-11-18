import subprocess

url = "https://kick.com"
try:
    result = subprocess.check_output(["yt-dlp", "-g", url], text=True).strip()
    m3u_content = f"#EXTM3U\n#EXTINF:-1,Ziad Mohamed TV\n{result}\n"
except Exception:
    m3u_content = "#EXTM3U\n#EXTINF:-1,Ziad Mohamed TV (Offline)\nhttps://githubusercontent.com\n"

with open("kick.m3u", "w", encoding="utf-8") as f:
    f.write(m3u_content)
