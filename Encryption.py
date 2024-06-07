def rail_fen_enc(msg, k):
    msg = msg.lower()
    d, r = k

    def encry_once(msg, d):
        rail = ['' for _ in range(d)]
        dir_down = False
        row = 0

        for char in msg:
            rail[row] += char
            if row == 0 or row == d - 1:
                dir_down = not dir_down
            row += 1 if dir_down else -1

        return ''.join(rail)

    encrypt_msg = msg
    for _ in range(r):
        encrypt_msg = encry_once(encrypt_msg, d)

    return encrypt_msg


msg = "Hello World"
k = (4, 5) 
encrypt_msg = rail_fen_enc(msg, k)
print("Encrypted msg:", encrypt_msg)