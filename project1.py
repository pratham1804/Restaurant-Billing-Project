exit=1
name=" "
samo=0
tea=0
vad=0
total=0


def username():
    global name
    name= input("Enter your Name: ")
    phno= input("Enter your Phone Number: ")
    print("Welcome ",name)


def cupsplates(choice):
    if choice==1 or choice==3:
        return "plates"
    elif choice==2:
        return "cups"
    
def printBill():
    i=1
    print(name,"Your Bill :",total)
    print("sr.\t|\tItem\t|\tQty\t|\tPrice\t|\tTotal")
    print("------------------------------------------------------------------------------------")
    if samo!=0 :
        print(i,"\t|\tSamosa\t|\t",samo,"\t|\t20\t|\t",samo*20)
        i+=1
    if tea!=0 :
        print(i,"\t|\tTea\t|\t",tea,"\t|\t10\t|\t",tea*10)
        i+=1
    if vad!=0 :
        print(i,"\t|\tVadapav\t|\t",vad,"\t|\t30\t|\t",vad*30)
        i+=1
    print("------------------------------------------------------------------------------------")
    print("                                                  total :",total)


def bill(item,rate):
    global total
    total=total+item*rate

def total_order(choice,rate):
    waiter=cupsplates(choice)
    item=int(input("How many"+waiter))
    bill(item,rate)
    print("OK ANYTHING ELSE")
    return item


def order(choice):
    if choice==1:
        print("You select Samosa")
        global samo
        samo+=total_order(choice,20)
    elif choice==2:
        print("You select Tea")
        global tea
        tea+=total_order(choice,10)
    elif choice==3:
        print("You select VadaPav")
        global vad
        vad+=total_order(choice,30)
    elif choice==0:
        printBill()
        print("EXIT")
        global exit
        exit=0
    else:
        print("WRONG INPUT PLEASE INPUT CORRECT OPTION")
        
    

    
def menu():
    print("\t\t::MENU::")
    print('''\t 1.SAMOSA :20
         2.Tea    :10
         3.Vadapav:30 
         0.EXIT''')
    choice=int(input("Enter your choice: "))
    order(choice)
    

def main():
    print("\t\t WELCOME TO MY WORLD RESTAURANT")
    username()
    while exit==1:
        menu()

main()
    
    
