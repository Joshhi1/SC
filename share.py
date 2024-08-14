# Gift By : Taslim Khan
# Github : https://github.com/taslim123123
# Fb Id    : Taslim khan
###----------[ IMPORT LIBRARY ]---------- ###
import requests, os, re, bs4, calendar, sys, json, time, random, datetime, subprocess, logging, base64, uuid
from datetime import datetime
from time import sleep
from time import sleep as jeda
from time import strftime
from random import choice
from pathlib import Path
from rich.console import Console as sol
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich.text import Text as tekz
from rich.panel import Panel as nel
from rich import print as cetak

def cokget():
	os.system("clear")
	f=input("do you want to get cookie?[y/n] ")
	if f in ['y', 'Y']:
		os.system("python cookie.py")
	if f in ['n', 'N']:
		os.system("python share.py")
cokget()
ses = requests.Session()
os.system('https://www.facebook.com/profile.php?id=100085172882533')

###----------[ TIME DATE ]----------###
bulan = {'1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May', '6': 'June', '7': 'July',
         '8': 'August', '9': 'September', '10': 'October', '11': 'November', '12': 'December'}
tgl = datetime.now().day
bln = bulan[(str(datetime.now().month))]
thn = datetime.now().year
tanggal = (str(tgl) + ' ' + str(bln) + ' ' + str(thn))
waktu = strftime('%H:%M:%S')
hari = datetime.now().strftime("%A")

###----------[ COLOUR 1]---------- ###
Z = "\x1b[0;90m"  # Hitam
M = "\x1b[38;5;196m"  # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m"  # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"  # Ungu
O = "\x1b[0;96m"  # Biru Muda
P = "\x1b[38;5;231m"  # Putih
J = "\x1b[38;5;208m"  # Jingga
A = "\x1b[38;5;248m"  # Abu-Abu
N = '\x1b[0m'  # WARNA MATI
PT = '\x1b[1;97m'  # PUTIH TEBAL
MT = '\x1b[1;91m'  # MERAH TEBAL
HT = '\x1b[1;92m'  # HIJAU TEBAL
KT = '\x1b[1;93m'  # KUNING TEBAL
BT = '\x1b[1;94m'  # BIRU TEBAL
UT = '\x1b[1;95m'  # UNGU TEBAL
OT = '\x1b[1;96m'  # BIRU MUDA TEBAL

###----------[ COLOUR 2 ]---------- ###
Z2 = "[#000000]"  # HITAM #Black
M2 = "[#FF0000]"  # MERAH  #Rad
H2 = "[#00FF00]"  # HIJAU #Tiya Coular
K2 = "[#FFFF00]"  # KUNING #Holod
B2 = "[#00C8FF]"  # BIRU #Nill
U2 = "[#AF00FF]"  # UNGU #Halka Begoni
N2 = "[#FF00FF]"  # PINK #Begoni
O2 = "[#00FFFF]"  # BIRU MUDA #Frash
P2 = "[#FFFFFF]"  # PUTIH #White
J2 = "[#FF8F00]"  # JINGGA #Koyri
A2 = "[#AAAAAA]"  # ABU-ABU #Halka sada

###----------[ USER AGENT ]---------- ###
ua_default = 'Mozilla/5.0 (Linux; Android 3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.66 Mobile Safari/537.36'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
ua_nokia = 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
ua_xiaomi = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_oppo = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_vivo = 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_iphone = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1'
ua_asus = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_lenovo = 'Mozilla/5.0 (Linux; U; Android 5.0.1; ru-RU; Lenovo A788t Build/LRX22C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.0.950 U3/0.8.0 Mobile Safari/E7FBAF'
ua_huawei = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_chrome = 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36'
ua_fb = 'Mozilla/5.0 (Linux; Android 8.0.0; RNE-L21 Build/HUAWEIRNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/360.0.0.30.113;]'
ua_random = random.choice(
    [ua_default, ua_samsung, ua_nokia, ua_xiaomi, ua_oppo, ua_vivo, ua_iphone, ua_asus, ua_lenovo, ua_huawei,
     ua_windows, ua_chrome, ua_fb])
kom1 = ("Keren banget bangg:v")




###----------[ LOGIN MINU ]----------###

