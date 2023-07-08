import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QLineEdit, QFormLayout, QSplitter, QMessageBox
from PyQt5.QtCore import Qt
class SplitterWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Game Of Thrones")
        self.setFixedWidth(1400)
        self.setFixedHeight(600)
        self.setupUI()
        self.setupDatabase()
#Arayüz oluşturulması
    def setupUI(self):
        cerceve = self.createMainSplitter()
        self.setCentralWidget(cerceve)
        cerceve.setStyleSheet("background: gray")
 #Veri tabanı kurulumu, kontrolü
    def setupDatabase(self):
        self.conn = sqlite3.connect("database.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
#Oluşturulan arayüzün widget'larının eklenmesi
    def createMainSplitter(self):
        cerceve = QSplitter(self)
        cerceve.setOrientation(Qt.Vertical)
        ustwdgt = self.UpperWidget()
        altwdgt = self.LowerSplitter()
        cerceve.addWidget(ustwdgt)
        cerceve.addWidget(altwdgt)
        return cerceve
#Oluşturulan arayüzün üst widget'larının eklenmesi
    def UpperWidget(self):
        ustwdgt = QWidget()
        ustwdgt.setFixedHeight(500) #Pencerenin boyutunun değiştirilmemesi için gerekli kod (uzunluk)
        ustwdgt.setFixedWidth(1400) #Pencerenin boyutunun değiştirilmemesi için gerekli kod (genişlik)
        ustwdgt.setStyleSheet("background-image: url('background.jpg'); background-repeat: no-repeat; background-position: center; ") #üst widget'ın tasarımı
        return ustwdgt
#Oluşturulan arayüzün alt widget'larının eklenmesi
    def LowerSplitter(self):
        altwdgt = QSplitter()
        altwdgt.setSizes([60, 40]) #altwdgt boyutlandırma
        altsolwdgt = QWidget()
        altsolcerceve = QHBoxLayout()
        altsollabel = QLabel("")
        altsollabel.setFixedWidth(1100) #Alt sol label boyutunun sabit kalması için gerekli kod (genişlik)
        altsolcerceve.addWidget(altsollabel)
        altsolwdgt.setLayout(altsolcerceve)
        altsagwdgt = self.LoginFormWidget() #altsagwdgt içerisine loginformwidget fonksiyonunu yerleştirmek için gerekli kod
        altwdgt.addWidget(altsolwdgt)
        altwdgt.addWidget(altsagwdgt)
        return altwdgt
#Giriş ve Kayıt Ol butonlarını yerleştiren fonksiyon
    def LoginFormWidget(self):
        wdgt = QWidget()
        cerceve = QFormLayout()
        kullaniciaditext = QLabel("Kullanıcı Adı:")
        kullaniciadiinput = QLineEdit()
        psswdtext = QLabel("Şifre:") #text giriş 
        psswdinput = QLineEdit()
        psswdinput.setEchoMode(QLineEdit.Password)
        kullaniciadiinput.setFixedWidth(210) #boyutunun sabit kalması için gerekli kod (genişlik)
        psswdinput.setFixedWidth(210) #boyutunun sabit kalması için gerekli kod (genişlik)
        cerceve.addRow(kullaniciaditext, kullaniciadiinput)
        cerceve.addRow(psswdtext, psswdinput)
        buton1cerceve = QHBoxLayout()
        buton1 = QPushButton("Giriş") #Giriş Buton
        buton2 = QPushButton("Kayıt Ol") #Kayıt Buton
        buton1.setFixedWidth(100) #boyutunun sabit kalması için gerekli kod (genişlik)
        buton2.setFixedWidth(100) #boyutunun sabit kalması için gerekli kod (genişlik)
        buton1cerceve.addWidget(buton1)
        buton1cerceve.addWidget(buton2)
        buton1cerceve.setAlignment(Qt.AlignLeft) #buton1cerceve degiskenini sola yaslamak için gerekli kod
        cerceve.addRow(" ", buton1cerceve)
        wdgt.setLayout(cerceve)
        buton1.setStyleSheet("border: 2px solid black; border-radius: 8px")
        buton2.setStyleSheet("border: 2px solid black; border-radius: 8px")
        buton1.clicked.connect(self.onLoginClicked) #Giriş butonuna tıklandığında çalışacak fonksiyon
        buton2.clicked.connect(self.onRegisterClicked)  #Kayıtol butonuna tıklandığında çalışacak fonksiyon

        return wdgt
#Giriş butonlarını çalıştıran fonksiyon

    def onLoginClicked(self):
        cerceve = self.sender().parent().layout()
        kullaniciadiinput = cerceve.itemAt(1).widget().text()
        psswdinput = cerceve.itemAt(3).widget().text()
        #password kontrolü
        if not kullaniciadiinput or not psswdinput:
            QMessageBox.warning(self, "Hata", "Kullanıcı adı ve şifre boş bırakılamaz.")
            return

        self.cursor.execute("SELECT * FROM users WHERE username = ?", (kullaniciadiinput,))
        result = self.cursor.fetchone()

        if result is not None:
            dbpsswd = result[1]  #veritabanından alınan şifrenin kontrolü
            if psswdinput == dbpsswd:
                QMessageBox.information(self, "Başarılı", "Giriş başarılı.")
                self.MainPage(kullaniciadiinput)
            else:
                QMessageBox.warning(self, "Hata", "Geçersiz kullanıcı adı veya şifre.")
        else:
            QMessageBox.warning(self, "Hata", "Geçersiz kullanıcı adı veya şifre.")
    #hikaye kısmının gerçekleşeceği pencere
    def MainPage(self, username):
        #global değişkenler
        sayac_buton2 = 0
        sayac_buton1 = 0
        hikaye_sayac = 0
        hikaye1_sayac1 = 0
        hikaye1_sayac2 = 0
        hikaye2_sayac1 = 0
        hikaye2_sayac2 = 0
        self.centralWidget().hide()
        yenisayfa = QWidget()
        yenisayfacerceve = QVBoxLayout()
        yenisayfaimg = QLabel()
        yenisayfaimg.setFixedHeight(500)
        yenisayfaimg.setFixedWidth(1382)
        yenisayfa.setStyleSheet("background-color: black")

        #arkaplan resmini değiştiren kod
        yenisayfaimg.setStyleSheet("background-image: url('background.jpg'); background-repeat: no-repeat; background-position: center; ") 
        #arkaplan resminin üzerine yazı yazan kod
        yenisayfatext = QLabel(f"Merhaba, {username}! Maceraya Hoş Geldin!")
        #arkaplan resminin üzerine yazılan yazının tasarımı, "0.3" background opacity eklemekte.
        yenisayfatext.setStyleSheet("color: black; font-size: 32pt; background-color: rgba(255, 255, 255, 0.3);")
        yenisayfacerceve.addWidget(yenisayfaimg)
        yenisayfacerceve.addWidget(yenisayfatext)
        splitter = QSplitter()
        buton1 = QPushButton("Devam Et.")
        buton2 = QPushButton("")
        buton2.setEnabled(False)
        sagsplit = QLabel(f"{username} | Oyuncu")
        sag = QLabel("Bölüm: 1")
        splitter.addWidget(buton1)
        splitter.addWidget(buton2)
        splitter.addWidget(sagsplit)
        splitter.addWidget(sag)
        sag.setStyleSheet("background: red; color:white; font-size: 12pt")
        sag.setAlignment(Qt.AlignCenter)
        sag.setFixedWidth(100)
        buton1.setStyleSheet("background: #abc")
        buton2.setStyleSheet("background: #abc")
        sagsplit.setStyleSheet("background: #cba; padding: 16px; font-size:10pt")
        buton1.setFixedHeight(90)
        buton1.setFixedWidth(340)
        buton2.setFixedHeight(90)
        buton2.setFixedWidth(340)
        

        #BattleofBastards hikayesini çalıştaracak kod
        def battleofbastards():
            nonlocal hikaye1_sayac1
            nonlocal hikaye1_sayac2
            nonlocal hikaye_sayac

            if hikaye_sayac == 1 and hikaye1_sayac2== 0: 
                yenisayfaimg.setStyleSheet("background-image: url('1/1.jpeg'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Battle of Bastards seçimi yapıldı. Başlıyor...")
                buton1.setText("Devam Et")
                buton2.setText("")
                sag.setText("Battle Of Bastards")
                sag.setStyleSheet("background: red; color:white; font-size: 8pt")
                buton1.setEnabled(True)
                buton2.setEnabled(True)
                hikaye1_sayac1 +=1
                hikaye1_sayac2 +=1
                print("Hikaye sayaç:", hikaye_sayac)
                    
            elif hikaye_sayac == 1 and hikaye1_sayac2==1:
                yenisayfaimg.setStyleSheet("background-image: url('1/1.jpeg'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Uzun yıllardır süren haksızlıklar ve acılarla dolu bir geçmişin ardından Kuzey Krallığı'nda umut belirmişti.")
                yenisayfatext.setStyleSheet("color: White; font-size: 16pt; background-color: rgba(0, 0, 0, 0.5);")
                buton1.setText("Devam Et")
                buton2.setText("")
                buton1.setEnabled(True) #buton1'i aktif hale getiren kod
                buton2.setEnabled(False)#buton2'i deaktif hale getiren kod
                hikaye1_sayac1 +=1
                hikaye1_sayac2 +=1

            elif hikaye_sayac == 1 and hikaye1_sayac2==2:
                yenisayfaimg.setStyleSheet("background-image: url('1/1.jpeg'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Jon Snow ve Sansa Stark, Winterfell'in karanlık gölgesinden kurtulmak ve Stark ailesinin onurlu mirasını geri kazanmak için bir araya gelmişlerdi.")
                buton1.setText("Devam Et")
                buton2.setText("")
                buton1.setEnabled(True)
                buton2.setEnabled(False)
                hikaye1_sayac1 +=1
                hikaye1_sayac2 +=1
            elif hikaye_sayac == 1 and hikaye1_sayac2==3:
                yenisayfaimg.setStyleSheet("background-image: url('1/1.jpeg'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Ramsay Bolton, Winterfell'in efendisi olarak zalimliği ve korkunç savaş yetenekleriyle ün kazanmıştı.")
                buton1.setText("Devam Et")
                buton2.setText("")
                buton1.setEnabled(True)
                buton2.setEnabled(False)
                hikaye1_sayac1 +=1
                hikaye1_sayac2 +=1
            elif hikaye_sayac == 1 and hikaye1_sayac2==4:
                yenisayfaimg.setStyleSheet("background-image: url('1/1.jpeg'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Jon ve Sansa, halklarını özgür kılmak ve adaleti sağlamak için müttefikler aramaya başladılar.")
                buton1.setText("Devam Et")
                buton2.setText("")
                buton1.setEnabled(True)
                buton2.setEnabled(False)
                hikaye1_sayac1 +=1
                hikaye1_sayac2 +=1
            elif hikaye_sayac == 1 and hikaye1_sayac2==5:
                yenisayfaimg.setStyleSheet("background-image: url('1/1.jpeg'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Sansa Stark, müttefiklerini savaşa ikna etmeye çalışırken, Jon çoktan savaşa girmişti bile.")
                buton1.setText("Devam Et")
                buton2.setText("")
                buton1.setEnabled(True)
                buton2.setEnabled(False)
                hikaye1_sayac1 +=1
                hikaye1_sayac2 +=1
            elif hikaye_sayac == 1 and hikaye1_sayac2==6:
                yenisayfaimg.setStyleSheet("background-image: url('1/1.jpeg'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("İki ordu da karşı karşıya gelmiş, birbirlerini tartıyorlardı. Üstün taraf zayıf tarafla alay ediyordu.")
                buton1.setText("Devam Et")
                buton2.setText("")
                buton1.setEnabled(True)
                buton2.setEnabled(False)
                hikaye1_sayac1 +=1
                hikaye1_sayac2 +=1
            elif hikaye_sayac == 1 and hikaye1_sayac2==7:
                yenisayfaimg.setStyleSheet("background-image: url('1/1.jpeg'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Ancak, Jon'un bilmediği bir şey vardı. Ramsay Bolton, Stark hanesinin en küçük oğlu, Rickon Stark'ı rehin almıştı. ")
                buton1.setText("Devam Et")
                buton2.setText("")
                buton1.setEnabled(True)
                buton2.setEnabled(False)
                hikaye1_sayac1 +=1
                hikaye1_sayac2 +=1
            elif hikaye_sayac == 1 and hikaye1_sayac2==8:
                yenisayfaimg.setStyleSheet("background-image: url('1/1.jpeg'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Ramsay, Rickon'un kulağına fısıldadı. 'Abine Koş' ")
                buton1.setText("Devam Et")
                buton2.setText("")
                buton1.setEnabled(True)
                buton2.setEnabled(False)
                hikaye1_sayac1 +=1
                hikaye1_sayac2 +=1
            elif hikaye_sayac == 1 and hikaye1_sayac2==9:
                yenisayfaimg.setStyleSheet("background-image: url('1/1.jpeg'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Rickon birazcık düşünüp, koşmaya başladı. Jon ise olacakları tahmin edebiliyordu. ")
                buton1.setText("Devam Et")
                buton2.setText("")
                buton1.setEnabled(True)
                buton2.setEnabled(False)
                hikaye1_sayac1 +=1
                hikaye1_sayac2 +=1
            elif hikaye_sayac == 1 and hikaye1_sayac2==10:
                yenisayfaimg.setStyleSheet("background-image: url('1/1.jpeg'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Ramsay, yayını aldı. Okunu yerleştirdi. Rickon'a fırlattı. ")
                buton1.setText("Devam Et")
                buton2.setText("")
                buton1.setEnabled(True)
                buton2.setEnabled(False)
                hikaye1_sayac1 +=1
                hikaye1_sayac2 +=1
            elif hikaye_sayac == 1 and hikaye1_sayac2==11:
                yenisayfaimg.setStyleSheet("background-image: url('1/1.jpeg'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Rickon koşmaya devam ediyordu, Jon ise atına atladı, yetişmeye çalışıyordu. ")
                buton1.setText("Devam Et")
                buton2.setText("")
                buton1.setEnabled(True)
                buton2.setEnabled(False)
                hikaye1_sayac1 +=1
                hikaye1_sayac2 +=1
            elif hikaye_sayac == 1 and hikaye1_sayac2==12:
                yenisayfaimg.setStyleSheet("background-image: url('1/1.jpeg'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Ramsay, ıskalıyordu. Ya da ıskalamak istiyordu. Rickon ve Jon birbirine çok yaklaşmıştı. ")
                buton1.setText("Devam Et")
                buton2.setText("")
                buton1.setEnabled(True)
                buton2.setEnabled(False)
                hikaye1_sayac1 +=1
                hikaye1_sayac2 +=1
            elif hikaye_sayac == 1 and hikaye1_sayac2==13:
                yenisayfaimg.setStyleSheet("background-image: url('1/1.jpeg'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Jon, Rickon'a elini uzattı. Tuttu. Ok Rickon'un göğüsünü deldi.")
                buton1.setText("Devam Et")
                buton2.setText("")
                buton1.setEnabled(True)
                buton2.setEnabled(False)
                hikaye1_sayac1 +=1
                hikaye1_sayac2 +=1
            elif hikaye_sayac == 1 and hikaye1_sayac2==14:
                yenisayfaimg.setStyleSheet("background-image: url('1/1.jpeg'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Jon şok olmuştu. Aptallık denilebilecek şeyi yapıyordu. Koca ordunun üstüne tek başına ilerliyordu.")
                buton1.setText("Devam Et")
                buton2.setText("")
                buton1.setEnabled(True)
                buton2.setEnabled(False)
                hikaye1_sayac1 +=1
                hikaye1_sayac2 +=1
            elif hikaye_sayac == 1 and hikaye1_sayac2==15:
                yenisayfaimg.setStyleSheet("background-image: url('1/1.jpeg'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Ramsay okçularına atış emrini verdi. Jon'un atı vuruldu, düştü.")
                buton1.setText("Devam Et")
                buton2.setText("")
                buton1.setEnabled(True)
                buton2.setEnabled(False)
                hikaye1_sayac1 +=1
                hikaye1_sayac2 +=1
            elif hikaye_sayac == 1 and hikaye1_sayac2==16:
                yenisayfaimg.setStyleSheet("background-image: url('1/7.jpeg'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Ancak, Ramsay atış emrini verdiği gibi, Jon'un komutasındaki askerler de hücuma geçmişti. ")
                buton1.setText("Devam Et")
                buton2.setText("")
                buton1.setEnabled(True)
                buton2.setEnabled(False)
                hikaye1_sayac1 +=1
                hikaye1_sayac2 +=1
            elif hikaye_sayac == 1 and hikaye1_sayac2==17:
                yenisayfaimg.setStyleSheet("background-image: url('1/7.jpeg'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Jon ölümünü kabullendi, son dansa hazırlanıyordu. Süvariler üstüne doğru geliyordu. Kılıcını çekti, bekledi.")
                buton1.setText("Devam Et")
                buton2.setText("")
                buton1.setEnabled(True)
                buton2.setEnabled(False)
                hikaye1_sayac1 +=1
                hikaye1_sayac2 +=1
            elif hikaye_sayac == 1 and hikaye1_sayac2==18:
                yenisayfaimg.setStyleSheet("background-image: url('1/7.jpeg'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Bekledi, bekledi ve bekledi. Süvariler ile çarpışacakken, komutasındaki askerleri yetişti. ")
                buton1.setText("Devam Et")
                buton2.setText("")
                buton1.setEnabled(True)
                buton2.setEnabled(False)
                hikaye1_sayac1 +=1
                hikaye1_sayac2 +=1
            elif hikaye_sayac == 1 and hikaye1_sayac2==19:
                yenisayfaimg.setStyleSheet("background-image: url('1/6.jpeg'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Kuzey'in en büyük savaşlarından birisi gerçekleşiyordu. Katliam yaşanıyordu.")
                buton1.setText("Devam Et")
                buton2.setText("")
                buton1.setEnabled(True)
                buton2.setEnabled(False)
                hikaye1_sayac1 +=1
                hikaye1_sayac2 +=1
            elif hikaye_sayac == 1 and hikaye1_sayac2==20:
                yenisayfaimg.setStyleSheet("background-image: url('1/4.jpeg'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Ramsay düşmanlarını sıkıştırmıştı.")
                buton1.setText("Devam Et")
                buton2.setText("")
                buton1.setEnabled(True)
                buton2.setEnabled(False)
                hikaye1_sayac1 +=1
                hikaye1_sayac2 +=1
            elif hikaye_sayac == 1 and hikaye1_sayac2==21:
                yenisayfaimg.setStyleSheet("background-image: url('1/3.jpeg'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Sansa ve müttefikleri Vale Hanesi, savaşa yetişmişti. Vadi'nin süvarileri hücuma kalkmış. Ramsay'ın ordusuna doğru ilerliyordu.")
                buton1.setText("Devam Et")
                buton2.setText("")
                buton1.setEnabled(True)
                buton2.setEnabled(False)
                hikaye1_sayac1 +=1
                hikaye1_sayac2 +=1
            elif hikaye_sayac == 1 and hikaye1_sayac2==22:
                yenisayfaimg.setStyleSheet("background-image: url('1/2.jpeg'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Süvariler, tam anlamıyla katliam yaptı. Ramsay, Winterfell'e, son savunmaya kaçtı.")
                buton1.setText("Devam Et")
                buton2.setText("")
                buton1.setEnabled(True)
                buton2.setEnabled(False)
                hikaye1_sayac1 +=1
                hikaye1_sayac2 +=1
            elif hikaye_sayac == 1 and hikaye1_sayac2==23:
                yenisayfaimg.setStyleSheet("background-image: url('1/8.jpeg'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Jon ve ordusu, Winterfell'e doğru ilerliyordu. Küçük bir muharebenin ardından, içeridelerdi.")
                buton1.setText("Devam Et")
                buton2.setText("")
                buton1.setEnabled(True)
                buton2.setEnabled(False)
                hikaye1_sayac1 +=1
                hikaye1_sayac2 +=1
            elif hikaye_sayac == 1 and hikaye1_sayac2==24:
                yenisayfaimg.setStyleSheet("background-image: url('1/1.jpeg'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Ramsay, avluda Jon'a sesleniyordu. 'Hadi şunu erkek erkeğe, bire bir bitirelim.'")
                buton1.setText("Devam Et")
                buton2.setText("")
                buton1.setEnabled(True)
                buton2.setEnabled(False)
                hikaye1_sayac1 +=1
                hikaye1_sayac2 +=1
            elif hikaye_sayac == 1 and hikaye1_sayac2==25:
                yenisayfaimg.setStyleSheet("background-image: url('1/5.jpeg'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Ramsay'ı vurmayı bekleyen okçular oklarını indirdi. Jon kalkanına davrandı, Ramsay'ın oklarını def etti.")
                buton1.setText("Devam Et")
                buton2.setText("")
                buton1.setEnabled(True)
                buton2.setEnabled(False)
                hikaye1_sayac1 +=1
                hikaye1_sayac2 +=1
            elif hikaye_sayac == 1 and hikaye1_sayac2==26:
                yenisayfaimg.setStyleSheet("background-image: url('1/5.jpeg'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Jon, Ramsay'e yetişti. Kalkanıyla saldırdı, Ramsay'i yere serdi. ")
                buton1.setText("Devam Et")
                buton2.setText("")
                buton1.setEnabled(True)
                buton2.setEnabled(False)
                hikaye1_sayac1 +=1
                hikaye1_sayac2 +=1
            elif hikaye_sayac == 1 and hikaye1_sayac2==27:
                yenisayfaimg.setStyleSheet("background-image: url('1/5.jpeg'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Stark Hanesi, tekrardan Winterfell'in sahibiydi. Jon, sonradan bırakacağı Kuzey'in Kralı ünvanını almıştı.")
                buton1.setText("Devam Et")
                buton2.setText("")
                buton1.setEnabled(True)
                buton2.setEnabled(False)
                hikaye1_sayac1 +=1
                hikaye1_sayac2 +=1
            elif hikaye_sayac == 1 and hikaye1_sayac2==28:
                yenisayfaimg.setStyleSheet("background-image: url('1/2.jpeg'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("SON")
                buton1.setText("")
                buton2.setText("")
                buton1.setEnabled(False)
                buton2.setEnabled(False)

    
            buton1.clicked.connect(Buton1Clicked)
            buton2.clicked.connect(Buton2Clicked)
        #RedWedding hikayesini çalıştaracak kod
        def redwedding():
            nonlocal hikaye2_sayac1
            nonlocal hikaye2_sayac2
            nonlocal hikaye_sayac

            if hikaye_sayac == 2 and hikaye2_sayac1== 0:
                yenisayfaimg.setStyleSheet("background-image: url('2/4.png'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("The Red Wedding seçimi yapıldı. Başlıyor...")
                buton1.setText("")
                buton2.setText("Devam Et")
                sag.setText("The Red Wedding")
                sag.setStyleSheet("background: red; color:white; font-size: 8pt")
                buton1.setEnabled(False)
                buton2.setEnabled(True)
                hikaye2_sayac1 +=1
                hikaye2_sayac2 +=1
                print("Hikaye sayaç:", hikaye_sayac) #Hikaye_Sayac'ı terminale yazan kod. Kontrol etmek amaçlı.
                    
            elif hikaye_sayac == 2 and hikaye2_sayac2==1:
                yenisayfaimg.setStyleSheet("background-image: url('2/10.png'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Yıllardır süren mücadelelerin ortasında, kuzeydeki Stark ailesi ile güneydeki Lannister ailesi arasında gergin bir atmosfer vardı.")
                yenisayfatext.setStyleSheet("color: black; font-size: 12pt; background-color: rgba(255, 255, 255, 0.3);")
                buton1.setText("")
                buton2.setText("Devam Et")
                buton1.setEnabled(False)
                buton2.setEnabled(True)
                hikaye2_sayac1 +=1
                hikaye2_sayac2 +=1

            elif hikaye_sayac == 2 and hikaye2_sayac2==2:
                yenisayfaimg.setStyleSheet("background-image: url('2/8.png'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Robb, Kuzey Krallığı'nın genç lideri olarak adaleti ve doğruluğu temsil ediyordu.")
                buton1.setText("")
                buton2.setText("Devam Et")
                buton1.setEnabled(False)
                buton2.setEnabled(True)
                hikaye2_sayac1 +=1
                hikaye2_sayac2 +=1
            elif hikaye_sayac == 2 and hikaye2_sayac2==3:
                yenisayfaimg.setStyleSheet("background-image: url('2/1.png'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Robb, savaşta ağır kayıplar vermiş ve güçlü müttefiklerini kaybetmişti. Bu yüzden, umutsuz bir şekilde güçlü bir ittifak kurmak amacıyla Frey hanesiyle evlenmeyi kabul etti.")
                buton1.setText("")
                buton2.setText("Devam Et")
                buton1.setEnabled(False)
                buton2.setEnabled(True)
                hikaye2_sayac1 +=1
                hikaye2_sayac2 +=1
            elif hikaye_sayac == 2 and hikaye2_sayac2==4:
                yenisayfaimg.setStyleSheet("background-image: url('2/5.png'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Ancak, Robb ve annesi Catelyn Stark için, bu davet ölümcül bir tuzaktı.")
                buton1.setText("")
                buton2.setText("Devam Et")
                buton1.setEnabled(False)
                buton2.setEnabled(True)
                hikaye2_sayac1 +=1
                hikaye2_sayac2 +=1
            elif hikaye_sayac == 2 and hikaye2_sayac2==5:
                yenisayfaimg.setStyleSheet("background-image: url('2/5.png'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Şimdi, sen Robb Stark olarak kararlar alacaksın. Bu kararlar gidişatı belirleyecek.")
                buton1.setText("")
                buton2.setText("Harika!")
                buton1.setEnabled(False)
                buton2.setEnabled(True)
                hikaye2_sayac1 +=1
                hikaye2_sayac2 +=1
                    
        def Buton2Clicked():
            nonlocal hikaye2_sayac1 
            nonlocal hikaye2_sayac2 
            nonlocal hikaye_sayac
            if hikaye_sayac == 2 and hikaye2_sayac2 == 6:
                yenisayfaimg.setStyleSheet("background-image: url('2/5.png'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Frey Kalesi'nde düğün gecesi. Robb Stark, annesi Catelyn ve sadık takipçileri burada bulunuyor. Müzik ve eğlence havası içinde her şey başlıyor.")
                buton1.setText("Davete Katıl")
                buton2.setText("")
                buton1.setEnabled(True)
                buton2.setEnabled(False)
                hikaye2_sayac1 += 1
                hikaye2_sayac2 += 1
            elif hikaye_sayac == 2 and hikaye2_sayac2 == 8:
                yenisayfaimg.setStyleSheet("background-image: url('2/5.png'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Arkanı dönüp annen ve karına baktın. Tuzak diye bağırdın.")
                buton1.setText("")
                buton2.setText("Devam Et")
                buton1.setEnabled(False)
                buton2.setEnabled(True)
                hikaye2_sayac2 += 1
                print(f"Hikaye_Sayac2=",hikaye2_sayac2)
            elif hikaye_sayac == 2 and hikaye2_sayac2 == 9:
                yenisayfaimg.setStyleSheet("background-image: url('2/5.png'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Ancak bu yaptığın kaçınılmaz sonu daha da hızlandırdı.")
                buton1.setText("Devam Et")
                buton2.setText("")
                buton1.setEnabled(True)
                buton2.setEnabled(False)
                hikaye2_sayac1+=4
                print(f"Hikaye_Sayac1=",hikaye2_sayac1)
            elif hikaye_sayac == 2 and hikaye2_sayac2 == 10:
                yenisayfaimg.setStyleSheet("background-image: url('2/5.png'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Robb tuzağı farketmiş olsa da, artık çok geç olmuştu. ")
                buton1.setText("")
                buton2.setText("Devam Et")
                buton1.setEnabled(False)
                buton2.setEnabled(True)
                hikaye2_sayac2-=2
                print(f"Hikaye_Sayac1=",hikaye2_sayac1)

        def Buton1Clicked():
            nonlocal hikaye2_sayac1 
            nonlocal hikaye2_sayac2
            nonlocal hikaye_sayac
            if hikaye_sayac == 2 and hikaye2_sayac1 == 7:
                yenisayfaimg.setStyleSheet("background-image: url('2/5.png'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Düğün gecesi Frey Kalesi'nde geldiğinde, herkes eğlence ve coşku içindeydi. Robb'un kalabalık gelmiş olması gerginlik yaratmıştı.")
                buton1.setText("Devam Et")
                buton2.setText("")
                buton1.setEnabled(True)
                buton2.setEnabled(False)
                hikaye2_sayac1 += 1
            elif hikaye_sayac == 2 and hikaye2_sayac1 == 8:
                yenisayfaimg.setStyleSheet("background-image: url('2/5.png'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Ailesi ve çok güvendiği askerleriyle birlikte davete katılan Genç Kurt, çok soğuktu.")
                buton1.setText("Devam Et")
                buton2.setText("")
                buton1.setEnabled(True)
                buton2.setEnabled(False)
                hikaye2_sayac1 += 1
            elif hikaye_sayac == 2 and hikaye2_sayac1 == 9:
                yenisayfaimg.setStyleSheet("background-image: url('2/5.png'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Genç Kurt Stark, ailesiyle ilgileniyor, askerleriyle birlikte gövde gösterisi yapıyordu.")
                buton1.setText("Devam Et")
                buton2.setText("")
                buton1.setEnabled(True)
                buton2.setEnabled(True)
                hikaye2_sayac1 += 1
            elif hikaye_sayac == 2 and hikaye2_sayac1 == 10:
                yenisayfaimg.setStyleSheet("background-image: url('2/5.png'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Ancak, bu yeterli olmayacaktı. Müzik ve eğlence havasına rağmen, Frey ailesi ve Lannister müttefikleri sinsi bir planı hayata geçirdi.")
                buton1.setText("Devam Et")
                buton2.setText("")
                buton1.setEnabled(True)
                buton2.setEnabled(False)
                hikaye2_sayac1 += 1
            elif hikaye_sayac == 2 and hikaye2_sayac1 == 11:
                yenisayfaimg.setStyleSheet("background-image: url('2/5.png'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Etraftaki Frey askerleri hareketlenmişti, ancak sakinlerdi.")
                buton1.setText("Dikkat Kesil")
                buton2.setText("İlk Sen Saldır")
                buton1.setEnabled(True)
                buton2.setEnabled(True)
                hikaye2_sayac1 += 1
                hikaye2_sayac2 +=1
                print(f"Hikaye_Sayac2=",hikaye2_sayac2)
            elif hikaye_sayac == 2 and hikaye2_sayac1 == 12:
                yenisayfaimg.setStyleSheet("background-image: url('2/1.png'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Robb Stark, etrafı daha dikkatli süzerken, Walder Frey kadeh kaldırıyordu.")
                buton1.setText("Devam Et")
                buton2.setText("")
                buton1.setEnabled(True)
                buton2.setEnabled(False)
                hikaye2_sayac1 += 1
            elif hikaye_sayac == 2 and hikaye2_sayac1 == 13:
                yenisayfaimg.setStyleSheet("background-image: url('2/1.png'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Majesteleri, diyerek başladı cümleye Frey. Sevgi ve saygı sunuyordu.")
                buton1.setText("Devam Et")
                buton2.setText("")
                buton1.setEnabled(True)
                buton2.setEnabled(False)
                hikaye2_sayac1 += 2
            elif hikaye_sayac == 2 and hikaye2_sayac1 == 15:
                yenisayfaimg.setStyleSheet("background-image: url('2/7.png'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Frey'in konuşması sırasında Robb balkonlara dikkat kesildi. Askerler vardı. Arbaletli askerler.")
                buton1.setText("Onlar Koruma Sağlıyor")
                buton2.setText("Bu Bir Tuzak")
                buton1.setEnabled(True)
                buton2.setEnabled(True)
                hikaye2_sayac1 += 1
                hikaye2_sayac2 +=2
            elif hikaye_sayac == 2 and hikaye2_sayac1 == 16:
                yenisayfaimg.setStyleSheet("background-image: url('2/7.png'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Robb düzgün düşünememişti. Frey'in konuşması bittiği gibi, askerler ok atmaya başladı.")
                buton1.setText("Devam Et")
                buton2.setText("")
                buton1.setEnabled(True)
                buton2.setEnabled(False)
                hikaye2_sayac1 += 1
            elif hikaye_sayac == 2 and hikaye2_sayac1 == 17:
                yenisayfaimg.setStyleSheet("background-image: url('2/3.png'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("İlk ok Robb'a geldi, annesi Catelyn, masanın altına saklandı hemen. Karısı, arkasından yaklaşan Frey tarafından katledildi.")
                buton1.setText("Devam Et")
                buton2.setText("")
                buton1.setEnabled(True)
                buton2.setEnabled(False)
                hikaye2_sayac1 += 1
            elif hikaye_sayac == 2 and hikaye2_sayac1 == 18:
                yenisayfaimg.setStyleSheet("background-image: url('2/3.png'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Robb ihanete uğramıştı. Neler olduğunu anlamadan, ikinci ok geldi. Üçüncü... dördüncü. Oracıkta yığıldı. ")
                buton1.setText("Devam Et")
                buton2.setText("")
                buton1.setEnabled(True)
                buton2.setEnabled(False)
                hikaye2_sayac1 += 1
            elif hikaye_sayac == 2 and hikaye2_sayac1 == 19:
                yenisayfaimg.setStyleSheet("background-image: url('2/9.png'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Bilincini henüz kaybetmemişti ki, karısına doğru sürünüyordu. Karısının başını son kez kollarına almıştı. ")
                buton1.setText("Devam Et")
                buton2.setText("")
                buton1.setEnabled(True)
                buton2.setEnabled(False)
                hikaye2_sayac1 += 1
            elif hikaye_sayac == 2 and hikaye2_sayac1 == 20:
                yenisayfaimg.setStyleSheet("background-image: url('2/9.png'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Catelyn, masanın altından bir bıçak bulup, Frey'in karısının boğazına yaslandı. Frey'lere hakaret ederken, karısını öldürmekle tehdit ediyordu. ")
                buton1.setText("Devam Et")
                buton2.setText("")
                buton1.setEnabled(True)
                buton2.setEnabled(False)
                hikaye2_sayac1 += 1
            elif hikaye_sayac == 2 and hikaye2_sayac1 == 21:
                yenisayfaimg.setStyleSheet("background-image: url('2/5.png'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Hayatta kalmaya çalışan Catelyn, oğlu ve gelinine baktı. Frey kadınının boğazını kesti. Diz çöküp ağlarken, arkasından yaklaşıp boğazını kestiler. ")
                buton1.setText("Devam Et")
                buton2.setText("")
                buton1.setEnabled(True)
                buton2.setEnabled(False)
                hikaye2_sayac1 += 1
            elif hikaye_sayac == 2 and hikaye2_sayac1 == 22:
                yenisayfaimg.setStyleSheet("background-image: url('2/15.jpeg'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Robb'un kurtunun da kafasını kesip, sopaya geçirip alay ettiler. Haberler yayılıyordu. ")
                buton1.setText("Devam Et")
                buton2.setText("")
                buton1.setEnabled(True)
                buton2.setEnabled(False)
                hikaye2_sayac1 += 1
            elif hikaye_sayac == 2 and hikaye2_sayac1 == 23:
                yenisayfaimg.setStyleSheet("background-image: url('2/15.jpeg'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("Lannister ve Frey hanesinin bu işbirliği, kuzeyin kapılarını onlara açtı. Stark hanesine büyük darbe olmuştu bu.")
                buton1.setText("Devam Et")
                buton2.setText("")
                buton1.setEnabled(True)
                buton2.setEnabled(False)
                hikaye2_sayac1 += 1
            elif hikaye_sayac == 2 and hikaye2_sayac1 == 24:
                yenisayfaimg.setStyleSheet("background-image: url('2/8.png'); background-repeat: no-repeat; background-position: center; ")
                yenisayfatext.setText("SON")
                buton1.setText("")
                buton2.setText("")
                buton1.setEnabled(False)
                buton2.setEnabled(False)
                hikaye2_sayac1 += 1

        buton1.clicked.connect(Buton1Clicked)
        buton2.clicked.connect(Buton2Clicked)

        #Buton1'e tıklandığında çalışacak kod
        def onButon1Clicked():
            nonlocal sayac_buton1
            nonlocal sayac_buton2
            nonlocal hikaye_sayac
            if hikaye_sayac==0:  
                if sayac_buton1 != 0:
                    # Eğer buton2'ye tıklanıldıysa, sayac_buton1'i sıfırla
                    sayac_buton2 = 0

                if sayac_buton1 == 0:
                    yenisayfatext.setText("Umarım Game of Thrones izlemişsindir.")
                    yenisayfaimg.setStyleSheet("background-image: url('img.png'); background-repeat: no-repeat; background-position: center; ")
                    buton1.setText("İzledim")
                    buton2.setText("İzlemedim")
                    buton1.setEnabled(True)
                    buton2.setEnabled(True)
                    sayac_buton1 +=1
                    print (sayac_buton1)
                    print (sayac_buton2)
                    
                elif sayac_buton1 == 1:
                    yenisayfatext.setText("O halde... Fotoğraftaki sağ alt köşedeki kişi kimdir?")
                    buton1.setText("Hodor")
                    buton2.setText("Oberyn Martell")
                    sayac_buton1 += 1
                    sayac_buton2 +=1
                    buton1.setEnabled(True)
                    buton2.setEnabled(True)
                    print (sayac_buton1)
                    print (sayac_buton2)

                elif sayac_buton1 == 2:
                    yenisayfatext.setText("Doğru! Bravo. Sana başarım atıyorum. Butonların yanında görebilirsin.")
                    buton1.setText("Teşekkürler")
                    buton2.setText("")
                    sagsplit.setText(f"{username} | Oyuncu | Nerd ")
                    buton2.setEnabled(False)
                    sayac_buton1 += 1
                    print (sayac_buton1)
                    print (sayac_buton2)

                elif sayac_buton1 == 3:
                    yenisayfatext.setText("Peki... Hangi hanedana daha yakın hissediyorsun kendini?")
                    buton1.setText("Stark.")
                    buton2.setText("Lannister.")
                    buton1.setEnabled(True)
                    buton2.setEnabled(True)
                    sayac_buton1 += 1
                    sayac_buton2 += 3
                    print (sayac_buton1)
                    print (sayac_buton2)

                elif sayac_buton1 == 4:
                    yenisayfatext.setText("Harika! Bir başarım kazandın!")
                    buton1.setText("Teşekkürler.")
                    buton2.setText("")
                    sagsplit.setText(f"{username} | Oyuncu | Nerd | House Stark")
                    buton1.setEnabled(True)
                    buton2.setEnabled(False)
                    sayac_buton1 += 1
                    print (sayac_buton1)
                    print (sayac_buton2)

                elif sayac_buton2 == 4 or sayac_buton1==5:
                    yenisayfaimg.setStyleSheet("background-image: url('secim1.png'); background-repeat: no-repeat; background-position: center; ")
                    yenisayfatext.setText("Şimdi... seçim vakti. Hangi hikayeyi oynamak istiyorsun?")
                    buton1.setText("Battle of Bastards")
                    buton2.setText("The Red Wedding")
                    buton1.setEnabled(True)
                    buton2.setEnabled(True)
                    sayac_buton1+=1
                    sayac_buton2+=5

                elif sayac_buton1==6:
                    hikaye_sayac +=1

            elif hikaye_sayac==1 and sayac_buton1 == 6:
                battleofbastards()

            else:
                redwedding()
        #Buton2'ye tıklandığında çalışacak kod
        def onButon2Clicked():
            nonlocal sayac_buton2
            nonlocal sayac_buton1
            nonlocal hikaye_sayac
            if hikaye_sayac==0:  
                if sayac_buton2 != 0:
                #Sayaçların birbirine karışmaması için, buton2'ye tıklandığında buton1'i 0'layan kod
                    sayac_buton1 = 0
            
                if sayac_buton2 == 0:
                    yenisayfatext.setText("Tüh, ne yazık. Neyse, çok da önemli değil.")
                    buton1.setText("")
                    buton2.setText("Peki, devam et.")
                    buton1.setEnabled(False)
                    buton2.setEnabled(True)
                    sayac_buton2 += 2
                    print (sayac_buton1)
                    print (sayac_buton2)

                elif sayac_buton2 == 1:
                    yenisayfatext.setText("Yanlış cevap. Başarımı kaçırdın. Ama üzülme, yenisi geliyor.")
                    buton1.setText("")
                    buton2.setText("Tüh.")
                    buton1.setEnabled(False)
                    buton2.setEnabled(True)
                    sayac_buton2 += 1
                    print (sayac_buton1)
                    print (sayac_buton2)

                elif sayac_buton2 == 2:
                    yenisayfatext.setText("Peki... Hangi hanedana daha yakın hissediyorsun kendini?")
                    buton1.setText("Stark.")
                    buton2.setText("Lannister.")
                    buton1.setEnabled(True)
                    buton2.setEnabled(True)
                    sayac_buton1 += 4
                    sayac_buton2 += 1
                    print (sayac_buton1)
                    print (sayac_buton2)

                elif sayac_buton2 == 3:
                    yenisayfatext.setText("Harika! Bir başarım kazandın! Butonların yanında görebilirsin.")
                    buton1.setText("")
                    buton2.setText("Teşekkürler.")
                    sagsplit.setText(f"{username}: | Oyuncu | House Lannister")
                    buton1.setEnabled(False)
                    buton2.setEnabled(True)
                    sayac_buton2 += 1
                    print (sayac_buton1)
                    print (sayac_buton2)
                    print("Hikaye sayaç:", hikaye_sayac)

                elif sayac_buton2 == 4 or sayac_buton1==5:
                    yenisayfaimg.setStyleSheet("background-image: url('secim1.png'); background-repeat: no-repeat; background-position: center; ")
                    yenisayfatext.setText("Şimdi... seçim vakti. Hangi hikayeyi oynamak istiyorsun?")
                    buton1.setText("Battle of Bastards")
                    buton2.setText("The Red Wedding")
                    buton1.setEnabled(True)
                    buton2.setEnabled(True)
                    sayac_buton1+=6
                    sayac_buton2+=1

                elif sayac_buton2==5:
                    hikaye_sayac +=2

            elif hikaye_sayac==2 and sayac_buton2 == 5:
                redwedding()    

        buton1.clicked.connect(onButon1Clicked) #onbuton1clicked fonksiyonunu butonlara tıklandığında çalıştıracak şekilde ayarlanmış kod
        buton2.clicked.connect(onButon2Clicked)

        yenisayfacerceve.addWidget(splitter)
        yenisayfa.setLayout(yenisayfacerceve)
        self.setCentralWidget(yenisayfa)
    #kayıtol butonuna tıklandıktan sonra çalışacak fonksiyon
    def onRegisterClicked(self):
        cerceve = self.sender().parent().layout()
        kullaniciadiinput = cerceve.itemAt(1).widget().text()
        psswdinput = cerceve.itemAt(3).widget().text()
        if not kullaniciadiinput or not psswdinput:
            QMessageBox.warning(self, "Hata", "Kullanıcı adı ve şifre boş bırakılamaz.")
            return

        self.cursor.execute("SELECT * FROM users WHERE username = ?", (kullaniciadiinput,))
        result = self.cursor.fetchone()

        if result is not None:
            QMessageBox.warning(self, "Hata", "Bu kullanıcı adı zaten kayıtlı.")
            return

        self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (kullaniciadiinput, psswdinput))
        self.conn.commit()

        QMessageBox.information(self, "Başarılı", "Kayıt başarılı.")
    #pencereyi kapatırken uyarı vermesi için gereken fonksiyon
    def closeEvent(self, event):
        reply = QMessageBox.question(
            self,
            "Çıkış",
            "Uygulamayı kapatmak istediğinizden emin misiniz?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            self.conn.close()
            event.accept()
        else:
            event.ignore()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplitterWindow()
    window.show()
    sys.exit(app.exec_())