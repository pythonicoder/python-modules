import sys
import typing


if len(sys.argv) != 2:
    print("Usage: ft_archive_creation.py <file>")

else:

    filename = sys.argv[1]

    print("=== Cyber Archives Recovery & Preservation ===")
    print("Accessing file '" + filename + "'")

    try:

        file: typing.TextIO = open(
            filename,
            "r"
        )

        content = file.read()

        print("---")
        print()
        print(content)

        print("---")

        file.close()

        print(
            "File '" +
            filename +
            "' closed."
        )

        lines = content.split("\n")
        new_content = ""

        i = 0
        while i < len(lines):
            new_content += (lines[i] + "#")

            if i != len(lines)-1:
                new_content += "\n"
            i += 1

        print("\nTransform data:")
        print("---")
        print()
        print(new_content)

        print("---")

        new_file = input("Enter new file name (or empty): ")

        if new_file == "":
            print("Not saving data.")
        else:
            print("Saving data to '" + new_file + "'")
            out: typing.TextIO = open(new_file, "w")
            out.write(new_content)
            out.close()
            print("Data saved in file '" + new_file + "'.")
    except Exception as e:
        print("Error opening file '" + filename + "':", e)
