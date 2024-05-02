#import module
import cgi,sys,codecs,os,cgitb
import datetime

#an instance for  input tag value in form tag 
form = cgi.FieldStorage() # form 태그 안에 있는 input을 저장해 받아온다. 
# 인코딩
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())
# client 요청 데이터 추출하기

if 'image_file' in form and 'message' in form:
    fileitem= form['image_file']     # form.getvalue(key = 'image_file')
    msg = form['message']            # form.getvalue(key = 'message')
   
    suffix = datetime.datetime.now().strftime('%y%m%d_%H%M%S')
    img_file = fileitem.filename
    save_path =f'./image/{img_file}'

# 서버에 이미지파일 저장하는 코드-----------------------------------------------

    with open(file=save_path, mode='wb') as f:
        f.write(fileitem.file.read())

    img_path = f'../image/{suffix}_{img_file}'
else: 
    img_path = "None" 
    msg = "None"   # 웹이 아니라 파이썬에서 실행하는 거
#-------------------------------------------------------------------------

# 요청에 대한 응답 html
print("Content-type: text/html; charset=utf-8") #html 출력, 이 문장은 header
print()

print("<TITLE>this is a script output</TITLE>")
print("<H1>this is a CGI script output</H1>")
# print(f"uwu : {form}") ## import error가 나면 버전부터 체크하기


print(f'<img src="{img_path}">')
# print(f'<h3> {fileitem}</h3>')
print(f'<h3> {msg}</h3>')