def register():
    pass

def login():
    pass

def recharge():
    pass

def reader():
    pass


func_dic = {
    '1': register,
    '2': login,
    '3': recharge,
    '4': reader
}

def run():
    while True:
        print('''
            1.用户注册
            2.用户登录
            3.用户充值
            4.阅读小说
        ''')
        chioce = input('请输入你的选择:').strip()
        if chioce == 'q':
            break

        # if not chioce.isdigit():
        #     print('请输入数字')
        #     continue

        if chioce not in func_dic:
            print('请输入正确的选择')
            continue


        func_dic.get(chioce)()
