import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox
from fpdf import FPDF
from re import sub
import pyttsx3
import os
##filedialog mdodule for opening file by its method --->filedialog.askopenfilename()
## fond module we used to get the tuple of diff font style to choose style of text implementatin
## messagebox module can use for displaying the msg on exit
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-2 ].id)

main_application=tk.Tk()
main_application.geometry('700x600')
fno=1
main_application.title('untitled {} - Baborias Text Editor'.format(fno))

####################### main menu###################################

main_menu=tk.Menu()

#file menu
file=tk.Menu(main_menu,tearoff=False)# tear of false willl break the unnecssry paddind form the file butoons
#file icons

new_icon=tk.PhotoImage(file=r'icons\new.png')
open_icon=tk.PhotoImage(file=r'icons\open.png')
save_icon=tk.PhotoImage(file=r'icons\save.png')
save_as_icon=tk.PhotoImage(file=r'icons\save_as.png')
exit_icon=tk.PhotoImage(file=r'icons\exit.png')




#edit menu
edit=tk.Menu(main_menu,tearoff=False)
#edit icons

copy_icon=tk.PhotoImage(file=r'icons\copy.png')
paste_icon=tk.PhotoImage(file=r'icons\paste.png')
cut_icon=tk.PhotoImage(file=r'icons\cut.png')
clear_icon=tk.PhotoImage(file=r'icons\clear_all.png')
find_icon=tk.PhotoImage(file=r'icons\find.png')



#view meanu
view=tk.Menu(main_menu,tearoff=False)
#view icons

toolbar_icon=tk.PhotoImage(file=r'icons\tool_bar.png')
statusbar_icon=tk.PhotoImage(file=r'icons\status_bar.png')



#theme menu

color_themes=tk.Menu(main_menu,tearoff=False)

#theme icons
light_default_icon=tk.PhotoImage(file=r'icons\light_default.png')
light_plus_icon=tk.PhotoImage(file=r'icons\light_plus.png')
dark_icon=tk.PhotoImage(file=r'icons\dark.png')
red_icon=tk.PhotoImage(file=r'icons\red.png')
monokai_icon=tk.PhotoImage(file=r'icons\monokai.png')
night_blue_icon=tk.PhotoImage(file=r'icons\night_blue.png')

#smart _feature icon
speech_typing_icon=tk.PhotoImage(file=r'icons\speech.png')
typing_master_icon=tk.PhotoImage(file=r'icons\typing_master.png')
pdf_maker_icon=tk.PhotoImage(file=r'icons\pdf.png')

smart_features=tk.Menu(main_menu,tearoff=False)



#cascade

main_menu.add_cascade(label='File',menu=file)
main_menu.add_cascade(label='Edit',menu=edit)
main_menu.add_cascade(label='View',menu=view)
main_menu.add_cascade(label='Color Theme',menu=color_themes)
main_menu.add_cascade(label='Smart Features',menu=smart_features)



#------------------------end of main menu---------------------------#

####################### toolbar ###################################
toolbar=ttk.Label(main_application)
toolbar.pack(side=tk.TOP,fill=tk.X)

#font box
font_tuple=tk.font.families()
font_family=tk.StringVar()
font_box=ttk.Combobox(toolbar,width=30,textvariable=font_family,state='readonly')
font_box['values']=font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0, column=0, padx=5)

#size  box

size_var=tk.IntVar()
font_size=ttk.Combobox(toolbar,width=14,textvariable=size_var,state='readonly')
font_size['values']=tuple(range(8,81)) #creating tupple from 8 to 81
font_size.current(4) # defult size will be 4th index
font_size.grid(row=0, column=1, padx=5)

#bold,italic and underline button intial properties:
is_bold='normal'
is_italic='roman'
is_underline = 'normal'


######## buttons functionality

# bold button functionality
def change_bold():
    global is_bold
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        is_bold='bold'
        if is_underline!='normal':
            text_editor.configure(font=(current_font_family,current_font_size,is_bold,is_italic,is_underline))
        else:
            text_editor.configure(font=(current_font_family,current_font_size,is_bold,is_italic))
    if text_property.actual()['weight'] == 'bold':
        is_bold='normal'
        if is_underline != 'normal':
            text_editor.configure(font=(current_font_family, current_font_size, is_bold, is_italic, is_underline))
        else:
            text_editor.configure(font=(current_font_family, current_font_size, is_bold, is_italic))




# italic functionlaity
def change_italic():
    global is_italic
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        is_italic='italic'
        if is_underline != 'normal':
            text_editor.configure(font=(current_font_family, current_font_size, is_bold, is_italic, is_underline))
        else:
            text_editor.configure(font=(current_font_family, current_font_size, is_bold, is_italic))
    if text_property.actual()['slant'] == 'italic':
        is_italic='roman'
        if is_underline != 'normal':
            text_editor.configure(font=(current_font_family, current_font_size, is_bold, is_italic, is_underline))
        else:
            text_editor.configure(font=(current_font_family, current_font_size, is_bold, is_italic))
