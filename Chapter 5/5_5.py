#Jerry Huang
#Period 4

def main():
    name = input("Enter your first name: ")
    name_length = len(name)
    random = 0
    final = 0
    for i in range(name_length):
        letter = name[random]
        A, a = 1, 1
        B, b = 2, 2
        C, c = 3, 3
        D, d = 4, 4
        E, e = 5, 5
        F, f = 6, 6
        G, g = 7, 7
        H, h = 8, 8
        I, i = 9, 9
        J, j = 10, 10
        K, k = 11, 11
        L, l = 12, 12
        M, m = 13, 13
        N, n = 14, 14
        O, o = 15, 15
        P, p = 16, 16
        Q, q = 17, 17
        R, r = 18, 18
        S, s = 19, 19
        T, t = 20, 20
        U, u = 21, 21
        V, v = 22, 22
        W, w = 23, 23
        X, x = 24, 24
        Y, y = 25, 25
        Z, z = 26, 26
        final = final + eval(letter)
        random = random + 1
    print(final)

main()
        
