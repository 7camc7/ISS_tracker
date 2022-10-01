import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 4.634915  # Your latitude
MY_LONG = -90.506882  # Your longitude
my_email = "codingpractice123321@gmail.com"
my_password = "didxhiewwwtfeoae"


def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_it_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.utcnow()
    current_hour = int(time_now.hour)

    if sunset < current_hour < sunrise:
        return True


while True:
    time.sleep(60)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()  # encrypt
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="claudiachurch00@gmail.com",
            msg=f"ISS visible \n\n Look at sky for ISS"
        )

