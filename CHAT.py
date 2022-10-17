#!/usr/bin/python
#coding=utf-8

import os
import re
import random

os.system('clear')

sapaan = ["hai juga","hai juga yang di sana"]
respon = ["sebenarnya gua juga udah lama suka sama kamu gua mau kok jadi pacar kamu","maaf ya gua udah punya pacar ","gak mau kamu jelek"]
ucapan = ["waalaikumsalam"]
ketawa = ["awokawok","muehehe"]
xxx = ["sama sama"]
xxxx = ["silahkan"]
texs = ['"Kamu laiknya karya seni. Tidak semua orang akan mengerti dirimu, tetapi orang-orang yang mengerti, tidak akan pernah melupakanmu."','"Orang yang tak pernah membuat kesalahan adalah orang yang tidak pernah berbuat apa-apa." - Norman Edwin','"Belajarlah dari kesalahan orang lain. Anda tak dapat hidup cukup lama untuk melakukan semua kesalahan itu sendiri." - Martin Vanbee','"Belajar memang melelahkan, namun akan lebih melelahkan lagi bila saat ini kamu tidak belajar."','"Diam adalah lebih baik daripada mengucapkan kata-kata yang tanpa makna." - Pythagoraz','"Jika Anda takut gagal, Anda tidak pantas untuk sukses!" - Charles Barkley','"Ingin menjadi orang lain adalah tindakan untuk menyia-nyiakan dirimu sendiri." - Kurt Cobain','"Jika kamu mencari satu orang yang akan mengubah hidupmu, lihatlah di cermin."','"Terkadang kita diuji bukan untuk menunjukkan kelemahan kita, tetapi untuk menemukan kekuatan kita."','Jangan pernah menyerah ketika kamu masih mampu berusaha lagi. Tidak ada kata berakhir sampai kamu berhenti mencoba','"Belajar bukan hanya mengetahui apa yang harus dilakukan, tapi melakukan apa yang sudah kita ketahui."','"Sukses adalah sebuah perjalanan, bukan sebuah tujuan. Usaha sering lebih penting daripada hasilnya."','"Kegagalan adalah kunci kesuksesan. Setiap kesalahan mengajarkan kita sesuatu."','"Kamu tidak bisa menyenangkan semua orang, dan kamu tidak bisa membuat semua orang menyukaimu," Katie Couric.','"Lakukan satu hal setiap hari yang membuatmu takut," Eleanor Roosevelt.','"Ingat, tidak ada yang bisa membuat Anda merasa rendah diri tanpa persetujuan Anda," Eleanor Roosevelt.','"Jika Anda menginginkan pelangi, Anda harus tahan dengan hujan," Dolly Parton.','"Hidup bukanlah tentang menemukan diri Anda sendiri. Hidup adalah tentang menciptakan diri Anda sendiri," George Bernard Shaw.','"Semua impian kita bisa menjadi kenyataan jika kita memiliki keberanian untuk mengejarnya," Walt Disney.','"Seseorang yang luar biasa itu sederhana dalam ucapannya, tetapi hebat dalam tindakannya."','" Jangan menjelaskan tentang dirimu kepada siapa pun, karena yang menyukaimu tidak butuh itu. Dan yang membencimu tidak percaya itu."','" Untuk mendapatkan apa yang diinginkan, kau harus bersabar dengan apa yang kau benci."','Balas dendam terbaik adalah menjadikan dirimu lebih baik."','"Jangan takut akan perubahan. Kita mungkin kehilangan sesuatu yang baik, namun kita akan peroleh sesuatu yang lebih baik lagi."','" Jika diammu bijak, maka diamlah. Apabila diammu diinjak, maka bicaralah supaya tak ada lagi orang yang menginjak dan meremehkan dirimu."','"Kegagalan dibuat hanya oleh mereka yang gagal untuk berani, bukan oleh mereka yang berani gagal."','"Janganlah pernah menyerah ketika kamu masih mampu berusaha lagi. Tidak ada kata berakhir sampai kamu berhenti mencoba." - Brian Dyson','"Lakukan apa yang harus kamu lakukan sampai kamu dapat melakukan apa yang ingin kamu lakukan." - Oprah Winfrey']
nama = ["tiara","amel","fitriani","karina","adelia","novita","nabila","azahra","rahma","nurul"]
xxxxx = ["gua lagi duduk","gua lagi rebahan","gua lagi chatan sama kamu","gua lagi gak ngapa ngapain","gua lagi mikirin kamu"]
yakin = ["beneran ngapain juga gua bohong","seriusan ngapain juga gua bohong"]

while True:
    x = input("\33[1;97m(+) ketik pesan : \33[1;96m")
    if re.findall(r'kamu mau gak', x):
        print("\n\33[1;97m(+) bot chat : \33[1;96m"+random.choice(respon), "\n")
    elif re.findall(r'assalamualaikum', x):
        print("\n\33[1;97m(+) bot chat : \33[1;96m"+random.choice(ucapan), "\n")
    elif re.findall(r'hai|hey|hay|hello', x):
        print("\n\33[1;97m(+) bot chat : \33[1;96m"+random.choice(sapaan), "\n")
    elif re.findall(r'hehe|haha|hihihi|xixixi|muehehe|awokawok', x):
        print("\n\33[1;97m(+) bot chat : \33[1;96m"+random.choice(ketawa), "\n")
    elif re.findall(r'makasih|terimakasih|terima kasih|thanks|thanks you', x):
        print("\n\33[1;97m(+) bot chat : \33[1;96m"+random.choice(xxx), "\n")
    elif re.findall(r'gua mau ngomong', x):
        print("\n\33[1;97m(+) bot chat : \33[1;96m"+random.choice(xxxx), "\n")
    elif re.findall(r'motivasi', x):
        print("\n\33[1;97m(+) bot chat : \33[1;92m"+random.choice(texs), "\n")
    elif re.findall(r'nama kamu siapa|nama mu siapa|kamu siapa', x):
        print("\n\33[1;97m(+) bot chat : \33[1;96mnama saya "+random.choice(nama), "\n")
    elif re.findall(r'kamu lagi ngapain|lagi ngapain|lagi apa', x):
        print("\n\33[1;97m(+) bot chat : \33[1;96m"+random.choice(xxxxx), "\n")
    elif re.findall(r'beneran|bener|seriusan|serius', x):
        print("\n\33[1;97m(+) bot chat : \33[1;96m"+random.choice(yakin), "\n")
    else:
        print("\n\33[1;97m(+) bot chat : \33[1;96msaya tidak mengerti !!!\n")