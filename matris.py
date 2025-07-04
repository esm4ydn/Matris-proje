import tkinter as tk
from tkinter import messagebox
from functools import reduce

def k_kucuk(k, lst):
    lst.sort()
    return lst[k - 1]


def bul_k_kucuk():
    try:
        k = int(entry_k.get())
        elemanlar = entry_liste.get()
        lst = list(map(int, elemanlar.split(',')))
        if k <= 0 or k > len(lst):
            messagebox.showerror("Hata", "Geçersiz k değeri girdiniz. Lütfen tekrar deneyin.")
        else:
            sonuc = k_kucuk(k, lst)
            entry_sonuc.delete(0, tk.END)
            entry_sonuc.insert(0, f"{k}. en küçük eleman: {sonuc}")
    except ValueError:
        messagebox.showerror("Hata", "Geçersiz değer girdiniz. Lütfen tekrar deneyin.")


def en_yakin_cift(hedefSayi, sayilar):
    sayilar.sort()
    en_yakin_cift = None
    min_fark = float('inf')

    sol = 0
    sag = len(sayilar) - 1

    while sol < sag:
        mevcut_toplam = sayilar[sol] + sayilar[sag]
        fark = abs(hedefSayi - mevcut_toplam)

        if fark < min_fark:
            min_fark = fark
            en_yakin_cift = (sayilar[sol], sayilar[sag])

        if mevcut_toplam < hedefSayi:
            sol += 1
        else:
            sag -= 1

    return en_yakin_cift


def yakın_cift_sonuc():
    hedef = int(entry_hedef.get())
    sayilar = list(map(int, entry_sayilar.get().split(",")))
    en_yakin_cift = en_yakin_cift(hedef, sayilar)
    sonuc_etiketi.config(
        text=f"{sayilar} listesindeki hedef sayıya en yakın çift: {en_yakin_cift} (Toplam: {sum(en_yakin_cift)})")


def tekrar_eden_elemanlar(liste):
    return list(set([x for x in liste if liste.count(x) > 1]))


def tekrar_edeni_bul():
    try:
        elemanlar = entry_list.get()
        liste = list(map(int, elemanlar.split(',')))
        sonuc = tekrar_eden_elemanlar(liste)
        messagebox.showinfo("Tekrar Eden Elemanlar", f"Tekrar Eden Elemanlar: {sonuc}")
    except ValueError:
        messagebox.showerror("Hata", "Geçersiz değer girdiniz. Lütfen tekrar deneyin.")


def matrix_boyutlari():
    satir_A = int(entry_satir_A.get())
    sutun_A = int(entry_sutun_A.get())
    satir_B = int(entry_satir_B.get())
    sutun_B = int(entry_sutun_B.get())

    if sutun_A != satir_B:
        sonuc_etiketi.config(text="Matris boyutları uyumsuz, çarpım yapılamaz.")
    else:
        matrix_degerleri_gir(satir_A, sutun_A, satir_B, sutun_B)


def matrix_degerleri_gir(satir_A, sutun_A, satir_B, sutun_B):
    entry_satir_A.grid_forget()
    entry_sutun_A.grid_forget()
    entry_satir_B.grid_forget()
    entry_sutun_B.grid_forget()
    satir_A_etiketi.grid_forget()
    sutun_A_etiketi.grid_forget()
    satir_B_etiketi.grid_forget()
    sutun_B_etiketi.grid_forget()
    hesapla_butonu.grid_forget()

    A_etiketi = tk.Label(pencere, text="Matris A Değerleri")
    A_etiketi.grid(row=0, column=0, padx=10, pady=10)
    B_etiketi = tk.Label(pencere, text="Matris B Değerleri")
    B_etiketi.grid(row=0, column=sutun_A + 2, padx=10, pady=10)

    entry_A = []
    entry_B = []

    for i in range(satir_A):
        satir_A_degerleri = []
        for j in range(sutun_A):
            entry = tk.Entry(pencere)
            entry.grid(row=i + 1, column=j, padx=5, pady=5)
            satir_A_degerleri.append(entry)
        entry_A.append(satir_A_degerleri)

    for i in range(satir_B):
        satir_B_degerleri = []
        for j in range(sutun_B):
            entry = tk.Entry(pencere)
            entry.grid(row=i + 1, column=sutun_A + 2 + j, padx=5, pady=5)
            satir_B_degerleri.append(entry)
        entry_B.append(satir_B_degerleri)

    hesapla_butonu_son = tk.Button(pencere, text="Hesapla", command=lambda: sonucu_hesapla(entry_A, entry_B))
    hesapla_butonu_son.grid(row=max(satir_A, satir_B) + 1, column=0, columnspan=sutun_A + sutun_B + 4, padx=10, pady=10)


