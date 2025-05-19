# Regex Data Extraction Project

This Python project demonstrates how to use regular expressions to extract various types of information from a sample data string. The script allows users to interactively search for specific data types such as emails, phone numbers, credit card numbers, currency amounts, time, URLs, HTML tags, and hashtags.

## Features

- Extracts the following from a sample data string:
  - Email addresses
  - Phone numbers (various formats)
  - Credit card numbers
  - Currency amounts
  - Time (24-hour and 12-hour formats)
  - URLs
  - HTML tags
  - Hashtags
- Interactive command-line interface for searching extracted data

## Usage

1. Make sure you have Python installed (version 3.x recommended).
2. Run the script:

   ```sh
   python regex_project.py
   ```

3. When prompted, enter one of the following search terms to view the extracted data:
   - `emails`
   - `phone numbers`
   - `credit card numbers`
   - `currency amounts`
   - `time`
   - `urls`
   - `html tags`
   - `hashtags`

4. Type `exit` to quit the program.

## Example

```
search for specific types of information in the data string.
Available search terms: emails, phone numbers, credit card numbers, currency amounts, time, urls, html tags, hashtags
Type "exit" to quit the program.
Please enter a search term: emails
Emails: ['user@example.com', 'firstname.lastname@company.co.uk']
```