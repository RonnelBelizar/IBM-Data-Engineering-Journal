# Copying text file contents to another text file

with open(r"C:\Users\Ronnel\Desktop\IBM Data Engineering\exercises\text_open.txt", "r") as source:
    with open(r"C:\Users\Ronnel\Desktop\IBM Data Engineering\exercises\blank_text.txt", "w") as destination:
        for line in source:
            destination.write(line + "\n")

with open(r"C:\Users\Ronnel\Desktop\IBM Data Engineering\exercises\blank_text.txt", "r") as file:
    print(file.read())
