# Assignment 7
# GUI application that allows the user to browse, search, and sort the Restaurants database
import tkinter
from tkinter import messagebox
import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import  ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
import xlrd
import tkSelenium_KI
import tkEnhancement



# GUI customizations for color, fonts, and spacing (you may change)
bg_color = 'steelblue'
fg_color = 'white'
label_fg = '#1d3549'
data_font = "Verdana 12 normal"
label_font = "Verdana 12 bold"
pad = 20

db = None    # db object is a global variable, that initially has no value


# GUI object that represents the Restaurant Browser application
class RestaurantBrowser:
    def __init__(self):
        # Main window and Label
        self.main_window = tkinter.Tk()
        self.main_window.title("TSI KI and Idea Manager")
        self.main_window.geometry('600x550')
        #self.main_window.geometry('660x650')
        self.main_window.configure(background=bg_color)
        tkinter.Label(self.main_window, text='KI and Idea Linker', fg=label_fg, bg=bg_color, padx=pad, pady=pad, font=label_font).grid(row=0, column=0, sticky=tkinter.constants.W)
		
        #scrollbar = Scrollbar(self.main_window)
        #scrollbar.grid(column=1, row=0, sticky='ns')

		
        
        # Refresh buttom
        self.ki_value= tkinter.StringVar()
        tkinter.Button(self.main_window, text="Link KI", command=lambda:self.link_ki(self.ki_value.get()), fg=label_fg, bg="#adebad", padx=10, font=label_font, borderwidth=0).grid(row=1, column=1, sticky=tkinter.constants.W)
        self.ki_value_entry = tkinter.Entry(self.main_window, width=15, font=data_font, textvariable=self.ki_value).grid(row=1, column=0)


        self.idea_value= tkinter.StringVar()#THIS IS USED as var for the linker
        tkinter.Button(self.main_window, text="Upvote Idea", command=lambda:self.upvote_idea(self.idea_value.get()), fg=label_fg, bg="#adebad", padx=10, font=label_font, borderwidth=0).grid(row=3, column=1, sticky=tkinter.constants.W)
        self.idea_value_entry = tkinter.Entry(self.main_window, width=15, font=data_font, textvariable=self.idea_value).grid(row=3, column=0)
		
        # Column header Buttons -- when a button is clicked, the restaurant data is sorted by the selected column
        try:
            #tkinter.Button(self.main_window, text='Watchdog Name', command=lambda: self.sort_db('Watchdog Name'), fg=label_fg, bg="#2db92d", anchor="w", padx=pad, font=label_font, borderwidth=0).grid(row=1, column=0, sticky=tkinter.constants.EW)
            #tkinter.Button(self.main_window, text='Complete', command=lambda: self.sort_db('Complete'), fg=label_fg, bg="#32cd32", anchor="w", padx=pad, font=label_font, borderwidth=0).grid(row=1, column=1, sticky=tkinter.constants.EW)
           # tkinter.Button(self.main_window, text='Update Status', command=lambda: self.sort_db('Complete'), fg=label_fg, bg="#32cd32", anchor="w", padx=pad, font=label_font, borderwidth=0).grid(row=1, column=2, sticky=tkinter.constants.EW)
            #Not sure if Lamda or EW (from W) fixed this
		 #Something in here is the issue
                self.output = tkinter.StringVar()
                self.output_label = tkinter.Label(self.main_window,
                                  textvariable=self.output,
                                  background=bg_color,
                                  font=label_font).grid(row=5, column=1)
# Call this function when the GUI is initialized to display all of the restaurant data
# self.display_rows(rows)
#self.min_refresh()



                tkinter.mainloop()
        except IndexError as err:
        	        print('Index error: ', err)
        #except Exception as err:
           # print('An error occurred: ', err)

    # Display all of the restaurant data in the rows parameter. 'rows' will contain the results of the most recent SQL query
    def link_ki(self, ki_value):
       # try: 
          tkSelenium_KI.ki_linker(ki_value)
        #except Exception as err:
        	        #print('An error occured', err)
    def upvote_idea(self, idea_value):
          tkEnhancement.upvote_idea(idea_value)  
	
          
# Connect to the database
# Define, execute, and fetch the results of the SQL query that retrieves all restaurant data
# Create the GUI object, RestaurantBrowser, and pass it the rows containing the restaurant data
def main():
	RestaurantBrowser()
    #add something in here?
    
    #  client .close()?
    #else:
       # print('Error:', dbname, 'does not exist')
    #except sqlite3.IntegrityError as err:
        #print('Integrity Error on connect:', err)
  #  except sqlite3.OperationalError as err:
     #   print('Operational Error on connect:', err)
    #except sqlite3.Error as err:
      #  print('Error on connect:', err)
main()
