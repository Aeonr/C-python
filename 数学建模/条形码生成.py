from PIL import Image, ImageDraw, ImageFont
from numpy.random import randint, random


def rndChar():
    s = "abcdefghjkmnpqrstuwxyABCDEFGHJKMNPRSTUWXY23456789"
    return s[randint(0, len(s))]


def rndColor():
    return tuple(randint(64, 256, 3))


w = 50 * 6;
h = 60
a = Image.new('RGB', (w, h), (255, 255, 255))
font = ImageFont.truetype("c:\\Windows\\Fonts\\simsun.ttc", 48)
b = ImageDraw.Draw(a)


def createLines(n):
    for i in range(n):
        begin = (randint(0, w), randint(0, h))
        end = (randint(0, w), randint(0, h))
        b.line([begin, end], fill=rndColor(), width=2)


def createPoints(rate):
    for x in range(w):
        for y in range(h):
            if random(1) <= rate:
                b.point((x, y), fill=rndColor())


def drawStr():
    Str = ' '
    for t in range(6):
        Chr = rndChar();
        Str = Str + Chr
        b.text((50 * t + 10, 5), Chr, font=font, fill=rndColor())
    print(Str)


createLines(6);
createPoints(0.15);
drawStr()
a.show();
a.save("figure20_15.png")
