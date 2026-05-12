def secure_archive(
    filename: str,
    action: str = "read",
    content: str = ""
) -> tuple[bool, str]:
    try:
        if action == "read":
            with open(filename, "r") as file:
                data = file.read()
                return (True, data)

        elif action == "write":
            with open(filename, "w") as file:
                file.write(content)
                return (True, "Content succesfully written to file")

        else:
            return (False, "Invalid action")
    except Exception as e:
        return (False, str(e))


print("=== Cyber Archives Security ===")

print("\nUsing 'secure_archive' to read from a nonexistent file:")

print(secure_archive("/not/existing/file"))

print("\nUsing 'secure_archive' to read from an inaccessible file:")

print(secure_archive("/etc/shadow"))

print("\nUsing 'secure_archive' to read from a regular file:")

print(secure_archive("./ancient_fragment.txt"))

print("\nUsing 'secure_archive' to write previous content to a new file:")

result = secure_archive("vault_copy.txt", "write", "[FRAGMENT COPY] secured")

print(result)
