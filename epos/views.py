from django.shortcuts import render

# Create your views here.
###

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
            cursor.execute("SELECT id,clr,pwh,pp,gzlx,rq,sj,ms,clcs,wczt,syyqm,bz FROM b_epos ORDER BY rq,sj")
            students = cursor.fetchall()
        return render(request, 'student/index.html', {'students': students})
    else:
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute(
                "SELECT id,clr,pwh,pp,gzlx,rq,sj,ms,clcs,wczt,syyqm,bz FROM b_epos where rq =%s  ORDER BY rq,sj",
                [rq1])
            students = cursor.fetchall()
        return render(request, 'student/index.html', {'students': students})

# def find(request):
#     # rq1 = request.GET['rq1']
#     # rq = request.POST.get("rq1", None)
#     # print(rq1)
#     # rq1='2021.1.1'
#     # if request.method == 'GET':
#     rq1 = request.POST.get('rq1', '')
#     conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="mysql", charset='utf8')
#     with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
#         cursor.execute("SELECT id,clr,pwh,pp,gzlx,rq,sj,ms,clcs,wczt,syyqm,bz FROM b_epos where rq =%s  ORDER BY rq,sj",
#                        [rq1])
#         students = cursor.fetchall()
#     return render(request, 'student/index.html', {'students': students})
#
#     # else:
#     #     rq = request.POST.get("rq1", None)
#     #     print('post')



# 学生信息新增处理函数
def add(request):
    if request.method == 'GET':
        return render(request, 'student/add.html')
    else:
        clr = request.POST.get('clr', '')
        pwh = request.POST.get('pwh', '')
        pp = request.POST.get('pp', '')
        gzlx = request.POST.get('gzlx', '')
        rq = request.POST.get('rq', '')
        sj = request.POST.get('sj', '')
        ms = request.POST.get('ms', '')
        clcs = request.POST.get('clcs', '')
        wczt = request.POST.get('wczt', '')
        syyqm = request.POST.get('syyqm', '')
        bz = request.POST.get('bz', '')
        conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="mysql", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("INSERT INTO b_epos (clr,pwh,pp,gzlx,rq,sj,ms,clcs,wczt,syyqm,bz) "
                           "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                           [clr, pwh, pp, gzlx, rq, sj, ms, clcs, wczt, syyqm, bz])
            conn.commit()
        return redirect('../')


# 学生信息修改处理函数
def edit(request):
    if request.method == 'GET':
        id = request.GET.get("id")
        conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="mysql", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("SELECT id,clr,pwh,pp,gzlx,rq,sj,ms,clcs,wczt,syyqm,bz FROM b_epos where id =%s", [id])
            student = cursor.fetchone()
        return render(request, 'student/edit.html', {'student': student})
    else:
        id = request.POST.get('id', '')
        clr = request.POST.get('clr', '')
        pwh = request.POST.get('pwh', '')
        pp = request.POST.get('pp', '')
        gzlx = request.POST.get('gzlx', '')
        rq = request.POST.get('rq', '')
        sj = request.POST.get('sj', '')
        ms = request.POST.get('ms', '')
        clcs = request.POST.get('clcs', '')
        wczt = request.POST.get('wczt', '')
        syyqm = request.POST.get('syyqm', '')
        bz = request.POST.get('bz', '')
        conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="mysql", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("UPDATE b_epos set clr=%s,pwh=%s,pp=%s,gzlx=%s,rq=%s,sj=%s,ms=%s,clcs=%s,wczt=%s,syyqm=%s,"
                           "bz=%s where id =%s",
                           [clr, pwh, pp, gzlx, rq, sj, ms, clcs, wczt, syyqm, bz, id])
            conn.commit()
        return redirect('../')


# 学生信息删除处理函数
def delete(request):
    id = request.GET.get("id")
    conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="mysql", charset='utf8')
    with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute("DELETE FROM b_epos WHERE id =%s", [id])
        conn.commit()
    return redirect('../')
