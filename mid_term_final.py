class Star_Cinema:
    hall_list=[]
    def entry_hall(self,Hall):
        self.Hall=Hall
        self.hall_list.append(Hall)

class Hall:
    def __init__(self,rows,cols,hall_no):
        self.__rows=rows
        self.__cols=cols
        self._hall_no=hall_no
        self.show_list=[]
        self.seats={}
    def entry_show(self,movie_name,id,time):
        info=[movie_name,id,time]
        self.show_list.append(info)
        self.seats[id] = [[0 for j in range(self.__cols)] for i in range(self.__rows)]

    def view_available_seats(self,id):
        print(f"Available seat for {id} ")
        for i in range(self.__rows):
           for j in range(self.__cols):
               print(f"seats: ({i}, {j})")

        print('Update seat matrix for Hall',self._hall_no)

        
        for row in self.seats[id]:
            print(row)

    def book_seat(self,id,row,colm):
            if row<self.__rows and colm<self.__cols:
                if self.seats[id][row][colm]==0:
                    self.seats[id][row][colm]=1
                    print(f"Seat ({row}, {colm}) booked for show {id}")
                else:
                    print('already booked')
            else:
                print('invalid')
    def view_show_list(self):
          for info in self.show_list:
          
               print('Movie name: ',info[0])
               print('Id: ',info[1])
               print('Time: ',info[2])
               print()

cine=Hall(5,5,1)
cine.entry_show('jawan majhi',111,'24 april 2024 9:00 AM')
cine.entry_show('Sujon majhi',112,'25 april 2024 9:00 AM')

run=True
while run:
    print('1. View all show today:')
    print('2. View availavle seat:')
    print('3. Book Ticket:')
    print('4. Exist:')


    option=int(input('Enter option: '))

    if option==1:
        cine.view_show_list()
    elif option == 2:
        id = int(input('Enter show id: '))
        found = False
        for info in cine.show_list:
            if info[1] == id:
                cine.view_available_seats(id)
                found = True
                break
        if found==False:
            print('Id not match')
    elif option==3:
            id=int(input('Show id: '))
            found=False
            for info in cine.show_list:
                if info[1]==id:
                    n=int(input('number of ticket: '))
                    for _ in range(n):
                        row=int(input('seat row: '))
                        colm=int(input('seat colm: '))
                        print()
                        cine.book_seat(id,row,colm) 
                    found=True
                    break
            if found==False:
                print('Id not match')
                   
    elif option==4:
        run=False
    else:
        print('Invalid option')
