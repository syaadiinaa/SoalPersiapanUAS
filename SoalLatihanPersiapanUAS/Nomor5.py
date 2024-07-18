def get_substring_positions(str1, str2):
    positions = []
    length = min(len(str1), len(str2))
    for i in range(length - 1):
        if str1[i:i+2] == str2[i:i+2]:
            positions.append(i)
    return positions

#penggunaan:
print(get_substring_positions("dobatz", "docatzz"))