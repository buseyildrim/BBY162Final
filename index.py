from tkinter import *
import tkinter.messagebox

class eserlerim:

    def __init__(self,anasayfa):
        self.anasayfa = anasayfa
        anasayfa.title("Mini Kütüphane")
        anasayfa.configure(background="white")

        self.eserleri_listele = Button(anasayfa, text="Eserleri Listele",bg="orange",fg="white",cursor="star",font="bold", command=self.eserleri_listele)
        self.eserleri_listele.grid(row="1")

        self.eser_ekle = Button(anasayfa, text="Eser Ekle", bg="purple",fg="white",cursor="heart",font="bold",command = self.eser_ekle)
        self.eser_ekle.grid(row="2")

        self.eser_ara = Button(anasayfa, text="Eser Ara", bg="blue",fg="white",cursor="star",font="bold",command=self.eser_ara)
        self.eser_ara.grid(row="3")


        self.cikis = Button(anasayfa, text ="Çıkış", command=exit, fg="black", bg="white",cursor="man")
        self.cikis.grid(row="4")


    def eser_ekle(self):
        global kitap_adi, yazar_adi, yayin_yili, pencere1
        pencere1 = Tk()
        baslik1 = pencere1.title("Eser Kayıt Penceresi")
        pencere1.configure(background="purple")

        kitap_adi = Entry(pencere1, width=27)
        kitap_adi.grid(column=2, row=3)
        yazar_adi = Entry(pencere1, width=27)
        yazar_adi.grid(column=2, row=4)
        yayin_yili = Entry(pencere1, width=27)
        yayin_yili.grid(column=2, row=8)
        self.kaydet = Button(pencere1, text="Kaydet", command=self.eser_kaydet, fg="purple", bg="white")
        self.kaydet.grid(column=1, row=9)

        self.cıkıs = Button(pencere1, text="Kapat", command=pencere1.destroy, fg="purple", bg="white", cursor="arrow")
        self.cıkıs.grid(column=3, row=9)
        Label(pencere1, bg="purple", fg="white", text=' ').grid(column=1, row=1)
        Label(pencere1, bg="purple", fg="white", text='Eser Adı: ').grid(column=1, row=3)
        Label(pencere1, bg="purple", fg="white", text='Yazar Adı: ').grid(column=1, row=4)
        Label(pencere1, bg="purple", fg="white", text='Yayın Yılı :').grid(column=1, row=8)

    def eser_kaydet(self):
        kayit_sis = str((kitap_adi.get() + "***" + yazar_adi.get() + "***" + yayin_yili.get()) + "\n")
        dosya = open("eserler.txt", "a")
        for i in kayit_sis:
            dosya.write(i)
        dosya.close()
        tkinter.messagebox.showinfo('Mesaj', 'Eser Başarıyla Eklendi..')
        command = pencere1.destroy()

    def eserleri_listele(self):
        pencere2 = Tk()
        baslik2 = pencere2.title("Kayıtlı Eserler")
        pencere2.configure(background="orange")
        file = open("eserler.txt")
        data = file.read()
        file.close()

        eser_liste = Label(pencere2, text=data, fg="white", bg="orange")
        eser_liste.pack()

        self.cıkıs = Button(pencere2, text="Kapat", command=pencere2.destroy, fg="orange", bg="white", cursor="star", font="bold")
        self.cıkıs.pack()


    def eser_ara(self):
        pencere3 = Tk()
        baslık4 = pencere3.title("Eser arama penceresi")
        pencere3.configure(background="blue")

        def kitap():
            pencere4 = Tk()
            baslik2 = pencere4.title("Aranılan Sonuç")
            pencere4.configure(background="blue")
            dosya = open("eserler.txt", "r")
            veri = dosya.readlines()
            dosya = open("eserler.txt")
            aranan = input("Aramak istediğiniz eserin ismini buraya giriniz!!: ")
            aranan = aranan.capitalize()
            aranan_varmi = dosya.read().find(aranan)


            if aranan_varmi != -1:
               print("Tebrikler! Aradığınız eser mecut.")
            else:
                print("Malesef! Aranılan eser bulunamadı.")
            dosya.close()

        self.labelKitap=Label(pencere3,bg="blue",fg="white",text="Eser İsmi ile Arama ")
        self.labelKitap.grid(row=0,column=0)
        self.butonKitap=Button(pencere3,text="onay",bg="white",fg="blue",cursor="star",font="bold",command=kitap)
        self.butonKitap.grid(row=0,column=2)


root = Tk()
yeniPencere = eserlerim(root)
root.mainloop()
