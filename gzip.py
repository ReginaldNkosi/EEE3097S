import os, sys, shutil, gzip, time
# tests the gzip compression method

filename_in = "EEE3097S_2022_Turntable_Example_Data.csv"
filename_out = "EEE3097S_2022_Turntable_Example_Data.csv.gz"

start = time.time()
with open(filename_in, "rb") as fin, gzip.open(filename_out, "wb") as fout:
    # Reads the file by chunks to avoid exhausting memory
    shutil.copyfileobj(fin, fout)

stop = time.time()
time = stop -start

print(f"Uncompressed size: {os.stat(filename_in).st_size}")
print(f"Compressed size: {os.stat(filename_out).st_size}")

print("Exectuion time in seconds: ", time)