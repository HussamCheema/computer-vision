from PIL import Image
import os

def read_image():
    pil_im = Image.open("empire_state.jpg")
    return pil_im

def show_image(img):
    img.show()

def convert_to_gray(img):
    return img.convert("L")

def change_format(img, path, file_name):
    try:
        out_path = os.path.join(path, file_name)
        print(out_path)
        img.save(out_path)
    except IOError:
        print("cannot convert", img)

def create_thumbnail(img, w=128, h=128):
    img.thumbnail((w,h))
    change_format(img, ".", "thumbnail.png")

def copy_paste_region(img, box):
    # left, upper, right, lower
    region = img.crop(box)
    region = region.transpose(Image.ROTATE_180)
    img.paste(region,box)
    change_format(img, ".", "pasted.png")

def resize(img, w, h):
    out = img.resize((w,h))
    change_format(out, ".", "resized.png")

def rotate(img, angle):
    out = img.rotate(angle)
    change_format(out, ".", "rotated.png")

if __name__ == "__main__":
    img = read_image()
    g_img = convert_to_gray(img)
    # show_image(img)
    # change_format(img, ".", "new.png")
    # create_thumbnail(img, 128, 128)
    # copy_paste_region(img, (100, 100, 400, 400))
    # resize(img, 200, 200)
    rotate(img, 45)