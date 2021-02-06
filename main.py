import json, os, requests

url='https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama='
logo="""
 ╭━<━━╮    ╭━━━━━━━━━━━━━━━╮
 ┃╭╮╭╮┃    │ zodiak finder │
┗┫┏━━┓┣┛   ╰━━━━━━━━━━━━━━━╯
 ┃╰━━╯┃   /  Coder : Tegar Dev
 ╰┳━━┳╯
  ┛  ┗        [ Dunia Kode ]
"""
def res():
    req=requests.get(url+nama+'&tanggal='+lahir)
    jeson=json.loads(req.text)
    data=jeson['data']
    print(40*'=')
    print('Nama: '+data['nama'])
    print('Umur: '+data['usia'])
    print('Hari Kelahiran: '+data['lahir'])
    print('Ulang Tahun: '+data['ultah'])
    print('Zodiak: '+data['zodiak'])


if __name__=='__main__':
    os.system('clear')
    print(logo)
    print(40*'=')
    nama=input('nama: ')
    lahir=input('tanggal lahir(ex.:11 05 2004)\ntanggal: ').replace(' ', '-')
    res()