

class Indenter:
    """ Building text indentation capability using context manager pattern"""
    def __init__(self):
        print('Initializing...')
        self._level = 0
    def print(self, text):
        print('     ' * (self._level -1) + text)
    def __enter__(self):
        print('Entering...')
        self._level += 1
        return self
    def __exit__(self, exc_type, exc_value, exc_tb):
        print('Exiting...')
        self._level -= 1


if __name__ == '__main__':
    with Indenter() as indent:
        indent.print('hi!')
        with indent:
            indent.print('hello')
            with indent:
                indent.print('bonjour')
        indent.print('hey')
            