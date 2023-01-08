import requests
import smtplib

# API key
api_key = "AIzaSyC31y9uP9Nc2swCrx_WnHfOZraqpIQ9wt0"

# initial address input
home = input("Enter current location\n")

# work address input
work = input("Enter destination\n")

# base url
url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"

# get response
r = requests.get(url + "origins=" + home + "&destinations=" + work + "&key=" + api_key)

# return time as text and as seconds
time = r.json()["rows"][0]["elements"][0]["duration"]["text"]
seconds = r.json()["rows"][0]["elements"][0]["duration"]["value"]

# print the travel time
print("\nThe total travel time from location to destination is", time)

# check if travel time is more than 1 hour
if (seconds > 3600):
    # email constraints
    sender = "..."
    recipient = "..."
    subject = "EMERGENCY"
    message = "Hi ,\n\n user is in probable danger."

    # format email
    email = "Subject: {}\n\n{}".format(subject, message)

    # get sender password
    password_file = open("password.txt", "r")
    password = password_file.readline()
    password_file.close()

    # creates SMTP session
    s = smtplib.SMTP("smtp.gmail.com", 587)

    # start TLS for security
    s.starttls()

    # authentication
    s.login(sender, password)

    # sending the mail
    s.sendmail(sender, recipient, email)

    # terminating the session
    s.quit()