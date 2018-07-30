import cv2


def crop_hero_template_img():
    # 221,189,46,72
    # 273,189,46,72
    # 221,269,46,72
    # 221,373,46,72
    x, y, w, h = 169, 189, 46, 72
    d_col, d_row, d_class = 52, 80, 184
    hero_num = [[21, 16], [21, 16], [21, 20]]
    img = cv2.imread('interface.png')
    for c, rows in enumerate(hero_num):
        for row, col in enumerate(rows):
            for _col in range(col):
                _x = x + _col * d_col
                _y = y + row * d_row + c * d_class
                crop_img = img[_y:_y + h, _x:_x + w]
                # crop_img = img[_y + h - 26:_y + h,
                #            int(_x + w / 2 - 13):int(_x + w / 2 + 13)]
                cv2.imshow("cropped", crop_img)
                cv2.waitKey(0)


def main():
    crop_hero_template_img()


if __name__ == '__main__':
    main()
