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
    init(autoreset=True)

    os.system('clear')
    banner.main()
    user_file = "username_list.txt"
    domain_file = "domain_list.txt"
    subject_file = "subject_list.txt"
    name_file = "fromname_list.txt"
    letter_file = "letter_list.txt"
    count_user = len(open(user_file).readlines(  ))
    count_domain = len(open(domain_file).readlines(  ))
    count_subject = len(open(subject_file).readlines(  ))
    count_name = len(open(name_file).readlines())
    count_letter = len(open(letter_file).readlines())
    print "Username found    : ",count_user
    print "Domain found      : ",count_domain
    print "Subject found     : ",count_subject
    print "Sender Name found : ",count_name
    print "Letter Found      : ",count_letter
    print count_user*count_domain*count_subject*count_name*count_letter, " Combination generated."
    mail_file = raw_input("Input your Mailist : ")
    count_mailist = len(open(mail_file).readlines())
    os.system("clear")
    banner.main()
    total_send = str(count_user*count_domain*count_subject*count_name*count_letter*count_mailist)
    print total_send + " Emails will be send"
    send = input("How Many Send      : ")
    delay = input("Input Delay Time   : ")
    os.system("clear")
    banner.main()
    fail = open('failed.txt', 'w+')
    api_file= open('api.txt','r')
    for api in api_file:
        api=api.rstrip()
    send_counter = 0
    break_counter = 0
    api_line=0
    domain=open(domain_file, 'r')
    for line in domain:
        domains=line.rstrip()
        user=open(user_file, 'r')
        for line in user:
            subjects=open(subject_file, 'r')
            users=line.rstrip()
            for line in subjects:
                subject=line.rstrip()
                name=open(name_file,'r')
                for line in name:
                    fromname=line.rstrip()
                    letter=open(letter_file, 'r')
                    for line  in letter:
                        letter=line.rstrip()
                        mail=open(mail_file,'r')
                        for xmailer in mail:
                            send_counter+=1
                            #BREAK
                            if (send == break_counter):
                                break_counter = 0
                                waktu = "Pause for " + str(delay) + " seconds..."
                                print (Style.BRIGHT + Fore.BLUE + waktu)
                                time.sleep(delay)

                            xmailer=xmailer.replace('\n', '')
                            frommail=str(users)+'@'+str(domains)
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
                            if "ok" in result:
                                print (Style. BRIGHT + Fore.RED + "[" + Fore.GREEN + str(send_counter) + Fore.RED + "|" + Fore.GREEN + str(total_send) + Fore.RED + "] " + Fore.GREEN + frommail_replaced + Fore.BLUE + " | " + Fore.GREEN + xmailer)
                            else:
                                fail.write(xmailer)
                                print (Style.BRIGHT + Fore.RED + xmailer + " | " + "FAIL! | " + "Logged to failed.txt")

                            break_counter+=1