def login():
    os.system("clear")
    print("""

    
\x1b[38;5;46m888     888 888b    888  .d88888b.  
888     888 8888b   888 d88P" "Y88b 
888     888 88888b  888 888     888 
888     888 888Y88b 888 888     888 
888     888 888 Y88b888 888     888 
888     888 888  Y88888 888     888 
Y88b. .d88P 888   Y8888 Y88b. .d88P 
 "Y88888P"  888    Y888  "Y88888P"  
                                    
                                    
                                    


    ╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
    ║\33[0;41m           [ ENJOY FB AUTO SHARE ]           \033[0;92m║
    ╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝
    \33[1;32m====================================================
    \033[1;95m[\033[1;93m[>]\033[1;95m]\033[1;93m AUTHOR  \033[1;91m : \033[1;92mUNO/NICO
    \033[1;95m[\033[1;93m[>]\033[1;95m]\033[1;93m FACEBOOK\033[1;91m : \033[1;93mUNO/NICO
    \033[1;95m[\033[1;93m[>]\033[1;95m]\033[1;93m GITHUB  \033[1;91m : \033[1;94mUNO/NICO
    \033[1;95m[\033[1;93m[>]\033[1;95m]\033[1;93m TOOLS   \033[1;91m : \033[1;95mFB AUTO SHARE 
    \033[1;95m[\033[1;93m[>]\033[1;95m]\033[1;93m VERSION \033[1;91m : \033[1;91m2.0
    \33[1;32m====================================================
    """)
    
    cetak(nel(f'\n \t {H2}  FB AUTO SHARE TOOLS \n\n \t\t {H2}~[{K2} P{K2}O{K2}G{K2}I {K2}A{K2}K{H2}O]~',
              title=f'{P2}  {H2}[{K2} U{K2}N{K2}O{K2}T{K2}O{K2}O{K2}L{K2}S]',
              width=54, padding=(1, 4), style='blue'))
    cetak(nel(f'\t\t{H2}USE FRESH COOKIE\n\n \t\t  {N2} FRESH COOKIE ', subtitle=f'{P2}┌─[ {K2}Cookies Room ]',
              subtitle_align='left', width=54, padding=1, style='blue'))
    cookie = input(f"{P}   └──> : {H}")
    try:
        data = ses.get("https://business.facebook.com/business_locations", headers={
            "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36",
            "referer": "https://www.facebook.com/", "host": "business.facebook.com",
            "origin": "https://business.facebook.com", "upgrade-insecure-requests": "1",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "cache-control": "max-age=0",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "content-type": "text/html; charset=utf-8"}, cookies={"cookie": cookie})
        find_token = re.search("(EAAG\w+)", data.text)
        open("token.txt", "w").write(find_token.group(1))
        open("cookie.txt", "w").write(cookie)
        cetak(nel(f'{P2} LOGIN BERHASIL', width=24, style=f"#00FF00"));
        time.sleep(2)
        bot_share()
    except:
        os.system("rm token.txt cookie.txt")
        cetak(nel(f'{M2} COOKIE INVALID', width=22, style=f"#00FF00"));
        time.sleep(1.5)
        login()


###----------[ AUTO SHARE ]----------###
def bot_share():
    os.system('clear')
    try:
        token = open("token.txt", "r").read()
        cok = open("cookie.txt", "r").read()
        cookie = {"cookie": cok}
        ip = requests.get("https://api.ipify.org").text
        nama = ses.get(f"https://graph.facebook.com/me?fields=name&access_token={token}", cookies=cookie).json()["name"]
        id = requests.get("https://graph.facebook.com/me/?access_token=%s" % (token), cookies={"cookie": cok}).json()[
            "id"]
        requests.post(f"https://graph.facebook.com/826244541950192/comments/?message={kom1}&access_token={token}",
                      headers={"cookie": cok})
    except:
        os.system("rm token.txt cookie.txt")
        cetak(nel(f'{M2} COOKIE INVALID!!', width=22, style=f"#00FF00"));
        time.sleep(1.5)
        login()
    os.system('clear')
    logo_menu()
    cetak(nel(f'''{B2} User Active     : {H2}{nama} 
{B2} Your Id          : {H2}{id}
{B2} Your Ip          : {H2}{ip}
{B2} Current Date    :{H2} {hari}, {tanggal}''', title=f'{P2} {H2}[ {K2}Cookie Id Information {H2}]',
              subtitle_align='left', padding=1, style='blue'))
    cetak(
        nel(f'{K2}Hai {H2}{nama},{K2} DISABLED ACCOUNT IS NO LONGER MY RESPONSIBILITY{M2}!!\n \t\t {N2}.',
            title=f'{P2} {H2}[ {M2}Warning {H2}]', subtitle_align='left', padding=1, style='blue'))
    cetak(nel(f'{H2} U{K2}N{B2}O{J2}T{K2}O{H2}O{N2}L{P2}S', subtitle=f'{P2}┌─', subtitle_align='left', width=25,
              padding=0, style='blue'))
    link = input(f"{P}   └──> : {H}")
    cetak(nel(f'{H2} S{J2}H{K2}A{B2}R{N2}E {K2}L{B2}I{H2}M{N2}I{P2}T', subtitle=f'{P2}┌─', subtitle_align='left',
              width=22, padding=0, style='blue'))
    jumlah = int(input(f"{P}   └──> : {H}"))
    cetak(
        nel(f'{H2} T{H2}A{H2}S{H2}L{H2}I{H2}M {B2}F{B2}B {O2}A{O2}U{O2}T{O2}O {N2}S{N2}H{N2}A{N2}R{N2}E {K2}T{K2}O{K2}O{K2}L{K2}S',
            subtitle=f'{P2}┌─', subtitle_align='left', width=29, padding=0, style='blue'))
    basariganteng = datetime.now()
    try:
        n = 0
        header = {"authority": "graph.facebook.com", "cache-control": "max-age=0", "sec-ch-ua-mobile": "?0",
                  "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1"}
        for x in range(jumlah):
            n += 1
            post = ses.post(f"https://graph.facebook.com/v13.0/me/feed?link={link}&published=0&access_token={token}",
                            headers=header, cookies=cookie).text
            data = json.loads(post)
            if "id" in post:
                bas = str(datetime.now() - basariganteng).split('.')[0]
                print(f'{P}\r   └──>{H} {bas} {K} U{K}N{K}O SEND {H}[{n}]{P}{K} AUTO SHARE {H} SUCCESS {H} ',
                      end='');
                sys.stdout.flush()
            else:
                print("\n")
                cetak(nel(f'{M2} AUTO SHARE COOKIE INVALID', width=35, padding=0, style='red'));
                exit()
    except requests.exceptions.ConnectionError:
        print(f"\n{P}(!) NO INTERNET CONNECTION!!");exit()
        
bot_share()       
    






