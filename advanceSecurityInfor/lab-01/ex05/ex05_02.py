import re

chuoi = input("Nhập chuỗi: ")  # Ví dụ: -100#^sdfkj8902w3ir021@swf-20
cac_so = [int(x) for x in re.findall(r'-?\d+', chuoi)]

tong_duong = sum(x for x in cac_so if x > 0)
tong_am = sum(x for x in cac_so if x < 0)

print(f"Giá trị dương: {tong_duong}. Giá trị âm: {tong_am}.")