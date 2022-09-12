import zlib, sys, time

filename_in = "EEE3097S_2022_Turntable_Example_Data.csv"
filename_out = "EEE3097S_2022_Turntable_Example_Data.csv.zl"

start = time.time()
with open(filename_in, mode="rb") as fin, open(filename_out, mode="wb") as fout:
    data = fin.read()
    compressed_data = zlib.compress(data, zlib.Z_BEST_COMPRESSION)
    stop = time.time()
    print(f"Original size: {sys.getsizeof(data)}")
    
    print(f"Compressed size: {sys.getsizeof(compressed_data)}")
    print("Compression time: ", stop-start)
    fout.write(compressed_data)