import re



#Requiremnt-1
def extractEmailAddresses(text):
    """Extracts all email addresses from a given text using regex."""
    emailPattern = r'[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(emailPattern, text)
    print("Extracted Emails:", emails)


###############################################################################################
#Requiremnt-2
def validateAndReplacePhoneNumbers(text):
    """Validates phone numbers in the format (XXX) XXX-XXXX and replaces invalid ones."""
    phonePattern = r'\(\d{3}\) \d{3}-\d{4}'
    validatedText = re.sub(r'\b(?!' + phonePattern + r'\b).*', "Invalid Number", text)
    print("Validated Text:", validatedText)


###############################################################################################
#Requiremnt-3
def extractDateFromString(text):
    """Extracts a date in the format DD-MM-YYYY using capturing groups in regex."""
    datePattern = r'(\d{2})-(\d{2})-(\d{4})'
    match = re.search(datePattern, text)
    if match:
        print("Extracted Date:", match.group())
    else:
        print("No valid date found.")

# Example usage

extractEmailAddresses("Contact us at support@example.com and info@domain.com.")
validateAndReplacePhoneNumbers("Call us at (123) 456-7890 or 987-654-3210.")
extractDateFromString("Today's date is 25-12-2024.")
