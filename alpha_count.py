from string import ascii_uppercase

def alpha_count(val):
    alpha_dict_count = {}

    for i in val:
        # print(f"Char int: {ord(i)}")
        capital = i.upper()

        if capital not in ascii_uppercase:
            continue

        if capital not in alpha_dict_count:
            alpha_dict_count[capital] = 1
        else: 
            alpha_dict_count[capital] += 1
        # alpha_count.append(alpha_count)

    return sorted(alpha_dict_count.items(), key=lambda item: item[1], reverse=True)