def sonucu_hesapla(entry_A, entry_B):
    A = [[int(entry_A[i][j].get()) for j in range(len(entry_A[0]))] for i in range(len(entry_A))]
    B = [[int(entry_B[i][j].get()) for j in range(len(entry_B[0]))] for i in range(len(entry_B))]
    sonuc = [[sum(a * b for a, b in zip(satir_A, sutun_B)) for sutun_B in zip(*B)] for satir_A in A]
    sonuc_etiketi.config(text=str(sonuc))

def kelime_tekrari(dosya_yolu):
    try:
        with open(dosya_yolu, 'r') as dosya:
            kelimeler = dosya.read().split()
    except FileNotFoundError:
        return "Dosya bulunamadı."
    kelime_sayilari = reduce(
        lambda sayilar, kelime: {**sayilar, kelime: sayilar.get(kelime, 0) + 1},
        map(str.lower, kelimeler),
        {}
    )
    return kelime_sayilari

def hesapla():
    dosya_yolu = dosya_girdisi.get()
    sonuc = kelime_tekrari(dosya_yolu)
    sonuc_metni = ""
    for kelime, sayi in sonuc.items():
        sonuc_metni += f"{kelime}={sayi}\n"
    sonuc_etiketi.config(text=sonuc_metni)

def en_kucuk_degeri_bul(liste, index=0, min_deger=float('inf')):
    if index < len(liste):
        if liste[index] < min_deger:
            min_deger = liste[index]
        return en_kucuk_degeri_bul(liste, index + 1, min_deger)
    return min_deger


def listeyi_al():
    try:
        liste = list(map(int, entry.get().split(',')))
        en_kucuk = en_kucuk_degeri_bul(liste)
        messagebox.showinfo("Sonuç", f"En küçük değer: {en_kucuk}")
    except ValueError:
        messagebox.showerror("Hata", "Geçersiz giriş. Lütfen sayıları virgülle ayırarak girin")


def karekok_hesapla(N, x0, tol=1e-10, maxiter=1000):
    def yardimci(tahmin):
        yeni_tahmin = 0.5 * (tahmin + N / tahmin)
        hata = abs(yeni_tahmin - tahmin)
        if hata < tol:
            return yeni_tahmin
        return yardimci(yeni_tahmin)

    return yardimci(x0)


def hesaplama_tamamla():
    try:
        N = float(entry_N.get())
        x0 = float(entry_x0.get())
        sonuc = karekok_hesapla(N, x0)
        sonuc_etiket.config(text=f"Karekök: {sonuc:.10f}")
    except ValueError:
        messagebox.showerror("Hata", "Geçersiz giriş!")

def eb_ortak_bolen(a, b):
    if b == 0:
        return a
    else:
        return eb_ortak_bolen(b, a % b)

def hesapla():
    sayi1 = int(girdi1.get())
    sayi2 = int(girdi2.get())
    sonuc = eb_ortak_bolen(sayi1, sayi2)
    sonuc_etiketi.config(text="En büyük ortak bölen: " + str(sonuc))

def asal_veya_degil(sayi, bolen=2):
    if sayi < 2:
        return False
    if sayi == 2:
        return True
    if sayi % bolen == 0:
        return False
    if bolen * bolen > sayi:
        return True
    return asal_veya_degil(sayi, bolen + 1)

def hesapla():
    sayi = int(veri.get())
    if asal_veya_degil(sayi):
        sonuc_etiketi.config(text="True")
    else:
        sonuc_etiketi.config(text="False")

sonuclar = []

def hizlandirici(n, k, fib_k, fib_k_1):
    global sonuclar
    sonuclar.append(f"{n} {k} {fib_k} {fib_k_1}")
    if k == n:
        return fib_k
    else:
        return hizlandirici(n, k + 1, fib_k + fib_k_1, fib_k)

