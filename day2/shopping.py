productory = [
    ('Ihone',5800),
    ('Mac Pro',9800),
    ('Bike',800),
    ('Watch',10600),
    ('Coffee',31),
    ('Alex Python',120)
]
shopping_list = []
salary = input('请输入您的工资:')
if salary.isdigit():
    salary = int(salary)
    while True:
        for index,key in enumerate(productory):
            #print(productory.index(key),key)
            print(index,key)
        user_choice = input('请选择要买的商品编号:')
        if user_choice.isdigit():   #判断是否是整数
            user_choice = int(user_choice)  #转换成整型
            if user_choice < len(productory) and user_choice >= 0:
                p_item = productory[user_choice]
                # print(p_item)
                if p_item[1] <= salary:
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    print(f'商品{p_item[1]}已添加到购物车,当前余额为:\033[31;1m{salary}\033[0m')
                else:
                    print(f'\033[41;1m 当前余额为{salary},请充值再购买！\033[0m')
            else:
                print('请输入正常的商品编号')
        elif user_choice == 'q':
            print('--------------已退出------------')
            print('已购买的商品:',shopping_list,)
            print(f'余额为:\033[31;1m{salary}\033[0m')
            exit()
        else:
            print('请输入重新正确的值！')
        # break


