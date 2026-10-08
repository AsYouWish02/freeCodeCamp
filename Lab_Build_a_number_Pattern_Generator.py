def number_pattern(n):
    result = ""
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    elif n < 1:
        return 'Argument must be an integer greater than 0.'
    for n1 in range(1, n + 1):
        # Tambahkan angka dan spasi ke dalam string
        result += str(n1) + " "
        
    # .strip() digunakan untuk membuang spasi berlebih di paling akhir string
    return result.strip()

number_pattern(4)
