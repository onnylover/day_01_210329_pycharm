#키보드에서 5개의 정수를 입력 받아 리스트에 저장하고 평균을 구하는 프로그램을 작성하시오

count = 0
avg = 0
while count < 5 :
    num = int(input("수를 입력해주세요 : "))
    avg += num
    count += 1
cal = float(avg/5)
print("평균 : %1.1f" %cal)