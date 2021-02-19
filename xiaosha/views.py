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
    sql='SELECT id,rq,sj,sfxs,zbry FROM b_xiaosha ORDER BY rq,sj'
    with SQLPoll() as db:
        students = db.fetch_all(sql, None)
    p = Paginator(students, 10)
    students = p.get_page(pag)
    page_num = p.page_range
    wz="/xiaosha/?pag="
    return render(request, 'xiaosha/index.html',
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
        sql='SELECT id,rq,sj,sfxs,zbry FROM b_xiaosha where rq =%s  ORDER BY rq,sj'
        with SQLPoll() as db:
            students = db.fetch_all(sql, rq1)
        p = Paginator(students, 10)
        students= p.get_page(pag)
        wz="/xiaosha/find?rq1="+rq2+"&pag="
        page_num=p.page_range
        return render(request, 'xiaosha/index.html',
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
        return render(request, 'xiaosha/add.html')
    else:
        rq = request.POST.get('rq', '')
        sj = request.POST.get('sj', '')
        sfxs = request.POST.get('sfxs', '')
        zbry = request.POST.get('zbry', '')
        sql ="INSERT INTO b_xiaosha (rq,sj,sfxs,zbry) values (%s,%s,%s,%s)"
        args=(rq, sj, sfxs, zbry)
        with SQLPoll() as db:
            db.execute(sql, args)
        return redirect('../')


# 学生信息修改处理函数
def edit(request):
    if request.method == 'GET':
        id = request.GET.get("id")
        sql ="SELECT id,rq,sj,sfxs,zbry FROM b_xiaosha where id =%s"
        with SQLPoll() as db:
            student = db.fetch_one(sql, id)
        return render(request, 'xiaosha/edit.html', {'student': student})
    else:
        id = request.POST.get('id', '')
        rq = request.POST.get('rq', '')
        sj = request.POST.get('sj', '')
        sfxs = request.POST.get('sfxs', '')
        zbry = request.POST.get('zbry', '')
        sql ="UPDATE b_xiaosha set rq=%s,sj=%s,sfxs=%s,zbry=%s where id =%s"
        args=(rq, sj, sfxs, zbry, id)
        with SQLPoll() as db:
            db.execute(sql, args)
        return redirect('../')


# 学生信息删除处理函数
def delete(request):
    id = request.GET.get("id")
    sql = "DELETE FROM b_xiaosha WHERE id =%s"
    with SQLPoll() as db:
        db.execute(sql, id)
    return redirect('../')