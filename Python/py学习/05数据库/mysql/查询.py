import pymysql


def main():
    # 创建connect连接
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='mysql数据库', database='数据库名')
    # 获得cursor对象
    cursor = conn.cursor()
    # 执行select语句，并返回
    count = cursor.execute('select * from 表')
    # 打印，返回的是行数
    print(count)

    for i in range(count):
        # 返回元祖

        # 返回一行，再取接着往下取
        print(cursor.fetchone())
        # 返回全部行数，取剩下的或者全部
        print(cursor.fetchall())
        # 可以加参数，返回参数
        print(cursor.fetchmany())



    cursor.close()
    conn.close()



if __name__ == '__main__':
    main()
