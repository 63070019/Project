from tkinter import *
from tkinter import messagebox
from random import choices


box, item, rate_box, sr_box, sr_rate, ssr_box, ssr_rate, grade = [], [], [], [], [], [], [], []


def clears():
    text_label.destroy()
    button_get['state'] = NORMAL


def get():
    global text_label
    tier = tier_t.get()
    if tier == 1:
        tier = "R"
    elif tier == 2:
        tier = "SR"
    elif tier == 3:
        tier = "SSR"
    elif tier == 4:
        tier = "None"
    elif tier == 0:
        messagebox.showerror("Error Tier", "Please select tier")
    
    if item_t.get() == "":
        messagebox.showerror("Error Item", "Please enter item")

    if tier != 0 and item_t.get() != "":
        text_label = Label(root, text="Save    Item:  %s      Tier:  %s       Rate:  %s"%(item_t.get(), tier, rate_t.get()), font = 'dubai 12 bold')
        print("รับค่า    Item:  %s      Tier:  %s       Rate:  %s"%(item_t.get(), tier, rate_t.get()))

        box.append(item_t.get())
        rate_box.append(float(rate_t.get()))
        grade.append(tier)


        if tier == "SR" or tier == "SSR":#ประกัน 10
                    sr_box.append(item_t.get())
                    sr_rate.append(float(rate_t.get()))
                    if tier == "SSR": #ประกันใหญ่
                        ssr_box.append(item_t.get())
                        ssr_rate.append(float(rate_t.get()))

        item_t.delete(0, END)
        rate_t.delete(0, END)

        text_label.pack()

        sampling_get['state'] = NORMAL
        button_get['state'] = DISABLED


def sampling_option():
    global garuntee_button
    global normal_button
    normal_button = Button(root, text=' Normal  ', font = 'dubai 10 bold', command=sampling_n, bg = 'oldlace')
    normal_button.pack()
    garuntee_button = Button(root, text='Garuntee', font = 'dubai 10 bold', command=sampling_g, bg = 'tomato')
    garuntee_button.pack()


def sampling_n():
    garuntee_button['state'] = DISABLED
    Label(root, text="สุ่มแบบ Normal", font = 'dubai 10 bold').pack()

    def sampling_calculate_n():
        get = []


        roll_all = int(roll_t.get())

        count = 0
        keeper = []
        printer = []


        for _ in range(1, roll_all+1):
            get.append(choices(box, weights=rate_box, k=1))
        for unit in get:
            if unit not in keeper:
                keeper.append(unit)
        for j in keeper:
            for k in get:
                if j == k:
                    count += 1
            printer.append(count)
            count = 0
        keeper = [i[0] for i in keeper]
        for l in range(len(keeper)):
            print("ได้รับ     %s"%keeper[l], end = " ")
            print("จำนวน     %s"%printer[l]+' ชิ้น')



    roll_label = Label(root, text="กี่ Roll", font = 'dubai 10 bold')
    roll_label.pack()
    roll_t = Entry(root)
    roll_t.pack()


    normal_submit = Button(root, text='Submit', font = 'dubai 10 bold', command=sampling_calculate_n,  bg = 'tomato')
    normal_submit.pack()


def sampling_g():
    normal_button['state'] = DISABLED
    Label(root, text="สุ่มแบบมี Garuntee", font = 'dubai 10 bold').pack()

    def sampling_calculate_g():
        if len(sr_box) == 0 :
            messagebox.showerror("Error SR", "Please enter SR")
        elif len(ssr_box) == 0:
            messagebox.showerror("Error SSR", "Please enter SSR")
        else:
            get = []

            garuntee = 0
            garuntee_option = int(garuntee_option_t.get())
            roll_all = int(roll_t.get())


            count = 0
            keeper = []
            printer = []


            for roll in range(1, roll_all+1):
                garuntee += 1
                if roll % 10 != 0:
                    get.append(choices(box, weights=rate_box, k=1))
                    if choices(box, weights=rate_box, k=1) in ssr_box: #ถ้าได้ SSR การันตีจะรีกับไปที่ 0
                        garuntee = 0
                else:
                    if garuntee == garuntee_option: #ได้ SSR แน่นอน การันตีจะรีกับไปที่ 0
                        get.append(choices(ssr_box, weights=ssr_rate, k=1)) # สุ่ม SSR
                        garuntee = 0
                    else:
                        get.append(choices(sr_box, weights=sr_rate, k=1)) # สุ่ม SR
                        if choices(sr_box, weights=sr_rate, k=1) in ssr_box: #ถ้าได้ SSR การันตีจะรีกับไปที่ 0
                            garuntee = 0


            for unit in get:
                if unit not in keeper:
                    keeper.append(unit)
            for j in keeper:
                for k in get:
                    if j == k:
                        count += 1
                printer.append(count)
                count = 0
            keeper = [i[0] for i in keeper]
            for l in range(len(keeper)):
                print("ได้รับ     %s"%keeper[l], end = " ")
                print("จำนวน     %s"%printer[l]+' ชิ้น')



    garuntee_option_label = Label(root, text="Garuntee Option(ประกัน)", font = 'dubai 10 bold')
    garuntee_option_label.pack()
    garuntee_option_t = Entry(root)
    garuntee_option_t.pack()



    roll_label = Label(root, text="กี่ Roll", font = 'dubai 10 bold')
    roll_label.pack()
    roll_t = Entry(root)
    roll_t.pack()

    garuntee_submit = Button(root, text='Submit', command=sampling_calculate_g, font = 'dubai 10 bold', bg = 'tomato')
    garuntee_submit.pack()



root = Tk()
root.title("Gacha_simulater")
root.geometry("500x800")


item_label = Label(root, text="Item", font = 'dubai 10 bold')
item_label.pack()
item_t = Entry(root, width=40)
item_t.pack()


rate_label = Label(root, text="Rate", font = 'dubai 10 bold')
rate_label.pack()
rate_t = Entry(root, width=40)
rate_t.pack()


tier_t = IntVar()

tier_label = Label(root, text="Tier", font = 'dubai 10 bold')
tier_label.pack()
Radiobutton(root, text='    R    ', variable=tier_t, value=1).pack()
Radiobutton(root, text='   SR   ', variable=tier_t, value=2).pack()
Radiobutton(root, text='  SSR  ', variable=tier_t, value=3).pack()
Radiobutton(root, text='None ', variable=tier_t, value=4).pack()


Label(root, text=" ").pack()

button_get = Button(root, text=' Get  ', font = 'dubai 10 bold', command = get, bg = 'tomato')
button_get.pack()

button_clear = Button(root, text='Clear', font = 'dubai 10 bold', command = clears, bg = 'oldlace')
button_clear.pack()


Label(root, text=" ").pack()

sampling_get = Button(root, text='Sampling', font = 'dubai 10 bold', command = sampling_option, bg = 'tomato')
sampling_get['state'] = DISABLED
sampling_get.pack()




root.mainloop()
