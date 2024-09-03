from time import sleep
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


plain_text = "CESAR School" # default plain_text


def encrpyt(plain_text: str = plain_text, debug_mode: int = 0) -> dict: # returns the nonce, plain text and tag (integrity checker) 
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_GCM)
    cipher_text, tag = cipher.encrypt_and_digest(plain_text.encode('utf-8'))
   
    result = {
        'cipher_text': b64encode(cipher_text).decode('utf-8'),
        'cipher_nonce': b64encode(cipher.nonce).decode('utf-8'),
        'integrity_tag': b64encode(tag).decode('utf-8'),
        'key': b64encode(key).decode('utf-8')
    }

    if debug_mode:
        print('\n')
        for k, v in result.items():
            print(f"{k}: {v}")

    return result


def decrypt(cipher: dict):
    try:
        key = b64decode(cipher['key'])
        nonce = b64decode(cipher['cipher_nonce'])
        cipher_text = b64decode(cipher['cipher_text'])
        integrity_tag = b64decode(cipher['integrity_tag'])
        
        cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
        plaintext = cipher.decrypt_and_verify(cipher_text, integrity_tag)
        
        print(f"\nThe original message was: {plaintext.decode('utf-8')}")

    except (ValueError, KeyError):
        print("Integrity tag checked incorrect decryption")


if __name__ == "__main__":
    cipher_object = encrpyt(plain_text, 1)
    decrypt(cipher_object)


    while True: # Que falta faz um do while
        path = int(input("\n[0] - Exit Program\n[1] - Change original message and try again\nInput: "))
        
        if path == 1:
            plain_text = input("New message: ")
            cipher_object = encrpyt(plain_text, 1)
            decrypt(cipher_object)
        elif path == 0:
            break
        else:
            for i in range(3):
                print('.', end='', flush=True)
                sleep(1)
            print(" bye")
            break