# underline functionality
def change_underline():
    global is_underline
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
        if is_bold != 'normal':
            is_underline='underline'
            text_editor.configure(font=(current_font_family, current_font_size, is_bold, is_italic, is_underline))
        else:
            text_editor.configure(font=(current_font_family, current_font_size,is_italic,is_underline))
    if text_property.actual()['underline'] == 1:
        is_underline='normal'
        if is_bold != 'normal':
            text_editor.configure(font=(current_font_family, current_font_size, is_bold, is_italic))
        else:
            text_editor.configure(font=(current_font_family, current_font_size,is_italic))

#bold button
bold_icon=tk.PhotoImage(file=r'icons\bold.png')
#bold button making
bold_btn=ttk.Button(toolbar,image=bold_icon,command=change_bold)
bold_btn.grid(row=0,column=2,padx=5)

# italic button
italic_icon = tk.PhotoImage(file=r'icons\italic.png')
#italic button making
italic_btn = ttk.Button(toolbar, image=italic_icon,command=change_italic)
italic_btn.grid(row=0, column=3, padx=5)

# underline button
underline_icon = tk.PhotoImage(file=r'icons\underline.png')
#underline button making
underline_btn = ttk.Button(toolbar, image=underline_icon,command=change_underline)
#underline_btn.configure(command=change_underline)
underline_btn.grid(row=0, column=4, padx=5)


# font color button
font_color_icon = tk.PhotoImage(file=r'icons\font_color.png')
# font functionality:::->
def change_font_color():
    color_var=tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])


#font color button making
font_color_btn = ttk.Button(toolbar, image=font_color_icon)
font_color_btn.configure(command=change_font_color)
font_color_btn.grid(row=0, column=5, padx=5)

# align left button
align_left_icon = tk.PhotoImage(file=r'icons\align_left.png')
align_left_btn = ttk.Button(toolbar, image=align_left_icon)
align_left_btn.grid(row=0, column=6, padx=5)

# align center button
align_center_icon = tk.PhotoImage(file=r'icons\align_center.png')
align_center_btn = ttk.Button(toolbar, image=align_center_icon)
align_center_btn.grid(row=0, column=7, padx=5)

# align right button
align_right_icon = tk.PhotoImage(file=r'icons\align_right.png')
align_right_btn = ttk.Button(toolbar, image=align_right_icon)
align_right_btn.grid(row=0, column=8, padx=5)





#------------------------end of toolbar---------------------------#

####################### text editor###################################

text_editor=tk.Text(main_application)
text_editor.config(wrap='word',relief=tk.FLAT)
scroll_bar=tk.Scrollbar(main_application)
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.focus_set()
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

#------------------------end of text editor---------------------------#


####################### status bar###################################

status_bar=ttk.Label(main_application,text='')
status_bar.pack(side=tk.BOTTOM)

#########status bar fuctionality####################################3
text_changed = False
def changed(event=None):
    global text_changed
    text_changed=True
    if text_editor.edit_modified():
        words = len(text_editor.get(1.0,'end-1c').split())# end-1c for removing the last new line character
        character =len(text_editor.get(1.0,'end-1c')) #.replace(' ','') if you not want sapce count
        status_bar.config(text=f'charcter:{character} words : {words}')
    text_editor.edit_modified(False)
text_editor.bind('<<Modified>>',changed)#shaveron sharveron modified
#----------------end of status bar fuctionality------------------#

#------------------------end of status bar---------------------------#

####################### main menu fuctionality###################################

#files_commands

#variable
url = ''

#new fucncionality-->

def new_file(event=None):
    global url,fno
    url=''
    fno+=1
    text_editor.delete(1.0,tk.END)
    main_application.title('untitled {} - Baborias Text Editor'.format(fno))  # it will make a title untitle.txt

file.add_command(label='New',image=new_icon,compound=tk.LEFT,accelerator='Ctrl+N',command=new_file)

#open fuctionality--->

def open_file(event=None):
    global url
    url=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File',filetypes=(('Text File','*.txt'),('All files','*.*')))
    try:
        with open (url,'r') as fr:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,fr.read())
    except FileNotFoundError:
        return
    except:
        return

    main_application.title(os.path.basename(url))#it will make a url as title

file.add_command(label='Open',image=open_icon,compound=tk.LEFT,accelerator='Ctrl+O',command=open_file)

#save functionality---->

