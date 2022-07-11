import requests
import datetime
import smtplib

# response = requests.get(url=" https://api.sunrise-sunset.org/json?lat=36.72016&lng=-4.42065&date=today")
my_latitude = 30.893109
my_longitude = 75.849901
today_hour = datetime.datetime.now().hour


def ISS_near_me():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()
    iss_lat = float(iss_data["iss_position"]["latitude"])
    iss_long = float(iss_data["iss_position"]["longitude"])

    if my_longitude-5 <= iss_long <= my_longitude+5 and my_latitude-5 <= iss_lat <= my_latitude+5:
        return True
    else:
        return False


def iss_mail():
    my_email = "satyamsharma3524@gmail.com"
    password = "edvfupwklpntyqrs"

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="nawalkumarsharma2@gmail.com",
                            msg=f"subject:ISS Near you, See in the Sky.\n\n"
                                f"International Space Station is near you.Go see it in the sky."
                            )


def ISS_time_now():
    if ISS_near_me() and sunrise > today_hour > sunset:
        print("Iss near you, mail sent!!!")
        iss_mail()
    else:
        print("Iss not near you, mail not sent!!!")


parameters = {
    "lat": my_latitude,
    "lng": my_longitude,
    "formatted": "0"
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


# checks weather the ISS is near you or not, if it is near you it will send a mail to your email id.
# if it is not near you it will not send a mail to your email id.
ISS_time_now()