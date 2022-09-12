import lzma, os, time
lzc = lzma.LZMACompressor()

filename_in = "EEE3097S_2022_Turntable_Example_Data.csv"
filename_out = "EEE3097S_2022_Turntable_Example_Data.csv.lz"

start = time.time()
with open(filename_in, mode="r") as fin, open(filename_out, "wb") as fout:
    for chunk in fin.read():
        compressed_chunk = lzc.compress(chunk.encode("ascii"))
        fout.write(compressed_chunk)
    fout.write(lzc.flush())
stop = time.time()
time = stop - start

print(f"Uncompressed size: {os.stat(filename_in).st_size}")
print(f"Compressed size: {os.stat(filename_out).st_size}"
print(time)