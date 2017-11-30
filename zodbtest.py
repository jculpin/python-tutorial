import ZODB, ZODB.FileStorage
import BTrees.OOBTree
import persistent
import transaction


class Account(persistent.Persistent):

    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount

    def cash(self, amount):
        assert amount < self.balance
        self.balance -= amount

storage = ZODB.FileStorage.FileStorage('mydata.fs')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root
root.accounts = BTrees.OOBTree.BTree()
root.accounts['account-1'] = Account()
transaction.commit()
