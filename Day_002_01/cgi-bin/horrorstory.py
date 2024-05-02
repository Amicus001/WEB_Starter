# url: http://localhost:8080/cgi-bin/horrorstory.py

## module import
import cgi, sys, codecs, os, cgitb
from pydoc import html
import torch

# web encoding-----------------------------------------------------
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())
# -----------------------------------------------------------------
# 함수 선언
def show_Browser(result=""):
    filename= './html/index.html'
    with open(filename, 'r', encoding='utf-8') as f:
        webpage = f.read()
    print("Content-Type: text/html; charset=utf-8")
    print()
    print(webpage.format(result))
# ----------------------------------------------------------------
# 판정
def detection(text):
    res = md.predict(text)
    return str(res[0])

#-----------------------------------------------------------------
# 기능 구현
# 학습 데이터 읽기
model_path= os.path.dirname(__file__)+'./model_scarystory.pth'
from torch import load
md = load(model_path)
# webpage form-> input list
form = cgi.FieldStorage()
text = form.getvalue('text')

# 판정
if text is not None:
    result_dict = {0:'추리형', 1:'경험담형'}
    result = detection(text)
    result = '이야기 : {}, 결과: {}입니다. '
else:
    result = 'there is no data'

# web 출력
show_Browser(result)