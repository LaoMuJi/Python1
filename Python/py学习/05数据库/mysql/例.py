import pymysql


class JD(object):
    def __init__(self):
        # 创建connection连接
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', password='mysql数据库', database='jing_dong', charset='utf8')
        # 获得cursor对象
        self.cursor = self.conn.cursor()

    def __del__(self):
        # 关闭cursor对象
        self.cursor.close()
        self.conn.close()

    def execute_sql(self, sql):
        self.cursor.execute(sql)
        for i in self.cursor.fetchall():
            print(i)

    def show_all_items(self):
        # 显示所有的商品
        sql = 'select * from goods;'
        self.execute_sql(sql)

    def show_cates(self):
        # 查询分类
        sql = 'select name from goods_cates;'
        self.execute_sql(sql)

    def show_brands(self):
        # 查询品牌分类
        sql = 'select name from good_brands;'
        self.execute_sql(sql)

    def add_brands(self):
        item_name = input('请输入商品分类的名称：')
        sql = '''insert into goods_brands (name) values('%s')''' % item_name
        self.cursor.execute(sql)
        # 保存
        self.conn.commit()  # 取消更改 self.conn.rollback()


    def get_info_by_name(self):
        # 根据名字查询商品
        find_name = input('请输入要查询商品的名字：')
        sql = 'select * from goods where name=%s'
        self.cursor.execute(sql,[find_name])
        print(self.cursor.fetchall())

    @staticmethod
    def print_menu():
        print('---京东---')
        print('1.所有的商品')
        print('2.所有的商品分类')
        print('3.所有的商品品牌分类')
        print('4.添加一个商品分类')
        print('5.根据名字查询一个商品')
        return input('请输入功能对应的序号：')

    def run(self):
        while True:
            num = self.print_menu()
            if num == '1':
                # 查询所有商品
                self.show_all_items()
            elif num == '2':
                # 查询分类
                self.show_cates()
            elif num == '3':
                # 查询品牌分类
                self.show_brands()
            elif num == '4':
                # 添加品牌分类
                self.add_brands()
            elif num == '5':
                # 根据名字查询商品
                self.get_info_by_name()
            else:
                print('输入错误，请重新输入')

def main():
    jd = JD()
    jd.run()

if __name__ == '__main__':
    main()