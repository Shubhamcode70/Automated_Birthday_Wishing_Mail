
import smtplib


import pandas as pd
import datetime as dt
import random

csv_data = pd.read_csv("birthdays.csv")
today = (dt.datetime.now().month, dt.datetime.now().day)

birthday_data = {(data_row.month, data_row.day) : data_row for (index, data_row) in csv_data.iterrows()}


if today in birthday_data:
    person = birthday_data[today]
    person_name = person['name']
    person_email = person['email']

    file = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file) as letter:
        letter_data = letter.read()
        mod_letter = letter_data.replace("[NAME]", person_name)

    #Sending The Modified Letter to Person
    with smtplib.SMTP("smtp.google.com") as connection:
      user = "a@gmail.com"
      password = "pwd@r.com"
      address = person_email

      connection.starttls()
      connection.login(user=user, password=password)
      connection.sendmail(from_addr=user,
                          to_addrs=address,
                          msg=f"Subject :Wish You Happiest Birthday\n\n\n{mod_letter}")






