# nested function

# def bicara(abjad):
#     def bilang(kata):
#         print(kata)

#     kalimat = abjad.split(' ')
#     for kata in kalimat:
#         bilang(kata)

# bicara("Coba untuk cetak sesuatu hal yang oke")


# print('='*30)

### ==========================================

# def count():
#     count = 0

#     def increment():
#         nonlocal count
#         count += 1
#         print(count)

#     increment()

# count()


# print('='*30)

### ========================================

# # closures

# def counter():
#     count = 0

#     def increment():
#         nonlocal count
#         count += 1
#         return count

#     return increment

# increment = counter()

# print(increment())
# print(increment())
# print(increment())
# print(increment())
# print(increment())
# print(increment())


# print('='*30)

### ======================================

# def logtime(func):
#     def wrapper():

#         val = func()
        
#         return val
#     return wrapper


# print(set(map(int, input().split())))

### =============================================

# for col in range(4):
#     if col % 2 == 0:
      
#          print(" |||||||| ")
#          print("||||||||||")
#          print("||||||||||")
#          print(" |||||||| ")
#     else:
#         print("----")

### ==============================================

# from time import sleep

# def finder(a, b):
#   ans1 = []
#   ans2 = []
#   for i in range(a, b + 1):
#     for j in range(2, i + 1):
#       if i % j == 0:
#         ans1.append(j)
      
#     if len(ans1) == 1:
#       ans2.append(i)
#       ans1.clear()

#     else:
#       ans1.clear()

#   print(f"Prime numbers between {a} and {b} are {ans2}")

# start = int(input("Enter lower number : "))
# end = int(input("Enter higher number : "))

# sleep(0.5)
# finder(start, end)

### ===============================================

# class burung:
#     spesies = "burung"

#     def __init__(self, namex, foody):
#         self.name = namex
#         self.food = foody
# ayama = burung("ayam", "cacing")
# bebeka = burung("bebek", "ikan")

# print(f"semua makan {ayama.name} juga {ayama.food}")
# print(ayama.name)
# print(ayama.food)
# print("bebek adalah {}".format(bebeka.__class__.spesies))
# print("{} makan {}".format(bebeka.name,bebeka.food))

### ===============================================

## from tkinter import *
## import webbrowser

## class win(Tk):
##     def__init__(self):
##         super().__init__()
##         d = ("Comic Sans Ms",10)
##         self['bg'] = '#007bff'
##         self.t = Button(self, text='google.com',font=d, command=lambda:
##     webbrowser.open('http://google.com'))
##         self.t.bind("<Motion>"self.p)
##         self.t.pack()
##     def p(self, event):
##         event.widget["font"] = d =('Comic Sans Ms',10,'italic')

## e = win()
## e.mainloop()

### =======================================

# from datetime import datetime, timedelta

# years = datetime(2021, 1, 1)
# times = timedelta(days=0, hours=12, minutes=0)

# result = (years + x * times for x in range(20))

# print('\n'.join(map("{:%Y-%m-%d %H:%M:%S}".format, result)))

### ======================================

# class computer():

#     def __init__(self):
#         self.__maxprice = 900

#     def sell(self):
#         print("Selling price : {}".format(self.__maxprice))

#     def setMaxPrice(self, price):
#         self.__maxprice = price

# co = computer()
# co.sell()

# co.__maxprice = 1000
# co.sell()

# co.setMaxPrice(1010)
# co.sell()


### ====================================

# class parrot:

#     def fly(self):
#         print("Parrot can fly")

#     def swim(self):
#         print("Parrot can't swim")

# class penguin:

#     def fly(self):
#         print("Penguin can't fly")

#     def swim(self):
#         print("Penguin can swim")

# def flyTest(bird):
#     bird.fly()
# def swimTest(bird):
#     bird.swim()

# bluu = parrot()
# pegg = penguin()

# flyTest(bluu)
# flyTest(pegg)
# swimTest(bluu)
# swimTest(pegg)

### =======================================

# def tambah(angka):
#     total = angka + 5
#     return total

# print(tambah(5))

### -------------------------------------

# tambah2 = lambda angka: angka+2
# print(tambah2(2))

### =======================================

# class animal:
#     def __init__(self, namez, agez):
#         self.name = namez
#         self.age = agez
    
#     def greet(self):
#         print("Hello : ",self.name)

# class cat(animal):
#     def __init__(self, namez, agez, foody, colorz):
#         super().__init__(namez, agez)
#         self.food = foody
#         self.color = colorz

# class dog(animal):
#     def __init__(self, namez, agez, feelz):
#         super().__init__(namez, agez)
#         self.feel = feelz

# cat1 = cat("oyen", 1, "ciki", "pink")
# dog1 = dog("dogo", 3, "happy")

# print(cat1.__dict__)
# print(dog1.__dict__)

# cat1.greet()
# dog1.greet()

### =======================================

# name = 'QQQ'
# age = 10
# hobby = 'play'

# print(f"hi {name} you're {age} years old u {hobby} right?")

### =======================================


