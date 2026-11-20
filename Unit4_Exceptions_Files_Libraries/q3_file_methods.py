"""Unit 4 - Q3: File Methods and Exception Handling"""

import os

FILENAME = "sample.txt"

# Create a sample file if it does not exist, so the program can run as-is.
if not os.path.exists(FILENAME):
    with open(FILENAME, "w") as tmp:
        tmp.write("Python is easy to learn.\nFiles store data permanently.\nExceptions handle errors.\n")


def demo(filename):
    f = None
    try:
        f = open(filename, "r")
    except FileNotFoundError:
        print(f"Error: '{filename}' was not found.")
    except PermissionError:
        print(f"Error: no permission to open '{filename}'.")
    except IsADirectoryError:  # Linux/macOS raise this instead of PermissionError for folders
        print(f"Error: '{filename}' is a directory, not a file.")
    else:
        print("File name :", f.name)
        print("File mode :", f.mode)

        print("\nread(10)      :", repr(f.read(10)))
        print("tell()        :", f.tell())

        f.seek(0)
        print("\nAfter seek(0), tell() =", f.tell())
        print("readline()    :", repr(f.readline()))
        print("tell()        :", f.tell())

        f.seek(0)
        print("\nreadlines()   :", f.readlines())

        f.seek(7)
        print("\nseek(7) then read(6):", repr(f.read(6)))
    finally:
        if f is not None:
            f.close()
            print("\nfinally: file closed.")
        else:
            print("\nfinally: nothing to close.")


print("=== Existing file ===")
demo(FILENAME)

print("\n=== Missing file ===")
demo("does_not_exist.txt")

print("\n=== Permission error (opening a directory) ===")
demo(".")
