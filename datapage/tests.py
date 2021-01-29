#
# # Create your views here.
# import json
# import MySQLdb
# from random import randrange
#
# from django.http import HttpResponse
#
# from django.shortcuts import render
#
#
#
# from pyecharts.charts import Bar,Page
# from pyecharts import options as opts
# from pyecharts.commons.utils import JsCode
# from pyecharts.components import Table
#
#
# if __name__ == "__main__":
#     page_simple_layout()
#
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd
from pyecharts.faker import Faker
engine = create_engine("mysql+pymysql://root:root@10.101.192.43:3306/mysql", encoding="utf-8")
session = sessionmaker(bind=engine)
sql ='''select ms as 描述,count(1) as 数量 from b_epos where gzlx='软件' and rq BETWEEN '2021.01.18' and '2021.01.24' group by gzlx'''
df=pd.read_sql(sql, engine )
print (df.columns.tolist())
a=df.values.tolist()

print (len(a))
if len(a)==0:
    a=[['无',0]]
print (a)



