from django.shortcuts import render

# Create your views here.
import time
import MySQLdb
from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="mysql", charset='utf8')
    with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute("SELECT id,rq,sj,sfxs,zbry FROM b_xiaosha ORDER BY rq,sj")
        students = cursor.fetchall()
    return render(request, 'xiaosha/index.html', {'students': students})


def find(request):
    request.encoding = 'utf-8'
    if 'rq1' in request.GET and request.GET['rq1']:
        rq1 = request.GET['rq1']
        rq1=time.strftime("%Y.%m.%d",time.strptime(rq1,"%Y-%m-%d"))
        conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="mysql", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute(
                "SELECT id,rq,sj,sfxs,zbry FROM b_xiaosha where rq =%s  ORDER BY rq,sj",
                [rq1])
            students = cursor.fetchall()
            return render(request, 'xiaosha/index.html', {'students': students})
    else:
        return redirect('../')



# 学生信息新增处理函数
def add(request):
    if request.method == 'GET':
        return render(request, 'xiaosha/add.html')
    else:
        rq = request.POST.get('rq', '')
        sj = request.POST.get('sj', '')
        sfxs = request.POST.get('sfxs', '')
        zbry = request.POST.get('zbry', '')
        conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="mysql", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("INSERT INTO b_xiaosha (rq,sj,sfxs,zbry) values (%s,%s,%s,%s)",[rq, sj, sfxs, zbry])
            conn.commit()
        return redirect('../')


# 学生信息修改处理函数
def edit(request):
    if request.method == 'GET':
        id = request.GET.get("id")
        conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="mysql", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("SELECT id,rq,sj,sfxs,zbry FROM b_xiaosha where id =%s", [id])
            student = cursor.fetchone()
        return render(request, 'xiaosha/edit.html', {'student': student})
    else:
        id = request.POST.get('id', '')
        rq = request.POST.get('rq', '')
        sj = request.POST.get('sj', '')
        sfxs = request.POST.get('sfxs', '')
        zbry = request.POST.get('zbry', '')
        conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="mysql", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("UPDATE b_xiaosha set rq=%s,sj=%s,sfxs=%s,zbry=%s where id =%s", [rq, sj, sfxs, zbry, id])
            conn.commit()
        return redirect('../')


# 学生信息删除处理函数
def delete(request):
    id = request.GET.get("id")
    conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="mysql", charset='utf8')
    with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute("DELETE FROM b_xiaosha WHERE id =%s", [id])
        conn.commit()
    return redirect('../')