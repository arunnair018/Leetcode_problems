i =15752
output = []
alphabet = "abcdefghijklmnopqrstuvwxyz"
alpha_dict = {idx+1:letter for idx, letter in enumerate(alphabet)}
while (i>0):
    modulo = i % 26
    if i % 26 == 0:
        i = i - 26
        modulo = 26
    output.append(alpha_dict[modulo])  
    i = i//26
print(''.join(output[::-1]))
