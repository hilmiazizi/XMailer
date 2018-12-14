1. Introduction

  XMailer is a progam that have sending mail function using php mail function.
XMailer using API that hosted on some web to send email. XMailer designed to send
bulk mailist that have delay function to maintain the hosting life.

2. Main Manual
- Place your mailist into one folder with xmailer
- Place your letter on Hosting that same folder with the api file
- You can put mail address to letter with !email! format
- You can generate random code on subject and letter with !code! format
- You can generate random IP on letter with !ip! format
- You can generate random number on from mail with !number! format
- All failed sending email will be logged to failed.txt
- You must install requests, colorama python module using command "pip install colorama requests"

3. XMailer Mode
XMailer has 3 Feature which is :
  - Normal Mode
    In this mode you must specify your own Inbox Combination whic is : From Name, From Mail, Subject, Letter
  - Split Mode
   In this mode you must specify your own combination on txt files that has been included with this package.
   All combination will splited to make more inbox rate.
    - From Mail
     You must specify your from mail list on frommail_list.txt with these sample format:
     noreply@somedomain.com
     support@somedomain.com
    - From Name
     You must specify your from name list on fromname_list.txt with these sample format:
      AppleID
      Apple
      Paypal
      Paypal Team
    - Letter
      You must specify your letter on letter_list.txt with these sample format:
      specialletter.html
      apple.html
      letter.html
    - Subject
      You must specify your subject on subject_list.txt with these sample format:
      Your AppleID has been locked due to unsual login.
      Your account will be limited until we hear from you
   - Auto Make Inbox Combination
      XMailer has a feature that allow you to bruteforcing mailbox filter using
      randomized inbox combination from list file. to use this mode you must
      specify From Name list on frommail_list.txt and Letter List on letter_list.txt
      and Subject List on subject_list.txt. and you must full fill username_list.txt
      and domain_list.txt. this list file for generating from mail. for example:
      we have a from mail address like this:
      noreply@somedomain.com
      from that frommail we can conclude that frommail has "noreply" username random
      "somedomain.com" domain.
      that all list file will be mixed one by one and send it to the desired address.
      so it will take some time to send if you have many list.
      
      
Keep this tool still free by donating, hilmiazizi19@gmail.com
