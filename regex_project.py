import re

# This is a sample data string
data = ''' Email addresses:
user@example.com
firstname.lastname@company.co.uk
URLs:
https://www.example.comLinks to an external site.
https://subdomain.example.org/pageLinks to an external site.
Phone numbers (various formats):
(123) 456-7890
123-456-7890
123.456.7890
Credit card numbers:
1234 5678 9012 3456
1234-5678-9012-3456
Time:
14:30 (24-hour format)
2:30 PM (12-hour format)
HTML tags:
<p>
<div class="example">
<img src="image.jpg" alt="description">
Hashtags:
#example
#ThisIsAHashtag
Currency amounts:
$19.99
$1,234.56
'''
# The following regex patterns are used to extract specific information from the data string
emails = re.findall(r"\b[\w.-]+@[\w.-]+\.\w+\b", data)
phone_numbers = re.findall(r"\d{3}[-.]\d{3}[-.]\d{4}|[(]\d{3}[)]\s\d{3}[-]\d{4}", data)
credit_nums = re.findall(r"\d{4}-\d{4}-\d{4}-\d{4}|\d{4}\s\d{4}\s\d{4}\s\d{4}", data)
currency_amounts = re.findall(r"(\$\S+)", data)
time = re.findall(r"(\d+:\S+)", data)
urls = re.findall(r"\b(https:\/\/\S+)", data)
html_tags = re.findall(r"(<.+>)", data)
hashtags = re.findall(r"(#\S+)", data)

# The following code block allows the user to search for specific types of information
print("search for specific types of information in the data string.")
print("Available search terms: emails, phone numbers, credit card numbers, currency amounts, time, urls, html tags, hashtags")
print("Type \"exit\" to quit the program.")
while True:
    search = input("Please enter a search term: ")

    if search == "exit". lower():
        print("Exiting the program.")
        break
    elif search == "emails".lower():
        print(f"Emails: {emails}")
    elif search == "phone numbers".lower().strip():
        print(f"Urls: {phone_numbers}")
    elif search == "credit card numbers".lower().strip():
        print(f"Credit Card Numbers: {credit_nums}")
    elif search == "currency amounts".lower().strip():
        print(f"Currency Amounts: {currency_amounts}")
    elif search == "time".lower():
        print(f"Time: {time}")
    elif search == "urls".lower().strip():
        print(f"URLs: {urls}")
    elif search == "html tags".lower().strip():
        print(f"HTML tags: {html_tags}")
    elif search == "hashtags".lower().strip():
        print(f"Hashtags: {hashtags}")
    else:
        print("Please enter a valid search term.")
        print("Available search terms: emails, phone numbers, credit card numbers, currency amounts, time, urls, html tags, hashtags")