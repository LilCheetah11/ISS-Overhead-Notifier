import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 18.147528 # Your latitude
MY_LONG = 73.977127 # Your longitude
my_email="oktim3070test@yahoo.com"
my_password="nkvgpjvabmhxqixg"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


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

time_now = datetime.now()



while True:
    # time.sleep(60)
    if time_now.hour >= sunset and time_now.hour <= sunrise and MY_LAT-5<=iss_latitude>=MY_LAT+5 and MY_LONG-5 <=iss_longitude>=MY_LONG+5:
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(user=my_email,password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg="Subject:LOOK UP☝\n\n The ISS is above you in the sky"
            )


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



