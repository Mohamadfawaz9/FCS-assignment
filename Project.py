# Add the cities to the graph
class Cities:
    def __init__(self):
        self.graph = {}

    def add_city(self):
        s = '''Please enter:
        1. If you want to add a city.
        2. If you want to add a neighbouring city.
        3. If you don't want to add cities or want to go back to main menu'''
        while True:         #This while loop is used to keep the user in the system
            print()
            print(s)
            print()
            answer = input("Enter 1, 2 or 3 according to the above options: ")
            print()
            if answer == "1":
                n_city = None
                while n_city != "STOP":         #This while loop is used to keep the user in this operation if he wants to repeat it
                    n_city = input("Enter the city name or 'stop' to exit: ").upper()   # n_city as "new city"
                    print()
                    if n_city not in self.graph.keys() and n_city != "STOP":
                        self.graph[n_city] = []
                    elif n_city in self.graph.keys() and n_city != "STOP":
                        print("This city already exist. Please try again or enter 'stop' to exit: ")
            elif answer == "2":
                city = input("Enter the name of the main city: ").upper()
                nhb_city = None
                while nhb_city != "STOP":
                    nhb_city = input("Enter the neighbouring city or 'stop' to exit: ").upper()  # nhb_city as "neighbouring city"
                    print()
                    if city in self.graph.keys() and nhb_city != "STOP":
                        if nhb_city not in self.graph.keys():
                            self.graph[nhb_city] = []
                            self.graph[nhb_city].append(city)
                            self.graph[city].append(nhb_city)
                        else:
                            self.graph[city].append(nhb_city)
                            self.graph[nhb_city].append(city)
                    elif city not in self.graph.keys() and nhb_city != "STOP":
                        self.graph[city] = []
                        if nhb_city not in self.graph.keys():
                            self.graph[nhb_city] = []
                            self.graph[nhb_city].append(city)
                            self.graph[city].append(nhb_city)
                        else:
                            self.graph[city].append(nhb_city)
                            self.graph[nhb_city].append(city)
                    
            elif answer == "3":
                return
            else:
                    print()
                    print("Invalid entry. Please try again.")
                    print()

    def delete_city(self,d):
        
        s = '''Please enter:
        1. To delete a city.
        2. To delete a connection between two cities.
        3. To go back to main menu'''
        while True:
            print()
            print(s)
            print()
            ans = input("Enter 1, 2 or 3 according to the above options: ")
            if ans == "1":
                city = input("Enter the name of the city to remove: ").upper()
                if city in self.graph.keys():
                    if self.graph[city][0] in d.driver.keys():
                        a = self.graph[city][0]
                        del d.driver[a]
                        del self.graph[city]
                        for value in self.graph.values():
                            while city in value:
                                value.remove(city)
                    else:
                        del self.graph[city]
                        for value in self.graph.values():
                            while city in value:
                                value.remove(city)
                else:
                    print("This entry is not correct. Please enter '1' and try again or enter '2' if you want to go back to main menu")
            elif ans == "2":
                city = input("Enter the name of the main city: ").upper()
                while city != "STOP":
                    o_city = input("the name of the city you want to remove: ").upper()
                    if city in self.graph.keys():
                        if o_city in self.graph[city]:
                            self.graph[city].remove(o_city)
                            print()
                            print(f"{city} and {o_city} are no longer connected.")
                            print()
                        else:
                            print(f"{city} and {o_city} are not connected.")
                    city = input("Enter the name of the main city or 'stop' to: ").upper()
            elif ans == "3":
                return
            else:
                    print()
                    print("Invalid entry. Please try again.")
                    print()

    def print_cities(self,d):
        s = '''Hello! Please enter:
        1. If you just want to see the registered cities in the system.
        2. If you want to see the connections between the cities.
        3. If you want to see the neighbouring cities of a city.
        4. If you want to see a certain city with its driver.
        5. If you want to go back to main menu.'''
        while True:
            print()
            print(s)
            print()
            entry = input("Enter a number from the above options according to what you want: ")
            if entry == "1":
                for key in self.graph.keys():
                    print(key, end = " - ")  #this one only prints the keys (the registered cities)
                print()
            elif entry == "2":
                print(self.graph)    # this one prints all the keys with their values (the cities and the ones it has connections with)
                print()
            elif entry == "3":
                city = input("Enter the name of the city: ").upper()
                if city in self.graph.keys():
                    if self.graph[city][0] in d.driver.keys():
                        print(f"{city}: {self.graph[city][1:len(self.graph[city])]}")
                    else:
                        print(f"{city}: {self.graph[city]}")
            elif entry == "4":
                while True:
                    city = input("Enter the name of a city: ")
                    if self.graph[city][0] in d.driver.keys(): 
                        print(f"{city}:{self.graph[city][0]}")
                        break
                    else:
                        k = '''This city does not have a driver. Do you want to add one?
                        Please enter:
                        1. If you want to add a driver
                        2. If you want to go back to the menu'''
                        print()
                        print(k)
                        print()
                        ans = input("Enter 1 or 2 according to the above options: ")
                        if ans == "1":
                            d.add_driver()
                            print(f"{city}:{self.graph[city][0]}")
                            break
                        elif ans == "2":
                            break
            elif entry == "5":
                return
            else:
                    print()
                    print("Invalid entry. Please try again.")
                    print()
    def print_drivers_delivering(self,d,q):
        print()
        print("To print all the delivery drivers that could reach a certain city, please enter the name of the city")
        print()
        # I am going to use breadth first search (BFS) algorithm to find all the drivers that could reach the city of the users choice
        city = input("Enter the name of the city here: ").upper()
        while city != "STOP":
            if city in self.graph.keys():
                for i in self.graph[city]:
                    if i not in d.driver.keys() and i not in q.queue and i != city:
                        q.enqueue(i)
                for i in q.queue:
                    for j in self.graph[i]:
                        if j not in d.driver.keys() and j not in q.queue and j != city:
                            q.enqueue(j)
                print()
                print(f"The drivers who deliver to {city} are: ",end = "")
                for z in q.queue:
                    if self.graph[z][0] in d.driver.keys():
                        print(self.graph[z][0], end = " - ")
                print()
                print()
                q.queue.clear()
                city = input("Enter the name of the city here or 'stop' to exit: ").upper()
            else:
                print("This city does not exist. Please enter a valid city or enter 'stop' to exit. ")
                city = input("Enter the name of the city here: ").upper()


