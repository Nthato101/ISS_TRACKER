import requests
from datetime import datetime
import smtplib
import time

MY_LAT = -26.0414147 # Your latitude
MY_LONG = 28.2220075 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


def sat_pos():

    lat_distance = abs(parameters["lat"] - iss_latitude)
    lng_distance = abs(parameters["lng"] - iss_longitude)

    if lat_distance <= 5 and lng_distance <= 5:
        return True
    else:
        return False


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


def is_night():

    if sunset <= time_now.hour <= sunrise and close:
        return True
    else:
        return False

# If the ISS is close to my current position




while True:
    
    close = sat_pos()

    night = is_night()

    if night and close:
        time.sleep(60)
        my_email = "nthato101@gmail.com"
        connection = smtplib.SMTP("smtp.gmail.com", port=587)
        connection.starttls()
        connection.login(user=my_email, password="ibjkmnsnpddibifr")
        connection.sendmail(from_addr=my_email, to_addrs="nthato101@gmail.com",
                            msg=f"Subject: ISS ABOVE YOU\n\n The iss is above you current location is "
                                f"Longitude:{iss_longitude} Latitude:{iss_latitude}")
        connection.close()
