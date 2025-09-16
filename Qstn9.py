#Write a program that:
#I. Uses regular expressions to extract all email addresses from a given text.
#II. Uses regular expressions to validate a date in the format &quot;YYYY-MM-DD&quot;.
#III. Uses regular expressions to replace all occurrences of a word with another word in a string.
#IV. Use regular expressions to split a string by all non-alphanumeric characters.

import re # this "re" gives access to regular expressions

# I. Extract all email addresses from a given text
def extract_emails(text):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(pattern, text)


# II. Validate a date in the format YYYY-MM-DD
def validate_date(date_str):
    pattern = r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$'
    return bool(re.match(pattern, date_str))


# III. Replace all occurrences of a word with another word
def replace_word(text, old_word, new_word):
    # \b ensures we replace only whole words
    pattern = r'\b' + re.escape(old_word) + r'\b'
    return re.sub(pattern, new_word, text)


# IV. Split a string by all non-alphanumeric characters
def split_by_non_alnum(text):
    pattern = r'[^a-zA-Z0-9]+'
    return [word for word in re.split(pattern, text) if word]


# DEMONSTRATION HERE

sample_text = "Contact us at support@example.com or admin@mail.org for help."
date1 = "2025-09-16"
date2 = "2025-13-40"
replace_text = "Python is great. I love Python because Python is powerful."
split_text = "Hello, world! This_is-a test."

# I. Extract emails
print("Extracted Emails:", extract_emails(sample_text))

# II. Validate dates
print("Is", date1, "valid?", validate_date(date1))
print("Is", date2, "valid?", validate_date(date2))

# III. Replace word
print("After Replacement:", replace_word(replace_text, "Python", "Java"))

# IV. Split string
print("Split Result:", split_by_non_alnum(split_text))
