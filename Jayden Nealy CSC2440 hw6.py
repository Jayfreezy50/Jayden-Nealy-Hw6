def input_string():
    S1 = input("Enter the first string (S1): ")
    S2 = input("Enter the second string (S2): ")
    return S1, S2


def uncommonConcat(S1, S2):
    set1 = set(S1)
    set2 = set(S2)
    common_chars = set1.intersection(set2)
    S1 = ''.join([char for char in S1 if char not in common_chars])
    S2 = ''.join([char for char in S2 if char not in common_chars])
    result = S1 + S2
    return result

if __name__ == "__main__":
    S1, S2 = input_string()
    output = uncommonConcat(S1, S2)
    print("Output:", output)