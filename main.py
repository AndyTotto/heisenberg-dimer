import numpy as np

def get_bit(input_state, i):
    # 取り出したいbitだけ立てる
    target_bit = input_state & 2 ** i
    # 0 or 1にする
    target_bit = target_bit >> i

    return target_bit

if __name__ == '__main__':
    H = np.zeros((2 ** 2, 2 ** 2))
    for state in range(2 ** 2):
        init_state = state
        print("init_state = " + str(bin(init_state)))

        # Jz計算
        temp_bit = 0
        Jz = 1.0
        for s_i in range(2):
            temp_bit = get_bit(state, s_i)
            Jz = Jz * 0.5 * (2 * temp_bit - 1)

        H[state][state] = H[state][state] + Jz

        # (Ji+Jj- + Ji-Jj+) / 2 の計算
        temp_bit_J1 = get_bit(state, 0)
        temp_bit_J2 = get_bit(state, 1)
        if temp_bit_J1 != temp_bit_J2:
            target_bits = 2**0 + 2**1
            target_element = state ^ target_bits
            #print(target_element)
            H[target_element][state] = 0.5

    print("matrix")
    print(H)
    test_eig, test_v = np.linalg.eig(H)
    print("eigen value")
    print(test_eig)
    print("eigen state")
    print(test_v)
