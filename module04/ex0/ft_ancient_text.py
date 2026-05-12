import sys
import typing

if len(sys.argv) != 2:
    print("Usage: ft_ancient_text.py <file>")
else:
    filename = sys.argv[1]

    print("=== Cyber Archives Recovery ===")
    print("Accessing file '" + filename + "'")

    try:
        file: typing.TextIO = open(
            filename,
            "r"
        )

        content = file.read()
        print()
        print(content)

        print("---")
        file.close()

        print(
            "File '" +
            filename +
            "' closed."
        )

    except Exception as e:
        print(
            "Error opening file '" +
            filename +
            "':",
            e
        )
