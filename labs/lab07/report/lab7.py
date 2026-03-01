import os


def generate_key(text):
    return os.urandom(len(text))


def text_to_hex(text):
    return ' '.join(f'{c:02X}' for c in text)


def en_de_crypt(text, key):
    return bytes([b ^ k for b,k in zip(text, key)])


def find_possible_key(fragment, cipher):
    key = []
    for i in range(len(cipher) - len(fragment) + 1):
        part = cipher[i:i+len(fragment)]
        key_part = en_de_crypt(part, fragment)
        key.append(key_part)
    return key

t = 'С Новым Годом, друзья!'


t_bytes = t.encode('utf-8')

k = generate_key(t_bytes)
cipher = en_de_crypt(t_bytes, k)
decrypted = en_de_crypt(cipher,k).decode('utf-8')

#case 1

print("original text:", t)
print("key (hex):" ,text_to_hex(k))
print("encrypt: " ,text_to_hex(cipher))
print("decrypt: " ,decrypted)

#case 2

fragment = 'С Новым'.encode('utf-8')
possible_k = find_possible_key(fragment, cipher)

print("\nPossible key fragments (hex):")
for kf in possible_k[:3]:
    print(text_to_hex(kf))


recover_fragment = en_de_crypt(cipher[:len(fragment)], possible_k[0])
print(recover_fragment.decode('utf-8'))



