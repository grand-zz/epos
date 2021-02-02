# Create your views here.
import json
import MySQLdb
from random import randrange
import time
from django.http import HttpResponse
from pyecharts.commons.utils import JsCode
from django.shortcuts import render, redirect

from pyecharts.charts import Bar,Page,Pie
from pyecharts import options as opts

from pyecharts.components import Table
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd
from jinja2 import Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig

# CurrentConfig.ONLINE_HOST ='D:/pyecharts-assets-master/assets/'
# 'D:/pyecharts-assets-master/assets/'
# CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./datapage/templates"))

def table_base(sql,titl) -> Table:
    # for arg in args:
    #     print(arg)
    table = Table()
    engine = create_engine("mysql+pymysql://root:root@10.101.192.43:3306/mysql", encoding="utf-8")
    session = sessionmaker(bind=engine)
    df = pd.read_sql(sql, engine)
    rows=df.values.tolist()
    headers=df.columns.tolist()
    if len(rows) == 0:
        headers=['记录','数量']
        rows = [['无', 0]]
    table.add(headers, rows).set_global_opts(
        title_opts=opts.ComponentTitleOpts(title=titl)
    )
    return table

def Pie_base(sql,titl) -> Pie:
    pie = Pie()
    engine = create_engine("mysql+pymysql://root:root@10.101.192.43:3306/mysql", encoding="utf-8")
    session = sessionmaker(bind=engine)
    # sql= "select gzlx as 故障类型,count(1) as 数量 from b_epos where rq BETWEEN '%s' and '%s' group by gzlx"% (rq1, rq2)
    df = pd.read_sql(sql, engine)
    rows=df.values.tolist()
    headers=df.columns.tolist()
    if len(rows) == 0:
        rows = [['无', 0]]
    pie.add("", rows)
    pie.set_global_opts(title_opts=opts.TitleOpts(title=titl))
    pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
    return pie

# def chart(request):
def zhou(rq1,rq2):
    # request.encoding = 'utf-8'
    # if 'rq1' in request.GET and request.GET['rq1']:
    #     # message = '你搜索的内容为: ' + request.GET['rq1']
    #     rq1 = request.GET['rq1']
    #     rq2 = request.GET['rq2']
    #     rq3 = request.GET['rq3']
    # print (rq1,rq2,rq3)
    sql1 = '''select pwh as 铺位号,pp as 品牌,gzlx as 故障类型,操作,软件,硬件,其它,操作+软件+硬件+其它 as 合计,rq as 日期,ms as 描述,clr as 处理人 from (select pwh,gzlx,pp,COUNT(if(gzlx='操作',true,null)) as 操作,COUNT(if(gzlx='软件',true,null)) as 软件,COUNT(if(gzlx='硬件',true,null)) as 硬件,COUNT(if(gzlx='其它',true,null)) as 其它,rq,ms,clr from b_epos where rq BETWEEN '%s' and '%s' group by pwh,gzlx,pp,rq,ms,clr) c order by rq,pwh''' % (
        rq1, rq2)
    titl1 = "POS前台收银问题处理汇总\n\n查询日期：%s--%s" % (rq1, rq2)
    sql2 = '''select gzlx as 故障类型,ms as 描述,count(1) as 数量 from b_epos where rq BETWEEN '%s' and '%s' group by gzlx,ms order by gzlx  DESC''' % (
        rq1, rq2)
    titl2 = "POS前台收银问题故障类型详细表\n\n查询日期：%s--%s" % (rq1, rq2)
    sql3 = "select dph as 店铺号,pp as 品牌,xm as 姓名,rq as 日期,zf as 总分,bz as 备注 from b_peixunjieguo where rq BETWEEN '%s' and '%s' order by 日期,店铺号" % (rq1, rq2)
    titl3 = "科传收银培训考核统计表\n\n培训日期：%s--%s" % (rq1, rq2)
    sql4 = "select dph as 店铺号,pp as 品牌,xm as 姓名,rq as 日期,if(bz='合格',bz,CONCAT('培训不及格&',bz)) as 类型,zf as 备注 from b_peixunjieguo where (rq BETWEEN '%s' and '%s') and bz<>'合格' Union All select pwh,pp,syyqm,rq,gzlx,ms from b_epos where gzlx='操作' and (rq BETWEEN '%s' and '%s') order by 类型,日期,店铺号" % (
    rq1, rq2,rq1, rq2)
    titl4 = "下周培训名单\n\n查询日期：%s--%s" % (rq1, rq2)
    sql5 = "select gzlx as 故障类型,count(1) as 数量 from b_epos where rq BETWEEN '%s' and '%s' group by gzlx" % (rq1, rq2)
    titl5 = "POS收银问题处理汇总\n\n查询日期：%s--%s" % (rq1, rq2)
    sql6 = "select ms as 描述,count(1) as 数量 from b_epos where gzlx='操作' and rq BETWEEN '%s' and '%s' group by 描述" % (
        rq1, rq2)
    titl6 = "操作类问题处理汇总\n\n查询日期：%s--%s" % (rq1, rq2)
    sql7 = "select ms as 描述,count(1) as 数量 from b_epos where gzlx='软件' and rq BETWEEN '%s' and '%s' group by 描述" % (
        rq1, rq2)
    titl7 = "软件类问题处理汇总\n\n查询日期：%s--%s" % (rq1, rq2)
    sql8 = "select ms as 描述,count(1) as 数量 from b_epos where gzlx='硬件' and rq BETWEEN '%s' and '%s' group by 描述" % (
        rq1, rq2)
    titl8 = "硬件类问题处理汇总\n\n查询日期：%s--%s" % (rq1, rq2)
    sql9 = "select ms as 描述,count(1) as 数量 from b_epos where gzlx='其它' and rq BETWEEN '%s' and '%s' group by 描述" % (
        rq1, rq2)
    titl9 = "其它类问题处理汇总\n\n查询日期：%s--%s" % (rq1, rq2)
    page = Page()
    page.add(
        table_base(sql1, titl1),
        table_base(sql2, titl2),
        Pie_base(sql5, titl5),
        Pie_base(sql6, titl6),
        Pie_base(sql7, titl7),
        Pie_base(sql8, titl8),
        Pie_base(sql9, titl9),
        table_base(sql3, titl3),
        table_base(sql4, titl4),
    )
    return page


def index(request):
    request.encoding = 'utf-8'
    if 'optionsRadios' in request.GET and request.GET['optionsRadios']:
        rq1 = request.GET['rq1']
        rq2 = request.GET['rq2']
        rq1=time.strftime("%Y.%m.%d",time.strptime(rq1,"%Y-%m-%d"))
        rq2=time.strftime("%Y.%m.%d",time.strptime(rq2,"%Y-%m-%d"))
        selet = request.GET['optionsRadios']
        page1 = Page()
        if selet =='zhou':
            page1=zhou(rq1,rq2)
    return HttpResponse(page1.render_embed())
# render(request, './datapage/index.html', selet)
#
def selet(request):
    return render(request, './datapage/selet.html')

