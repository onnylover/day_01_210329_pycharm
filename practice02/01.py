
#파이썬 경로명 s = '/usr/local/bin/python' 에서 각각의 디렉토리 경로명을 분리하여 출력하세요.

s = '/usr/local/bin/python'
s = s.lstrip("/")
l = s.split("/")
print(l)

ll = s.rsplit("python")
ll.pop()
ll.append("python")
print(ll)

# l = s.split("/")
# l.pop(0)
# print(l)
#
# ll = s.rsplit("python")
# ll.pop()
# ll.append("python")
# print(ll)