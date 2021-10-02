from sqlite3 import connect
from datetime import date, datetime
now = datetime.now()
# from psycopg2 import connect
# h = 'localhost'
# u = 'postgres'
# p = 'Abb@$123'
# db = 'Telegrambot'


DATABASE = 'Telegrambot.db'

def createuser(id,firstname,username):
    try:
        con = connect(DATABASE)
        cur = con.cursor()
        sql = f'''
        INSERT INTO peoples (chat_id, firstname, username, date)
        VALUES ('{id}','{firstname}','{username}','{now}');
                '''
        cur.execute(sql)
        con.commit()
        cur.close()
    except Exception as e:
        print(e)

def createimages(id,name):
    try:
        con = connect(DATABASE)
        cur = con.cursor()
        sql = f'''
        INSERT INTO imagefiles (chat_id, imagefilename,  date)
        VALUES ('{id}','{name}','{now}');
                '''
        cur.execute(sql)
        con.commit()
        cur.close()

    except Exception as e:
        print(e)

def get_people():
    try:
        con = connect(DATABASE)
        cursor = con.cursor()
        sql = '''
        SELECT * FROM peoples;
                '''
        cursor.execute(sql)
        res = []
        for i in cursor.fetchall():
            res.append(i)
        return res

    except Exception as e:
        print(e)


def get_admin_id():
    try:
        con = connect(DATABASE)
        cursor = con.cursor()
        sql = '''
        SELECT chat_id
        FROM peoples WHERE admin='True';
                '''
        cursor.execute(sql)
        res = []
        for i in cursor.fetchall():
            res.append(i[0])
        return list(res)

    except Exception as e:
        print(e)

def get_people_info(id):
    try:
        con = connect(DATABASE)
        cursor = con.cursor()
        sql = f'''
               SELECT *
	FROM peoples WHERE chat_id = '{id}';
                '''
        cursor.execute(sql)
        res = []
        for i in cursor.fetchall():
            res.append(i)
        return res[0]

    except Exception as e:
        print(e)

def get_people_name(id):
    try:
        con = connect(DATABASE)
        cursor = con.cursor()
        sql = f'''
               SELECT firstname
	FROM peoples WHERE chat_id = '{id}';
                '''
        cursor.execute(sql)
        res = []
        for i in cursor.fetchall():
            res.append(i)
        return list(res[0])[0]

    except Exception as e:
        print(e)

def get_images(id):
    try:
        con = connect(DATABASE)
        cursor = con.cursor()
        sql = f'''
                SELECT * FROM imagefiles
                WHERE chat_id = {id}
                '''
        cursor.execute(sql)
        res = []
        for i in cursor.fetchall():
            res.append(i)
        return res
    except Exception as e:
        print(e)

def get_peoples_chat_id():
    try:
        con = connect(DATABASE)
        cursor = con.cursor()
        sql = '''
               SELECT chat_id
	FROM peoples;
                '''
        cursor.execute(sql)
        res = []
        for i in cursor.fetchall():
            res.append(i[0])
        return res

    except Exception as e:
        print(e)

def createactiveuser(id):
    try:
        con = connect(DATABASE)
        cur = con.cursor()
        sql = f'''
        UPDATE peoples
        SET active = 'True' WHERE chat_id = {id};
                '''
        cur.execute(sql)
        con.commit()
        cur.close()
    except Exception as e:
        print(e)

def get_active_usres_id():
    try:
        con = connect(DATABASE)
        cur = con.cursor()
        sql = '''
               SELECT chat_id
	FROM peoples WHERE active='True';
                '''
        cur.execute(sql)
        res = []
        for i in cur.fetchall():
            res.append(i[0])
        return res
    except Exception as e:
        print(e)


def createactiveusernumber(id,phone):
    try:
        con = connect(DATABASE)
        cur = con.cursor()
        sql = f'''
               UPDATE peoples SET phone_number="{phone}" WHERE chat_id={id};
                '''

        cur.execute(sql)
        con.commit()
        cur.close()
    except Exception as e:
        print(e)


