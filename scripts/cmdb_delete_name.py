#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb


def delete_data():
    db = MySQLdb.connect('192.168.10.191', 'cmdb', '65daigou@ezbuy', 'cmdb')
    cursor = db.cursor()
    select_sql = """select name  from asset_goservices where ip  like '192.168.10.6%';"""
    try:
        cursor.execute(select_sql)
        results = cursor.fetchall()
        for n in results:
            name = n[0]
            delete_sql = """delete from asset_goservices where name like '{}' and ip like '192.168.10.6%';""".format(
                name)
            print(delete_sql)
            try:
                cursor.execute(delete_sql)
                db.commit()
            except:
                db.rollback()
        db.close()
    except Exception as e:
        print('error: {}'.format(e))

delete_data()
