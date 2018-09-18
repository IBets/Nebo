class BufferPosition:
    def __init__(self):
        self.buf = []

    def add(self, vec3):
        self.buf.append(vec3.x)
        self.buf.append(vec3.y)
        self.buf.append(vec3.z)

    @property
    def data(self):
        return self.buf

    @property
    def size(self):
        return len(self.buf)