def get_users_count():
    try:
        con = connect(DATABASE)
        cursor = con.cursor()
        sql = f'''
        SELECT COUNT(id)
	FROM peoples;
                '''
        cursor.execute(sql)
        res = []
        for i in cursor.fetchall():
            res.append(i)
        return list(res[0])[0]

    except Exception as e:
        print(e)

def get_active_users_count():
    try:
        con = connect(DATABASE)
        cursor = con.cursor()
        sql = f'''
        SELECT COUNT(id) FROM peoples WHERE active='True';
                '''
        cursor.execute(sql)
        res = []
        for i in cursor.fetchall():
            res.append(i)
        return list(res[0])[0]

    except Exception as e:
        print(e)

def edithomepagetext(edit):
    try:
        con = connect(DATABASE)
        cur = con.cursor()
        sql = f'''
               UPDATE malumot SET tanishuv='{edit}' WHERE id=1;
                '''

        cur.execute(sql)
        con.commit()
        cur.close()
    except Exception as e:
        print(e)


def edithomepagebatafsiltext(edit):
    try:
        con = connect(DATABASE)
        cur = con.cursor()
        sql = f'''
               UPDATE malumot SET batafsil='{edit}' WHERE id=1;
                '''

        cur.execute(sql)
        con.commit()
        cur.close()
    except Exception as e:
        print(e)

def edithomepagetulovtext(edit):
    try:
        con = connect(DATABASE)
        cur = con.cursor()
        sql = f'''
               UPDATE malumot SET tulov='{edit}' WHERE id=1;
                '''

        cur.execute(sql)
        con.commit()
        cur.close()
    except Exception as e:
        print(e)

def edithomepagealoqatext(edit):
    try:
        con = connect(DATABASE)
        cur = con.cursor()
        sql = f'''
               UPDATE malumot SET aloqa='{edit}' WHERE id=1;
                '''

        cur.execute(sql)
        con.commit()
        cur.close()
    except Exception as e:
        print(e)

def gethomepagetext():
    try:
        con = connect(DATABASE)
        cursor = con.cursor()
        sql = '''
               SELECT tanishuv
	FROM malumot;
                '''
        cursor.execute(sql)
        res = []
        for i in cursor.fetchall():
            res.append(i[0])
        return res[0]

    except Exception as e:
        print(e)

def gethomepagebatafsiltext():
    try:
        con = connect(DATABASE)
        cursor = con.cursor()
        sql = '''
               SELECT batafsil FROM malumot;
                '''
        cursor.execute(sql)
        res = []
        for i in cursor.fetchall():
            res.append(i[0])
        return res[0]

    except Exception as e:
        print(e)

def gethomepagetulovtext():
    try:
        con = connect(DATABASE)
        cursor = con.cursor()
        sql = '''
               SELECT tulov FROM malumot;
                '''
        cursor.execute(sql)
        res = []
        for i in cursor.fetchall():
            res.append(i[0])
        return res[0]

    except Exception as e:
        print(e)

def gethomepagealoqatext():
    try:
        con = connect(DATABASE)
        cursor = con.cursor()
        sql = '''
               SELECT aloqa FROM malumot;
                '''
        cursor.execute(sql)
        res = []
        for i in cursor.fetchall():
            res.append(i[0])
        return res[0]

    except Exception as e:
        print(e)
def edithomepagedasturtext(edit):
    try:
        con = connect(DATABASE)
        cur = con.cursor()
        sql = f'''
               UPDATE malumot SET dastur='{edit}' WHERE id=1;
                '''

        cur.execute(sql)
        con.commit()
        cur.close()
    except Exception as e:
        print(e)

def gethomepagedasturtext():
    try:
        con = connect(DATABASE)
        cursor = con.cursor()
        sql = '''
               SELECT dastur FROM malumot;
                '''
        cursor.execute(sql)
        res = []
        for i in cursor.fetchall():
            res.append(i[0])
        return res[0]

    except Exception as e:
        print(e)



