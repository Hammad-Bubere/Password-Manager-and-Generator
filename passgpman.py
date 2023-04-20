
def passgen():   
    import random
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers ="0123456789"
    symbols ="!#$%^&*()<>?{}[]\/;."
    all =lower+upper+numbers+symbols
    print("______password Generator______")
    
    while True:
        
        length = int(input("Enter the password length\n Or press 0 for exit: "))
        if length == 0:
            print("Exiting Password Generator......")
            break
        if length <8 or length >70:
            print("Please input password length more than 8 and less than 70 !!")
            print("Back to Main Menu")
            break
        
        elif length >=8  :
            password ="".join (random.sample(all,length))
            print ("Your generated password is: ",password)
        elif length <=70:
             password ="".join (random.sample(all,length))
             print ("Your generated password is: ",password)
        else:
            print("your entered invalid length !!\n Max length Exceeded !!!")
            break

    
def passman():
    from cryptography.fernet import Fernet
    def write_key():
        key = Fernet.generate_key()
        with open('key.key','wb') as key_file:
            key_file.write(key)
    
    write_key()

            
    def load_key():
            with open('key.key','rb') as file:
                key = file.read()
                file.close()
                return key
        
    key = load_key()
    fer = Fernet(key)

    def view():
        try:
            with open ('bv55m0QO.txt','r') as f:
                for line in f.readlines():
                    data = line.rstrip()
                    user, passw = data.split("|")
                print("Account Info...\n")
                print("user:", user,"\npassword:",fer.decrypt(passw.encode()).decode())
            f.close()
        except FileNotFoundError as e:
            print("there is no data in file\nFile does not exist",type(e))
    

    def add():
         print("Add your Account Info....\n")
         u_name = input ("User name: ")
         pwd = input ("Password: ")
         with open ('bv55m0QO.txt','a') as f:
             f.write( u_name + "|" + fer.encrypt(pwd.encode()).decode() +"\n")
        
    while True:
        print("\n_____Password Manager_____\nChoose your operation")
        print("1.add username & pass\n2.view username & pass")
        mode = input ("press q for quit \n").lower()
        if mode == "q":
            print("Exiting Password Manager!!")
            break
        if mode == "2":
            view()
        elif mode == "1":
            add()
        else:
            print("Invalid choice!!!")
            continue

while True:
        print("\n*************Main Menu****************")
        print("1.Generate password \n2.Manage password")
        pro = input ("Press 'q' or 'Q' for quit \nEnter your choice: ").lower()
        if pro == "q":
            print("Exiting Program .......")
            break
        if pro == "1":
            passgen()
        elif pro == "2":
            passman()
        else:
            print("Invalid choice")
        continue