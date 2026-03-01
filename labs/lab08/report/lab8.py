import os

def generate_key(text):
    return os.urandom(len(text))

def txt_to_hex(text):
    return ' '.join(f'{c:02X}' for c in text)

def en_de_crypt(text, key):
    return bytes(x ^ y for x,y in zip(text, key))

t1 = 'Привет'
t2 = 'Покааа'

t_byte1 = t1.encode('utf-8')
t_byte2 = t2.encode('utf-8')

k = generate_key(t_byte1)
print(txt_to_hex(k))

en1 = en_de_crypt(t_byte1, k)
en2 = en_de_crypt(t_byte2, k)

de1 = en_de_crypt(en1, k)
de2 = en_de_crypt(en2, k)

print("\ndecrypt1 = ", txt_to_hex(de1),"\ntext1 = ", de1.decode('utf-8'),"\ndecrpyt2 = ", txt_to_hex(de2) ,"\ntext2 = ", de2.decode('utf-8'))


# c1 ^ c2
r = en_de_crypt(en1, en2)
print("\nC1 ^ C2 = ", txt_to_hex(r))

print("Decipher the second text, knowing the first one: ", en_de_crypt(t_byte1, r).decode('utf-8'))
print("Decipher the first text, knowing the second one: ", en_de_crypt(t_byte2, r).decode('utf-8'))
