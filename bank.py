#Users
ids={
    "0000":{
        'id':'0000',
        'name':'moataz',
        'passcode':'2702',
        'balance':'5000'
    },
    "0001":{
        'id':'0001',
        'name':'mohamed',
        'passcode':'2013',
        'balance':'8000'
    },
    "0002":{
        'id':'0002',
        'name':'eslam',
        'passcode':'1982',
        'balance':'6500'
    },
    "0003":{
        'id':'0003',
        'name':'ziad',
        'passcode':'2315',
        'balance':'3500'
    }
}
print('-----Bank App-----')
#system vars
x=()
y=()
sign_up=()
op=()
new_user=()
id_current=(3)
pass_enter=()
balance_enter=()
user_check=()
index=()
id_holder=()
user_edit=()
pass_change=()
name_change=()
user_balance=()
#atm vars
withdrawal=()
deposit=()
user_balance=()
pass_try=()
confirmation=()
transaction=()
transaction_holder=()
recieverID=()
id_show=()
name=()
#signin
while True:
    sign_up=int(input('What is the operation : \nsign in : 1\nlogin : 2\nExit : 3\nEnter the no : '))
#account managment    
    if sign_up == 1:
        id_current+=1
        id_format=(f'{id_current:04d}')
        new_user=input('enter your first name : ')
        pass_enter=(input('Make a passcode : '))
        balance_enter=int(input('deposit your cash : '))
        ids[id_format]={
            'id':id_format,
            'name': new_user,
            'passcode':pass_enter,
            'balance':balance_enter
        }
        id_show=ids[id_format]['id']
        print(f'your ID is {id_show} remember it .')
        print('============================')
#user selecting
    elif sign_up == 2:
        user_check=input('enter your user id : ')
        pass_try=input('enter your passcode : ')
        if pass_try==ids[user_check]['passcode']:
#operation selecting
            name=ids[user_check]['name']
            print(f'Hi {name}')
            op=int(input('--operation--\ndeposit : 1\nwithdrawal : 2\nview balance : 3\nchange passcode : 4\nchange username : 5\nTransfer money : 6\ndelete account : 7\nExit : 8 \nchoose : '))
#deposit        
            if op == 1:
                deposit=int(input('please insert the money : '))
                if deposit<=0:
                    print('invalid money amount')
                    print('============================')
                else :
                    user_balance=int(ids[user_check]['balance'])+deposit
                    ids[user_check]['balance']=user_balance
                    print(f'your balance now is {user_balance}')
                    print('============================')
#withdrawal            
            elif op == 2:
                withdrawal=int(input('you want to withdraw how much : '))
                user_balance=int(ids[user_check]['balance'])
                if withdrawal>user_balance:
                    print('no enough balance')
                    print('============================')
                else:
                    print('okay')
                    user_balance-=withdrawal
                    print(f'your balance now is {user_balance}')
                    print('============================')
#view balance            
            elif op ==3:
                user_balance=ids[user_check]['balance']
                print(f'your balance is : {user_balance}')
                print('============================')  
#change passcode
            elif op == 4:
                pass_change=int(input('enter the new passcode : '))
                ids[user_check]['passcodes']=pass_change
                print(f'done your passcode now is {pass_change}')
                print('============================')  
#change username            
            elif op == 5:
                name_change=input('Enter the new username : ')
                ids[user_check]['name']=name_change
                print(f'done your username now is {name_change}')
                print('============================')
#transaction  
            elif op==6:
                recieverID=int(input('enter the ID you want to send money to : '))
                recieverID=(f'{recieverID:04d}')
                transaction=int(input('Enter the money transfer : '))
                user_balance=int(ids[user_check]['balance'])
#names
                x=(ids[user_check]['name'])
                y=(ids[recieverID]['name'])
                if transaction <= user_balance:
                    transaction_holder=(int(ids[recieverID]['balance'])+transaction)
                    ids[recieverID]['balance']=transaction_holder
                    user_balance=int(ids[user_check]['balance'])-transaction
                    ids[user_check]['balance']=user_balance
                    print(f'you have send {transaction} SAR to {y}')
                    print('============================')
                else:
                    print('LOW BALANCE!')
#delete user
            elif op ==7:
                confirmation=int(input('---CONFIRM---\nYes : 1\nNo : 2\nEnter : '))
                if confirmation==1:
                    del ids[user_check]
                    print('done')
                    print('============================')
                else:
                    print('Ok take care')  
#Exit            
            elif op ==8:
                print('thank you')
                break
        else : 
            print('wrong password or ID')
            print('============================')
    elif sign_up == 3:
        print('Thank you')
        break