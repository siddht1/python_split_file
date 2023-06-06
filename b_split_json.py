import os
import json
import math

def get_chunk_size():
    """
    Returns the chunk size as entered by the user.
    """
    while True:
        try:
            chunk_size = int(input("Enter chunk size in bytes: "))
            return chunk_size
        except ValueError:
            print("Invalid input, please enter an integer value.")

def create_directory(directory):
    """
    Creates a directory if it does not already exist.
    """
    if not os.path.exists(directory):
        os.mkdir(directory)
        print("Directory", directory, "created.")
    else:
        print("Directory", directory, "already exists.")

def split_file(file_source, chunk_size):
    """
    Splits a file into chunks of size chunk_size and returns a list of the split file names.
    """
    with open(file_source, 'rb') as read_bin:
        data = read_bin.read()
    info = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
    split_files = []
    for i, chunk in enumerate(info):
        split_file_name = f"{file_source}.part.{i}"
        with open(split_file_name, 'wb') as write_bin:
            for byte in chunk:
                write_bin.write(byte.to_bytes(1, byteorder='big'))
        split_files.append(split_file_name)
    return split_files

def create_map_file(file_source, file_size, chunk_size, split_files):
    """
    Creates a JSON map file containing information about the split files.
    """
    ab = file_source.split('.')
    directory = ab[0]
    struct = {
        "file": file_source,
        "file_size": file_size,
        "split_size": chunk_size,
        "split_number_of_files": math.ceil(file_size/chunk_size),
        "destination_directory": directory,
        "number_of_split_file_created": len(split_files),
        "split_file": split_files
    }
    with open(f"{file_source}.map.json", 'w') as jsn_file:
        json.dump(struct, jsn_file, indent=4)

if __name__ == '__main__':
    file_source = 'Ram_Setu_2022_Hindi_Full_Movie_CAMRip_(FilmyZilla.vin) (1).mp4'
    file_size = os.path.getsize(file_source)
    print(f"Size of file {file_source} is {file_size}")
    chunk_size = get_chunk_size()
    print(f"Files will be split into {chunk_size} byte chunks.")
    create_directory(file_source.split('.')[0])
    split_files = split_file(file_source, chunk_size)
    create_map_file(file_source, file_size, chunk_size, split_files)
```

Explanation:
- The code starts by defining three functions: `get_chunk_size()`, `create_directory()` and `split_file()`.
- `get_chunk_size()` prompts the user to enter the chunk size and returns the entered value as an integer.
- `create_directory()` creates a directory if it does not already exist.
- `split_file()` reads the source file in binary mode, splits it into chunks of size chunk_size and writes each chunk to a split file. It returns a list of the split file names.
- The `create_map_file()` function creates a dictionary containing information about the split files and writes it to a JSON map file using `json.dump()`.
- In the `main` block, the source file name and size are obtained using `os.path.getsize()`.
- The user is prompted to enter the chunk size using `get_chunk_size()`.
- The destination directory is created using `create_directory()`.
- The source file is split into chunks using `split_file()`.
- The JSON map file is created using `create_map_file()`.
