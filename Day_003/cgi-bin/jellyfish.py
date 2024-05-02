# url: http://localhost:8080/cgi-bin/jellyfish.py

## module import
import cgi, sys, codecs, os, cgitb
from pydoc import html
import torch

# web encoding-----------------------------------------------------
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())
# -----------------------------------------------------------------

# 함수 선언------------------------------------------------
def show_Browser(result=""):
    filename = '../jellyfish.html'
    with open(filename, 'r', encoding='utf-8') as f:
        webpage = f.read()
    print("Content-Type: text/html; charset=utf-8")
    print()
    print(webpage.format(result))

# ----------------------------------------------------------------
# 판정
# -----------------------------------------------------------------

def detection(text):
    res = md.predict(text)
    return str(res[0])

# ----------------------------------------------------------------
# 기능 구현
# 학습 데이터 읽기------------------------------------------------
model_path = os.path.dirname(__file__)+'../Day_002_01/cgi-bin/model_JellyFish_best.pth'
from torch import load
md = load(model_path)

# 웹페이지 form에 input값 가져오기
form = cgi.FieldStorage()
img = form.getvalue('JellyfishImage')

# 판정하기
if img is not None:
    result_dict = {0:'Barrel', 1: 'blue', 2:'compass', 3:'lions mane', 4:'mauve stinger', 5:"Moon"}
    result = detection(img)
    result = "🪼🪼this is a {} Jellyfish! 🪼🪼"
else: 
    result = 'there is no data'

# web 출력------------------------------------------------

show_Browser(result = result)