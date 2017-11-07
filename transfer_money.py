# coding:utf8
import sys
import MySQLdb

class TransferMoney(object):
    def __init__(self, conn):
        self.conn = conn

    def transfer(self, source_accid, target_accid, money):
        try:
            self.check_acct_available(source_accid)
            self.check_acct_available(target_accid)
            self.has_enough_money(source_accid, money)
            self.reduce_money(source_accid, money)
            self.add_money(target_accid, money)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print str(e)

    def check_acct_available(self, accid):
        cursor = self.conn.cursor()
        try:
            sql = "select * from test where accid=%s" % accid
            cursor.execute(sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception('账号%s不存在' % accid)
            else:
                print '账号%s确认成功' % accid
        finally:
            cursor.close()

    def has_enough_money(self, accid, money):
        cursor = self.conn.cursor()
        try:
            sql = "select * from test where accid=%s and money>=%s" % (accid, money)
            cursor.execute(sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception('账号%s余额不足' % accid)
            else:
                print '账号%s余额%s确认成功' % (accid, money)
        finally:
            cursor.close()

    def reduce_money(self, accid, money):
        cursor = self.conn.cursor()
        try:
            sql = "update test set money = money -%s where accid=%s" % (money, accid)
            cursor.execute(sql)
            rs = cursor.rowcount
            if rs != 1:
                raise Exception('账号%s减款失败' % accid)
            else:
                print '账号%s减款%s成功' % (accid, money)
        finally:
            cursor.close()

    def add_money(self, accid, money):
        cursor = self.conn.cursor()
        try:
            sql = "update test set money = money +%s where accid=%s" % (money, accid)
            cursor.execute(sql)
            rs = cursor.rowcount
            if rs != 1:
                raise Exception('账号%s加款失败' % accid)
            else:
                print '账号%s加款%s成功' % (accid, money)
        finally:
            cursor.close()

if __name__=='__main__':
    source_accid = sys.argv[1]
    target_accid = sys.argv[2]
    money = sys.argv[3]

    db = MySQLdb.Connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='123456',
        db='python-test',
        charset='utf8'
    )

    tr_money = TransferMoney(db)

    try:
        tr_money.transfer(source_accid, target_accid, money)
    except Exception as e:
        print '出现问题:' + str(e)
    finally:
        db.close()