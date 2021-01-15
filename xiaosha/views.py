from django.shortcuts import render

# Create your views here.
import MySQLdb
from django.shortcuts import render, redirect


# Create your views here.
# 故障处理记录处理函数
def index(request):
    rq1 = request.POST.get('rq1')
    conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="mysql", charset='utf8')
    if rq1 is None :
        # print(rq1)
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("SELECT id,rq,sj,sfxs,zbry FROM b_xiaosha ORDER BY rq,sj")
            students = cursor.fetchall()
        return render(request, 'xiaosha/index.html', {'students': students})
    else:
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute(
                "SELECT id,rq,sj,sfxs,zbry FROM b_xiaosha where rq =%s  ORDER BY rq,sj",
                [rq1])
            students = cursor.fetchall()
        return render(request, 'xiaosha/index.html', {'students': students})