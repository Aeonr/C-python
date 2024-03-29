import pyautogui

# 移动鼠标到指定位置
pyautogui.moveTo(x, y, duration=seconds)

# 鼠标左键点击
pyautogui.click(x, y, button='left')

# 鼠标右键点击
pyautogui.click(x, y, button='right')

# 鼠标双击
pyautogui.doubleClick(x, y, button='left')

# 鼠标拖拽
pyautogui.dragTo(x, y, duration=seconds, button='left')

# 鼠标释放
pyautogui.mouseUp(x, y, button='left')

# 输入文本
pyautogui.typewrite('Hello, world!')

# 按下一个键
pyautogui.press('enter')

# 按住并快速释放一个键
pyautogui.keyDown('shift')
pyautogui.keyUp('shift')


# 滑动到页面最底部
pyautogui.scroll(1000)

# 等待一段时间，让页面加载完成
time.sleep(5)

# 滑动到页面最底部
pyautogui.scroll(1000)