def save_file(eveent=None):
    global url
    try:
        if url: #run in case of file already exist
            content=str(text_editor.get(1.0,'end-1c'))
            with open(url,'w',encoding='utf-8') as fw:
                fw.write(content)
        else: #will run in case of new file
            url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetype=(('Text File','*.txt'),('All files','*.*')))
            main_application.title(os.path.basename(url.name))  # it will make a url as title
            content2=text_editor.get(1.0,'end-1c')
            url.write(content2)
            url.close()
            url=url.name

    except : # not show any exception in case of excption but simply return the fuction
        return


file.add_command(label='Save',image=save_icon,compound=tk.LEFT,accelerator='Ctrl+S',command=save_file)

#save as functionality------>

def save_as_file(event=None):
    global url
    try:
        content=text_editor.get(1.0,'end-1c')
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetype=(('Text File','*.txt'),('All file','*.*')))
        url.write(content)
        url.close()
    except:
        return



file.add_command(label='Save as',image=save_as_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+S',command=save_as_file)

#exit functionality----->
def exit_file(event=None):
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning', 'Do you want to save the file ?')
            if mbox is True:
                if url:
                    content = text_editor.get(1.0, 'end-1c')
                    with open(url, 'w', encoding='utf-8') as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    content2 = str(text_editor.get(1.0, 'end-1c'))
                    url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except BaseException as b:
        print(b)
file.add_command(label='Exit',image=exit_icon,compound=tk.LEFT,accelerator='Ctrl+Q',command=exit_file)



#edit commands

edit.add_command(label='Copy',image=copy_icon,compound=tk.LEFT,accelerator='Ctrl+C',command=lambda:text_editor.event_generate('<Control c>'))
edit.add_command(label='Paste',image=paste_icon,compound=tk.LEFT,accelerator='Ctrl+V',command=lambda:text_editor.event_generate('<Control v>'))
edit.add_command(label='Cut',image=cut_icon,compound=tk.LEFT,accelerator='Ctrl+X',command=lambda:text_editor.event_generate('<Control x>'))
edit.add_command(label='Clear',image=clear_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+X',command=lambda:text_editor.delete(1.0,tk.END))

#find fuctionality *************************
def find_func(event=None):
    def find(event=None):
        word=find_input.get()
        text_editor.tag_remove('match','1.0',tk.END)# it is compulsory to remove previous tag on new searh
        matches=0
        if word:
            start_pos='1.0'
            while True:
                start_pos=text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos=f'{start_pos }+{len(word)}c' #####????????
                text_editor.tag_add('match',start_pos,end_pos)
                matches+=1
                start_pos=end_pos
                text_editor.tag_config('match',foreground='red',background='yellow')


    def replace(event=None):
        word=find_input.get()
        replace_text=replace_input.get()
        content=text_editor.get(1.0,tk.END)
        new_content=content.replace(word,replace_text)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)



    find_dialogue = tk.Toplevel()
    find_dialogue.geometry('380x180+500+200')
    find_dialogue.title('Find')
    find_dialogue.resizable(0, 0)##this will stop to maximizing the find\replace window

    ## frame
    find_frame = ttk.LabelFrame(find_dialogue, text='Find/Replace')
    find_frame.pack(pady=20)

    ## labels
    text_find_label = ttk.Label(find_frame, text='Find : ')
    text_replace_label = ttk.Label(find_frame, text='Replace')

    ## entry
    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)

    ## button
    find_button = ttk.Button(find_frame, text='Find',command=find)
    replace_button = ttk.Button(find_frame, text='Replace',command=replace)

    ## label grid
    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)

    ## entry grid
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)

    ## button grid
    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)

    find_dialogue.mainloop()

edit.add_command(label='Find',image=find_icon,compound=tk.LEFT,accelerator='Ctrl+F',command=find_func)
#end of find functionality--------------->

