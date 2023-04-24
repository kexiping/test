import requests
import random

# 要访问的目标页面
targetUrl = "https://hotels.ctrip.com/hotels/detail/?hotelId=373052&checkIn"

# 要访问的目标HTTPS页面
# targetUrl = "https://hotels.ctrip.com/hotels/detail/?hotelId=373052&checkIn"

# 代理服务器(产品官网 www.16yun.cn)
proxyHost = "t.16yun.cn"
proxyPort = "31111"

# 代理验证信息
proxyUser = "username"
proxyPass = "password"

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host" : proxyHost,
    "port" : proxyPort,
    "user" : proxyUser,
    "pass" : proxyPass,
}

# 设置 http和https访问都是用HTTP代理
proxies = {
        "http"  : proxyMeta,
        "https" : proxyMeta,
    }


#  设置IP切换头
tunnel = random.randint(1,10000)
headers = {"Proxy-Tunnel": str(tunnel)}



resp = requests.get(targetUrl, proxies=proxies, headers=headers)

print resp.status_code
print resp.text