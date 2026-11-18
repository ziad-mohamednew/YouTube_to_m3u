import curl_cffi.requests as requests

url = "https://kick.com"
try:
    response = requests.get(url, impersonate="chrome")
    data = response.json()
    playback_url = data.get("playback_url")
    if playback_url:
        m3u_content = f"#EXTM3U\n#EXTINF:-1,Ziad Mohamed TV\n{playback_url}\n"
    else:
        m3u_content = "#EXTM3U\n#EXTINF:-1,Ziad Mohamed TV (Offline)\nhttps://githubusercontent.com\n"
except Exception:
    m3u_content = "#EXTM3U\n#EXTINF:-1,Ziad Mohamed TV (Error)\nhttps://githubusercontent.com\n"

with open("kick.m3u", "w", encoding="utf-8") as f:
    f.write(m3u_content)
