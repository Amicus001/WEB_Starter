## module import
import cgi, sys, codecs, os
import cgitb
# web encoding----------------------------------------------------------
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())
#--------------------------------------------------------------------
#사용자 정의 함수
#---------------------------------------------------------------------
def show_Browser(result=""):    
    # HTML 파일 읽기: body 문자열
    filename='./html/index.html'
    with open(filename, 'r', encoding='utf-8') as f:
        #html header
        print("Content-Type: text/html; charset=utf-8")
        print() # header / body 구분,  한줄 띄우지 않으면 화면이 나오지 않는다......

        # html body
        print(f.read().format(result))
#--------------------------------------------------------------------
# 요청 처리 / 브라우징
#--------------------------------------------------------------------
## client request data: form data saving instance
form = cgi.FieldStorage()

## data extraction--------------------------------------------------
if 'data' in form and 'num' in form:
    result = form.getvalue('data') + form.getvalue('num')
else:
    result = 'there is no data'


# browsing
show_Browser(result = result)