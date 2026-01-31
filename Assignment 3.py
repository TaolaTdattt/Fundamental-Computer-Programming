#1
num = 1
while num <= 1000:
    if num % 3 == 0:
        print(num)
    num += 1

#2
while True:
    inches = float(input("Nhập inch vào đây: "))
    if inches < 0:
        break
    cm = inches * 2.54
    print(inches, "inch bằng", cm, "cm")

#3
numbers = []
while True:
    value = input("Nhập số thực vào đây (nếu đã nhập đủ hãy bỏ trống): ")
    if value == "":
        break
    numbers.append(float(value))
print("Số lớn nhất là:", max(numbers))
print("Số nhỏ nhất là:", min(numbers))

#4
import random
number = random.randint(1, 10)
while True:
    guess = int(input("Đoán số từ 1 đến 10: "))
    if guess < number:
        print("Quá nhỏ")
    elif guess > number:
        print("Quá lớn")
    else:
        print("Đúng rồi")
        break

#5
true_user_name = "python"
true_password = "rules"
so_lan_thu = 0
while so_lan_thu < 5:
    user_name = input("Nhập tên đăng nhập: ")
    password = input("Nhập mật khẩu: ")
    
    if user_name == true_user_name and password == true_password:
        print("Welcome")
        break
    else:
        so_lan_thu += 1
        print("Thử lại, tên đăng nhập hoặc mật khẩu không đúng")

if so_lan_thu == 5:
    print("Access denied")

#6
def lay_ky_tu_giua(a):
    n = len(a)
    if n % 2 == 0:
        giua = a[n//2 - 1 : n//2 + 1]
        print("2 ký tự ở giữa là:", giua)
    else:
        giua = a[n//2]
        print("Ký tự ở giữa là:", giua)
lay_ky_tu_giua("LHTD")
lay_ky_tu_giua("HELLO")

#7
def viet_tat(a):
    words = a.split()
    tat = ""
    for word in words:
        tat += word[0].upper()
    return tat
print(viet_tat("unidentified foreign object"))