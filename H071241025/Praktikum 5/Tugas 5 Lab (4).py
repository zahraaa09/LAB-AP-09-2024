def membuat_substring(s):
    substring = []
    panjang = len(s)
    
    for jumlah_panjang in range(1, panjang + 1):
        for start in range(panjang - jumlah_panjang + 1):
            substring.append(s[start:start + jumlah_panjang])
    
    return substring

input_string = input("Input your string: ")
result = membuat_substring(input_string)
print("=====================")

for substring in result:
    print(substring)