import random as r
horuf_kochak = ['a' , 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
horuf_bozorg = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
adad = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
character = ['@' , '#' , '*' ,'?', '!']

def password_easy():  # ساخت رمز عبور آسان تشکیل شده از حروف کوچک و اعداد
    a  , b , c , d , e ,f ,g ,h= r.choice(horuf_kochak) , r.choice(horuf_kochak) , r.choice(horuf_kochak) , r.choice(horuf_kochak) ,r.choice(adad) , r.choice(adad) ,r.choice(adad) ,r.choice(adad)

    password = a + h + b + c + d + f +e + g
    return password

def password_normal() : # ساخت رمز عبور تشکیل شده از حروف کوچک و بزرگ و اعداد
    a  , b , c , d , e ,f ,g ,h= r.choice(horuf_kochak) , r.choice(horuf_kochak) , r.choice(horuf_kochak) , r.choice(horuf_bozorg) ,r.choice(horuf_bozorg) , r.choice(adad) , r.choice(adad) ,r.choice(adad)
    # password = ""
    # pas = []
    # pas1 = [a  , b , c , d , e ,f ,g ,h]
    # for i in range(8):
    #     pas.append(r.choice(pas1.pop()))
    password = a + d +h + g + e + b + c +f
    # for i in pas:
    #     password += i
    return password

def password_hard(): # ساخت پسورد ساخته شده از اعداد حروف کوچک و بزرگ و کارکتر ها
    a  , b , c , d , e ,f ,g ,h = r.choice(horuf_kochak) , r.choice(horuf_kochak) , r.choice(horuf_bozorg) , r.choice(horuf_bozorg) , r.choice(adad) , r.choice(adad) , r.choice(adad) , r.choice(character)

    password = a + e +c + h +d +f +g +b
    return password

print("سلام به برنامه ساخت پسورد خوش آمدید")

def porsesh() :  # پرسش و انتخاب نوع پسورد توسط کاربر
    password = input("چه نوع پسوردی می خواهید؟ آسان، متوسط، سخت:\n")
    while(True):
        if password == "آسان":
            print(f"پسورد  شما:\n {password_easy()}")
            break
        elif password == "متوسط" :
            print(f"پسورد شما:\n{password_normal()}")
            break
        elif password == "سخت" :
            print(f"پسورد شما:\n{password_hard()}")
            break
        else :
            password = input("لطفا درست پاسخ دهید: چه نوع پسوردی میخواهید؟ آسان، متوسط، سخت:\n")

print(porsesh()) # اجرای تابع بالا برای یک بار


while(True): # درخواست دوباره تولید پسورد توسط کاربر
    pas_digar = input("آیا پسورد دیگری می خواهید? بله، خیر:\n")
    if pas_digar == "بله" :
        print(porsesh())
    elif pas_digar == "خیر" :
        break
    else:
        print("لطفا وقتی ازتان سوال می پرسم درست جواب دهید.\n")
print("برنامه تمام شد. خداحافظ")