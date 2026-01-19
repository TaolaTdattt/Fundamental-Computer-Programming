#1
Size_limit = 42
length = float(input("Nhập chiều dài của con cái: "))

if length >= Size_limit:
    print("Đã đạt yêu cầu về chiều dài")
else:
    difference = Size_limit - length
    print("Thả cá về hồ!")
    print("Con cá ngắn hơn hơn kích thước quy định", difference, "cm")


#2
Class = input("Nhập hạng cabin của bạn(lưu ý viết hoa tất cả các chữ cái): ")
if Class == "LUX":
    print("Cabin ở boong trên cùng, có ban công.")
elif Class == "A":
    print("Nằm phía trên khoang để xe oto, có cửa sổ.")
elif Class == "B":
    print("Cabin không có cửa sổ, nằm phía trên khoang để xe oto.")
elif Class == "C":
    print("Cabin không có cửa sổ, nằm phía dưới khoang xe oto.")
else:
    print("Hạng cabin không hợp lệ.")


#3
biological_sex = input("Nhập giới tính sinh học của bạn (Male/Female): ")
hemoglobin_value = float(input("Nhập mức hemoglobin của bạn (g/L): "))

if biological_sex == "Male":
    if hemoglobin_value < 134:
        print("giá trị hemoglobin thấp")
    elif 134 < hemoglobin_value < 167:
        print("giá trị hemoglobin bình thường")
    else:
        print("giá trị hemoglobin cao")

elif biological_sex == "Female":
    if hemoglobin_value < 117:
        print("giá trị hemoglobin thấp")
    elif 117 < hemoglobin_value < 155:
        print("giá trị hemoglobin bình thường")
    else:
        print("giá trị hemoglobin cao")


#4
Year = int(input("Nhập năm bạn muốn kiểm tra: "))
if (Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0):
    print(Year, "là năm nhuận")
else:
    print(Year, "không phải là năm nhuận")


#5
Diameter1 = float(input("Nhập đường kính pizza thứ 1 (cm): "))
Diameter2 = float(input("Nhập đường kính pizza thứ 2 (cm): "))
Price1 = float(input("Nhập giá tiền pizza thứ 1 (USD): "))
Price2 = float(input("Nhập giá tiền pizza thứ 2 (USD): "))

import math
Radi1 = Diameter1 / 2
Area1 = math.pi * (Radi1 ** 2)
a = Price1 / Area1

Radi2 = Diameter2 / 2
Area2 = math.pi * (Radi2 ** 2)
b = Price2 / Area2

if a < b:
    print("Pizza thứ 1 rẻ hơn")
elif b < a:
    print("Pizza thứ 2 rẻ hơn")
else:
    print("Giá tiền của hai loại pizza bằng nhau")