#klass kalkulaatoriks
class Kalkulaator():
    def liitmine(self,x, y): #defineeritud meetod liitmine
        return x + y
    
    def lahutamine (self, x, y): #defineeritud meetod lahutamine
        return x - y
    
    def korrutamine (self, x, y): #defineeritud meetod korrutamine
        return x * y
    
    def jagamine (self, x, y): #defineeritud meetud jagamine
        if y == 0: #vaatab kas tahetakse jagada nulliga
            return "Viga: Nulliga ei saa jagada." #Kui eelmine tingimus osutus tõeseks väljastab mis ma jutumärkidesse kirjutasin
        return x / y #jagab x y-ga
    
    def ruutjuur (self, x): #defineeritud meetod ruutjuure saamiseks
        if x < 0: #vaatab kas x on negatiivne arv
            return "Viga: Ruutjuur ei saa olla negatiivne." #kui eelmine tingimus osutus tõeseks väljastab jutumärkides oleva lause
        return x ** 0.5 # teeb antud arvust ruutjuure
    
    def astendamine(self, x, y): #defineeritud meetod astendamine
        return x ** y # Teeb astendamise
    
    def jaak(self):                  #jäägi leidmise meetod   
        return self.a % self.b
    
    def protsent(self, x, y): #defineeritud meetod protsendi leidmiseks
        return (x / y) * 100 #arvutab protsendi
    
    

def main(): #kasutaja liides
    kalkulaator = Kalkulaator()
    print("Tere tulemast kalkulaatori rakendusse") # prindib tervituse
    
    while True:
        print("\nVali Tegevus: ") # prindib kasutaja valikud
        print ("1. Liitmine")
        print ("2. Lahutamine")
        print ("3. Korrutamine")
        print ("4. Jagamine")
        print ("5. Ruutjuur")
        print ("6. Astendamine")
        print ("7. Jääk")
        print("8. Protsent")
        print("9. Välju")
        
        valik = int(input("Valige millist tegevust soovite teha(1-9): ")) # küsib kasutajalt mida ta soovib teha
        if valik == 9: # kontrollib kas kasutaja sisestus on 9
            print("Aitäh kalkulaatori rakenduse kasutamise eest!") #kui tingimus oli tõene prindib minu antud lause
            break #lõpetab tegevuse
        num1 = float(input("Sisestage esimene number: ")) #küsib kasutajal siestada esimese arvu millega soovitakse arvutada
        if valik !=5: #Kontrollib kas kasutaja sisestus ei olnud 5 kui oli liigub edasi kui ei olnud läheb edasi ja küsib kasutajalt teist numbrit
            num2 = float(input("Sisestage teine number: ")) #küsib kasutajal siestada teise arvu millega soovitakse arvutada
            
        if valik == 1: #Kui kasutaja valik oli 1 läheb siit edasi
            print("Tulemus: ", kalkulaator.liitmine(num1,num2)) # prindib tulemuse
        elif valik == 2: #Kui kasutaja valik oli 2 läheb siit edasi
            print("Tulemus: ", kalkulaator.lahutamine(num1,num2)) # prindib tulemuse
        elif valik == 3: #Kui kasutaja valik oli 3 läheb siit edasi
            print("Tulemus: ", kalkulaator.korrutamine(num1,num2)) # prindib tulemuse
        elif valik == 4: #Kui kasutaja valik oli 4 läheb siit edasi
            print("Tulemus: ", kalkulaator.jagamine(num1,num2)) # prindib tulemuse
        elif valik == 5: #Kui kasutaja valik oli 5 läheb siit edasi
            print("Tulemus: ", kalkulaator.ruutjuur(num1)) # prindib tulemuse
        elif valik == 6: #Kui kasutaja valik oli 6 läheb siit edasi
            print("Tulemus: ", kalkulaator.astendamine(num1,num2)) # prindib tulemuse
        elif valik == 7: #Kui kasutaja valik oli 7 läheb siit edasi
            print ("Tulemus: ", kalkulaator.jaak(num1,num2)) # prindib tulemuse
        elif valik == 8: #Kui kasutaja valik oli 8 läheb siit edasi
            print("Tulemus: ", kalkulaator.protsent(num1,num2)) # prindib tulemuse
        else: #Kui kasutaja valik ei olnud midagi valikutest  läheb siit edasi
            print("Vale sisestus, proovige uuesti.") # prindib tulemuse
            
if __name__ == "__main__":
    main()