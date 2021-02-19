from django.shortcuts import render
# Create your views here.
# import MySQLdb
# import pymysql
from pool import SQLPoll
import time
from django.shortcuts import render, redirect
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    request.encoding = 'utf-8'
    pag = request.GET.get('pag')
    if pag:
        pag = int(pag)
    else:
        pag = 1
    rq2=''
    sql ="SELECT id,rq,dph,pp,xm,scfs,xsfs,zf,bz,pxyy,qtbz FROM b_peixunjieguo ORDER BY rq"
    # conn = pymysql.connect(host="localhost", user="root", passwd="root", db="mysql", charset='utf8')
    # with conn.cursor(cursorclass=pymysql.cursors.DictCursor) as cursor:
    # cursor=conn.cursor(pymysql.cursors.DictCursor)
    # cursor.execute("SELECT id,rq,dph,pp,xm,scfs,xsfs,zf,bz,pxyy,qtbz FROM b_peixunjieguo ORDER BY rq")
    # students = cursor.fetchall()
    # cursor.close()
    with SQLPoll() as db:
        students = db.fetch_all(sql, None)
    p = Paginator(students, 10)
    students = p.get_page(pag)
    page_num = p.page_range
    wz="/peixun/?pag="
    return render(request, 'peixun/index.html',
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
        sql ="SELECT id,rq,dph,pp,xm,scfs,xsfs,zf,bz,pxyy,qtbz FROM b_peixunjieguo where rq =%s  ORDER BY rq"
        # conn = pymysql.connect(host="localhost", user="root", passwd="root", db="mysql", charset='utf8')
        # cursor = conn.cursor(pymysql.cursors.DictCursor)
        # cursor.execute(
        #     "SELECT id,rq,dph,pp,xm,scfs,xsfs,zf,bz,pxyy,qtbz FROM b_peixunjieguo where rq =%s  ORDER BY rq",[rq1])
        # students = cursor.fetchall()
        # cursor.close()
        sql ="SELECT id,rq,dph,pp,xm,scfs,xsfs,zf,bz,pxyy,qtbz FROM b_peixunjieguo where rq =%s  ORDER BY rq"
        with SQLPoll() as db:
            students = db.fetch_all(sql, rq1)
        p = Paginator(students, 10)
        students= p.get_page(pag)
        wz="/peixun/find?rq1="+rq2+"&pag="
        page_num=p.page_range
        return render(request, 'peixun/index.html',
                  {
                      'students': students,
                      'wz':wz,
                      'page_num':page_num,
                      'rq2': rq2
                  }
                  )
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
        # conn = pymysql.connect(host="localhost", user="root", passwd="root", db="mysql", charset='utf8')
        # cursor = conn.cursor(pymysql.cursors.DictCursor)
        # cursor.execute("INSERT INTO b_peixunjieguo (rq,dph,pp,xm,scfs,xsfs,zf,bz,pxyy,qtbz) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",[rq,dph,pp,xm,scfs,xsfs,zf,bz,pxyy,qtbz])
        # conn.commit()
        # cursor.close()
        sql ="INSERT INTO b_peixunjieguo (rq,dph,pp,xm,scfs,xsfs,zf,bz,pxyy,qtbz) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        args=(rq,dph,pp,xm,scfs,xsfs,zf,bz,pxyy,qtbz)
        with SQLPoll() as db:
            db.execute(sql, args)
        return redirect('../')


# 学生信息修改处理函数
def edit(request):
    if request.method == 'GET':
        id = request.GET.get("id")
        # conn = pymysql.connect(host="localhost", user="root", passwd="root", db="mysql", charset='utf8')
        # cursor = conn.cursor(pymysql.cursors.DictCursor)
        # cursor.execute("SELECT id,rq,dph,pp,xm,scfs,xsfs,zf,bz,pxyy,qtbz FROM b_peixunjieguo where id =%s", [id])
        # student = cursor.fetchone()
        # cursor.close()
        sql ="SELECT id,rq,dph,pp,xm,scfs,xsfs,zf,bz,pxyy,qtbz FROM b_peixunjieguo where id =%s"
        with SQLPoll() as db:
            student = db.fetch_one(sql, id)
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
        # conn = pymysql.connect(host="localhost", user="root", passwd="root", db="mysql", charset='utf8')
        # cursor = conn.cursor(pymysql.cursors.DictCursor)
        # cursor.execute("UPDATE b_peixunjieguo set rq=%s,dph=%s,pp=%s,xm=%s,scfs=%s,xsfs=%s,zf=%s,bz=%s,pxyy=%s,qtbz=%s where id =%s", [rq, dph, pp, xm, scfs, xsfs, zf, bz, pxyy, qtbz, id])
        # conn.commit()
        # cursor.close()
        sql ="UPDATE b_peixunjieguo set rq=%s,dph=%s,pp=%s,xm=%s,scfs=%s,xsfs=%s,zf=%s,bz=%s,pxyy=%s,qtbz=%s where id =%s"
        args=(rq, dph, pp, xm, scfs, xsfs, zf, bz, pxyy, qtbz, id)
        with SQLPoll() as db:
            db.execute(sql, args)
        return redirect('../')


# 学生信息删除处理函数
def delete(request):
    id = request.GET.get("id")
    # conn = pymysql.connect(host="localhost", user="root", passwd="root", db="mysql", charset='utf8')
    # cursor = conn.cursor(pymysql.cursors.DictCursor)
    # cursor.execute("DELETE FROM b_peixunjieguo WHERE id =%s", [id])
    # conn.commit()
    # cursor.close()
    sql = "DELETE FROM b_peixunjieguo WHERE id =%s"
    with SQLPoll() as db:
        db.execute(sql, id)
    return redirect('../')