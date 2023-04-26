import argparse

LEN_ENGLISH_ALPHABET = 26

def encrypt(args):
    crypto(args.text, args.key,-LEN_ENGLISH_ALPHABET)

def decrypt(args):
    crypto(args.text,-args.key,LEN_ENGLISH_ALPHABET)

def crypto(text,key,alphabet_len):
    result = ""
    for c in text:
        if (c.isspace()):
            result += c
            continue
        next_c = ord(c) + key
        if(next_c not in range(ord('a'),ord('z')+1) and next_c not in range(ord('A'),ord('Z')+1)):
            next_c += alphabet_len
        result += chr(next_c)
    print(result)



def main():
    parser = argparse.ArgumentParser(prog='ccipher',description='Encrypt / Decrypt TEXT using the Ceasar Cipher')
    subparsers = parser.add_subparsers(required=True)
    parser.add_argument('text',metavar='TEXT')

    # create the parser for the "encrypt" command
    parser_encrypt = subparsers.add_parser('encrypt', help='encrypt TEXT')
    parser_encrypt.add_argument('-k','--key', default=3, help='bar help')
    parser_encrypt.set_defaults(func=encrypt)

    # create the parser for the "decrypt" command
    parser_decrypt = subparsers.add_parser('decrypt', help='decrypt TEXT')
    parser_decrypt.add_argument('-k','--key', default=3, help='bar help')
    parser_decrypt.set_defaults(func=decrypt)

    args = parser.parse_args()
    args.func(args)
    
    # print(args, subparsers)


if (__name__ == "__main__"):
    main()



