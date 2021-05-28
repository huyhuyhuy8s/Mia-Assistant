while True:
    num = input("Vui lòng nhập vào một con số nhé! ")
    try:
        val = int(num)
        print("Dữ liệu bạn nhập vào là số.")
        print("Giá trị của nó là: ", val)
        break; # Thoát khỏi vòng lặp
    except ValueError:
        try:
            val = float(num)
            print("Dữ liệu nhập vào là float")
            print("Giá trị của nó là: ", val)
            break; # Thoát khỏi vòng lặp
        except ValueError:
            print("Đây không phải là một số, vui lòng nhập lại!")