#view checkbutton and functionality:
show_toolbar=tk.BooleanVar()
show_toolbar.set(True)
show_statusbar=tk.BooleanVar()
show_statusbar.set(True)
def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        toolbar.pack_forget()
        show_toolbar=False
    else:
        text_editor.pack_forget()# we can't pack directly on showing because it will disturb our arrangemnet
                                    #thats why we are deleting everything first
        status_bar.pack_forget()
        toolbar.pack(side=tk.TOP,fill=tk.X)
        text_editor.pack(fill=tk.BOTH,expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar=True
def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar=False
    else:
        status_bar.pack(side=tk.BOTTOM,)
        show_statusbar=True


view.add_checkbutton(label='Tool Bar',image=toolbar_icon,variable=show_toolbar,command=hide_toolbar,compound=tk.LEFT)
view.add_checkbutton(label='Status Bar',variable=show_statusbar,image=statusbar_icon,command=hide_statusbar,compound=tk.LEFT)


#theme icons radiobutton

theme_choice=tk.StringVar()
color_icons=(light_default_icon,light_plus_icon,dark_icon,red_icon,monokai_icon,night_blue_icon)
color_dict={
    'Light Default':('#000000','#ffffff'), #(font color, bakground color)
    'Light Plus':('#474747','#e0e0e0'),
    'Dark':('#c4c4c4','#2d2d2d'),
    'Red':('#2d2d2d','#ffe8e8'),
    'Monakai':('#d3b774','#474747'),
    'Night Blue':('#ededed','#6b9dc2')
}
def change_theme():
    chosen_theme=theme_choice.get()
    color_tuple=color_dict.get(chosen_theme)
    fg_color,bg_color=color_tuple  #tupple unpacking
    text_editor.config(bg=bg_color,fg=fg_color)


count=0
for i in color_dict:
    color_themes.add_radiobutton(label=i,image=color_icons[count],variable=theme_choice,compound=tk.LEFT,command=change_theme)
    count+=1

# smart feature fuctionality-->

#pdf maker functionality
def pdf_maker(event=None):
    global url
    mbox = messagebox.askquestion('Pdf Convertor: file must be saved before preceding', 'Do you want to make Pdf')
    if mbox=='yes':
        if url:
            f_name=os.path.basename(url)
            pdf_name=sub('.txt','.pdf',f_name) #from regular expressio subsiture function that will convert txt extention to pdf
            try:
                f = open(url, 'r')
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial', size=10)
                for line in f.readlines():
                    pdf.cell(w=190, h=5, txt=line, border=0, ln=1, align='L')
                pdf.output(pdf_name)
                res=messagebox.askquestion('File save Sucessfully','Do you want to open pdf')
                if res=='yes':
                    os.system(pdf_name)
                else:
                    pass
                return
            except:
                return
        else:
            mbox = messagebox.showwarning('','File not saved')

#listen text functionality


def speak(event=None):
    text= text_editor.get(1.0, 'end')
    engine.say(text)
    engine.runAndWait()


#typing master functionlity
def typing_master(event=None):
    messagebox.showinfo('Typing Master','Sorry!! this is under construction')

smart_features.add_command(label='Listen Text',image=speech_typing_icon,compound=tk.LEFT,command=speak)
smart_features.add_command(label='Typing Master',image=typing_master_icon,compound=tk.LEFT,command=typing_master)
smart_features.add_command(label='Make Pdf',image=pdf_maker_icon,compound=tk.LEFT,command=pdf_maker)

#------------------------end of main menu fuctionality---------------------------#


############## tool bar funcionality######################################

#font family functionlity
current_font_family='Arial'
current_font_size=10

def change_font_type(event=None):
    global current_font_family
    current_font_family=font_family.get()
    text_editor.config(font=(current_font_family,current_font_size))

def change_font_size(event=None):
    global current_font_size
    current_font_size=font_size.get()
    text_editor.config(font=(current_font_family,current_font_size))

font_box.bind('<<ComboboxSelected>>',change_font_type) #bind will automatically add event on combox selection
font_size.bind('<<ComboboxSelected>>',change_font_size)

text_editor.config(font=('Arial',10)) #by default will be


#align functionality

#align left fuctionality
def align_left():
    text_content=text_editor.get(1.0,'end')#taking content of text field into variable
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)#deleting the previous content
    text_editor.insert(tk.INSERT,text_content,'left')# what and where you have to insert
                                                       #and writing text at left position
align_left_btn.configure(command=align_left)

#align center fuctionality
def align_center():
    text_content=text_editor.get(1.0,'end')#taking content of text field into variable
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)#deleting the previous content
    text_editor.insert(tk.INSERT,text_content,'center')# what and where you have to insert
                                                       #and writing text at left position
align_center_btn.configure(command=align_center)

#align right fuctionality
def align_right():
    text_content=text_editor.get(1.0,'end')#taking content of text field into variable
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)#deleting the previous content
    text_editor.insert(tk.INSERT,text_content,'right')# what and where you have to insert
                                                       #and writing text at left position
align_right_btn.configure(command=align_right)


#------------------end of tool bar functionality-------------------------#

####right key _press fuctionality:
def right_click_func(event=None):
    pass




####end of right click functionality--->
main_application.config(menu=main_menu)
##binding shortcut keys:::-->
main_application.bind('<Control-n>',new_file)
main_application.bind('<Control-o>',open_file)
main_application.bind('<Control-s>',save_file)
main_application.bind('<Control-Alt-s>',save_as_file)
main_application.bind('<Control-x>',exit_file)
main_application.bind('<Control-f>',find_func)
main_application.bind('<Button-3>',right_click_func)


main_application.mainloop()