class Drivers:
    def __init__(self):
        self.driver = {}
        self.size = 0

    def add_driver(self,c):
        w = '''Please enter:
        1. To enter a driver.
        2. To go back to main menu'''
        while True:
            print()
            print(w)
            print()
            ans = input("Enter 1 or 2 according to the above options: ")
            if ans == "1":
                print()
                print("To add a driver, you have to pick the city from where he is starting.")
                print()
                city = input("Enter the starting city: ").upper()
                if city not in c.graph.keys():
                    print()
                    print("The city does not exist. Do you want to add this city?")
                    print()
                    answer = input("Answer with yes or no: ").lower()
                    if answer == "yes":
                        c.add_city()
                    elif answer == "no":
                        continue
                else:
                    self.size += 1
                    ID = 2024000 + self.size
                    driver_name = input("Enter driver's name: ").upper()
                    self.driver[driver_name] = [city,ID]
                    c.graph[city].insert(0,driver_name)
            elif ans == "2":
                return
            else:
                    print()
                    print("Invalid entry. Please try again.")
                    print()

    def delete_driver(self,c):
        s = '''Please enter:
        1. To remove a driver.
        2. To go back to main menu'''
        print()
        print(s)
        print()
        ans = input("Enter 1 or 2 according to the above options: ")
        while True:
            ans = input("Enter 1 or 2 according to the above options: ")
            if ans == "1":
                print()
                driver = input("Enter the name of the driver to remove: ").upper()
                print()
                if driver in self.driver.keys():
                    a = self.driver[driver][0]
                    del(self.driver[driver])
                    c.graph[a].pop(0)
                else:
                    print()
                    print("This entry is not correct. Please try again or enter '2' if you want to go back to main menu")
                    print()
                continue
            elif ans == "2":
                return
            else:
                    print()
                    print("Invalid entry. Please try again.")
                    print()

    def print_drivers(self):
        s = '''Hello! Please enter:
        1. If you just want to see the registered drivers in the system.
        2. If you want to see the drivers with their information.
        3. If you want to see the information of a specific driver.
        4. If you want to go back to main menu.'''
        while True:
            print()
            print(s)
            print()
            entry = input("Enter a number from the above options according to what you want: ")
            print()
            if entry == "1":
                if len(self.driver) != 0:     
                    for key in self.driver.keys():
                        print(key, end = " - ")  #this one only prints the keys (the registered drivers)
                    print()
                    print()
                else:
                    print("There are no drivers registered.")
            elif entry == "2":
                if len(self.driver) != 0:
                    print()
                    for key,value in self.driver.items():
                        print(f"{key}: {value}")    # this one prints all the keys with their values (the drivers and their information)
                    print()
                else:
                    print("There are no drivers registered.")
            elif entry == "3":
                if len(self.driver) != 0:
                    driver = input("Enter the full name of the driver you want to search for: ").upper()
                    if driver in self.driver.keys():
                        print()
                        print(f"{driver}: {self.driver[driver]}")
                        print()
                    else:
                        print()
                        print("This driver does not exist. Please enter '3' to try again or enter '4' if you want to go back to main menu")
                        print()
                else:
                    print("There are no drivers registered.")
            elif entry == "4":
                return
            else:
                    print()
                    print("Invalid entry. Please try again.")
                    print()

