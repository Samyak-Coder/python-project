import webbrowser

print("Co-shield:")
print("          Welcome to co-shield.")
print("We will help you to be safe and be aware about the causes and symptoms of COVID-19.")
print("commands are:")
print("             1)co_scan")
print("             2)FAQ")
print("             3)Exit")
print("             4)GetVaccinated")
print("             5)VaccineInfo")
command_input = input("Please enter you command.")

if command_input == "co_scan":
    print("Co-shield:")
    print("          Please answer all the quetions.")
    lung = input("do you have any lung disease?yes/no")
    d = input("do u have diabetes?yes/no")
    age: int = int(input("Please enter your age."))
    vc = input("Are you vaccinated?yes/no")
    temp: int = int(input("Please input your temperature.(Please enter the value in fahrenheit.)"))
    ox = input("Please input your oxygen level")
    score = int(0)
    if lung == "yes":
        score = int(score) + 10
        print("You have a lung disease so pls concern Doctor.")
    elif lung == "no":
        score = int(score) + 0
    else:
        lung = input("Please give the answer in yes/no. do u have any lung disease?yes/no")

    if d == "yes":
        score = int(score) + 10
        print("You have a Diabetes so pls concern Doctor.")
    elif d == "no":
        score = int(score) + 0
    else:
        d = input('Please give the answer in yes/no. do u have Diabetes?yes/no')

    if int(60) > int(age):
        score = int(score) + 10
    elif int(age) >= int(60):
        score = int(score) + 0
    else:
        age = input("Please type ur age in numbers.What is ur age?")

    if vc == "yes":
        score = int(score) - 10
    elif vc == "no":
        score = int(score) + 10
        print("Please consider getting Vaccinated")
    else:
        vc = input("Please give the answer in yes/no. Are u vaccinated?yes/no")

    if int(temp) <= int(98):
        score = int(score) - 10
    elif int(temp) >= int(98):
        score = int(score) + 10
    else:
        temp = input("Please type ur temperature in degree fahrenheit .What is ur temperature?")

    if int(ox) <= int(95):
        score = int(score) + 10
    elif int(ox) >= int(95):
        score = int(score) + 0
    else:
        ox = input("Please type ur Oxygen level")

    if int(score) >= int(50):
        print("You are at High risk please concern doctor!")

    elif int(score) <= int(50):
        print("You are at low risk but take care!")

elif command_input == "FAQ":
    url = "https://www.youtube.com/YouTubeIndia"
    new = 2
    webbrowser.open(url=url,new=new)
    print("Now You will be redirected to a link.")

elif command_input == "end":
    exit()

elif command_input == "GetVaccinated":
    url = "https://www.cowin.gov.in/"
    new = 2
    webbrowser.open(url=url,new=new)
    print("Now You will be redirected to a link.")

elif command_input == "VaccineInfo":
    url = "https://www.who.int/news-room/q-a-detail/coronavirus-disease-(covid-19)-vaccines?adgroupsurvey={adgroupsurvey}&gclid=CjwKCAjwo4mIBhBsEiwAKgzXOFWiUR1TgECinkAiSOsIZhrP0P1Tuhxt4nTciYZVs9lVRU-rFm_4yRoCTpgQAvD_BwE"
    new = 2
    webbrowser.open(url=url,new=new)
    print("Now You will be redirected to a link.")    
    

else:
    print("Please restart the application you have put a wrong input.")