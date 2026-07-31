file_path = input("Enter file path:" ).strip()

try:
    with open(file_path, mode="r", encoding="utf-8") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("File not found")

except PermissionError:
    print("Permission denied")

finally:
    print("Program finished")

