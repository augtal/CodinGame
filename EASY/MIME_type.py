import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

input1 = ["png image/png", "TIFF image/TIFF", "css text/css", "TXT text/plain"]


input2 = [
    "example.TXT",
    "referecnce.txt",
    "strangename.tiff",
    "resolv.CSS",
    "matrix.TiFF",
    "lanDsCape.Png",
    "extract.cSs"
]

n = len(input1)  # Number of elements which make up the association table.
q = len(input2)  # Number Q of file names to be analyzed.


diction = {}

for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input1[i].split(" ")
    diction[ext.lower()] = mt

for i in range(q):
    fname = input2[i].split(".")  # One file name per line.

    if len(fname) > 1:
        if fname[len(fname) - 1].lower() in diction:
            print(diction[fname[len(fname) - 1].lower()])
        else:
            print("UNKNOWN")
    else:
        print("UNKNOWN")

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


# For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.
