##################### Extra Hard Starting Project ######################
import smtplib
import pandas as pd
import datetime as dt
import random, os

MY_EMAIL = "*@gmail.com"
MY_PASSWORD = "*"

directory_path = "birthday-wisher-extrahard-start/letter_templates"
letter_files = [L for L in os.listdir(directory_path) if L.endswith(".txt")]
birthday_members = pd.read_csv("birthday-wisher-extrahard-start/birthdays.csv")

now = dt.datetime.now()
month = now.month
day = now.day

birthday_match_people = birthday_members[(birthday_members.month == month) & (birthday_members.day == day)]

if not birthday_match_people.empty and letter_files:
    for index, person in birthday_match_people.iterrows():
        random_file = random.choice(letter_files)
        file_path = os.path.join(directory_path, random_file)

        with open(file_path) as letter_file:
            contents = letter_file.read()
            contents = contents.replace("[NAME]", person["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_members.email,
            msg=f"Subject:Birthday Card!!!!!\n\n{contents}"
        )