def fibonacci_hesapla():
    global sonuclar, girdi_sayi
    sayi = int(girdi_sayi.get())
    sonuclar = []
    sonuc = hizlandirici(sayi, 1, 1, 0)
    if sonuclar:
        sonuclar.append(f"{sayi} {sayi} {sonuc} {sonuclar[-1].split()[2]}")
        sonuc_etiketi0.config(text="\n".join(sonuclar))

ana_menu = tk.Tk()
ana_menu.title("Program")
ana_menu.geometry("800x750")
ana_menu.configure(bg="light blue")
karsıla = tk.Label(ana_menu, text="Hoş geldiniz!",bg="light blue",fg="purple", font=("Arial", 16))
karsıla.pack(pady=5)

secim = tk.Label(ana_menu,text="Yapmak İstediğiniz İşlemi Seçiniz: ",bg="light blue",fg="black", font=("Arial", 14))
secim.pack(pady=5)

def buton_1():
    button = tk.Button(ana_menu, text="K'nıncı En Küçük Elemanı Bulma", command=knin_deger_bul_pencere_1, fg="purple",
                       bg="pink", width=40, height=2, font="Times 12 bold")
    button.pack(pady=10)

def buton_2():
    button = tk.Button(ana_menu, text="En Yakın Çift Sayıyı Bulma", command=yakin_cift_pencere_2, fg="black",
                       bg="pink", width=40, height=2, font="Times 12 bold")
    button.pack(pady=2)

def buton_3():
    button = tk.Button(ana_menu, text="Tekrar Eden Elemanları Bulma", command=tekrar_eden_bul_pencere_3, fg="purple",
                       bg="pink", width=40, height=2, font="Times 12 bold")
    button.pack(pady=10)

def buton_4():
    button = tk.Button(ana_menu, text="Matris Çarpımı", command=matrix_carp_pencere_4, fg="black",
                       bg="pink", width=40, height=2, font="Times 12 bold")
    button.pack(pady=2)

def buton_5():
    button = tk.Button(ana_menu, text="Bir Text Dosyasındaki Kelimelerin Frekansını Bulma",
             command=kelime_say_pencere_5, fg="purple", bg="pink", width=40, height=2, font="Times 12 bold")
    button.pack(pady=10)

def buton_6():
    button = tk.Button(ana_menu, text="Liste İçinde En Küçük Değeri Bulma", command=en_kucuk_bul_pencere_6, fg="black",
                       bg="pink", width=40, height=2, font="Times 12 bold")
    button.pack(pady=2)

def buton_7():
    button = tk.Button(ana_menu, text="Tekrarlamalı Yöntemle Karekök Fonksiyonu Alma", command=karekok_al_pencere_7,
                       fg="purple",bg="pink", width=40, height=2, font="Times 12 bold")
    button.pack(pady=10)

def buton_8():
    button = tk.Button(ana_menu, text="En Büyük Ortak Bölen Bulma", command=ebob_hesabı_pencere_8,
                       fg="black",bg="pink", width=40, height=2, font="Times 12 bold")
    button.pack(pady=2)

def buton_9():
    button = tk.Button(ana_menu, text="Asallık Sayı Kontrolü", command=asal_pencere_9,fg="purple",bg="pink", width=40,
                       height=2, font="Times 12 bold")
    button.pack(pady=10)

def buton_10():
    button = tk.Button(ana_menu, text="Hızlı Fibonacci Hesabı", command=fibonacci_hesabı_pencere10 ,fg="black",bg="pink",
                       width=40,  height=2, font="Times 12 bold")
    button.pack(pady=2)

def knin_deger_bul_pencere_1():
    pencere_1 = tk.Tk()
    pencere_1.title("K'nıncı En Küçük Elemanı Bulma")
    pencere_1.geometry("400x300")
    pencere_1.configure(bg="pink")
    label_k = tk.Label(pencere_1, text="k değerini girin:")
    label_k.pack(pady=10)

    global entry_k, entry_liste, entry_sonuc

    entry_k = tk.Entry(pencere_1)
    entry_k.pack(pady=10)

    label_liste = tk.Label(pencere_1, text="Listeyi virgülle ayırarak girin:")
    label_liste.pack(pady=10)

    entry_liste = tk.Entry(pencere_1)
    entry_liste.pack(pady=10)

    button_hesapla = tk.Button(pencere_1, text="k’nıncı En Küçük Elemanı Bulma", command=bul_k_kucuk)
    button_hesapla.pack(pady=10)

    label_sonuc = tk.Label(pencere_1, text="Sonuç:")
    label_sonuc.pack(pady=10)

    entry_sonuc = tk.Entry(pencere_1)
    entry_sonuc.pack(pady=10)


