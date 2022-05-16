import smtplib
import datetime as dt
import random

my_email = "satyamsharma3524@gmail.com"
password = "edvfupwklpntyqrs"
with open("quotes.txt", "r") as quotes:
    quotes_list = quotes.readlines()

todays_day = dt.datetime.weekday(dt.datetime.now())

if todays_day == 0:
    # send mail on monday
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="gauravsatyam3524@gmail.com",
                            msg=f"subject:Monday Motivation Quotes : Python System\n\n {quotes_list[random.randint(0, len(quotes_list)-1)]}"
                            )

else:
    print("It's not Monday. No mail to send")


