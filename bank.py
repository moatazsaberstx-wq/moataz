#Users
ids=['0000','0001','0002','0003']
users=['moataz','malek','ziad','eyad']
passcodes=['2702','6767','1289','4011']
balances=[15000,8000,12000,10000]
print('-----Bank App-----')
#system vars
sign_up=()
op=()
NewUser=()
id_current=(3)
pass_enter=()
balance_enter=()
user_check=()
index=()
id_holder=()
user_edit=()
pass_change=()
name_change=()
#atm vars
withdrawal=()
deposit=()
pass_try=()
confirmation=()
transaction=()
transaction_holder=()
recieverID=()
#signin
while True:
    sign_up=int(input('What is the operation : \nsign in : 1\nlogin : 2\nExit : 3\nEnter the no : '))
#account managment    
    if sign_up == 1:
        id_current+=1
        id_format=(f'{id_current:04d}')
        ids.append(id_format)
        NewUser=input('enter your first name : ')
        users.append(NewUser)
        pass_enter=int(input('Make a passcode : '))
        passcodes.append(pass_enter)
        balance_enter=int(input('deposit your cash : '))
        balances.append(balance_enter)
        print(f'your ID is {ids[-1]} memories it ')
        print('=================')
#user selecting
    elif sign_up == 2:
        user_check=(input('enter your ID code : '))
        id_holder=(ids.index(user_check))
        pass_try=(input('enter your password : '))
        if pass_try == (passcodes[id_holder]):   
            print(f'Hi {users[id_holder]}')
#operation selecting
            op=int(input('--operation--\ndeposit : 1\nwithdrawal : 2\nview balance : 3\nchange passcode : 4\nchange username : 5\nTransfer money : 6\ndelete account : 7\nExit : 8 \nchoose : '))
            print('=================')
    #deposit        
            if op == 1:
                deposit=int(input('Please insert the money : '))
                user_edit=((int(balances[id_holder]))+deposit)
                balances[id_holder]=user_edit
                print('=================')    
    #withdrawal            
            elif op == 2:
                withdrawal=int(input('you want to withdraw how much : '))
                if withdrawal<=balances[id_holder]:
                    user_edit=((int(balances[id_holder]))-withdrawal)
                    balances[id_holder]=user_edit
                    print('=================')  
                else : print('Not enough balance\n=================')
    #view balance            
            elif op ==3:
                print(f'your balance is : {balances[id_holder]}')
                print('=================')  
    #change passcode
            elif op == 4:
                pass_change=int(input('enter the new passcode : '))
                passcodes[id_holder]=pass_change
                print('=================')  
    #change username            
            elif op == 5:
                name_change=input('the new username : ')
                old_name=(users[id_holder])
                users[id_holder]=name_change
                print('=================')  
    #Exit            
            elif op ==8:
                print('thank you')
                break
            elif op ==7:
                confirmation=int(input('---CONFIRM---\nYes : 1\nNo : 2'))
                if confirmation==1:
                    users.remove(users[id_holder])
                    ids.remove(ids[id_holder])
                    passcodes.remove(passcodes[id_holder])
                    balances.remove(balances[id_holder])
                    print('done')
                else:print('Ok take care\n=================')  
            elif op==6:
                recieverID=int(input('enter the ID you want to send money to : '))
                transaction=int(input('Enter the money transfer : '))
                if transaction <= balances[id_holder]:
                    transaction_holder=((int(balances[id_holder]))-transaction)
                    balances[id_holder]=transaction_holder
                    balances[recieverID]+=transaction
                else:print('LOW BALANCE!')
        else : print('wrong password or ID')
    elif sign_up == 3:
        print('Thank you')
        break