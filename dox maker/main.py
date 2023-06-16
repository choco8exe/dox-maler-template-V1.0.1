import time
from os import name, system
 
try :
    from pystyle import *
    from escape import Escape



except ModuleNotFoundError :
    print("Module introuvable")
    time.sleep(1.5)
    print("installation des modules ......")
    time.sleep(1)

try :
    system("pip install escape")
    system("pip install pystyle")
    system("cls")
    time.sleep(1)
    print("module installer sans soucis .")
    time.sleep(1)
    system("cls")

except :
    print("les module ne peuvent etre installer .")
    time.sleep(2)
    print("verifier que 'pip' est bien installer et ajouter a votre 'patch' !")
    input()
    quit()

if name == "nt":
        system("title DOX WRITTER V1.0.1")
        def clear():
            system("cls")
else:
    def clear():
        system("clear")



banner = """

               ...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO
       ::::::;       ;          OOOOO
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,     /  /     DOOOO
 ,::::::;::::::;;;;::::;,   /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O
  `:::::`::::::::;' /  / `:#
   ::::::`:::::;'  /  /   `#

"""



def main():
    print(Colorate.Diagonal(Colors.red_to_purple, Center.XCenter(banner)))
    input()
    print(Escape("simple dox maker created by choco8exe#8725").red())
    print("")
    print("")

    user = Write.Input("entree le createur du dox -> ", Colors.red_to_yellow, interval=0.005)
    print("")
    time.sleep(2)
    clear()

    print(Escape("enter").red() + Escape (" no ").blue() + Escape("if you dont have this info").red())
    print("")
    name1 = Write.Input("entree le nom prenom de la victime -> ", Colors.red_to_yellow, interval=0.005)
    print("")
    time.sleep(2)
    clear()

    print(Escape("enter").red() + Escape (" no ").blue() + Escape("if you dont have this info").red())
    print("")
    age = Write.Input("entree l'age de la victime -> ", Colors.red_to_yellow, interval=0.005)
    print("")
    time.sleep(2)
    clear()

    print(Escape("enter").red() + Escape (" no ").blue() + Escape("if you dont have this info").red())
    print("")
    DOB = Write.Input("entree la date d'anniversaire de la victime -> ", Colors.red_to_yellow, interval=0.005)
    print("")
    time.sleep(2)
    clear()

    print(Escape("enter").red() + Escape (" no ").blue() + Escape("if you dont have this info").red())
    print("")
    IP  = Write.Input("entree l'IP de la victime -> ", Colors.red_to_yellow, interval=0.005)
    print("")
    time.sleep(2)
    clear()

    print(Escape("enter").red() + Escape (" no ").blue() + Escape("if you dont have this info").red())
    print("")
    RELATION = Write.Input("entree la relation de la victime -> ", Colors.red_to_yellow, interval=0.005)
    print("")
    time.sleep(2)
    clear()

    print(Escape("enter").red() + Escape (" no ").blue() + Escape("if you dont have this info").red())
    print("")
    phone = Write.Input("entree le numero de telephone de la victime -> ", Colors.red_to_yellow, interval=0.005)
    print("")
    time.sleep(2)
    clear()

    print(Escape("enter").red() + Escape (" no ").blue() + Escape("if you dont have this info").red())
    print("")
    Genre = Write.Input("entree le Genre (sexe) de la victime -> ", Colors.red_to_yellow, interval=0.005)
    print("")
    time.sleep(2)
    clear()

    print(Escape("enter").red() + Escape (" no ").blue() + Escape("if you dont have this info").red())
    print("")
    ADRSS = Write.Input("entree l'adresse de la victime -> ", Colors.red_to_yellow, interval=0.005)
    print("")
    time.sleep(2)
    clear()

    print(Escape("enter").red() + Escape (" no ").blue() + Escape("if you dont have this info").red())
    print("")
    discord = Write.Input("entree le discord de la victime -> ", Colors.red_to_yellow, interval=0.005)
    print("")
    time.sleep(2)
    clear()

    print(Escape("enter").red() + Escape (" no ").blue() + Escape("if you dont have this info").red())
    print("")
    fcb = Write.Input("entree le facebook de la victime -> ", Colors.red_to_yellow, interval=0.005)
    print("")
    time.sleep(2)
    clear()

    print(Escape("enter").red() + Escape (" no ").blue() + Escape("if you dont have this info").red())
    print("")
    insta= Write.Input("entree l'instagram de la victime -> ", Colors.red_to_yellow, interval=0.005)
    print("")
    time.sleep(2)
    clear()

    print(Escape("enter").red() + Escape (" no ").blue() + Escape("if you dont have this info").red())
    print("")
    ytb = Write.Input("entree le youtube de la victime -> ", Colors.red_to_yellow, interval=0.005)
    print("")
    time.sleep(2)
    clear()

    print(Escape("enter").red() + Escape (" no ").blue() + Escape("if you dont have this info").red())
    print("")
    twit = Write.Input("entree le twitter de la victime -> ", Colors.red_to_yellow, interval=0.005)
    print("")
    time.sleep(2)
    clear()

    print(Escape("enter").red() + Escape (" no ").blue() + Escape("if you dont have this info").red())
    print("")
    tik = Write.Input("entree le TikTok de la victime -> ", Colors.red_to_yellow, interval=0.005)
    print("")
    time.sleep(2)
    clear()

    print(Escape("enter").red() + Escape (" no ").blue() + Escape("if you dont have this info").red())
    print("")
    pict1 = Write.Input("entree une image1 (url) de la victime -> ", Colors.red_to_yellow, interval=0.005)
    print("")
    time.sleep(2)
    clear()

    print(Escape("enter").red() + Escape (" no ").blue() + Escape("if you dont have this info").red())
    print("")
    pict2 = Write.Input("entree une image2 (url) de la victime -> ", Colors.red_to_yellow, interval=0.005)
    print("")
    time.sleep(2)
    clear()

    print(Escape("enter").red() + Escape (" no ").blue() + Escape("if you dont have this info").red())
    print("")
    pict3 = Write.Input("entree une image3 (url) de la victime -> ", Colors.red_to_yellow, interval=0.005)
    print("")
    time.sleep(2)
    clear()

    print(Escape("enter").red() + Escape (" no ").blue() + Escape("if you dont have this info").red())
    print("")
    pict4 = Write.Input("entree une image4 (url) de la victime -> ", Colors.red_to_yellow, interval=0.005)
    print("")
    time.sleep(2)
    clear()

    print(Escape("enter").red() + Escape (" no ").blue() + Escape("if you dont have this info").red())
    print("")
    pict5 = Write.Input("entree une image5 (url) de la victime -> ", Colors.red_to_yellow, interval=0.005)
    print("")
    time.sleep(2)
    clear()

    

    if name1 == ("no",""):
        name1 = ("name not found !")

    if age == ("no",""):
        age = ("age not found !")
    
    if DOB == ("no",""):
        DOB = ("DOB not found !")

    if IP == ("no",""):
        IP = ("IP not found !")

    if RELATION == ("no",""):
        RELATION = ("Relation not found !")

    if phone == ("no",""):
        phone = ("phone not found !")
        
    if Genre == ("no",""):
        Genre = ("genre not found !")
    
    if ADRSS == ("no",""):
        ADRSS = ("Address not found !")

    if discord == ("no",""):
        discord  = ("discord not found !")
    
    if fcb == ("no",""):
        fcb = ("Facebook not found !")

    if insta ==("no",""):
        insta = ("Instagram not found !")

    if ytb == ("no",""):
        ytb = ("Youtube not found !")

    if twit == ("no",""):
        twit = ("Twitter not found !")

    if tik == ("no",""):
        tik = ("TikTok not found !")

    if pict1 ==("no",""):
        pict1 = ("picture not found !")
    
    if pict2 ==("no",""):
        pict2 = ("picture not found !")

    if pict3 ==("no",""):
        pict3 = ("picture not found !")

    if pict4 ==("no",""):
        pict4 = ("picture not found !")

    if pict5 ==("no",""):
        pict5 = ("picture not found !")

    dox = """ 
  .--.      .-'.      .--.      .--.      .--.      .--.      .`-.      .--.  .--.      .-'.      .--.      .--.      .--.      .--.
:::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\:::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.
'      `--'      `.-'      `--'      `--'      `--'      `-.'      `--'      `'      `--'      `.-'      `--'      `--'      `--'  


✟ - Basic Info - ✟
» Full Name            : """+ name1  +"""
» Age                  : """+ age +"""
» D.O.B                : """+ DOB +"""
» IP Address           : """+ IP  +"""
» Relationship Status  : """+ RELATION +"""
» Phone #              : """+ phone +"""
» Gender               : """+ Genre +"""
» Address              : """+ ADRSS +"""     

✟ - Online Info - ✟
» Discord              : """+ discord  +"""
» Facebook             : """+ fcb  +"""
» Instagram            : """+ insta  +"""
» YTB                  : """+ ytb  +"""
» Twitter              : """+ twit  +"""
» TikTok               : """+ tik  +"""


✟ - picture - ✟
"""+pict1+"""
"""+pict2+"""
"""+pict3+"""
"""+pict4+"""
"""+pict5+"""


                                                               𝖕𝖗𝖔𝖌𝖗𝖆𝖒 𝖒𝖆𝖉𝖊 𝖇𝖞 𝖈𝖍𝖔𝖈𝖔8𝖊𝖝𝖊#8725
                                                                 𝖉𝖔𝖝 𝖒𝖆𝖉𝖊 𝖇𝖞 """ + user + """
                                                      
                                                   /\                               ______,....----,
                                     /VVVVVVVVVVVVVV|==================='"'"'"'"'"'"       ___,..-'
                                     `^^^^^^^^^^^^^^|======================----------"'"''""
                                                   \/
                                     
  .--.      .-'.      .--.      .--.      .--.      .--.      .`-.      .--.  .--.      .-'.      .--.      .--.      .--.      .--.
:::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\:::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.
'      `--'      `.-'      `--'      `--'      `--'      `-.'      `--'      `'      `--'      `.-'      `--'      `--'      `--'  


"""


    with open("ɎØɄⱤ ĐɆ₳Đ.txt", "w", encoding="utf-8") as f:
        f.write(dox)
    f.close()
    print("Dox cree")
    time.sleep(5)
    quit()







if __name__ == '__main__':
    while True:
        main()
credit =                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  """𝕤𝕚𝕞𝕡𝕝𝕖 𝕕𝕠𝕩 𝕞𝕒𝕜𝕖𝕣 𝕔𝕣𝕖𝕒𝕥𝕖𝕕 𝕓𝕪 𝕔𝕙𝕠𝕔𝕠𝟠𝕖𝕩𝕖#𝟠𝟟𝟚𝟝"""