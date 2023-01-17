str_lst = input('문자열을 입력하세요. : ')

s1, s2, s3 = str_lst.split()
if s1.lower()[-1] == s2.lower()[0] and s2.lower()[-1] == s3.lower()[0] :
    print("Pass")
else :
    print("Fail")