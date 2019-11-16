from PIL import Image

# 生成path图像的缩略图
def make_thumb(path, width_h,heigt_h):
    pixbuf = Image.open(path)
    width, height = pixbuf.size

    if width > width_h:
        width = width_h
        height = heigt_h
        pixbuf.thumbnail((width, height), Image.ANTIALIAS)
        return pixbuf

