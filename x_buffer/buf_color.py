class BufferColor:
    def __init__(self):
        self.buf = []

    def add(self, r, g, b):
        self.buf.append(r)
        self.buf.append(g)
        self.buf.append(b)

    @property
    def data(self):
        return self.buf

    @property
    def size(self):
        return len(self.buf)
