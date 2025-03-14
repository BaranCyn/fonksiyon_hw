class Human:
    #built_in #constructor #initialize
    def __init__(self,name):
        self.name = name
        print("Bir human instance'i üretildi")
    def talk(self,sentence):
       
        print(f"{self.name}:  {sentence}")
        def walk(self):
            print(f"{self.name} is walking")

            #instance=> örnek
            human1 = Human("Enes")
            
            human1.talk("Merhaba")
            human1.walk()

            human2 = Human("Halit")
          
            human2.talk("Selam")
            human2.walk()


            