from PIL import Image

img = Image.open('C:\\Users\\CYH10\\Desktop\\wallhaven-we13kp_2880x1800.png')
m = min(img.size)
img = img.crop((0, 0, m, m))

m //= 3
for r in range(0, 3):
    for c in range(0, 3):
        t = img.crop((c * m, r * m, (c + 1) * m, (r + 1) * m))
        t.save(f'C:\\Users\\CYH10\\Desktop\\wallhaven-we13kp_{3 * r + c}.png')