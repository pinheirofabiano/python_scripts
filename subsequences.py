sequence = input("Digit the peptide sequence: ")

peptides_80 = []
for i in range(0, len(sequence)-80):
    peptides_80 += [''.join(sequence[i:i+80])]
ofile = open("subsequences.txt", "w")
for i in range(len(peptides_80)):
    ofile.write(">" + "subsequence" + str(i) + "\n" + peptides_80[i] + "\n")
ofile.close()


