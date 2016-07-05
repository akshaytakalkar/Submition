import sys
inp = open(sys.argv[1], "rb")
out = open("utf8encoder_out.txt", "w")


def main():
    try:
        byte = inp.read(2)
        while byte:
            val = get_value(byte)
            byte = inp.read(2)
            binary_str = str('{0:08b}'.format(val))
            if val < 128:
                result = '0' + binary_str
                out.write(chr(int(result, 2)))

            elif val < 2048:
                length = len(binary_str)
                if length > 6:
                    right = binary_str[-6:]
                    right = '10'+right
                    left = binary_str[:length-6]
                    dif = 5 - len(left)
                    for k in range(dif):
                        left = '0'+left
                    left = '110'+left
                    out.write(chr(int(left, 2))+chr(int(right, 2)))

            else:
                length = len(binary_str)
                if length > 11:
                    right = binary_str[-6:]
                    mid = binary_str[-12:-6]
                    left = binary_str[:-12]
                    right = '10' + right
                    mid = '10' + mid
                    diff = 4 - len(left)
                    for k in range(diff):
                        left = '0'+left
                    left = '1110' + left
                    out.write(chr(int(left, 2))+chr(int(mid, 2))+chr(int(right, 2)))

    finally:
        inp.close()
        out.close()


def get_value(b):
    return int("".join(map(lambda x: '%02x' % ord(x), b)), 16)

main()
