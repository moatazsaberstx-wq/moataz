import json 
with open ('problems/bank/bank.json','r') as f:
    bank=json.load(f)
    
def new_acc(count) : 
    id=(f'{count:04d}')
    bank[id]={
        "id":id,
        "name" : input('enter your name : ') ,
        "passcode" : (input('enter the passcode : ')),
        "balance" : int(input('insert the money : '))
    }



def log(id,pass_t):
    if pass_t != bank[id]["passcode"] :
        return False
    else :
        return True



def deposit(id,money):
    bank[id]["balance"]+=money



def withdraw(id,money):
    bank[id]["balance"]-=money
    

def send(id,reciever,money):
    if bank[id]["balance"] < money:
        print('suffecient balance')
        return 0
    else :
        if receiver not in bank:
            print("wrong receiver ID")
            return 0
        else : 
            bank[id]["balance"]-=money
            bank[reciever]["balance"]+=money


def view(id):
    print(f'your have {bank[id]["balance"]}')



def pass_change(id,old_pass):
    if bank[id]["passcode"]==old_pass:
        new_pass=input('enter the new passcode : ')
        bank[id]["passcode"]=new_pass
    else :
        print('the old password you entered is wrong')
        return 0



def change_name(id):
    new_name=input('enter the new user name : ')
    bank[id]["name"]=new_name


def del_acc(id,passcode):
    if passcode==bank[id]["passcode"]:
        print('sure ? ')
        print('after this point you won\'t be able to recover your account')
        confirmation=input('to confirm enter CONFIRM (uppercase) : ')
        if confirmation == "CONFIRM" :
            del bank[id]
            print("your request has been done .")
            return True
        else :
            print('YOUR ACCOUNT HASN\'T BEEN DELETED')
            return True


run = True
while run :
    print("------------------")
    print('New Account : 1')
    print('Login : 2')
    print('Exit : 0')
    sign_in=(input('choose : '))
    print('------------------')
    if sign_in == "1":
        new_acc(len(bank.keys()))
    
    
    
    
    elif sign_in == "2":
        user_id=input('enter your ID : ')
        pass_t=input('enter your passcode : ')
        if log(user_id,pass_t):
            print(f'Hello {bank[user_id]["name"]}')
            while run:
                print('-------------------')
                print("deposit  : 1")
                print('withdraw : 2')
                print('transfer : 3')
                print('view balance : 4')
                print("Exit : 0")
                print('-------------------')
                print('change password : 5')
                print("change name     : 6")
                print('DELETE ACCOUNT  : 7')
                op=input('Choose : ')
                print('-------------------')
                if op == "1":
                    money_i=int(input('Insert the money : '))
                    deposit(user_id,money_i)
                
                
                
                elif op == "2":
                    money_i=int(input('Enter the ammount of money : '))
                    withdraw(user_id,money_i)
                
                
                elif op == "3":
                    receiver=input('send to : ')
                    money_i=int(input('enter the ammount of money : '))
                    send(user_id,receiver,money_i)
                
                
                elif op == "4":
                    view(user_id)
                
                
                elif op == "5":
                    passcode_try=input('enter your old password : ')
                    pass_change(user_id,passcode_try)
                
                
                elif op == "6":
                    change_name(user_id)
                
                
                elif op == "7":
                    passcode_confirm=input('enter your passcode : ')
                    del_acc(user_id,passcode_confirm)
                    if del_acc:
                        break
                
                
                elif op == "0":
                    run = False
                
                
                
        else:
            print('Wrong passcode or ID')
    
    
    
    elif sign_in == "0":
        run = False
    else :
        print('=============')
        print("invalid input")
        print('=============')




with open('problems/bank/bank.json',"w") as f:
    json.dump(bank,f,indent=2)