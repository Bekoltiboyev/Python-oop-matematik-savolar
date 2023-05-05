# ================ Beknazar Oltiboyev ================

import random as r
import operator
import random
# 1 darajali savolar 
# 1-5 sonlarni random 
# 2 darajali savolar 
# 1-10 sonlarni random
# 3 darajali savolar 
# 1-15 sonlarni random
# 4 darajali savolar 
# 1-20 sonlarni random 
# 5 darajali savolar 
# 1-25 sonlarni random va +,-,*,/ amalarni ham random qiling
# 6 darajali savolar 
# 1-20 sonlarni random va +,-,*,/ amalarni ham random qiling


ismi = input("ismingizni kiriting: ")
daraja = int(input("savolar qiyinlik darajasini tanlang 1,2,3,4,5: "))


class Matematika:
    def __init__(self, ism):
        self.ism = ism
    def one_dagre(self):
        arifmetik = input("arifmetik operatorni tanglang +,-,*,/: ")
        
        if arifmetik == "+":
            togri = 0
            xato = 0
            for i in range(1, 21):
                x = r.randint(1,5)
                y = r.randint(1,5)
                sv = int(input(f"{x} + {y} = "))
                if sv == x+y:
                    togri += 1
                else:
                    xato += 1  
            print(f"{togri} ta togri {xato } ta xato qildingiz {self.ism}")  
        elif arifmetik == "-":
            togri = 0
            xato = 0
            for i in range(1, 21):
                x = r.randint(1,5)
                y = r.randint(1,5)
                sv = int(input(f"{x} - {y} = "))
                if sv == x-y:
                    togri += 1
                else:
                    xato += 1 
            print(f"{togri} ta togri {xato } ta xato qildingiz {self.ism}")         
        elif arifmetik == "*":
            togri = 0
            xato = 0
            for i in range(1, 21):
                x = r.randint(1,5)
                y = r.randint(1,5)
                sv = int(input(f"{x} * {y} = "))
                if sv == x*y:
                    togri += 1
                else:
                    xato += 1
            print(f"{togri} ta togri {xato } ta xato qildingiz {self.ism}") 
            
        else:
            togri = 0
            xato = 0
            for i in range(1, 21):
                x = r.randint(1,5)
                y = r.randint(1,5)
                sv = float(input(f"{x} / {y} = "))
                if sv == x/y:
                    togri += 1
                else:
                    xato += 1
            print(f"{togri} ta togri {xato } ta xato qildingiz {self.ism}")           
    def two_dagre(self):
        arifmetik = input("arifmetik operatorni tanglang +,-,*,/: ")
        
        if arifmetik == "+":
            togri = 0
            xato = 0
            for i in range(1, 21):
                x = r.randint(1,10)
                y = r.randint(1,10)
                sv = int(input(f"{x} + {y} = "))
                if sv == x+y:
                    togri += 1
                else:
                    xato += 1  
            print(f"{togri} ta togri {xato } ta xato qildingiz {self.ism}")  
        elif arifmetik == "-":
            togri = 0
            xato = 0
            for i in range(1, 21):
                x = r.randint(1,10)
                y = r.randint(1,10)
                sv = int(input(f"{x} - {y} = "))
                if sv == x-y:
                    togri += 1
                else:
                    xato += 1 
            print(f"{togri} ta togri {xato } ta xato qildingiz {self.ism}")         
        elif arifmetik == "*":
            togri = 0
            xato = 0
            for i in range(1, 21):
                x = r.randint(1,10)
                y = r.randint(1,10)
                sv = int(input(f"{x} * {y} = "))
                if sv == x*y:
                    togri += 1
                else:
                    xato += 1
            print(f"{togri} ta togri {xato } ta xato qildingiz {self.ism}") 
            
        else:
            togri = 0
            xato = 0
            for i in range(1, 21):
                x = r.randint(1,10)
                y = r.randint(1,10)
                sv = float(input(f"{x} / {y} = "))
                if sv == x/y:
                    togri += 1
                else:
                    xato += 1
            print(f"{togri} ta togri {xato } ta xato qildingiz {self.ism}")           
    def three_dagre(self):
        arifmetik = input("arifmetik operatorni tanglang +,-,*,/: ")
        
        if arifmetik == "+":
            togri = 0
            xato = 0
            for i in range(1, 21):
                x = r.randint(1,15)
                y = r.randint(1,15)
                sv = int(input(f"{x} + {y} = "))
                if sv == x+y:
                    togri += 1
                else:
                    xato += 1  
            print(f"{togri} ta togri {xato } ta xato qildingiz {self.ism}")  
        elif arifmetik == "-":
            togri = 0
            xato = 0
            for i in range(1, 21):
                x = r.randint(1,15)
                y = r.randint(1,15)
                sv = int(input(f"{x} - {y} = "))
                if sv == x-y:
                    togri += 1
                else:
                    xato += 1 
            print(f"{togri} ta togri {xato } ta xato qildingiz {self.ism}")         
        elif arifmetik == "*":
            togri = 0
            xato = 0
            for i in range(1, 21):
                x = r.randint(1,15)
                y = r.randint(1,15)
                sv = int(input(f"{x} * {y} = "))
                if sv == x*y:
                    togri += 1
                else:
                    xato += 1
            print(f"{togri} ta togri {xato } ta xato qildingiz {self.ism}") 
            
        else:
            togri = 0
            xato = 0
            for i in range(1, 21):
                x = r.randint(1,15)
                y = r.randint(1,15)
                sv = float(input(f"{x} / {y} = "))
                if sv == x/y:
                    togri += 1
                else:
                    xato += 1
            print(f"{togri} ta togri {xato } ta xato qildingiz {self.ism}")           
    def two_dagre(self):
        arifmetik = input("arifmetik operatorni tanglang +,-,*,/: ")
        
        if arifmetik == "+":
            togri = 0
            xato = 0
            for i in range(1, 21):
                x = r.randint(1,25)
                y = r.randint(1,25)
                sv = int(input(f"{x} + {y} = "))
                if sv == x+y:
                    togri += 1
                else:
                    xato += 1  
            print(f"{togri} ta togri {xato } ta xato qildingiz {self.ism}")  
        elif arifmetik == "-":
            togri = 0
            xato = 0
            for i in range(1, 21):
                x = r.randint(1,20)
                y = r.randint(1,20)
                sv = int(input(f"{x} - {y} = "))
                if sv == x-y:
                    togri += 1
                else:
                    xato += 1 
            print(f"{togri} ta togri {xato } ta xato qildingiz {self.ism}")         
        elif arifmetik == "*":
            togri = 0
            xato = 0
            for i in range(1, 21):
                x = r.randint(1,20)
                y = r.randint(1,20)
                sv = int(input(f"{x} * {y} = "))
                if sv == x*y:
                    togri += 1
                else:
                    xato += 1
            print(f"{togri} ta togri {xato } ta xato qildingiz {self.ism}") 
            
        else:
            togri = 0
            xato = 0
            for i in range(1, 21):
                x = r.randint(1,20)
                y = r.randint(1,20)
                sv = float(input(f"{x} / {y} = "))
                if sv == x/y:
                    togri += 1
                else:
                    xato += 1
            print(f"{togri} ta togri {xato } ta xato qildingiz {self.ism}")           
    def four_dagre(self):
        arifmetik = input("arifmetik operatorni tanglang +,-,*,/: ")
        
        if arifmetik == "+":
            togri = 0
            xato = 0
            for i in range(1, 21):
                y = r.randint(1,25)
                x = r.randint(1,25)
                sv = int(input(f"{x} + {y} = "))
                if sv == x+y:
                    togri += 1
                else:
                    xato += 1  
            print(f"{togri} ta togri {xato } ta xato qildingiz {self.ism}")  
        elif arifmetik == "-":
            togri = 0
            xato = 0
            for i in range(1, 21):
                x = r.randint(1,25)
                y = r.randint(1,25)
                sv = int(input(f"{x} - {y} = "))
                if sv == x-y:
                    togri += 1
                else:
                    xato += 1 
            print(f"{togri} ta togri {xato } ta xato qildingiz {self.ism}")         
        elif arifmetik == "*":
            togri = 0
            xato = 0
            for i in range(1, 21):
                x = r.randint(1,25)
                y = r.randint(1,25)
                sv = int(input(f"{x} * {y} = "))
                if sv == x*y:
                    togri += 1
                else:
                    xato += 1
            print(f"{togri} ta togri {xato } ta xato qildingiz {self.ism}") 
    def aralash(self):
            togri = 0
            xato = 0
            operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul)]
            for i in range(10):
                a = random.randint(1, 20)
                b = random.randint(1, 20)
                op, fn = random.choice(operators)
                prompt = "{} {} {}?\n".format(a, op, b)
                if int(input(prompt)) == fn(a, b):
                    togri += 1
                    print("to'g'ri")
                else:
                    xato += 1
                    print("xato")
            print(f"{togri} ta togri {xato } ta xato qildingiz {self.ism}") 
            
        

matem = Matematika(ismi)
if daraja == 1:
    matem.one_dagre()
elif daraja == 2:
    matem.two_dagre()
elif daraja == 3:
    matem.three_dagre()
elif daraja == 4:
    matem.four_dagre()
else:
    matem.aralash()

