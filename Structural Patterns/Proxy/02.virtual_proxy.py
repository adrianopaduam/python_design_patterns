class Bitmap:
    def __init__(self, file_name) -> None:
        self.file_name = file_name
        print(f'Loading image from {self.file_name}')

    def draw(self):
        print(f'Drawing image {self.file_name}')


class LazyBitmapProxy:
    def __init__(self, file_name) -> None:
        self.file_name = file_name
        self._bitmap = None

    def draw(self):
        if not self._bitmap:
            self._bitmap = Bitmap(self.file_name)

        self._bitmap.draw()


def draw_image(image):
    print('About to draw image')
    image.draw()
    print('Done drawing image')


if __name__ == '__main__':
    bmp = Bitmap('image.jpg')
    draw_image(bmp)

    print('----')

    bmp = LazyBitmapProxy('image.jpg')
    draw_image(bmp)
    draw_image(bmp)
