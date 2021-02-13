from django.shortcuts import render

# Create your views here.
import time
import MySQLdb
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
# Create your views here.
conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="mysql", charset='utf8')
with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
    cursor.execute("SELECT id,sjbh,sbxlqk,sbwd,gzcl,xjr,shr,rq FROM b_shujingxj ORDER BY rq")
    students = cursor.fetchall()
    p = Paginator(students, 10)
    print(p.count)
    print(p.num_pages)
    print(p.page_range)
    page1 = p.page(4)
    page2 = p.get_page(4)
    #
    # print(page1.object_list)
    # print(page1.start_index())
    # print(page2.object_list)
    # print(page2)
    # for student in page2:
    #     print(student)
    #     print(student.get('shr'))
        # print(type(student))
        # print(student.keys())
        # print(student.full_name|upper)

    for i in page2.paginator.page_range:
        print(i)




