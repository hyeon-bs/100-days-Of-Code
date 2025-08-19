# import smtplib

# my_email = "*@gmail.com"
# password = "*"

# # connection = smtplib.SMTP("smtp.gmail.com")
# # connection.close()

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, 
#                         to_addrs="*@gmail.com", 
#                         msg="Subject:Hello\n\nThis is the boby email."
#                         )

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year= 1995, month=12, day=15, hour=4)
print(date_of_birth)
