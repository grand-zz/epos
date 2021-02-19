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
    sql='SELECT id,shh,pp,pwh,azlx,zjsl,azrq,zjry,bz FROM b_zhuangjijilv ORDER BY azrq'
    with SQLPoll() as db:
        students = db.fetch_all(sql, None)
    p = Paginator(students, 10)
    students = p.get_page(pag)
    page_num = p.page_range
    wz="/zhuangji/?pag="
    return render(request, 'zhuangji/index.html',
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
        sql='SELECT id,shh,pp,pwh,azlx,zjsl,azrq,zjry,bz  FROM b_zhuangjijilv where azrq =%s  ORDER BY azrq'
        with SQLPoll() as db:
            students = db.fetch_all(sql, rq1)
        p = Paginator(students, 10)
        students= p.get_page(pag)
        wz="/zhuangji/find?rq1="+rq2+"&pag="
        page_num=p.page_range
        return render(request, 'zhuangji/index.html',
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
        sql ="INSERT INTO b_zhuangjijilv (shh,pp,pwh,azlx,zjsl,azrq,zjry,bz) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        args=(shh,pp,pwh,azlx,zjsl,azrq,zjry,bz)
        with SQLPoll() as db:
            db.execute(sql, args)
        return redirect('../')


# 学生信息修改处理函数
def edit(request):
    if request.method == 'GET':
        id = request.GET.get("id")
        sql ="SELECT id,shh,pp,pwh,azlx,zjsl,azrq,zjry,bz FROM b_zhuangjijilv where id =%s"
        with SQLPoll() as db:
            student = db.fetch_one(sql, id)
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
        sql ="UPDATE b_zhuangjijilv set shh=%s,pp=%s,pwh=%s,azlx=%s,zjsl=%s,azrq=%s,zjry=%s,bz=%s where id =%s"
        args=(shh, pp, pwh, azlx, zjsl, azrq, zjry, bz, id)
        with SQLPoll() as db:
            db.execute(sql, args)
        return redirect('../')


# 学生信息删除处理函数
def delete(request):
    id = request.GET.get("id")
    sql = "DELETE FROM b_zhuangjijilv WHERE id =%s"
    with SQLPoll() as db:
        db.execute(sql, id)
    return redirect('../')