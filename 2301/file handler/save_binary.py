with open('binary.bin', 'wb') as f:
    # data = b'\xea\xb0\x80'  # 1110_1010_1011_0000_1000_0000
    data = bytes([255, 0, 127])
    f.write(data)