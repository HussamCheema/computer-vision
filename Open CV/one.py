# Image read and write
import cv2

def read_show_image():
    # 2nd argument:
    # 1->color (cv2.IMREAD_COLOR)
    # 0->grey (cv2.IMREAD_GRAYSCALE)
    # -1->colored with alpha channel (IMREAD_UNCHANGED)
    img = cv2.imread("Resources/lena.png", 0)
    cv2.imshow("Image", img)

    # 0-> if you don't want window to be closed ever
    _ = cv2.waitKey(5000) # Show image for 5 seconds
    cv2.destroyAllWindows()
    return img

def write_image(img):
    cv2.imwrite("Resources/lena_new.jpg", img)

if __name__ == "__main__":
    img = read_show_image()
    write_image(img)