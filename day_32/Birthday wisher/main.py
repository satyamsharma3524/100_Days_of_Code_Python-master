import datetime
import pandas
import random
import smtplib


my_email = "satyamsharma3524@gmail.com"
password = "edvfupwklpntyqrs"

today = datetime.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")

birthday_dict = {(data_row["month"], data_row["day"]) : data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    letter_temp_path = f"letter_templates/letter_{random.randint(1,3)}.txt"

    with open(letter_temp_path) as letter:
        birthday_person = birthday_dict[today_tuple]
        letter_content = letter.read()
        l1 = letter_content.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["email"],
                            msg=f"subject:Happy Birthday!!!\n\n {l1}"
                            )

