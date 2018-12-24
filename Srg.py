number = random.randint (1,10)
tries = 1

playername = input("Merhaba, isminiz nedir?")
print ("Hoşgeldin" , playername , ".")

question = input ("Aklımda bir oyun var. Oynamak ister misin? [Y/N]")
if question == "n":
    print ("Pekala.. Oynamak istediğinde tekrar gel.")
elif question == "y":
    print ("Aklımda 1 ve 10 arasında bir sayı var!")
    guess = int(input("Tahminini yap:"))
    if guess > number:
        print ("Daha küçük...")
    elif guess < number:
        print ("Daha büyük...")

while guess != number:
    tries += 1
    guess = int(input("Tekrar dene:"))
    if guess < number:
        print ("Daha büyük...")
    elif guess > number:
        print ("Daha küçük...")

if guess == number:
    print("Tahminin doğru! Sayı:" , number , "idi ve" , tries , "denemede buldun!")
