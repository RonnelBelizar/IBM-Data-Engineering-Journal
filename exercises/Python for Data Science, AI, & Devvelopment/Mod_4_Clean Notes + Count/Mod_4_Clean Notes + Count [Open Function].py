# ============================================================
# 📝 Exercise: Clean Notes + Count "Python"
# ============================================================

# You are given a text file called "notes.txt" with content like this:
#
# Python is fun
#
# I love learning Python
#
# Data engineering is cool
#
# Python Python everywhere
#
# Your tasks:
# 1️⃣ Open "notes.txt" in read mode.
# 2️⃣ Clean the text:
#     - Remove blank lines.
#     - Strip spaces at the start and end of each line.
# 3️⃣ Write the cleaned lines into a new file called "clean_notes.txt".
# 4️⃣ Count how many times the word "Python" appears in the cleaned text.
# 5️⃣ Save the count in a new file called "summary.txt" with this format:
#        The word 'Python' appeared X times.
# 6️⃣ Print the content of "summary.txt" to verify.

text = r"C:\Users\Ronnel\Desktop\IBM Data Engineering\exercises\Python\Python for Data Science, AI, & Devvelopment\Mod_4_Clean Notes + Count\notes.txt"
directory = r"C:\Users\Ronnel\Desktop\IBM Data Engineering\exercises\Python\Python for Data Science, AI, & Devvelopment\Mod_4_Clean Notes + Count"

python_counter = 0

with open(text, "r") as source:
    with open(fr"{directory}\clean_note.txt", "w") as destination:
        for line in source:
            clean_lines = line.strip()
            if clean_lines == "":
                continue
            destination.write(clean_lines + "\n")

with open(fr"{directory}\clean_note.txt", "r") as file:
    print(file.read())
    file.seek(0)
    words = file.read()
    file.seek(0)
    for word in words.split():
        if word == "Python":
            python_counter += 1

print(f"Python count = {python_counter}")

with open(fr"{directory}\summary.txt", "w") as filewrite:
    filewrite.write(f"\"Python\" appeared {python_counter} times.")
