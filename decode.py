binary = input("Put the Binary code here\n")
binlist = binary.split(" ")

chrlist = []
for i in binlist:
    chrlist.append(chr(int(i,2)))
print("".join(chrlist))
