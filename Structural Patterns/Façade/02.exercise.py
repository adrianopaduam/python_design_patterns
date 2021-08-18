from random import randint


class Generator:
    def generate(self, count):
        return [randint(1, 9) for _ in range(count)]


class Splitter:
    def split(self, array):
        result = []

        row_count = len(array)
        col_count = len(array[0])

        for r in range(row_count):
            the_row = []
            for c in range(col_count):
                the_row.append(array[r][c])
            result.append(the_row)

        for c in range(col_count):
            the_col = []
            for r in range(row_count):
                the_col.append(array[r][c])
            result.append(the_col)

        diag1 = []
        diag2 = []

        for c in range(col_count):
            for r in range(row_count):
                if c == r:
                    diag1.append(array[r][c])
                r2 = row_count - r - 1
                if c == r2:
                    diag2.append(array[r][c])

        result.append(diag1)
        result.append(diag2)

        return result


class Verifier:
    def verify(self, arrays):
        first = sum(arrays[0])

        for i in range(1, len(arrays)):
            if sum(arrays[i]) != first:
                return False

        return True


class MagicSquareGenerator:
    def __init__(self) -> None:
        self.generator = Generator()
        self.splitter = Splitter()
        self.verifier = Verifier()

    def generate(self, size):
        is_valid_square = False
        square = None

        while not is_valid_square:
            square = [self.generator.generate(size) for _ in range(size)]

            splitted_square = self.splitter.split(square)

            is_valid_square = self.verifier.verify(splitted_square)

        return square


if __name__ == '__main__':
    generator = MagicSquareGenerator()

    magic_suare = generator.generate(3)

    print(magic_suare)
