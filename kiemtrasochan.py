def kiem_tra_so_chan(n):
    if n % 2 == 0:
        return True
    else:
        return False

# Chạy thử chương trình
so = int(input("Nhập một số nguyên: "))

if kiem_tra_so_chan(so):
    print(f"{so} là số chẵn")
else:
    print(f"{so} là số lẻ")