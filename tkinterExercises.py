from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import ttk
from tkinter import Canvas
from tkinter import Spinbox
from tkinter import Entry
from tkinter import Radiobutton
from tkinter import scrolledtext as tkst
from tkinter import Listbox
import webbrowser


root = Tk()

root.title('Introduction to Tkinter')

root.geometry('800x680')
root.resizable(0,0)

#middle widgets

welcome_text = Label(root, text = 'Welcome to Tkinter', font = ('Arial Bold',15))
welcome_text.place(y= 20, x = 400, anchor = 'center')

#right widgets

def open_youtube():
	webbrowser.open_new('https://www.youtube.com')
youtube_button = Button(root, text = 'Go to Youtube', command = open_youtube)
youtube_button.place(x = 200, y = 50, anchor = 'center')



def write_text():
	sentence = Tk()
	sentence.title('Welcome developer!')
	label = Label(sentence, text = 'You are the best!', font = ('Arial Bold', 15))
	label.place(x = 100, y = 20, anchor = 'center')
	close_button = Button(sentence, text = 'Okay', command = sentence.destroy)
	close_button.place(x = 100, y = 50, anchor = 'center')
	sentence.geometry('200x80')
	sentence.mainloop()
print_button = Button(root, text = "Say: You are the best!", command = write_text)
print_button.place(x = 200, y = 100, anchor = 'center')

def popup():
	popup = Tk()

	popup.title("Dev's Message")
	
	label = Label(popup, text = 'No pain no gain', font = ('Arial', 16))
	label.place(x = 150, y = 20, anchor = 'center')
	
	exit_popup = Button(popup, text = 'Okay', command = popup.destroy)
	exit_popup.place(x = 150, y = 50, anchor = 'center')
	popup.geometry('300x90')
	popup.mainloop()

message_button = Button(root, text = "Dev's Message", command = popup)
message_button.place(x = 200, y = 150, anchor = 'center')

planguages_heading = Label(root, text = 'Choose programming language', font = ('Arial Bold', 12))
planguages_heading.place(x = 200, y = 200, anchor = 'center')

planguages_combobox = ttk.Combobox(root, values = ['Python', 'Java', 'C++'])
planguages_combobox.place(x = 200, y = 250, anchor = 'center')


myLevel_title = Label(root, text = 'Choose your programming level', font = ('Arial Bold', 12))
myLevel_title.place(x = 200, y = 300, anchor = 'center')


masterLevel_checkbutton = ttk.Checkbutton(text = 'Master', )
masterLevel_checkbutton.place(x = 200, y = 340, anchor = 'center')
intermLevel_checkbutton = ttk.Checkbutton(text = 'Intermediate', )
intermLevel_checkbutton.place(x = 200, y = 370, anchor = 'center')
beginLevel_checkbutton = ttk.Checkbutton(text = 'Beginner', )
beginLevel_checkbutton.place(x = 200, y = 400, anchor = 'center')

experiences_title = Label(root, text = 'Programming Experiences', font = ('Arial Bold',12))
experiences_title.place(x = 200, y = 450, anchor = 'center')
experiences = Listbox(root, height = '8', width = '20')
experiences.insert(1, 'Python')
experiences.insert(2, 'HTML')
experiences.insert(3, 'CSS')
experiences.place(x = 200, y = 540, anchor = 'center')

#left widgets

compilers_label = Label(root, text = 'Choose your prefered compiler', font = ('Arial Bold', 12))
compilers_label.place(x = 600, y = 50, anchor = 'center')

compilers_spinbox = Spinbox(root, values = ['VS code', 'Atom', 'Notepad++'])
compilers_spinbox.place(x = 600, y = 90, anchor = 'center')

name_label = Label(root, text = 'Name', font = ('Arial', 12)).place(x = 490, y = 140, anchor = 'w')
password_label = Label(root, text = 'Password', font = ('Arial', 12)).place(x = 490, y = 180, anchor = 'w')
name_entry = Entry(root)
name_entry.place(x = 560, y = 125)
password_entry = Entry(root)
password_entry.place(x = 560, y = 165)

l = []
def submit_ID_info():
	l.append((name_entry.get(), password_entry.get()))
	confirm = Tk()
	confirm.title('Confirmation')
	thankyou = Label(confirm, text = 'Thank you for your information!', font = ('Arial Bold', 15))
	thankyou.place(x = 150, y = 20, anchor = 'center')
	escape_confirm = Button(confirm, text = 'Okay', command = confirm.destroy)
	escape_confirm.place(x = 150, y = 60, anchor = 'center')
	confirm.geometry('300x100')
	confirm.mainloop()
submit_id = Button(root, text = 'Submit', activebackground = 'blue', activeforeground = 'white', command = submit_ID_info).place(x = 750, y = 220, anchor = 'e')

sexuality_title = Label(root, text = 'Choose your sexuality:', font = ('Arial Bold', 12))
sexuality_title.place(x = 600, y = 290, anchor = 'center')
male = Radiobutton(root, text = 'Male', value = 1)
male.place(x = 480, y = 330, anchor = 'w')
female = Radiobutton(root, text = 'Female', value = 2)
female.place(x = 580, y = 330, anchor = 'w')
others = Radiobutton(root, text = 'Others', value = 3)
others.place(x = 680, y = 330, anchor = 'w')

blackboard_title = Label(root, text = 'BLACKBOARD', font = ('Arial Bold', 12))
blackboard_title.place(x = 600, y = 420, anchor = 'center')
blackboard = tkst.ScrolledText(root, width = 40, height = 10, bg = 'black', fg = 'white')
blackboard.place(x = 615, y = 530, anchor = 'center')

#midle widgets
exit_project_button = Button(root, text = 'Exit Program', font = ('Arial Bold', 11),command = root.destroy)
exit_project_button.place(x = 400, y = 660, anchor = 'center')

root.mainloop()

print(l)


