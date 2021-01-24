from django.shortcuts import render
# Create your views here.
import MySQLdb
from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="mysql", charset='utf8')
    with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute("SELECT id,rq,dph,pp,xm,scfs,xsfs,zf,bz,pxyy,qtbz FROM b_peixunjieguo ORDER BY rq")
        students = cursor.fetchall()
    return render(request, 'peixun/index.html', {'students': students})


def find(request):
    request.encoding = 'utf-8'
    if 'rq1' in request.GET and request.GET['rq1']:
        rq1 = request.GET['rq1']
        conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="mysql", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute(
                "SELECT id,rq,dph,pp,xm,scfs,xsfs,zf,bz,pxyy,qtbz FROM b_peixunjieguo where rq =%s  ORDER BY rq",[rq1])
            students = cursor.fetchall()
            return render(request, 'peixun/index.html', {'students': students})
    else:
        return redirect('../')



# 学生信息新增处理函数
def add(request):
    if request.method == 'GET':
        return render(request, 'peixun/add.html')
    else:
        rq = request.POST.get('rq', '')
        dph = request.POST.get('dph', '')
        pp = request.POST.get('pp', '')
        xm = request.POST.get('xm', '')
        scfs = request.POST.get('scfs', '')
        xsfs = request.POST.get('xsfs', '')
        zf = request.POST.get('zf', '')
        bz = request.POST.get('bz', '')
        pxyy = request.POST.get('pxyy', '')
        qtbz = request.POST.get('qtbz', '')
        conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="mysql", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("INSERT INTO b_peixunjieguo (rq,dph,pp,xm,scfs,xsfs,zf,bz,pxyy,qtbz) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",[rq,dph,pp,xm,scfs,xsfs,zf,bz,pxyy,qtbz])
            conn.commit()
        return redirect('../')


# 学生信息修改处理函数
def edit(request):
    if request.method == 'GET':
        id = request.GET.get("id")
        conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="mysql", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("SELECT id,rq,dph,pp,xm,scfs,xsfs,zf,bz,pxyy,qtbz FROM b_peixunjieguo where id =%s", [id])
            student = cursor.fetchone()
        return render(request, 'peixun/edit.html', {'student': student})
    else:
        id = request.POST.get('id', '')
        rq = request.POST.get('rq', '')
        dph = request.POST.get('dph', '')
        pp = request.POST.get('pp', '')
        xm = request.POST.get('xm', '')
        scfs = request.POST.get('scfs', '')
        xsfs = request.POST.get('xsfs', '')
        zf = request.POST.get('zf', '')
        bz = request.POST.get('bz', '')
        pxyy = request.POST.get('pxyy', '')
        qtbz = request.POST.get('qtbz', '')
        conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="mysql", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("UPDATE b_peixunjieguo set rq=%s,dph=%s,pp=%s,xm=%s,scfs=%s,xsfs=%s,zf=%s,bz=%s,pxyy=%s,qtbz=%s where id =%s", [rq, dph, pp, xm, scfs, xsfs, zf, bz, pxyy, qtbz, id])
            conn.commit()
        return redirect('../')


# 学生信息删除处理函数
def delete(request):
    id = request.GET.get("id")
    conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="mysql", charset='utf8')
    with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute("DELETE FROM b_peixunjieguo WHERE id =%s", [id])
        conn.commit()
    return redirect('../')