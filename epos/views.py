from django.shortcuts import render

# Create your views here.
###
import time
import MySQLdb
from django.shortcuts import render, redirect
from django.core.paginator import Paginator


# Create your views here.
# 故障处理记录处理函数

# def index(request):
#     rq1 = request.POST.get('rq1')
#     conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="mysql", charset='utf8')
#     if rq1 is None :
#         # print(rq1)
#         with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
#             cursor.execute("SELECT id,clr,pwh,pp,gzlx,rq,sj,ms,clcs,wczt,syyqm,bz FROM b_epos ORDER BY rq,sj")
#             students = cursor.fetchall()
#         return render(request, 'student/index.html', {'students': students})
#     else:
#         with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
#             cursor.execute(
#                 "SELECT id,clr,pwh,pp,gzlx,rq,sj,ms,clcs,wczt,syyqm,bz FROM b_epos where rq =%s  ORDER BY rq,sj",
#                 [rq1])
#             students = cursor.fetchall()
#         return render(request, 'student/index.html', {'students': students})


def index(request):
    request.encoding = 'utf-8'
    pag = request.GET.get('pag')
    if pag:
        pag = int(pag)
    else:
        pag = 1
    rq2=''
    conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="mysql", charset='utf8')
    with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute("SELECT id,clr,pwh,pp,gzlx,rq,sj,ms,clcs,wczt,syyqm,bz FROM b_epos ORDER BY rq,sj")
        students = cursor.fetchall()
        p = Paginator(students, 8)
        students = p.get_page(pag)
        page_num = p.page_range
        wz="/epos/?pag="
    return render(request, 'student/index.html',
                  {
                      'students': students,
                      'wz': wz,
                      'page_num': page_num,
                      'rq2': rq2
                  }
                  )


def find(request):
    request.encoding = 'utf-8'
    if 'rq1' in request.GET and request.GET['rq1']:
        rq1= request.GET['rq1']
        rq2= request.GET['rq1']
        pag= request.GET['pag']
        if pag:
            pag = int(pag)
        else:
            pag = 1
        rq1=time.strftime("%Y.%m.%d",time.strptime(rq1,"%Y-%m-%d"))
        conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="mysql", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute(
                "SELECT id,clr,pwh,pp,gzlx,rq,sj,ms,clcs,wczt,syyqm,bz FROM b_epos where rq =%s  ORDER BY rq,sj", [rq1])
            students = cursor.fetchall()
            p = Paginator(students, 8)
            students= p.get_page(pag)
            wz="/epos/find?rq1="+rq2+"&pag="
            page_num=p.page_range
            return render(request, 'student/index.html',
                          {
                              'students': students,
                              'wz':wz,
                              'page_num':page_num,
                              'rq2':rq2
                          }
                          )
    else:
        return redirect('../')


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
