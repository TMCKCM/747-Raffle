from bs4 import BeautifulSoup as soup
import requests
import time

#FINESSED FROM https://thebot.net/threads/gmail-dot-trick-generator-in-python.322682/
def dot_trick(username):
    emails = []
    username_length = len(username)
    combinations = pow(2, username_length - 1)
    padding = "{0:0" + str(username_length - 1) + "b}"
    for i in range(0, combinations):
        bin = padding.format(i)
        full_email = ""

        for j in range(0, username_length - 1):
            full_email += (username[j]);
            if bin[j] == "1":
                full_email += "."
        full_email += (username[j + 1])
        emails.append(full_email + "@gmail.com")
        emails.append(full_email + "@googlemail.com")
    return emails
#END OF FINESSESISM


def signup(emailchosen):
    s = requests.session()
    s.get("https://www.google.com")
    counter = 0
    for email in dot_trick(emailchosen):
        s.cookies.clear()
        headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3334.0 Safari/537.36"}
        headers1={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3334.0 Safari/537.36", "content-type":"application/json; charset=UTF-8"}
        payload={"email":email,"firstName":NAME,"lastName":LASTNAME,"gender":"M","datepicker":"7/23/1998","dateOfBirth":"1998-07-23","countryOfSite":"US","newsletterDomain":"United States","newsletterLanguage":"en","newsletterTypeId":"40000","source":"543452387","eventType":"adi_eCom_Basketball_adidas747","sendMail":"Y","consents":{"consent":[{"consentType":"AMF","consentValue":"N","consentVersion":"ADIUS_VER_1"}]}}
        print("a*")
        a=s.get("http://www.adidas.com/us/747warehousest_signup?cm_sp=747-EVENT-PAGE-TICKETS-_-SIGN-UP", headers=headers)
        print("a")
        print("b*")
        b=s.options("https://brand.campaign.adidas.com/api/scv/subscription/newsletter/create", headers=headers)
        print("b")
        print("c*")
        c=s.post("https://brand.campaign.adidas.com/api/scv/subscription/newsletter/create", json=payload, headers=headers1)
        print("c")
        counter += 1
        time.sleep(1)
        print(c.text+" ["+str(counter)+"]")
    print("Done ("+str(counter)+")")
print("----------------------")
print("747 SIGNUP SCRIPT")
print("BY TMCKCM")
print("----------------------")
email=input("Gmail without '@gmail.com': ")
NAME = input("Name: ")
LASTNAME=input("Surname: ")
signup(email)
