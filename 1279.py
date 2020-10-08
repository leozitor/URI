if __name__ == '__main__':
    i = 0
    while True:
        try:

            y = int(input())
            if i != 0:
                print()
            bisexto = False
            huluculu = False
            bulukulu = False

            if y % 15 == 0:
                huluculu = True
            if ((y % 4 == 0) and (y % 100 != 0)) or (y % 400 == 0):
                bisexto = True

            if y % 55 == 0:
                if bisexto:
                    bulukulu = True

            if bisexto:
                print("This is leap year.")
                if huluculu:
                    print("This is huluculu festival year.")
                if bulukulu:
                    print("This is bulukulu festival year.")
            elif huluculu:
                print("This is huluculu festival year.")
            else:
                print("This is an ordinary year.")
            i = 1
        except:
            break
