# Add the cities to the graph
class Cities:
    def __init__(self):
        self.graph = {}

    def add_city(self):
        s = '''Please enter:
        1. If you want to add a city.
        2. If you want to add a neighbouring city.
        3. If you don't want to add cities or want to go back to main menu'''
        print(s)
        while True:
            answer = input("Enter 1, 2 or 3 according to the above options: ")
            if answer == "1":
                n_city = input("Enter the city name: ").upper()   # n_city as "new city"
                if n_city not in self.graph:
                    self.graph[n_city] = []
                else:
                    print(s)
            elif answer == "2":
                city = input("Enter the name of the main city: ").upper()
                nhb_city = input("Enter the neighbouring city: ").upper()  # nhb_city as "neighbouring city"
                if nhb_city not in self.graph:
                    self.graph[nhb_city] = []
                    self.graph[nhb_city].append(city)
                    self.graph[city].append(nhb_city)
                else:
                    self.graph[city].append(nhb_city)
            elif answer == "3":
                return

    def delete_city(self):
        d = Drivers()
        s = '''Please enter:
        1. To delete a city.
        2. To go back to main menu'''
        print(s)
        ans = input("Enter 1 or 2 according to the above options: ")
        while True:
            if ans == "1":
                city = input("Enter the name of the city to remove: ").upper()
                if city in self.graph:
                    if self.graph[city][0] in d.driver:
                        a = self.graph[city][0]
                        del d.driver[a]
                        del self.graph[city]
                    else:
                        del self.graph[city]
                else:
                    print("This entry is not correct. Please enter '1' and try again or enter '2' if you want to go back to main menu")
            elif ans == "2":
                return

    def print_cities(self):
        d = Drivers
        s = '''Hello! Please enter:
        1. If you just want to see the registered cities in the system.
        2. If you want to see the connections between the cities.
        3. If you want to see the neighbouring cities of a city.
        4. If you want to go back to main menu.'''
        print(s)
        while True:
            entry = input("Enter a number from the above options according to what you want: ")
            if entry == "1":
                for key in self.graph:
                    print(key, end = " - ")  #this one only prints the keys (the registered cities)
                return
            elif entry == "2":
                print(self.graph)    # this one prints all the keys with their values (the cities and the ones it has connections with)
                return
            elif entry == "3":
                city = input("Enter the name of the city: ").upper()
                if city in self.graph:
                    if self.graph[city][0] in d.driver:
                        print(f"{city}: {self.graph[city][1:len(self.graph[city])]}")
                    else:
                        print(f"{city}: {self.graph[city]}")
            elif entry == "4":
                return
    def print_drivers_delivering(self):
        c = Cities()
        d = Drivers()
        q = Queue()
        drivers_delivering = []
        print("To print all the delivery drivers that could reach a certain city, please enter the name of the city")
        # I am going to use breadth first search (BFS) algorithm to find all the drivers that could reach the city of the users choice
        city = input("Enter the name of the city here: ").upper()
        while city != 'stop':
            if city in c.graph:
                q.enqueue(city)
                for i in c.graph[city]:
                    if i not in d.driver and i not in q.queue:
                        q.enqueue(i)
                for i in q.queue[1:]:
                    for j in c.graph[i]:
                        if j not in d.driver and j not in q.queue:
                            q.enqueue(j)
                for z in q.queue:
                    if c.graph[z][0] in d.driver:
                        drivers_delivering.append(c.graph[z][0])
                        q.dequeue()
                if len(q.queue) == 0:
                    print(f"The drivers who deliver to {city} are: {drivers_delivering}")
                    return 
            else:
                print("This city does not exist. Please enter a valid city or enter 'stop' to exit. ")
                city = input("Enter the name of the city here: ").upper()


class Drivers:
    def __init__(self):
        self.driver = {}
        self.size = 0

    def add_driver(self):
        c = Cities()
        w = '''Please enter:
        1. To enter a driver.
        2. To go back to main menu'''
        while True:
            print(w)
            ans = input("Enter 1 or 2 according to the above options:")
            if ans == "1":
                print("To add a driver, you have to pick the city from where he is starting.")
                city = input("Enter the starting city: ").upper()
                if city not in c.graph:
                    print("The city does not exist. Do you want to add this city?")
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

    def delete_driver(self):
        s = '''Please enter:
        1. To remove a driver.
        2. To go back to main menu'''
        print(s)
        ans = input("Enter 1 or 2 according to the above options: ")
        while True:
            if ans == "1":
                driver = input("Enter the name of the driver to remove: ").upper()
                if driver in self.driver:
                    a = self.driver[driver][0]
                    del(self.driver[driver])
                    self.graph[a].pop(0)
                else:
                    print("This entry is not correct. Please try again or enter '2' if you want to go back to main menu")
            elif ans == "2":
                return

    def print_drivers(self):
        s = '''Hello! Please enter:
        1. If you just want to see the registered drivers in the system.
        2. If you want to see the drivers with their information.
        3. If you want to see the information of a specific driver.
        4. If you want to go back to main menu.'''
        while True:
            print(s)
            entry = input("Enter a number from the above options according to what you want: ")
            if entry == "1":
                for key in self.driver:
                    print(key, end = " - ")  #this one only prints the keys (the registered drivers)
                return
            elif entry == "2":
                print(driver for driver in self.driver.items())    # this one prints all the keys with their values (the drivers and their information)
                return
            elif entry == "3":
                driver = input("Enter the full name of the driver you want to search for")
                if driver in self.driver:
                    print(f"{driver}: {self.driver[driver]}")
                else:
                    print("This driver does not exist. Please enter '3' to try again or enter '4' if you want to go back to main menu")
            elif entry == "4":
                return

def employee():
    while True:
        s = '''Hello! Please enter:
        1. To go to the drivers' menu.
        2. To go to the cities' menu.
        3. To exit the system.'''
        print(s)
        entry = input("Enter 1, 2 or 3 according to the above options: ")
        if entry == "1":
            d = Drivers()
            st = '''Enter:
            1. To view all the drivers.
            2. To add a driver.
            3. To delete a driver.
            4. To go back to main menu'''
            while True:
                print(st)
                ans = input("Enter 1, 2 or 3 according to the above options: ")
                if ans == "1":
                    d.print_drivers()
                elif ans == "2":
                    d.add_driver()
                elif ans == "3":
                    d.delete_driver()
                elif ans == "4":
                    break
        elif entry == "2":
            c = Cities()
            ci = '''Please Enter:
            1. Show cities.
            2. Print neighboring cities.
            3. Print Drivers delivering to city.
            4. Add a city.
            5. Delete a city.
            6. Go back to main menu'''
            while True:
                print(ci)
                answ = input("Enter a number from the above options according to what you want: ")
                if answ == "1":
                    c.print_cities()
                elif answ == "2":
                    c.print_cities()
                elif answ == "3":
                    c.print_drivers_delivering()
                elif answ == "4":
                    c.add_city()
                elif answ == "5":
                    c.delete_city()
                elif answ == "6":
                    break
        elif entry == "3":
            return
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):
        self.queue.pop(0)

employee()