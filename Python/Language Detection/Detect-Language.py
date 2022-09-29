from langdetect import detect
text = input('Enter any text in any language => ')
country_code = detect(text)
print(f"Country Code - {str(country_code).upper()}")