def yakin_cift_pencere_2():
    pencere_2 = tk.Tk()
    pencere_2.title("En Yakın Çift Sayıyı Bulma")
    pencere_2.geometry("400x300")
    pencere_2.configure(bg="light blue")

    label_hedef = tk.Label(pencere_2, text="Hedef Sayı:")
    label_hedef.pack(pady=10)
    entry_hedef = tk.Entry(pencere_2)
    entry_hedef.pack(pady=10)

    label_sayilar = tk.Label(pencere_2, text="Sayılar (Virgülle Ayrılmış):")
    label_sayilar.pack(pady=10)
    entry_sayilar = tk.Entry(pencere_2)
    entry_sayilar.pack(pady=10)

    button = tk.Button(pencere_2, text="En Yakın Çifti Bul", command=yakin_cift_sonuc)
    button.pack(pady=10)


def tekrar_eden_bul_pencere_3():
    pencere_3 = tk.Tk()
    pencere_3.title("Tekrar Eden Elemanları Bulma")
    pencere_3.geometry("400x300")
    pencere_3.configure(bg="pink")

    label_liste = tk.Label(pencere_3, text="Listeyi virgülle ayırarak girin:")
    label_liste.pack(pady=10)

    entry_liste = tk.Entry(pencere_3)
    entry_liste.pack(pady=10)

    button_bul = tk.Button(pencere_3, text="Tekrar Eden Elemanları Bul", command=tekrar_edeni_bul)
    button_bul.pack(pady=10)


def matrix_carp_pencere_4():
    pencere_4 = tk.Tk()
    pencere_4.title("Matris Çarpımı")
    pencere_4.geometry("800x400")
    pencere_4.configure(bg="light blue")

    label_satir_A = tk.Label(pencere_4, text="A~Matrisinin Satır Sayısı:")
    label_satir_A.grid(row=0, column=0, padx=10, pady=10)
    entry_satir_A = tk.Entry(pencere_4)
    entry_satir_A.grid(row=0, column=1, padx=10, pady=10)

    label_sutun_A = tk.Label(pencere_4, text="A~Matrisinin Sütun Sayısı:")
    label_sutun_A.grid(row=1, column=0, padx=10, pady=10)
    entry_sutun_A = tk.Entry(pencere_4)
    entry_sutun_A.grid(row=1, column=1, padx=10, pady=10)

    label_satir_B = tk.Label(pencere_4, text="B~Matrisinin Satır Sayısı:")
    label_satir_B.grid(row=0, column=2, padx=10, pady=10)
    entry_satir_B = tk.Entry(pencere_4)
    entry_satir_B.grid(row=0, column=3, padx=10, pady=10)

    label_sutun_B = tk.Label(pencere_4, text="B~Matrisinin Sütun Sayısı:")
    label_sutun_B.grid(row=1, column=2, padx=10, pady=10)
    entry_sutun_B = tk.Entry(pencere_4)
    entry_sutun_B.grid(row=1, column=3, padx=10, pady=10)

    hesapla_butonu = tk.Button(pencere_4, text="Devam Et", command=matris_boyutlarini_hesapla)
    hesapla_butonu.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

    sonuc_etiketi = tk.Label(pencere_4, text="")
    sonuc_etiketi.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

def kelime_say_pencere_5():
    pencere_5 = tk.Tk()
    pencere_5.title("Bir Text Dosyasındaki Kelimelerin Frekansını Bulma")
    pencere_5.geometry("700x800")
    pencere_5.configure(bg="pink")
    etiket = tk.Label(pencere_5,
        text='Lütfen dosya yolunu giriniz (örn: C:\\\\Users\\\\kullanici_adiniz\\\\Masaüstü\\\\dosya.txt): ')
    etiket.pack()

    dosya_girdisi = tk.Entry(pencere_5, width=60, font=("Arial", 12))
    dosya_girdisi.pack(pady=20)

    buton = tk.Button(pencere_5, text="Hesapla", command=hesapla)
    buton.pack()

    sonuc_etiketi = tk.Label(pencere_5, text="",bg="pink", font=("Arial", 12), wraplength=600, justify="left")
    sonuc_etiketi.pack()

    pencere_5.mainloop()

