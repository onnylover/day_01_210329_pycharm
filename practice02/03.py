
#문제3.
#1)다음 문자열을 모든 소문자를 대문자로 변환하고, 문자 ',', '.','\n'를 없앤 후에 중복 없이 각 단어를 순서대로 출력하세요.
s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""

target = [", ",". ","\n","."]
i = 0
while i < len(target):
     s = s.replace(str(target[i])," ")
     i += 1
s = s.upper()
s = s.rstrip()
l = s.split(" ")
l.sort()
nodup = list(set(l))
nodup.sort()
i = 0
while i < len(nodup):
    print(nodup[i])
    i += 1
print()

# #2)각 단어의 빈도수도 함께 출력해 보세요
target = [", ",". ","\n","."]
i = 0
while i < len(target):
     s = s.replace(str(target[i])," ")
     i += 1
s = s.upper()
s = s.rstrip()
l = s.split(" ")
l.sort()
nodup = list(set(l))
nodup.sort()
i = 0
while i < len(nodup):
    print("%s : %d" %(nodup[i],l.count(nodup[i])))
    i += 1