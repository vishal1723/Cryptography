def rail_fen_decrypt(ciphertext, k):
    d, r = k

    def decry_once(ciphertext, d):
        rail = [['\n' for _ in range(len(ciphertext))] for _ in range(d)]
        index = 0
        dir_down = None
        row, col = 0, 0

        for char in ciphertext:
            if row == 0:
                dir_down = True
            if row == d - 1:
                dir_down = False
            rail[row][col] = '*'
            col += 1
            row += 1 if dir_down else -1

        for i in range(d):
            for j in range(len(ciphertext)):
                if rail[i][j] == '*' and index < len(ciphertext):
                    rail[i][j] = ciphertext[index]
                    index += 1

        res = []
        row, col = 0, 0
        for char in ciphertext:
            if row == 0:
                dir_down = True
            if row == d - 1:
                dir_down = False
            if rail[row][col] != '*':
                res.append(rail[row][col])
                col += 1
            row += 1 if dir_down else -1

        return ''.join(res)

    decry_msg = ciphertext
    for _ in range(r):
        decry_msg = decry_once(decry_msg, d)

    return decry_msg


encrypted_message = "TAOTINEN KAT I ODIOAEI OHHLSCTE TTETOEL BI IHI GAO   EPSEA TO SS  EEK  ELRCPTSIY EANRPHMCYEK E CREAAIEJURTE  IEASHI MA DRN RH  AUWTA RF EFTFHENTPSF Q   TAILB E TTECAPMSIYIY SRPURNTBL YCL OANAO  E  TVREAOSHOTTNULSRHK"
k = (3, 3) 
decry_msg = rail_fen_decrypt(encrypted_message, k)
print("Decrypted Message:", decry_msg)