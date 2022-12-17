def fq():
    p = int(input("введите основание системы, p = "))
    Np = int(input(f"Исходное число N{p} = "))
    k = int(1)
    N10 = int(0)

    while not Np==0:
        N10 = N10 + (Np % 10) * k
        k = k * p
        Np = Np // 10
    print("N10 = ", N10)
def fw():
    a='0123456789'
    nums=list(a)
    print(nums)
def fe():
    N10=int(input("N10="))
    p=int(input("p="))
    k=int(1)
    Np=int(0)
    while not N10==0:
        Np=Np+(N10%p)*k
        k=k*10
        N10=N10//p
    print(f"Np={Np}")
def fr():
    X = int(1)
    Y = int(1)
    Z = int()
    p = int(input("введите p (2<p<10) :"))
    print(p,"-ичная таблица умножения")
    for X in range(1,p):
    z=[]
    for Y in range(1,p):
        Z = (X * Y // p)*10 + (X * Y)%p
        z.append(Z)
    print(z)
def ft():
    morse_dic = {
    'а' : '.-',
    'б' : '-...',    
    'в' : '.--', 
    'г' : '--.', 
    'д' : '-..', 
    'е' : '.', 
    'ж' : '...-', 
    'з' : '--..', 
    'и' : '..', 
    'й' : '.---', 
    'к' : '-.-', 
    'л' : '.-..', 
    'м' : '--', 
    'н' : '-', 
    'о' : '---', 
    'п' : '.--.', 
    'р' : '.-.', 
    'с' : '...', 
    'т' : '-', 
    'у' : '..-', 
    'ф' : '..-.', 
    'х' : '....', 
    'ц' : '-.-.', 
    'ч' : '---.', 
    'ш' : '----', 
    'щ' : '--.-', 
    'ъ' : '.--.-', 
    'ы' : '-.--', 
    'ь' : '-..-', 
    'э' : '..-..', 
    'ю' : '..--', 
    'я' : '.-.-', 
    }

    word = input("Введите слово: ")

    morse_word = '' 
    for letter in word:
    letter = letter.lower()
    
    print(f"{letter}: {morse_dic[letter]}")
def fy():
    a=int(input("введите значение 1k(k принадлежит отрезку [1;5], k принадлежит целым числам)"))
    if a==1:
        fq()
    elif a==2:
        fw()
    elif a==3:
        fe()
    elif a==4:
        fr()
    elif a==5:
        ft()
print('ку')
fy()