def en_kucuk_bul_pencere_6():
    pencere_6 = tk.Tk()
    pencere_6.title("En Küçük Değeri Bulma")
    pencere_6.geometry("400x300")
    pencere_6.configure(bg="pink")

    giris_etiketi = tk.Label(pencere_6, text="Listeyi virgülle ayırarak giriniz:")
    giris_etiketi.pack()
    giris = tk.Entry(pencere_6)
    giris.pack()

    bul_butonu = tk.Button(pencere_6, text="En Küçük Değeri Bul", command=listeyi_al)
    bul_butonu.pack()

    pencere_6.mainloop()

    for kelime, sayi in sonuc.items():
        print(f"{kelime}={sayi}")

def karekok_al_pencere_7():
    pencere_7 = tk.Tk()
    pencere_7.title("Karekök Hesaplama")
    pencere_7.geometry("400x300")
    pencere_7.configure(bg="light blue")

    etiket_N = tk.Label(pencere_7, text="Sayı (N):")
    etiket_N.pack()
    giris_N = tk.Entry(pencere_7)
    giris_N.pack()

    etiket_x0 = tk.Label(pencere_7, text="Başlangıç tahmini (x0):")
    etiket_x0.pack()
    giris_x0 = tk.Entry(pencere_7)
    giris_x0.pack()

    hesapla_butonu = tk.Button(pencere_7, text="Karekök Hesapla", command=hesaplama_tamamla)
    hesapla_butonu.pack()

    sonuc_etiketi = tk.Label(pencere_7, text="")
    sonuc_etiketi.pack()

    pencere_7.mainloop()

def ebob_hesabı_pencere_8():
    pencere_8 = tk.Tk()
    pencere_8.title("En Büyük Ortak Bölen Bulma")
    pencere_8.geometry("400x300")
    pencere_8.configure(bg="light blue")

    etiket1 = tk.Label(pencere_8, text="Birinci Sayı:", font=("Arial", 10))
    etiket1.pack(pady=5)

    girdi1 = tk.Entry(pencere_8)
    girdi1.pack(pady=5)

    etiket2 = tk.Label(pencere_8, text="İkinci Sayı:", font=("Arial", 10))
    etiket2.pack(pady=5)

    girdi2 = tk.Entry(pencere_8)
    girdi2.pack(pady=5)

    hesapla_dugme = tk.Button(pencere_8, text="Hesapla", command=hesapla)
    hesapla_dugme.pack(pady=5)

    sonuc_etiketi = tk.Label(pencere_8, text="", font=("Arial", 12), bg="light blue")
    sonuc_etiketi.pack()

    pencere_8.mainloop()

def asal_pencere_9():
    global veri, sonuc_etiketi
    pencere_9 = tk.Tk()
    pencere_9.title("Asal Sayı Kontrolü")
    pencere_9.geometry("400x300")
    pencere_9.configure(bg="pink")

    etiket = tk.Label(pencere_9, text="Bir sayı girin:")
    etiket.pack(pady=10)

    veri = tk.Entry(pencere_9)
    veri.pack()

    hesapla_dugme = tk.Button(pencere_9, text="Hesapla", command=hesapla)
    hesapla_dugme.pack(pady=10)

    sonuc_etiketi = tk.Label(pencere_9, text="", bg="pink")
    sonuc_etiketi.pack()

    pencere_9.mainloop()

def fibonacci_hesabı_pencere10():
    global girdi_sayi, sonuc_etiketi0
    pencere_10 = tk.Tk()
    pencere_10.title("Fibonacci Hesaplama")
    pencere_10.geometry("400x300")
    pencere_10.configure(bg="pink")
    etiket = tk.Label(pencere_10, text="Fibonacci serisinde kaçıncı sayıyı hesaplamak istiyorsunuz?")
    etiket.pack(pady=10)

    girdi_sayi = tk.Entry(pencere_10)
    girdi_sayi.pack()

    hesapla_dugme = tk.Button(pencere_10, text="Hesapla", command=fibonacci_hesapla)
    hesapla_dugme.pack(pady=10)

    sonuc_etiketi0 = tk.Label(pencere_10, text="", bg="pink")
    sonuc_etiketi0.pack()

    pencere_10.mainloop()

buton_1()
buton_2()
buton_3()
buton_4()
buton_5()
buton_6()
buton_7()
buton_8()
buton_9()
buton_10()
ana_menu.mainloop()