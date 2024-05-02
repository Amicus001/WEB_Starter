#import module
import cgi


#an instance for  input tag value in form tag 
form = cgi.FieldStorage() # form 태그 안에 있는 input을 저장해 받아온다. 

# client 요청 데이터 추출하기
if 'image_file' in form and 'message' in form:
    filename = form['image_file']     # form.getvalue(key = 'image_file')
    msg = form['message']      # form.getvalue(key = 'message')



# 요청에 대한 응답 html
print("Content-type: text/html; charset=utf-8") #html 출력, 이 문장은 header
print()

print("<TITLE>this is a script output</TITLE>")
print("<H1>this is a CGI script output</H1>")
print(f"uwu : {form}") ## import error가 나면 버전부터 체크하기


print(f'<img src="{filename}">')
print(f'<h3> {msg}</h3>')
