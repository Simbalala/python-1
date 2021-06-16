import struct


def ushort_uint(buf):
    return struct.unpack_from('>HL', buf)


def buf2latin(buf):
    lbuf = len(buf)
    l = struct.unpack_from('>H', buf)[0]
    d = bytearray(buf)
    j = 0
    s = ''
    for i in range(lbuf):
        c = chr(d[i])
        if c.isalpha():
            if j < l:
                s += c
                j += 1
            else:
                break
    return (l, s)


def ascii2buf(*args):
    buf = b''
    l = len(args)
    buf += struct.pack(b'bbbbb', 0, 0, 0, l, 0)
    for key, value in enumerate(args):
        fmt = 'b' + str(len(value)) + 's'
        buf += struct.pack(fmt, len(value), value.encode('ascii'))
        if key != l - 1:
            buf += struct.pack('b', 0)
    return buf
