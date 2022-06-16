
def file_gen(filename, start, end):
    seq = ""
    with open('insulin_amino','r') as insulin_file:
        with open(filename, 'w') as new_file:
            data = insulin_file.read()
            for char in range(start - 1, end):
                seq += data[char]
            new_file.write(seq)
            new_file.close()
        insulin_file.close()


"creating a file for lsinsulin-seq-clean.txt 1 .. 24"

file_gen('lsinsulin-seq-clean.txt', 1, 24)
file_gen('binsulin-seq-clean.txt', 25, 54)
file_gen('cinsulin-seq-clean.txt', 55, 89)
file_gen('ainsulin-seq-clean.txt', 90, 110)