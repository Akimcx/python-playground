import argparse

def encrypt(args):
    for k,v in args:
        print(f"${k} => {v}")

def decrypt(args):
    print(args)

def main():
    parser = argparse.ArgumentParser(prog='ccipher',description='Encrypt / Decrypt TEXT')
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
    exit(0)

    print(sys.argv)
    args_count = len(sys.argv)
    if(args_count < 2):
        usage()
        exit(0)
    
    commands = sys.argv[1]
    text = sys.argv[2]

    if(commands == "encrypt"):
        print( encrypt(text) )
    elif(commands == "decrypt"):
        print( decrypt(text) )
    else:
        print(f"ERR: Unknown sub_commands `{commands}`")
        usage()
        exit(1)



