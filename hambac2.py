import math

def giai_phuong_trinh_bac_3(a, b, c, d):
    """
    Giải phương trình bậc 3 dạng ax^3 + bx^2 + cx + d = 0.

    Args:
    a, b, c, d (float): Các hệ số của phương trình bậc 3.

    Returns:
    None: In kết quả ra màn hình.
    """
    if a == 0:
        print("Đây không phải là phương trình bậc 3.")
        return

    p = (3*a*c - b**2) / (3*a**2)
    q = (2*b**3 - 9*a*b*c + 27*a**2*d) / (27*a**3)

    delta = (q**2/4) + (p**3/27)

    if delta > 0:
        u = math.cbrt(-q/2 + math.sqrt(delta))
        v = math.cbrt(-q/2 - math.sqrt(delta))
        x1 = u + v - b/(3*a)
        x2 = -(u + v)/2 - b/(3*a) + 1j * math.sqrt(3)/2 * (u - v)
        x3 = -(u + v)/2 - b/(3*a) - 1j * math.sqrt(3)/2 * (u - v)
        print(f"Phương trình có một nghiệm thực và hai nghiệm phức:")
        print(f"x1 = {x1:.4f}")
        print(f"x2 = {x2:.4f}")
        print(f"x3 = {x3:.4f}")
    elif delta == 0:
        if p == q == 0:
            x = -b / (3*a)
            print(f"Phương trình có nghiệm bội bậc 3: x = {x:.4f}")
        else:
            x1 = -3*q/(2*p) - b/(3*a)
            x2 = x3 = 3*q/(2*p) - b/(3*a)
            print(f"Phương trình có một nghiệm đơn và một nghiệm kép:")
            print(f"x1 = {x1:.4f}")
            print(f"x2 = x3 = {x2:.4f}")
    else:
        phi = math.acos(-q/(2*math.sqrt(-(p**3/27))))
        x1 = 2 * math.sqrt(-p/3) * math.cos(phi/3) - b/(3*a)
        x2 = 2 * math.sqrt(-p/3) * math.cos((phi + 2*math.pi)/3) - b/(3*a)
        x3 = 2 * math.sqrt(-p/3) * math.cos((phi + 4*math.pi)/3) - b/(3*a)
        print(f"Phương trình có ba nghiệm thực phân biệt:")
        print(f"x1 = {x1:.4f}")
        print(f"x2 = {x2:.4f}")
        print(f"x3 = {x3:.4f}")

# Sử dụng hàm
print("Giải phương trình bậc 3: ax^3 + bx^2 + cx + d = 0")
try:
    a = float(input("Nhập hệ số a: "))
    b = float(input("Nhập hệ số b: "))
    c = float(input("Nhập hệ số c: "))
    d = float(input("Nhập hệ số d: "))
    giai_phuong_trinh_bac_3(a, b, c, d)
except ValueError:
    print("Lỗi: Vui lòng nhập các hệ số là số thực.")