class Queue:
    def __init__(self):
        self.queue = []     # Here I am storing the cities found in the same graph to search for their drivers

    def enqueue(self,item):
        self.queue.append(item)     #here I add through this function the cities connected in the same graph

    def dequeue(self):          #I did not use this function
        self.queue.pop(0)

def employee():
    c = Cities()
    d = Drivers()
    q = Queue()
    while True:
        s = '''Hello! Please enter:
        1. To go to the drivers' menu.
        2. To go to the cities' menu.
        3. To exit the system.'''
        print()
        print(s)
        print()
        entry = input("Enter 1, 2 or 3 according to the above options: ")
        if entry == "1":            #This is the drivers' menu
            st = '''Enter:
            1. To view all the drivers.
            2. To add a driver.
            3. To delete a driver.
            4. To go back to main menu'''
            while True:
                print()
                print(st)
                print()
                ans = input("Enter 1, 2 or 3 according to the above options: ")
                if ans == "1":
                    d.print_drivers()
                elif ans == "2":
                    d.add_driver(c)
                elif ans == "3":
                    d.delete_driver(c)
                elif ans == "4":
                    break
                else:
                    print()
                    print("Invalid entry. Please try again.")
                    print()
        elif entry == "2":          #This is the cities' menu
            ci = '''Please Enter:
            1. Show cities.
            2. Print neighboring cities.
            3. Print Drivers delivering to city.
            4. Add a city.
            5. Delete a city.
            6. Go back to main menu'''
            while True:
                print()
                print(ci)
                print()
                answ = input("Enter a number from the above options according to what you want: ")
                if answ == "1":
                    c.print_cities(d)
                elif answ == "2":
                    c.print_cities(d)
                elif answ == "3":
                    c.print_drivers_delivering(d,q)
                elif answ == "4":
                    c.add_city()
                elif answ == "5":
                    c.delete_city(d)
                elif answ == "6":
                    break
                else:
                    print()
                    print("Invalid entry. Please try again.")
                    print()
        elif entry == "3":
            return

employee()