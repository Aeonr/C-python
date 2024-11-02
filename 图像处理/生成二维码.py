import qrcode
from PIL import Image, ImageDraw, ImageFont
import os


def create_qrcode_with_logo_and_text(data, logo_path, output_folder, text=None):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img = img.convert("RGB")

    if logo_path:
        logo = Image.open(logo_path)
        logo_size = img.size[0] // 5
        logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
        img.paste(logo, (img.size[0] // 2 - logo_size // 2, img.size[1] // 2 - logo_size // 2))

    if text:
        draw = ImageDraw.Draw(img)
        font_size = img.size[0] // 20
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except IOError:
            font = ImageFont.load_default()
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
        draw.text(((img.size[0] - text_width) / 2, img.size[1] - text_height - 10), text, fill=(0, 0, 0), font=font)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    # Sanitize the output filename to avoid issues with special characters
    # output_filename = f"qrcode_{data[:10].replace('/', '_')}.png"
    output_filename = f"qrcode_{data.split('=')[1]}.png"
    output_path = os.path.join(output_folder, output_filename)
    img.save(output_path)


if __name__ == '__main__':
    create_qrcode_with_logo_and_text('https://test.hzcxsoft.com/scan?dvcode=2020230619000301', r'C:\Users\Desktop\test.png', r'C:\Users\Desktop\mytest', '设备号XXX')
