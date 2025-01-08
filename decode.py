def main():
    print("Do you want to turn binary into text or text into binary? (decode/convert)\n")
    choice = input().lower()

    if choice == "decode":
        decoder()
    elif choice == "convert":
        string_to_binary()
        
# is very messy, I'll clean up later :333
def convert()):
    str = input("Put the text you want to turn to binary!\n")
    binary = ''.join(format(ord(i), '08b') for i in str)
    print(binary)
    
def decoder():
    binary = input("Put the Binary code here\n")
    binlist = binary.split(" ")

    chrlist = []
    for i in binlist:
        chrlist.append(chr(int(i,2)))
    print("".join(chrlist))
main()
