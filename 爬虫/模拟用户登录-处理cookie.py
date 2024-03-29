#登录-得到cookie
#请求到url
#使用session进行请求
import requests
session=requests.session()
url="https://passport.17k.com/sns/qqCallback.action?fromUrl=https%3A%2F%2Fuser.17k.com%2Fwww%2F&code=873DEB63D5F934480610CEE98F5FBE33"
resp=session.get(url)
resp.encoding='utf-8'
print(resp.text)