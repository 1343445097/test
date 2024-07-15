# -*- coding: utf-8 -*-
# @Time    : 2024/7/14 17:00
# @Author  : YangYin
# @File    : Djangosql.py
# @Software: PyCharm


from django.db import connection

class DjangoSql:
    def select(self,sql):
        cursor = connection.cursor()
        cursor.execute(sql)
        data = []
        try:
            rawData = cursor.fetchall()
            # print(cursor.description)
            col_names = [desc[0] for desc in cursor.description]

            for row in rawData:
                d = {}
                for index,value in enumerate(row):
                    d[col_names[index]] = value
                data.append(d)
        except Exception as e:
            print("Djangosql::select error {} - {}".format(sql,str(e)))
        return data

    def insert(self,tb_name,d):
        sql = "insert into {}({}) values ({})".format(tb_name,",".join(d.keys()),",".join(map(lambda x:"'"+str(x)+"'",d.values())))
        return self.execute(sql)

    def execute(self,sql):
        ret = False
        try:
            cursor = connection.cursor()
            e = cursor.execute(sql)
            print(type(e),e)
            ret = True
        except Exception as e:
            print("Djangosql::select error {} - {}".format(sql, str(e)))
        return ret