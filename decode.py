def main():
    print("Do you want to turn binary into text or text into binary? (decode/convert)")
    choice = input().strip().lower()

    if choice == "decode":
        decoder()
    elif choice == "convert":
        convert()
    else:
        print("not real command, Please choose either 'decode' or 'convert' greg")

def convert():
    text = input("Enter the text you want to convert to binary:\n")
    binary = ' '.join(format(ord(char), '08b') for char in text)
    print("Binary code:")
    print(binary)

def decoder():
    binary = input("Enter the binary code (use space to separate each byte):\n")
    try:
        text = ''.join(chr(int(byte, 2)) for byte in binary.split())
        print("Decoded text:")
        print(text)
    except ValueError:
        print("Make sure to space and make sure that it's valid plz greg")

if __name__ == "__main__":
    main()
