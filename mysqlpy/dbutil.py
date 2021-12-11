import pymysql
def insert(table, data, db):
    cursor = db.cursor()
    for item in data:
        keys = ','.join(item.keys())
        values = ','.join(['%s'] * len(item))
        sql = 'insert into {table}({keys}) VALUES({values})'.format(table=table, keys=keys, values=values)
        try:
            if cursor.execute(sql, tuple(item.values())):
                print('insert successful')
                db.commit()
        except Exception as e:
            print("insert failed!", e)
            db.rollback()