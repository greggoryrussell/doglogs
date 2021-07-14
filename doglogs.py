#!./venv/bin/python3
from datetime import date, datetime
import csv
import os.path
class PromptMenu:

    def __init__(self):
        self.keep_promting = True
        self.menu_items = {
            "q" : "Quit",
            "?" : "Print this menu",
            "v" : "Print this shell's current version",
            "d" : "Print the Date and Time",
            "p" : "Record your dog's business event with the current time and date in a file named Dog-Business.csv"
            }
        self.version = "1.0" # Or Git Tag 

    def check_input(self,inp):
        if inp in self.menu_items:
            print('Input was "' + inp + '"')
            if inp == "?":
                self.help_menu()
            if inp == "q":
                print('Quitting program!')
                self.keep_promting = False
            if inp == "v":
                self.print_version()
            if inp == "d":
                print("The Current Date is " + return_date_string())
                print("The Time is " + return_current_time() )
            if inp == "p":
                print('Poop Mode Selected')
                t = return_current_time()
                d = return_date_string()
                normality_status = ['Normal','Concerning']
                p = input('(N)ormal?\n(C)oncerning?\nType the First Letter to make your choice: ')
                # 'p' will take on the normality_status so it can write it into the CSV
                if p.lower() == 'c':
                    p = 'Concerning'
                elif p.lower() == 'n':
                    p = 'Normal'
                else: 
                    print('Error! Not a valid choice!')
                    return # Return back to the command prompt
                    
                print("You chose: " + p)
                opt_comment = input("Optional Comment? ")
                filename = './Dog-Business.csv'
                file_exists = os.path.isfile(filename)
                with open(filename, mode="a") as csv_file:
                    fieldnames = ['Date','Timestamp','Status','Optional Comment']
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    
                    if not file_exists:
                        writer.writeheader()

                    writer.writerow({'Date': d, 'Timestamp': t, 'Status': str(p), 'Optional Comment': str(opt_comment)})
                

        else:
            print("Input Error: I'm not sure what to do about " + inp)
    
    def help_menu(self):
        """ 
        Iterates through a dictionary of the menu prompt choices whenever this function is called.
        """
        for k in self.menu_items:
            print(k + " == " + self.menu_items[k])

    def print_version(self):
        print('Dog Logs Shell version: ' + self.version )


def return_date_string():
    """
    Returns a string of today's date.
    """
    today = date.today() 
    yy = str(today.year)
    mm = str(today.month)
    dd = str(today.day)
    date_stamp = str(mm + "/" + dd + "/" + yy)
    return date_stamp 

def return_current_time():
    # current date and time
    now = datetime.now()

    t = now.strftime("%H:%M:%S")
    return(t)

def main():
    menu = PromptMenu()
    print(30 * '#')
    menu.print_version()
    print('Type \'?\' for the help menu.')
    
    while menu.keep_promting:
        choice = str(input('Input Command: > '))
        menu.check_input(str(choice))

if __name__ == "__main__":
    main()