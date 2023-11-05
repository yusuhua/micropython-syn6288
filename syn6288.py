from machine import UART, Pin
import utime as time

SYN6288_TYPE_GB2312 = const(0x00)
SYN6288_TYPE_GBK = const(0x01)
SYN6288_TYPE_BIG5 = const(0x02)
SYN6288_TYPE_UNICODE = const(0x03)

SYN6288_MODE_COMMON = const(0x00)
SYN6288_MODE_BACKGROUND_1  = const(1 << 3)
SYN6288_MODE_BACKGROUND_2  = const(2 << 3)
SYN6288_MODE_BACKGROUND_3  = const(3 << 3)
SYN6288_MODE_BACKGROUND_4  = const(4 << 3)
SYN6288_MODE_BACKGROUND_5  = const(5 << 3)
SYN6288_MODE_BACKGROUND_6  = const(6 << 3)
SYN6288_MODE_BACKGROUND_7  = const(7 << 3)
SYN6288_MODE_BACKGROUND_8  = const(8 << 3)
SYN6288_MODE_BACKGROUND_9  = const(9 << 3)
SYN6288_MODE_BACKGROUND_10  = const(10 << 3)
SYN6288_MODE_BACKGROUND_11  = const(11 << 3)
SYN6288_MODE_BACKGROUND_12  = const(12 << 3)
SYN6288_MODE_BACKGROUND_13  = const(13 << 3)
SYN6288_MODE_BACKGROUND_14  = const(14 << 3)
SYN6288_MODE_BACKGROUND_15  = const(15 << 3)

SYN6288_SOUND_A = 'a'
SYN6288_SOUND_B = 'b'
SYN6288_SOUND_C = 'c'
SYN6288_SOUND_D = 'd'
SYN6288_SOUND_E = 'e'
SYN6288_SOUND_F = 'f'
SYN6288_SOUND_G = 'g'
SYN6288_SOUND_H = 'h'
SYN6288_SOUND_I = 'i'
SYN6288_SOUND_J = 'j'
SYN6288_SOUND_K = 'k'
SYN6288_SOUND_L = 'l'
SYN6288_SOUND_M = 'm'
SYN6288_SOUND_N = 'n'
SYN6288_SOUND_O = 'o'
SYN6288_SOUND_P = 'p'
SYN6288_SOUND_Q = 'q'
SYN6288_SOUND_R = 'r'
SYN6288_SOUND_S = 's'
SYN6288_SOUND_T = 't'
SYN6288_SOUND_U = 'u'
SYN6288_SOUND_V = 'v'
SYN6288_SOUND_W = 'w'
SYN6288_SOUND_X = 'x'
SYN6288_SOUND_Y = 'y'

SYN6288_MESSAGE_A = 'a'
SYN6288_MESSAGE_B = 'b'
SYN6288_MESSAGE_C = 'c'
SYN6288_MESSAGE_D = 'd'
SYN6288_MESSAGE_E = 'e'
SYN6288_MESSAGE_F = 'f'
SYN6288_MESSAGE_G = 'g'
SYN6288_MESSAGE_H = 'h'

SYN6288_RING_A = 'a'
SYN6288_RING_B = 'b'
SYN6288_RING_C = 'c'
SYN6288_RING_D = 'd'
SYN6288_RING_E = 'e'
SYN6288_RING_F = 'f'
SYN6288_RING_G = 'g'
SYN6288_RING_H = 'h'
SYN6288_RING_I = 'i'
SYN6288_RING_J = 'j'
SYN6288_RING_K = 'k'
SYN6288_RING_L = 'l'
SYN6288_RING_M = 'm'
SYN6288_RING_N = 'n'
SYN6288_RING_O = 'o'

class Syn6288(object):
    def __init__(self, uart:UART, busy=None):
        'Note: the baudrate can only be 9600, 19200, or 38400'
        if uart is None:
            raise RuntimeError("uart cannot be None")
        self.uart = uart
        self.busy = Pin(busy, Pin.IN, Pin.PULL_UP) if isinstance(busy, int) else busy

    def send_synthesis(self, data, encoding=SYN6288_TYPE_GB2312, mode=SYN6288_MODE_COMMON):
        eec = 0
        buf = [0xFD, 0x00, 0, 0x01, mode]
        buf[2] = len(data) + 3
        buf[4] += encoding
        buf += list(bytearray(data, "utf-8"))
        for i in range(len(buf)):
            eec ^= int(buf[i])
        buf.append(eec)
        self.uart.write(bytearray(buf))
        
    def send_sound(self, sound=SYN6288_SOUND_A, v=10):
        self.send_synthesis("[v%s][x1]sound%s" % (v, sound))
        
    def send_message(self, message=SYN6288_MESSAGE_A, v=10):
        self.send_synthesis("[v%s][x1]msg%s" % (v, message))
        
    def send_ring(self, ring=SYN6288_RING_A, v=10):
        self.send_synthesis("[v%s][x1]ring%s" % (v, ring))
        
    def sync(self):
        if self.busy is None:
            return
        while (self.busy.value() != 1):
            time.sleep_ms(5)
        while (self.busy.value() != 0):
            time.sleep_ms(5)
