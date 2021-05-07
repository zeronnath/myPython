#! /usr/bin/env python3
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
import webbrowser
from time import sleep

url = input('https://apply.42seoul.kr/users/zeronnath_at_gmail-com/introductions_users')
chrome_path='C://Program Files (x86)//Google//Chrome//Application//chrome.exe %s'
fox='C://Program Files//Mozilla Firefox//firefox.exe %s'
opera='C://Users//Thuban//AppData//Local//Programs//Opera//launcher.exe %s'
for i in range(2) :
    print("refreshing...")
    #webbrowser.open(url, new=0)
    webbrowser.get(chrome_path).open(url, new=2)
    webbrowser.get(fox).open(url, new=2)
    webbrowser.get(opera).open(url, new=2)
    sleep(1)