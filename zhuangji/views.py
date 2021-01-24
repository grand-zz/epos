from django.shortcuts import render

# Create your views here.
import MySQLdb
from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="mysql", charset='utf8')
    with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute("SELECT id,shh,pp,pwh,azlx,zjsl,azrq,zjry,bz FROM b_zhuangjijilv ORDER BY azrq")
        students = cursor.fetchall()
    return render(request, 'zhuangji/index.html', {'students': students})


def find(request):
    request.encoding = 'utf-8'
    if 'rq1' in request.GET and request.GET['rq1']:
        rq1 = request.GET['rq1']
        conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="mysql", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute(
                "SELECT id,shh,pp,pwh,azlx,zjsl,azrq,zjry,bz  FROM b_zhuangjijilv where azrq =%s  ORDER BY azrq",
                [rq1])
            students = cursor.fetchall()
            return render(request, 'zhuangji/index.html', {'students': students})
    else:
        return redirect('../')



# 学生信息新增处理函数
def add(request):
    if request.method == 'GET':
        return render(request, 'zhuangji/add.html')
    else:
        shh = request.POST.get('shh', '')
        pp = request.POST.get('pp', '')
        pwh = request.POST.get('pwh', '')
        azlx = request.POST.get('azlx', '')
        zjsl = request.POST.get('zjsl', '')
        azrq = request.POST.get('azrq', '')
        zjry = request.POST.get('zjry', '')
        bz = request.POST.get('bz', '')
        conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="mysql", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("INSERT INTO b_zhuangjijilv (shh,pp,pwh,azlx,zjsl,azrq,zjry,bz) values (%s,%s,%s,%s,%s,%s,%s,%s)",[shh,pp,pwh,azlx,zjsl,azrq,zjry,bz])
            conn.commit()
        return redirect('../')


# 学生信息修改处理函数
def edit(request):
    if request.method == 'GET':
        id = request.GET.get("id")
        conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="mysql", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("SELECT id,shh,pp,pwh,azlx,zjsl,azrq,zjry,bz FROM b_zhuangjijilv where id =%s", [id])
            student = cursor.fetchone()
        return render(request, 'zhuangji/edit.html', {'student': student})
    else:
        id = request.POST.get('id', '')
        shh = request.POST.get('shh', '')
        pp = request.POST.get('pp', '')
        pwh = request.POST.get('pwh', '')
        azlx = request.POST.get('azlx', '')
        zjsl = request.POST.get('zjsl', '')
        azrq = request.POST.get('azrq', '')
        zjry = request.POST.get('zjry', '')
        bz = request.POST.get('bz', '')
        conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="mysql", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("UPDATE b_zhuangjijilv set shh=%s,pp=%s,pwh=%s,azlx=%s,zjsl=%s,azrq=%s,zjry=%s,bz=%s where id =%s", [shh, pp, pwh, azlx, zjsl, azrq, zjry, bz, id])
            conn.commit()
        return redirect('../')


# 学生信息删除处理函数
def delete(request):
    id = request.GET.get("id")
    conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="mysql", charset='utf8')
    with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute("DELETE FROM b_zhuangjijilv WHERE id =%s", [id])
        conn.commit()
    return redirect('../')