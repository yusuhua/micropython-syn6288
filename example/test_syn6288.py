from gb2312 import Gb2312
from machine import UART
from syn6288 import *
import utime as time

gb2312 = Gb2312()
uart1 = UART(1, baudrate=9600, bits=8, parity=None, stop=1, tx=43)
syn6288 = Syn6288(uart=uart1, busy=44)

# syn6288.send_synthesis(gb2312.encode('今天气温23.5℃'))
syn6288.send_synthesis(gb2312.encode("春眠不觉晓，处处闻啼鸟；夜来风雨声，花落知多少。"), mode=SYN6288_MODE_BACKGROUND_1)
# syn6288.sync()
# syn6288.send_synthesis(gb2312.encode('2013-10-23'))
# for s in "abcdefghijklmnopqrstuvwxy":
#     print(s)
#     syn6288.send_sound(s)
#     syn6288.sync()
#     time.sleep(1)
# for s in "abcdefgh":
#     print(s)
#     syn6288.send_message(s)
#     syn6288.sync()
#     time.sleep(1)
# for s in "abcdefghijklmno":
#     print(s)
#     syn6288.send_ring(s)
#     syn6288.sync()
#     time.sleep(1)
# syn6288.send_sound(SYN6288_SOUND_A)