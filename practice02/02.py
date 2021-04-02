#문제2. 다음과 같은 텍스트에서 모든 태그를 제외한 텍스트만 출력하세요.

s = """
    <html>
        <body style='background-color:#ffff'>
            <h4>Click</h4>
            <a href='http://www.python.org'>Here</a>
            <p>
                To connect to the most powerful tools in the world.
            </p>
        </body>
    </html>
    """

l = s.find("<")
g = s.find(">")
print(l)
print(g)
t = s.replace(s[5],"")
print(t)

#for 문으로 find 함수 조합
#find는 시작 위치, substring 이라는 기능으로 해도 됨

# import re
# def remove_tag(content):
#    cleanr =re.compile('<.*?>')
#    cleantext = re.sub(cleanr, '', content)
#    return cleantext
#
# s = """
#     <html>
#         <body style='background-color:#ffff'>
#             <h4>Click</h4>
#             <a href='http://www.python.org'>Here</a>
#             <p>
#                 To connect to the most powerful tools in the world.
#             </p>
#         </body>
#     </html>
#     """
#
# print(remove_tag(s))