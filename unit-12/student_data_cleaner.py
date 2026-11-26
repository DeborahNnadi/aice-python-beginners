# Simulate student data profile

full_name = "  Prayer Nworah  "
email_address = "    PrayerNWORAH@GMAIL.com   "
telephone_number = "  +234-701-234-5678  "

# Clean and format each field
clean_name = full_name.strip().title()
clean_email = email_address.strip().lower()
clean_phone = telephone_number.strip().replace("-","")

#Display the cleaned profile

print(f"Name: {clean_name}")
print(f"Email: {clean_email}")
print(f"Phone: {clean_phone}")

#Validation checks

print(len(clean_name))


