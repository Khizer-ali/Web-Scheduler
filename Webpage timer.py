import time
import webbrowser

set_alarm = input("Set website alarm as H:M:S")
url = input("Enter website")
actual_time = time.strftime("%I:%M:%S")

while (actual_time != set_alarm):
    print("The alarm is " + actual_time)
    actual_time = time.strftime("%I:%M:%S")
    time.sleep(1)

if(actual_time == set_alarm):
    print("Your webpage is opening")
    webbrowser.open(url)

