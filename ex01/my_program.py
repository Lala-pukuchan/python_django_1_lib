#!/usr/bin/env python3
import os
import sys


def main():
    # add local_lib to sys.path so that system can find the path module
    sys.path.insert(0, os.path.join(os.getcwd(), "local_lib"))
    from path import Path

    # create path object
    folder = Path("test_folder")

    # create folder and file
    folder.mkdir_p()
    file = folder / "test_file.txt"
    file.write_text("Hello, this is a test.")

    # read file
    content = file.read_text()
    print("File content:")
    print(content)


if __name__ == "__main__":
    main()
