from django.shortcuts import render

# Create your views here.
import time
import MySQLdb
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
    conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="mysql", charset='utf8')
    with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute("SELECT id,sjbh,sbxlqk,sbwd,gzcl,xjr,shr,rq FROM b_shujingxj ORDER BY rq")
        students = cursor.fetchall()
        p = Paginator(students, 10)
        students = p.get_page(pag)
        page_num = p.page_range
        wz="/shujing/?pag="
    return render(request, 'shujing/index.html',
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
                "SELECT id,sjbh,sbxlqk,sbwd,gzcl,xjr,shr,rq FROM b_shujingxj where rq =%s  ORDER BY rq",
                [rq1])
            students = cursor.fetchall()
            p = Paginator(students, 10)
            students= p.get_page(pag)
            wz="/shujing/find?rq1="+rq2+"&pag="
            page_num=p.page_range
            return render(request, 'shujing/index.html',
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
        return render(request, 'shujing/add.html')
    else:
        sjbh = request.POST.get('sjbh', '')
        sbxlqk = request.POST.get('sbxlqk', '')
        sbwd = request.POST.get('sbwd', '')
        gzcl = request.POST.get('gzcl', '')
        xjr = request.POST.get('xjr', '')
        shr = request.POST.get('shr', '')
        rq = request.POST.get('rq', '')
        conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="mysql", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("INSERT INTO b_shujingxj (sjbh,sbxlqk,sbwd,gzcl,xjr,shr,rq) values (%s,%s,%s,%s,%s,%s,%s)",[sjbh, sbxlqk, sbwd, gzcl, xjr, shr, rq])
            conn.commit()
        return redirect('../')


# 学生信息修改处理函数
def edit(request):
    if request.method == 'GET':
        id = request.GET.get("id")
        conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="mysql", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("SELECT id,sjbh,sbxlqk,sbwd,gzcl,xjr,shr,rq FROM b_shujingxj where id =%s", [id])
            student = cursor.fetchone()
        return render(request, 'shujing/edit.html', {'student': student})
    else:
        id = request.POST.get('id', '')
        sjbh = request.POST.get('sjbh', '')
        sbxlqk = request.POST.get('sbxlqk', '')
        sbwd = request.POST.get('sbwd', '')
        gzcl = request.POST.get('gzcl', '')
        xjr = request.POST.get('xjr', '')
        shr = request.POST.get('shr', '')
        rq = request.POST.get('rq', '')
        conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="mysql", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("UPDATE b_shujingxj set sjbh=%s,sbxlqk=%s,sbwd=%s,gzcl=%s,xjr=%s,shr=%s,rq=%s where id =%s", [sjbh,sbxlqk,sbwd,gzcl,xjr,shr,rq, id])
            conn.commit()
        return redirect('../')


# 学生信息删除处理函数
def delete(request):
    id = request.GET.get("id")
    conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="mysql", charset='utf8')
    with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute("DELETE FROM b_shujingxj WHERE id =%s", [id])
        conn.commit()
    return redirect('../')