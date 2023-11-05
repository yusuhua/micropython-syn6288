class Gb2312(object):
    def __init__(self):
        self.f = open('utf2gb2312.bin', 'r', encoding='utf-8')

    def b2i(self, byte):
        'bytes转int'
        r = 0
        for i in range(len(byte)):
            r = (r << 8) + byte[i]
        return r

    def i2b(self, num):
        'int转bytes'
        num = int(num, 16)
        return num.to_bytes(2, 'big')

    def one_char(self, char):
        '将一个字符转化成gb2312'
        utf_byte = char.encode('utf-8')
        r = self.B_S(0, 7296, self.b2i(utf_byte))
        gb2312_byte = self.i2b(r)
        return gb2312_byte

    def encode(self, st):
        '将字符串转化成gb2312'
        r = b''
        for s in st:
            if len(s.encode('utf-8')) <= 1:
                r += s.encode('utf-8')
            else:
                r += self.one_char(s)
        return r

    def B_S(self, low, high, m):
        '二分查找'
        if 0 <= low <= high <= 7296:
            mid = (low + high) // 2
            self.f.seek(mid * 12)
            data = self.f.read(12)
            utf = data[0:6]
            if int(utf, 16) < m:
                return self.B_S(mid + 1, high, m)
            elif int(utf, 16) > m:
                return self.B_S(low, mid - 1, m)
            else:
                return data[7:-1]

    def __del__(self):
        self.f.close()
