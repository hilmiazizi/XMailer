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

    os.system('clear')
    banner.main()

    #Declare List File
    letter_list = open('letter_list.txt', 'r')
    subject_list = open('subject_list.txt', 'r')
    frommail_list = open('frommail_list.txt', 'r')
    fromname_list = open('fromname_list.txt', 'r')

    #Count List
    count_letter = len(open('letter_list.txt').readlines(  ))
    count_subject = len(open('subject_list.txt').readlines(  ))
    count_frommail = len(open('frommail_list.txt').readlines(  ))
    count_fromname = len(open('fromname_list.txt').readlines(  ))

    print (Style.BRIGHT + "Letter Found    : " + Fore.GREEN + str(count_letter))
    print (Style.BRIGHT + "Subject Found   : " + Fore.GREEN + str(count_subject))
    print (Style.BRIGHT + "From Mail Found : " + Fore.GREEN + str(count_frommail))
    print (Style.BRIGHT + "From Name Found : " + Fore.GREEN + str(count_fromname))

    mailist = raw_input(Style.BRIGHT + "Input Your Mailist : ")
    send    = input(Style.BRIGHT + "How Many Send      : ")
    delay   = input(Style.BRIGHT + "Break Time         : ")
    break_counter = 0
    count_mailist = len(open(mailist).readlines(  ))
    send_counter = 0

    #Open File
    mail_list = open(mailist,'r')
    fail = open('failed.txt', 'w+')
    api_file= open('api.txt','r')
    for api in api_file:
        api=api.rstrip()

    #Default Pointer Value
    frommail_line = 0
    fromname_line = 0
    subject_line = 0
    letter_line = 0

    #Load all list by line
    with letter_list as letter:
        letter_split = [line.rstrip() for line in letter]
    with subject_list as subject:
        subject_split = [line.rstrip() for line in subject]
    with frommail_list as mail:
        mail_split = [line.rstrip() for line in mail]
    with fromname_list as name:
        name_split = [line.rstrip() for line in name]


    #Sending Function
    for xmailer in mail_list:
        send_counter+=1

        #BREAK
        if (send == break_counter):
            break_counter = 0
            waktu = "Pause for " + str(delay) + " seconds..."
            print (Style.BRIGHT + Fore.BLUE + waktu)
            time.sleep(delay)

        xmailer = xmailer.replace("\n", "")

        #From Mail Split
        if (frommail_line == count_frommail):
            frommail_line = 0
        frommail = mail_split[frommail_line]
        frommail_line+=1

        #From Name Split
        if (fromname_line == count_fromname):
            fromname_line = 0
        fromname = name_split[fromname_line]
        fromname_line+=1

        #Subject Split
        if (subject_line == count_subject):
            subject_line = 0
        subject = subject_split[subject_line]
        subject_line+=1

        #Letter Split
        if (letter_line == count_letter):
            letter_line = 0
        letter = letter_split[letter_line]
        letter_line+=1

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

        #Generate IP function
        oct1 = random.randrange(40,254)
    	oct2 = random.randrange(2,254)
    	oct3 = random.randrange(2,254)
    	oct4 = random.randrange(2,254)
    	ip = str(oct1)+"."+str(oct2)+"."+str(oct3)+"."+str(oct4)

        payload = "?to=%s&name=%s&letter=%s&from=%s&subject=%s&code=%s&ip=%s" % (xmailer,fromname,letter,frommail_replaced,subject_replaced,code,ip)
        requests.packages.urllib3.disable_warnings()
        url = api+payload
        response = requests.get(url, verify=False)
        result = response.text
        result = result.replace('\n', ' ')
        subject_replaced = subject_replaced.replace("%20", " ")
        subject_replaced = subject_replaced.replace("%23", "#")

        break_counter+=1
        if "ok" in result:
            print (Style. BRIGHT + Fore.RED + "[" + Fore.GREEN + str(send_counter) + Fore.RED + "|" + Fore.GREEN + str(count_mailist) + Fore.RED + "] " + Fore.GREEN + frommail_replaced + Fore.BLUE + " | " + Fore.GREEN + xmailer)
        else:
            fail.write(xmailer)
            print (Style.BRIGHT + Fore.RED + xmailer + " | " + "FAIL! | " + "Logged to failed.txt")
 