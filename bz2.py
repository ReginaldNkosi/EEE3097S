import bz2, os, sys, time
# bz2 data compression method

filename_in = "EEE3097S_2022_Turntable_Example_Data.csv"
filename_out = "EEE3097S_2022_Turntable_Example_Data.csv.bz"

start = time.time()
with open(filename_in, mode="rb") as fin, bz2.open(filename_out, "wb") as fout:
    fout.write(fin.read())
stop = time.time()

time = stop - start
print(f"Uncompressed size: {os.stat(filename_in).st_size}")

print(f"Compressed size: {os.stat(filename_out).st_size}"
print("Time:",time)