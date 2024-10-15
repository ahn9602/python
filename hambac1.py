def ptbac1(a, b):
    if a == 0:
        if b == 0:
            print("Phương trình vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        x = -b / a
        print(f"Nghiệm của phương trình là: x = {x}")

# Sử dụng hàm
print("Giải phương trình bậc 1: ax + b = 0")
try:
    a = float(input("Nhập hệ số a: "))
    b = float(input("Nhập hệ số b: "))
    ptbac1(a, b)
except ValueError:
    print("Lỗi: Vui lòng nhập các hệ số là số thực.")
