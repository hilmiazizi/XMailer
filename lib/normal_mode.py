def main():
    import os
    import time
    import banner
    import string
    import requests
    import random
    import string
    from urllib import quote
    from io import BytesIO
    from StringIO import StringIO
    from colorama import init, Fore, Style
    banner.main()
    frommail = raw_input(Style.BRIGHT + "Input Your From Mail : ")
    fromname = raw_input(Style.BRIGHT + "Input Your From Name : ")
    subject  = raw_input(Style.BRIGHT + "Input Your Subject   : ")
    letter   = raw_input(Style.BRIGHT + "Input Your Letter    : ")
    os.system('clear')
    banner.main()
    print(Style.BRIGHT + Fore.GREEN + "From Mail : " + Fore.BLUE + frommail)
    print(Style.BRIGHT + Fore.GREEN + "From Name : " + Fore.BLUE +  fromname)
    print(Style.BRIGHT + Fore.GREEN + "Subject   : " + Fore.BLUE +  subject)
    print(Style.BRIGHT + Fore.GREEN + "Letter    : " + Fore.BLUE +  letter)
    mailist = raw_input(Style.BRIGHT + Style.BRIGHT + "Input Your Mailist File : ")
    send    = input(Style.BRIGHT + "How Many Send           : ")
    delay   = input(Style.BRIGHT + "Input Delay Time        : ")

    #Declaration
    count_mailist = len(open(mailist).readlines(  ))
    mail_list = open(mailist, 'r')
    fail = open('failed.txt', 'w+')
    send_counter = 0
    break_counter = 0
    api_file= open('api.txt','r')
    for api in api_file:
        api=api.rstrip()
    #Main function
    for xmailer in mail_list :
        send_counter+=1
        xmailer=xmailer.rstrip()
        #BREAK
        if (send == break_counter):
            break_counter = 0
            waktu = "Pause for " + str(delay) + " seconds..."
            print (Style.BRIGHT + Fore.BLUE + waktu)
            time.sleep(delay)

        #Generate Random Case number
        randchar0 =random.choice(string.ascii_uppercase)
        randchar1 =random.choice(string.ascii_uppercase)
        randchar2 =random.choice(string.ascii_uppercase)
        randchar3 =random.choice(string.ascii_uppercase)
        randchar4 =random.choice(string.ascii_uppercase)
        randint0 = random.randrange(0,9)
        randint1 = random.randrange(0,9)
        randint2 = random.randrange(0,9)
        randint3 = random.randrange(0,9)
        randint4 = random.randrange(0,9)
        code = "%23"+randchar0+randchar1+randchar2+str(randint0)+str(randint1)+randchar3+str(randint2)+str(randint3)+str(randint4)+randchar4
        subject_replaced = subject.replace("!code!", code)
        subject_replaced = subject_replaced.replace(" ","%20")

        #Generate Random Number in From Mail
        if (count_mailist < 9):
            randnumb = random.randrange(0,9)
        elif (count_mailist < 99 and count_mailist > 9):
            randnumb = random.randrange(0,99)
        elif (count_mailist < 999 and count_mailist > 99):
            randnumb = random.randrange(0,999)
        elif (count_mailist < 9999 and count_mailist > 999):
            randnumb = random.randrange(0,9999)
        elif (count_mailist < 99999 and count_mailist > 9999):
            randnumb = random.randrange(0,99999)
        elif (count_mailist < 999999 and count_mailist > 99999):
            randnumb = random.randrange(0,999999)
        frommail_replaced = frommail.replace("!number!", str(randnumb))


        #Generate IP function
        oct1 = random.randrange(40,254)
        oct2 = random.randrange(2,254)
        oct3 = random.randrange(2,254)
        oct4 = random.randrange(2,254)
        ip = str(oct1)+"."+str(oct2)+"."+str(oct3)+"."+str(oct4)

        #mail function
        payload = "?to=%s&name=%s&letter=%s&from=%s&subject=%s&code=%s&ip=%s" % (xmailer,fromname,letter,frommail_replaced,subject_replaced,code,ip)
        requests.packages.urllib3.disable_warnings()
        url = api+payload
        response = requests.get(url, verify=False)
        result = response.text
        result = result.replace('\n', ' ')
        subject_replaced = subject_replaced.replace("%20", " ")
        subject_replaced = subject_replaced.replace("%23", "#")
        if "ok" in result:
           print (Style. BRIGHT + Fore.RED + "[" + Fore.GREEN + str(send_counter) + Fore.RED + "|" + Fore.GREEN + str(count_mailist) + Fore.RED + "] " + Fore.GREEN + frommail_replaced + Fore.BLUE + " | " + Fore.GREEN + xmailer)
        else:
            fail.write(xmailer)
            print (Style.BRIGHT + Fore.RED + xmailer + " | " + "FAIL! | " + "Logged to failed.txt")