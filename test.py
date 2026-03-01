from twocaptcha import TwoCaptcha

api_key = '8ef4d5850d970790349c9c78831adb21'
solver = TwoCaptcha(api_key)
result = solver.normal('captcha.png')
print(result['code'])
