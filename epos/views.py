from django.shortcuts import render

# Create your views here.
###
import time
from pool import SQLPoll
from django.shortcuts import render, redirect
from django.core.paginator import Paginator


# Create your views here.
# 故障处理记录处理函数

def index(request):
    request.encoding = 'utf-8'
    pag = request.GET.get('pag')
    if pag:
        pag = int(pag)
    else:
        pag = 1
    rq2=''
    sql='SELECT id,clr,pwh,pp,gzlx,rq,sj,ms,clcs,wczt,syyqm,bz FROM b_epos ORDER BY rq,sj'
    with SQLPoll() as db:
        students = db.fetch_all(sql, None)
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
        sql='SELECT id,clr,pwh,pp,gzlx,rq,sj,ms,clcs,wczt,syyqm,bz FROM b_epos where rq =%s  ORDER BY rq,sj'
        with SQLPoll() as db:
            students = db.fetch_all(sql, rq1)
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
        sql ="INSERT INTO b_epos (clr,pwh,pp,gzlx,rq,sj,ms,clcs,wczt,syyqm,bz) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        args=(clr, pwh, pp, gzlx, rq, sj, ms, clcs, wczt, syyqm, bz)
        with SQLPoll() as db:
            db.execute(sql, args)
        return redirect('../')


# 学生信息修改处理函数
def edit(request):
    if request.method == 'GET':
        id = request.GET.get("id")
        sql ="SELECT id,clr,pwh,pp,gzlx,rq,sj,ms,clcs,wczt,syyqm,bz FROM b_epos where id =%s"
        with SQLPoll() as db:
            student = db.fetch_one(sql, id)
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
        sql ="UPDATE b_epos set clr=%s,pwh=%s,pp=%s,gzlx=%s,rq=%s,sj=%s,ms=%s,clcs=%s,wczt=%s,syyqm=%s,bz=%s where id =%s"
        args=(clr, pwh, pp, gzlx, rq, sj, ms, clcs, wczt, syyqm, bz, id)
        with SQLPoll() as db:
            db.execute(sql, args)
        return redirect('../')


# 学生信息删除处理函数
def delete(request):
    id = request.GET.get("id")
    sql = "DELETE FROM b_epos WHERE id =%s"
    with SQLPoll() as db:
        db.execute(sql, id)
    return redirect('../')
