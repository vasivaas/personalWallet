from upload_data.uploader import Uploader
from models.account import Account
from models.user import User

uploader = Uploader()
user = User('Vasa')
account = Account('lmfemfm', '00000wefff', user)
user1 = User('Vova')
account1 = Account('log', 'passvovacool', user1)
account_list = [account, account1]

if __name__ == '__main__':
    res = uploader.load_data()
    print(res)
    for account in account_list:
        res.insert(0, account)
    uploader.save_data(res)
