from django.shortcuts import render

# Create your views here.
import time
import MySQLdb
from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="mysql", charset='utf8')
    with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute("SELECT id,xlqk,gzcl,xjr,shr,rq,bz FROM b_yysxj ORDER BY rq")
        students = cursor.fetchall()
    return render(request, 'yunyingshang/index.html', {'students': students})


def find(request):
    request.encoding = 'utf-8'
    if 'rq1' in request.GET and request.GET['rq1']:
        rq1 = request.GET['rq1']
        rq1=time.strftime("%Y.%m.%d",time.strptime(rq1,"%Y-%m-%d"))
        conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="mysql", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute(
                "SELECT id,xlqk,gzcl,xjr,shr,rq,bz FROM b_yysxj where rq =%s  ORDER BY rq",
                [rq1])
            students = cursor.fetchall()
            return render(request, 'yunyingshang/index.html', {'students': students})
    else:
        return redirect('../')



# 学生信息新增处理函数
def add(request):
    if request.method == 'GET':
        return render(request, 'yunyingshang/add.html')
    else:
        xlqk = request.POST.get('xlqk', '')
        gzcl = request.POST.get('gzcl', '')
        xjr = request.POST.get('xjr', '')
        shr = request.POST.get('shr', '')
        rq = request.POST.get('rq', '')
        bz = request.POST.get('bz', '')
        conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="mysql", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("INSERT INTO b_yysxj (xlqk,gzcl,xjr,shr,rq,bz) values (%s,%s,%s,%s,%s,%s)",[xlqk,gzcl,xjr,shr,rq,bz])
            conn.commit()
        return redirect('../')


# 学生信息修改处理函数
def edit(request):
    if request.method == 'GET':
        id = request.GET.get("id")
        conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="mysql", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("SELECT id,xlqk,gzcl,xjr,shr,rq,bz FROM b_yysxj where id =%s", [id])
            student = cursor.fetchone()
        return render(request, 'yunyingshang/edit.html', {'student': student})
    else:
        id = request.POST.get('id', '')
        xlqk = request.POST.get('xlqk', '')
        gzcl = request.POST.get('gzcl', '')
        xjr = request.POST.get('xjr', '')
        shr = request.POST.get('shr', '')
        rq = request.POST.get('rq', '')
        bz = request.POST.get('bz', '')
        conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="mysql", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("UPDATE b_yysxj set xlqk=%s,gzcl=%s,xjr=%s,shr=%s,rq=%s,bz=%s where id =%s", [xlqk,gzcl,xjr,shr,rq,bz,id])
            conn.commit()
        return redirect('../')


# 学生信息删除处理函数
def delete(request):
    id = request.GET.get("id")
    conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="mysql", charset='utf8')
    with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute("DELETE FROM b_yysxj WHERE id =%s", [id])
        conn.commit()
    return redirect('../')