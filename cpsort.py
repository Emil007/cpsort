import csv
import glob
import os

# Get the current directory as the folder path
folder_path = os.getcwd()

# Initialize an empty set to store unique emails
unique_emails = set()
all_emails = []

# Loop through each root*.csv file in the folder
for file_path in glob.glob(folder_path + "/root*.csv"):
    with open(file_path, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header row

        # Iterate through each row in the CSV
        for row in csv_reader:
            emails = row[3].replace('"', "").split(",")  # Extract emails from the fourth column
            all_emails.extend(email.strip() for email in emails)
            unique_emails.update(email.strip() for email in emails)

# Remove duplicates from the list of all emails
unique_emails = set(all_emails)

# Write the unique emails to a text file in groups of 100
output_file = "emails.txt"
with open(output_file, "w") as txt_file:
    emails = list(unique_emails)
    for i, email in enumerate(emails, start=1):
        txt_file.write(email)
        if i % 100 == 0 and i != len(emails):
            txt_file.write("\n\n")
        elif i != len(emails):
            txt_file.write(";")

# Get the counts
total_emails = len(all_emails)
duplicate_count = total_emails - len(unique_emails)

# Print the summary
print("Emails found: ", total_emails)
print("Duplicates removed: ", duplicate_count)
print("Unique emails remaining: ", len(unique_emails))

