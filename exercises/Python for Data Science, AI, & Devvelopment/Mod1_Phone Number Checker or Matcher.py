# Phone Number Matcher/Checker

import re

contact = r"Ronnel Belizar - 09154797401"   # Var for checking 11 digit number
# Checks "contact" if "phone" is found inside
phone = r"\d\d\d\d\d\d\d\d\d\d\d"
match = re.search(phone, contact)

if match:                                   # Retrieves the substring "09154797401"
    print("Phone number:", match.group())
else:
    print("Match not found")
