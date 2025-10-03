import re

# Var for checking any non-characters
contact = r"Ronnel Belizar - 09154797401"

phone = r"\W"   # Checks "contact" if non-characters exist

match = re.findall(phone, contact)

print("Matches:", match)
#   Matches: [' ', ' ', '-', ' ']
