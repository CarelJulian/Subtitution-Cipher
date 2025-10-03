#Substitution Cipher

def encrypt(plaintext, key): # Fungsi untuk enkripsi plaintext menggunakan substitution cipher
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # alfabet standar
    mapping_encrypt = dict(zip(alphabet, key))  
    
    ciphertext = ""
    for char in plaintext.upper():  
        if char in mapping_encrypt:
            ciphertext += mapping_encrypt[char]  # substitusi huruf
        else:
            ciphertext += char  
    return ciphertext


def decrypt(ciphertext, key): # Fungsi untuk dekripsi ciphertext menggunakan substitution cipher
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # alfabet standar
    mapping_decrypt = dict(zip(key, alphabet))  
    
    plaintext = ""
    for char in ciphertext.upper():
        if char in mapping_decrypt:
            plaintext += mapping_decrypt[char]  # substitusi balik
        else:
            plaintext += char  
    return plaintext

# Bagian uji coba program

if __name__ == "__main__":
    key = "QWERTYUIOPASDFGHJKLZXCVBNM" # contoh kunci acak (pastikan 26 huruf, tanpa duplikasi)
    # Contoh 1
    print(" Contoh 1 ")
    plaintext1 = "HALO"
    cipher1 = encrypt(plaintext1, key)
    print("Plaintext :", plaintext1)
    print("Ciphertext:", cipher1)
    print("Dekripsi  :", decrypt(cipher1, key))

    # Contoh 2
    print("\n Contoh 2 ")
    plaintext2 = "SUBTITUTION CIPHER"
    cipher2 = encrypt(plaintext2, key)
    print("Plaintext :", plaintext2)
    print("Ciphertext:", cipher2)
    print("Dekripsi  :", decrypt(cipher2, key))

    # Contoh 3
    print("\n Contoh 3 ")
    plaintext3 = "KRIPTOGRAFI"
    cipher3 = encrypt(plaintext3, key)
    print("Plaintext :", plaintext3)
    print("Ciphertext:", cipher3)
    print("Dekripsi  :", decrypt(cipher3, key))
