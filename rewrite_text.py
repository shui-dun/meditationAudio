import os
import requests
from sha256 import sha256

"""
之前的冥想音频因为是静态内容显得无趣
因此，对于每句冥想内容，通过deepseek获得改写后的冥想文本
"""
def rewrite_text(origin):
    # 看看有没有缓存
    origin_hash = sha256(origin)
    cache_file = os.path.join("rewrite-cache", origin_hash + ".txt")
    if os.path.exists(cache_file):
        with open(cache_file, "r", encoding="utf-8") as f:
            return f.read()
            
    # 如果没有缓存，调用deepseek
    apiKey = os.getenv("DEEPSEEK_API_KEY")
    if not apiKey:
        raise ValueError("未设置 DEEPSEEK_API_KEY 环境变量")
        
    api_url = "https://api.lkeap.cloud.tencent.com/v1/chat/completions"
    prompt = f"润色以下内容，要求字数和原文差不多，含义也要差不多。并注意除了润色之后的文本，不要输出其他任何内容。你需要润色的内容如下：\n{origin}"
    
    try:
        response = requests.post(
            api_url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {apiKey}"
            },
            json={
                "model": "deepseek-v3",
                "messages": [{"role": "user", "content": prompt}],
                "stream": False
            }
        )
        
        response.raise_for_status()
        data = response.json()["choices"][0]["message"]["content"]
        
        # 清理文本
        data = data.replace('\n', ' ').strip()
        data = data.replace('"', '').replace('"', '')
        data = data.replace('**', '')
        
        # 保存到缓存
        os.makedirs("rewrite-cache", exist_ok=True)
        with open(cache_file, "w", encoding="utf-8") as f:
            f.write(data)
            
        print(f"为原始文本 {origin} 生成了新文本: {data}")
            
        return data
        
    except Exception as e:
        print(f"调用 API 出错: {str(e)}")
        return origin  # 出错时返回原文
