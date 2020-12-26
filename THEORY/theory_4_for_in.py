days = ("Mon", "Tue", "Wed", "Thu", "Fir")

# x is variable
# day란 변수가 생성되는시점은 작업이 시작되는 시점에서 생김
for day in days:
    print(day)

# if else in for
for day in days:
    if day is "Wed":
        break
    else:
        print(day)