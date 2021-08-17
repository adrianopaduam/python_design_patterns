class FileWithLogging:
    def __init__(self, file):
        self.file = file

    def writelines(self, strings):
        self.file.writelines(strings)
        print(f'wrote {len(strings)} lines')

    def __getattr__(self, item: str):
        return getattr(self.__dict__['file'], item)

    def __setattr__(self, key, value):
        if key == 'file':
            self.__dict__[key] = value
        else:
            setattr(self.__dict__['file'], key)

    def __delattr__(self, name):
        delattr(self.__dict__['file'], name)

    # def __enter__(self):
    #     return self.file.__enter__()

    # def __exit__(self, *args, **kwargs):
    #     return self.file.__exit__(*args, **kwargs)

    def __iter__(self):
        return self.file.__iter__()

    def __next__(self):
        return self.file.__next__()


if __name__ == '__main__':
    file = FileWithLogging(open('assets/hello.txt', 'w'))
    file.writelines(['hello', 'world'])
    file.write('testing')
    file.close()

    # In conextmanaging scope print doesn`t work
    # with FileWithLogging(open('assets/hello.txt', 'w')) as file:
    #     file.writelines(['hello', 'world'])
    #     file.write('testing')
