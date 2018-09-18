class BufferSize:
    def __init__(self):
        self.buf = []

    def add(self, size):
        self.buf.append(size)

    @property
    def data(self):
        return self.buf

    @property
    def size(self):
        return len(self.buf)
