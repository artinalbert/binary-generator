def binary_to_octal(binary: str):
    octal = ''
    while len(binary) != 0:
        print(f'binary: {binary}')
        if len(binary) >= 3:
            octal = str(int(binary[-3])*4 + int(binary[-2])*2 + int(binary[-1]) * 1) + octal
        elif len(binary) >= 2:
            octal = str(int(binary[-2]) * 2 + int(binary[-1]) * 1) + octal
        else:
            octal = str(int(binary[-1]) * 1) + octal
        binary = binary[:-3]
    return octal
