    
class rental_vehicle():
    
    def __init__(self):
        pass
        
    def display():
        rent = open('rent.txt', 'r')
        file1 = rent.read()
        print("Vehicle numbers")
        print(file1)

    def rentvehicle(self):
        rent = open('rent.txt', 'a')
        input1 = open('untitled.txt','r')
        outputfile = open('Output.txt','a')
        contents = input1.readlines()
        vehiclenumber = contents[3]
        print("Enter the Vehicle number you want to book")
        #check = object4.check_availability(vehiclenumber)
        if check == 1:
              print("Vehicle already booked enter different Vehicle number") 
              outputfile.write("1. Vehicle already booked enter different Vehicle number")
        else:
            print("Vehicle Booked Successfully")
            rent.write('\n'+vehiclenumber + '\n')
            outputfile.write("1. Vehicle Booked Successfully:"+ vehiclenumber +'\n')
        rent.close()
        outputfile.close()


    def edit(self):
        print("Enter the Vehicle number you want to edit")
        input1 = open('untitled.txt','r')
        outputfile = open('Output.txt','a')
        contents = input1.readlines()
        vehiclenumber = contents[13]
        rent = open("rent.txt", "r")
        lines = rent.readlines()
        rent.close()

        rent1 = open("rent.txt", "w")
        for line in lines:
            if line != vehiclenumber:
                rent1.write(line)
        print("Enter the new vehiclenumber")
        vn1 = contents[14]
        rent1.write(vn1 + '\n')
        print("Editing Vehicle id successfull")
        outputfile.write('\n'+"3. Vehicle number to be edited:"+ vehiclenumber +'\n')
        outputfile.write("   Vehicle number edited to:"+ vn1 +'\n')
        rent1.close()
        outputfile.close()


    def delete(self):
        print("Enter the Vehicle id you want to delete")
        rent = open("rent.txt", "r")
        input1 = open('untitled.txt','r')
        outputfile = open('Output.txt','a')
        contents = input1.readlines()
        lines = rent.readlines()
        rent.close()
        vehiclenumber = contents[18]
        rent1 = open("rent.txt", "w")
        for line in lines:
            if line != vehiclenumber:
                rent1.write(line)
        print("Vehicle Id deleted successfully")
        outputfile.write('\n'+"4. Deleted Vehicle number:"+vehiclenumber +'\n')         
        rent.close()
        outputfile.close()
        #input1.close()

    def search(self):
        print("Enter the Vehicle id you want to search")
        input1 = open('untitled.txt','r')
        contents = input1.readlines()
        vehiclenumber = contents[8]
        outputfile = open('Output.txt','a')
        rent = open('rent.txt', 'r')
        contents = rent.readlines() 
        for line in contents:
            if line == vehiclenumber:
                a = 1
                break
            else:
                a = 0
        if a == 1:
            print("Vehicle id found in the records")
            outputfile.write('\n'+"2. Vehicle id found in the records:"+ vehiclenumber +'\n')
        else:
            print("No vehicle found")
            outputfile.write('\n'+"2. No Vehicle id found in the records:"+ vehiclenumber +'\n')
        rent.close()

object2 = rental_vehicle()


class check():
    
    def __init__(self):
        pass
        
        
    def check_availability(self):
        rent = open('rent.txt', 'r')
        contents = rent.readlines()
        input1 = open('untitled.txt','r')
        contents = input1.readlines()
        vehiclenumber = contents[3]
        self.vehiclenumber = vehiclenumber
        for line in contents:  
            if self.vehiclenumber in line:
                return 1
            
object4 = check()    

class choose():
     def choose_option(self):
        print("Choose the option u want to perform")
        print("Enter 1- Rent Vehicle")
        print("Enter 2- Edit")
        print("Enter 3- Search")
        print("Enter 4- Delete")
        print("Enter 5- View")
        print("Enter choice:")
        
object3 = choose()

class options(rental_vehicle, choose):
    
    def __init__(self, choice):
        self.choice = choice
     
    def choice_selection(self,choice):
        #print(choice)
        if choice == 1:
            print("rent")
            object1.rentvehicle()
        elif choice == 2:
            print("search")
            object1.search()
        elif choice == 3:
            print("edit")
            object1.edit()
        elif choice == 4:
            print("delete")
            object1.delete()
        elif choice == 5:
            print("display")
            object1.display()
        else:
            exit()

object1 = options(choice)


i = 0
a = 0
for i in range(4):  
        print("Enter the userid")
        print("Enter the password")
        input1 = open('untitled.txt','r')
        contents = input1.readlines()
        userid = int(contents[a + 0])
        print(userid)
        password = int(contents[a + 1])
        print(password)
        choice = int(contents[a + 2])
        print(choice)
        #vehiclenumber = contents[a + 3]
        if (userid == 3166) & (password == 3166 ):
            print("login Successfull")
            object1.choose_option()
            object1.choice_selection(choice)
        else:
            print("Enter valid userid and password")
        i = i+1
        a = i*5
        input1.close()
