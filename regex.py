import re

def extract_emails(text):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(pattern, text)

def extract_urls(text):
    pattern = r'https?://(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z]{2,6}\b(?:[-a-zA-Z0-9@:%_\+.~#?&/=]*)'
    return re.findall(pattern, text)

def extract_phone_numbers(text):
    pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    return re.findall(pattern, text)

def extract_credit_card_numbers(text):
    pattern = r'\b(?:\d{4}[-\s]?){3}\d{4}\b'
    return re.findall(pattern, text)
def extract_time(text):
    pattern = r'\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?\b'
    return re.findall(pattern, text)

def extract_html_tags(text):
    pattern = r'<[^>]+>'
    return re.findall(pattern, text)

def extract_hashtags(text):
    pattern = r'#[A-Za-z0-9_]+'
    return re.findall(pattern, text)

def extract_currency_amounts(text):
    pattern = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
    return re.findall(pattern, text)

# Sample text
test_text = """
Emails: lauraceline@gmail.com, laura.celine@company.co.uk
URLs: https://www.laura.com, http://subdomain.example.org/page
Phones: (123) 456-7890, 123-456-7890, 123.456.7890
Credit Cards: 1234 5678 9012 3456, 1234-5678-9012-3456
Times: 14:30, 2:30 PM
HTML: <p>, <div class="example">, <img src="image.jpg" alt="description">
Hashtags: #example, #ThisIsAHashtag
Currency: $19.99, $1,234.56
"""

print("Extracted Emails:", extract_emails(test_text))
print("Extracted URLs:", extract_urls(test_text))
print("Extracted Phone Numbers:", extract_phone_numbers(test_text))
print("Extracted Credit Card Numbers:", extract_credit_card_numbers(test_text))
print("Extracted Times:", extract_time(test_text))
print("Extracted HTML Tags:", extract_html_tags(test_text))
print("Extracted Hashtags:", extract_hashtags(test_text))
print("Extracted Currency Amounts:", extract_currency_amounts(test_text))

