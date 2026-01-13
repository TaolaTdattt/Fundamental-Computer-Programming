#1
name = input("Nhap ten cua ban: ")
print("Xin chào " + name)

#2
a = int(input("Nhập bán kính hình tròn: ") )
Chu_vi = 2 * 3.14 * a

print("Chu vi hình tròn là: ", Chu_vi)


#3
a = int(input("Nhập chiều dài hình chữ nhật: ") )
b = int(input("Nhập chiều rộng hình chữ nhật: ") )

Chu_vi = 2 * (a + b)
Dien_tich = a * b

print("Chu vi hình chữ nhật là: ", Chu_vi)
print("Diện tích hình chữ nhật là: ", Dien_tich)


#4
a = float(input("Nhập số nguyên a: ") )
b = float(input("Nhập số nguyên b: ") )
c = float(input("Nhập số nguyên c: ") )

Tong = a + b + c
Tich = a * b * c
Gia_tri_trung_binh = Tong / 3

print("Tổng 3 số nguyên là: ", Tong)
print("Tích 3 số nguyên là: ", Tich)
print("Giá trị trung bình của 3 số nguyên là: ", Gia_tri_trung_binh)


#5
talents = float(input("Nhập talents vào đây: ") )
pounds = float(input("Nhập pounds vào đây: ") )
lots = float(input("Nhập lots vào đây: ") )

Tong = (talents * 20 * 32 * 13.3) + (pounds * 32 * 13.3) + (lots * 13.3)
Kilograms = Tong // 1000
grams = Tong % 1000

print (Kilograms, "kg", grams, "g")


#6
import random
Mk3 = ""
for i in range(3):
    Mk3 += str(random.randint(0, 9))

Mk4 = ""
for i in range(4):
    Mk4 += str(random.randint(1, 6))

print("Mã khóa 3 số là: ", Mk3)
print("Mã khóa 4 số là: ", Mk4)
