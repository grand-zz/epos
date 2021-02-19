from django.shortcuts import render

# Create your views here.
import time
from pool import SQLPoll
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
    sql='SELECT id,xlqk,gzcl,xjr,shr,rq,bz FROM b_yysxj ORDER BY rq'
    with SQLPoll() as db:
        students = db.fetch_all(sql, None)
    p = Paginator(students, 10)
    students = p.get_page(pag)
    page_num = p.page_range
    wz="/yunyingshang/?pag="
    return render(request, 'yunyingshang/index.html',
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
        sql='SELECT id,xlqk,gzcl,xjr,shr,rq,bz FROM b_yysxj where rq =%s  ORDER BY rq'
        with SQLPoll() as db:
            students = db.fetch_all(sql, rq1)
        p = Paginator(students, 10)
        students= p.get_page(pag)
        wz="/yunyingshang/find?rq1="+rq2+"&pag="
        page_num=p.page_range
        return render(request, 'yunyingshang/index.html',
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
        return render(request, 'yunyingshang/add.html')
    else:
        xlqk = request.POST.get('xlqk', '')
        gzcl = request.POST.get('gzcl', '')
        xjr = request.POST.get('xjr', '')
        shr = request.POST.get('shr', '')
        rq = request.POST.get('rq', '')
        bz = request.POST.get('bz', '')
        sql ="INSERT INTO b_yysxj (xlqk,gzcl,xjr,shr,rq,bz) values (%s,%s,%s,%s,%s,%s)"
        args=(xlqk,gzcl,xjr,shr,rq,bz)
        with SQLPoll() as db:
            db.execute(sql, args)
        return redirect('../')


# 学生信息修改处理函数
def edit(request):
    if request.method == 'GET':
        id = request.GET.get("id")
        sql ="SELECT id,xlqk,gzcl,xjr,shr,rq,bz FROM b_yysxj where id =%s"
        with SQLPoll() as db:
            student = db.fetch_one(sql, id)
        return render(request, 'yunyingshang/edit.html', {'student': student})
    else:
        id = request.POST.get('id', '')
        xlqk = request.POST.get('xlqk', '')
        gzcl = request.POST.get('gzcl', '')
        xjr = request.POST.get('xjr', '')
        shr = request.POST.get('shr', '')
        rq = request.POST.get('rq', '')
        bz = request.POST.get('bz', '')
        sql ="UPDATE b_yysxj set xlqk=%s,gzcl=%s,xjr=%s,shr=%s,rq=%s,bz=%s where id =%s"
        args=(xlqk,gzcl,xjr,shr,rq,bz,id)
        with SQLPoll() as db:
            db.execute(sql, args)
        return redirect('../')


# 学生信息删除处理函数
def delete(request):
    id = request.GET.get("id")
    sql = "DELETE FROM b_yysxj WHERE id =%s"
    with SQLPoll() as db:
        db.execute(sql, id)
    return redirect('../')