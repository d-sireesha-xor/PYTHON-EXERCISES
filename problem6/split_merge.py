import os
import threading

INPUT_FILE = "10mb-examplefile-com.txt"
CHUNK_SIZE = 1024 * 1024  # 1 MB
CHUNK_FOLDER = "chunks"
MERGED_FILE = "merged_file.txt"

def split_file():
    if not os.path.exists(CHUNK_FOLDER):
        os.makedirs(CHUNK_FOLDER)

    with open(INPUT_FILE, "rb") as f:
        chunk_num = 0
        while True:
            chunk_data = f.read(CHUNK_SIZE)
            if not chunk_data:
                break
            chunk_filename = os.path.join(CHUNK_FOLDER, f"chunk_{chunk_num}.bin")
            with open(chunk_filename, "wb") as chunk_file:
                chunk_file.write(chunk_data)
            chunk_num += 1
    print(f"File split into {chunk_num} chunks.")

def merge_chunk(chunk_filename, result_dict, index):
    """Thread function to read a chunk and store in dictionary"""
    with open(chunk_filename, "rb") as f:
        data = f.read()
        result_dict[index] = data


def merge_chunks():
    chunk_files = sorted(os.listdir(CHUNK_FOLDER), key=lambda x: int(x.split("_")[1].split(".")[0]))
    threads = []
    result_dict = {}

    for idx, chunk_file in enumerate(chunk_files):
        t = threading.Thread(target=merge_chunk, args=(os.path.join(CHUNK_FOLDER, chunk_file), result_dict, idx))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    with open(MERGED_FILE, "wb") as f:
        for idx in range(len(result_dict)):
            f.write(result_dict[idx])

    print(f"Chunks merged into {MERGED_FILE}")

def verify_files():
    with open(INPUT_FILE, "rb") as f1, open(MERGED_FILE, "rb") as f2:
        original = f1.read()
        merged = f2.read()
    if original == merged:
        print("SUCCESS: Merged file is identical to original!")
    else:
        print("ERROR: Files are different!")

if __name__ == "__main__":
    split_file()
    merge_chunks()
    verify_files()
