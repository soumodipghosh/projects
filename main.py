from tkinter import *
import random
from time import sleep
import threading

#######functionality part
totaltime=60
time=0
wrongwords=0
elapsedtimeinminutes=0
def start_timer():
    startbutton.config(state=DISABLED)
    global time
    textarea.config(state=NORMAL)
    textarea.focus()

    for time in range(1,61):
        elapsed_timer_label.config(text=time)
        remainingtime=totaltime-time
        remaining_timer_label.config(text=remainingtime)
        sleep(1)
        root.update()

    textarea.config(state=DISABLED)
    resetbutton.config(state=NORMAL)

def count():
    global wrongwords
    while time!=totaltime:
        entered_paragraph=textarea.get(1.0,END).split()
        totalwords=len(entered_paragraph)
    totalwords_count_label.config(text=totalwords)

    para_word_list=label_paragraph["text"].split()

    for pair in list(zip(para_word_list, entered_paragraph)):
        if pair[0]!=pair[1]:
            wrongwords+=1

    wrongwords_count_label.config(text=wrongwords)

    elapsedtimeinminutes=time/60
    wpm=(totalwords-wrongwords)/elapsedtimeinminutes
    wpm_count_label.config(text=wpm)
    gross_wpm=totalwords/elapsedtimeinminutes
    accuracy=wpm/gross_wpm*100
    accuracy=round(accuracy)
    accuracy_percentage_label.config(text=str(accuracy)+"%")

def start():
    t1=threading.Thread(target=start_timer)
    t1.start()

    t2=threading.Thread(target=count)
    t2.start()

def reset():
    global time,elapsedtimeinminutes
    time=0
    elapsedtimeinminutes=0
    startbutton.config(state=NORMAL)
    resetbutton.config(state=DISABLED)
    textarea.config(state=NORMAL)
    textarea.delete(1.0,END)
    textarea.config(state=DISABLED)

    elapsed_timer_label.config(text="0")
    remaining_timer_label.config(text="0")
    wpm_count_label.config(text="0")
    accuracy_percentage_label.config(text="0")
    totalwords_count_label.config(text="0")
    wrongwords_count_label.config(text="0")


root = Tk()
root.geometry("900x700+200+10")
root.resizable (0,0)

mainframe=Frame(root,bd=0)
mainframe.grid ()

titleframe=Frame(mainframe,bg="orange")
titleframe.grid(row=0, column=0)

titleLabel=Label(titleframe,text="Master Typing", font=("algerian",30,"bold"),bg="goldenrod3",fg="white",width=40,bd=10)
titleLabel.grid(pady=5)

paragraph_frame=(mainframe)
paragraph_frame.grid(row=1,column=0)

paragraph_list=["Electric car's are the future in the auto industry. As climate change get's worse, governments are going to start limiting the number of gasoline car's being built. The cost of gas will continue to rise, which will make it harder for people to afford to run gas powered cars.",
                "Installing solar panels will improve your finance. Secondly, many parts of the world have the solar panels set up so a family can sell the electricity back to the electric company.",
                "Life a journey travelled on the highway of time. Therefore, time is precious. Every moment in life should be properly utilized, as time, once lost, can never be recovered.",
                "Recently, i had the pleasure of seeing one of william shakespeare's most beloved comedies, A Midsummer Night's Dream, performed beautifully at the Los Angeles Repertory Theatre in downtown Los Angeles.",
                "A paragraph is often defined as a group of related sentences in which one single, main idea is developed. In a typical paragraph, the first sentence declares the main topic of the paragraph and the rest of the sentences develop or support the main idea.",
                "Discipline is one such trait that requires a set of rules, behavioral patterns and paradigm. If you bring together these aspects, you get a balanced life.",
                "Weather in Wisconsin has been especially fierce this week. It all beqan on Tuesday, when a tornado swept through the St. Croix River Valley. Wednesday evening another tornado dropped down on the suburbs of Milwaukee."]

random.shuffle(paragraph_list)

label_paragraph =Label(paragraph_frame,text=paragraph_list[0],wraplength=700,justify=LEFT,font=("arial",15,"bold"))
label_paragraph.grid(row=1,column=0)

textarea_frame=Frame(mainframe)
textarea_frame.grid(row=2,column=0)

textarea=Text(textarea_frame,font=("arial",10,"bold"),width=100,height=7,bd=4,relief=GROOVE,wrap="word")
textarea.grid()

frame_output=Frame(mainframe)
frame_output.grid(row=3,column=0)

elapsed_time_label=Label(frame_output,text="Elapsed Time",font=("Tahoma",12,"bold"),fg="red")
elapsed_time_label.grid(row=0,column=0,padx=2)

elapsed_timer_label=Label(frame_output,text="0",font=("Tahoma",12,"bold"),fg="black")
elapsed_timer_label.grid(row=0,column=1,padx=2)

remaining_time_label=Label(frame_output,text="Remaining Time",font=("Tahoma",12,"bold"),fg="red")
remaining_time_label.grid(row=0,column=2,padx=2)

remaining_timer_label=Label(frame_output,text="60",font=("Tahoma",12,"bold"),fg="black")
remaining_timer_label.grid(row=0,column=3,padx=2)

wpm_label=Label(frame_output,text="WPM",font=("Tahoma",12,"bold"),fg="red")
wpm_label.grid(row=0,column=4,padx=2)

wpm_count_label=Label(frame_output,text="0",font=("Tahoma",12,"bold"),fg="black")
wpm_count_label.grid(row=0,column=5,padx=2)

totalwords_label=Label(frame_output,text="Total words",font=("Tahoma",12,"bold"),fg="red")
totalwords_label.grid(row=0,column=6,padx=2)

totalwords_count_label=Label(frame_output,text="0",font=("Tahoma",12,"bold"),fg="black")
totalwords_count_label.grid(row=0,column=7,padx=2)

wrongwords_label=Label(frame_output,text="Wrong words",font=("Tahoma",12,"bold"),fg="red")
wrongwords_label.grid(row=0,column=8,padx=2)

wrongwords_count_label=Label(frame_output,text="0",font=("Tahoma",12,"bold"),fg="black")
wrongwords_count_label.grid(row=0,column=9,padx=2)

accuracy_label=Label(frame_output,text="Accuracy",font=("Tahoma",12,"bold"),fg="red")
accuracy_label.grid(row=0,column=10,padx=2)

accuracy_percentage_label=Label(frame_output,text="0",font=("Tahoma",12,"bold"),fg="black")
accuracy_percentage_label.grid(row=0,column=11,padx=2)

buttons_frame=Frame(mainframe)
buttons_frame.grid(row=4,column=0)

startbutton=Button(buttons_frame,text="Start", command=start)
startbutton.grid(row=0,column=0,padx=20)

resetbutton=Button(buttons_frame,text="Reset", state=DISABLED, command=reset)
resetbutton.grid(row=0,column=1,padx=20)

exitbutton=Button(buttons_frame,text="Exit", command=root.destroy)
exitbutton.grid(row=0,column=2,padx=20)

keyboard_frame=Frame(mainframe)
keyboard_frame.grid(row=5,column=0)

frame1to0=Frame(keyboard_frame)
frame1to0.grid(row=0,column=0,pady=3)

label1=Label(frame1to0,text="1",bg="black",fg="white",font=("arial",10,"bold"),width=5,height=2,bd=10,relief=GROOVE)
label2=Label(frame1to0,text="2",bg="black",fg="white",font=("arial",10,"bold"),width=5,height=2,bd=10,relief=GROOVE)
label3=Label(frame1to0,text="3",bg="black",fg="white",font=("arial",10,"bold"),width=5,height=2,bd=10,relief=GROOVE)
label4=Label(frame1to0,text="4",bg="black",fg="white",font=("arial",10,"bold"),width=5,height=2,bd=10,relief=GROOVE)
label5=Label(frame1to0,text="5",bg="black",fg="white",font=("arial",10,"bold"),width=5,height=2,bd=10,relief=GROOVE)
label6=Label(frame1to0,text="6",bg="black",fg="white",font=("arial",10,"bold"),width=5,height=2,bd=10,relief=GROOVE)
label7=Label(frame1to0,text="7",bg="black",fg="white",font=("arial",10,"bold"),width=5,height=2,bd=10,relief=GROOVE)
label8=Label(frame1to0,text="8",bg="black",fg="white",font=("arial",10,"bold"),width=5,height=2,bd=10,relief=GROOVE)
label9=Label(frame1to0,text="9",bg="black",fg="white",font=("arial",10,"bold"),width=5,height=2,bd=10,relief=GROOVE)
label0=Label(frame1to0,text="0",bg="black",fg="white",font=("arial",10,"bold"),width=5,height=2,bd=10,relief=GROOVE)
label1.grid(row=0,column=0,padx=5)
label2.grid(row=0,column=1,padx=5)
label3.grid(row=0,column=2,padx=5)
label4.grid(row=0,column=3,padx=5)
label5.grid(row=0,column=4,padx=5)
label6.grid(row=0,column=5,padx=5)
label7.grid(row=0,column=6,padx=5)
label8.grid(row=0,column=7,padx=5)
label9.grid(row=0,column=8,padx=5)
label0.grid(row=0,column=9,padx=5)

frameqtop = Frame(keyboard_frame)
frameqtop.grid(row=1, column=0,pady=3)
labelQ=Label(frameqtop,text="Q",bg="black",fg="white",font=("arial",10,"bold"),width=5,height=2,bd=10,relief=GROOVE)
labelW=Label(frameqtop,text="W",bg="black",fg="white",font=("arial",10,"bold"),width=5,height=2,bd=10,relief=GROOVE)
labelE=Label(frameqtop,text="E",bg="black",fg="white",font=("arial",10,"bold"),width=5,height=2,bd=10,relief=GROOVE)
labelR=Label(frameqtop,text="R",bg="black",fg="white",font=("arial",10,"bold"),width=5,height=2,bd=10,relief=GROOVE)
labelT=Label(frameqtop,text="T",bg="black",fg="white",font=("arial",10,"bold"),width=5,height=2,bd=10,relief=GROOVE)
labelY=Label(frameqtop,text="Y",bg="black",fg="white",font=("arial",10,"bold"),width=5,height=2,bd=10,relief=GROOVE)
labelU=Label(frameqtop,text="U",bg="black",fg="white",font=("arial",10,"bold"),width=5,height=2,bd=10,relief=GROOVE)
labelI=Label(frameqtop,text="I",bg="black",fg="white",font=("arial",10,"bold"),width=5,height=2,bd=10,relief=GROOVE)
labelO=Label(frameqtop,text="O",bg="black",fg="white",font=("arial",10,"bold"),width=5,height=2,bd=10,relief=GROOVE)
labelP=Label(frameqtop,text="P",bg="black",fg="white",font=("arial",10,"bold"),width=5,height=2,bd=10,relief=GROOVE)
labelQ.grid(row=0,column=0,padx=5)
labelW.grid(row=0,column=1,padx=5)
labelE.grid(row=0,column=2,padx=5)
labelR.grid(row=0,column=3,padx=5)
labelT.grid(row=0,column=4,padx=5)
labelY.grid(row=0,column=5,padx=5)
labelU.grid(row=0,column=6,padx=5)
labelI.grid(row=0,column=7,padx=5)
labelO.grid(row=0,column=8,padx=5)
labelP.grid(row=0,column=9,padx=5)

frameatol=Frame(keyboard_frame)
frameatol.grid(row=2,column=0,pady=3)
labelA=Label(frameatol,text="A",bg="black",fg="white",font=("arial",10,"bold"),width=5,height=2,bd=10,relief=GROOVE)
labelS=Label(frameatol,text="S",bg="black",fg="white",font=("arial",10,"bold"),width=5,height=2,bd=10,relief=GROOVE)
labelD=Label(frameatol,text="D",bg="black",fg="white",font=("arial",10,"bold"),width=5,height=2,bd=10,relief=GROOVE)
labelF=Label(frameatol,text="F",bg="black",fg="white",font=("arial",10,"bold"),width=5,height=2,bd=10,relief=GROOVE)
labelG=Label(frameatol,text="G",bg="black",fg="white",font=("arial",10,"bold"),width=5,height=2,bd=10,relief=GROOVE)
labelH=Label(frameatol,text="H",bg="black",fg="white",font=("arial",10,"bold"),width=5,height=2,bd=10,relief=GROOVE)
labelJ=Label(frameatol,text="J",bg="black",fg="white",font=("arial",10,"bold"),width=5,height=2,bd=10,relief=GROOVE)
labelK=Label(frameatol,text="K",bg="black",fg="white",font=("arial",10,"bold"),width=5,height=2,bd=10,relief=GROOVE)
labelL=Label(frameatol,text="L",bg="black",fg="white",font=("arial",10,"bold"),width=5,height=2,bd=10,relief=GROOVE)
labelA.grid(row=0,column=0,padx=5)
labelS.grid(row=0,column=1,padx=5)
labelD.grid(row=0,column=2,padx=5)
labelF.grid(row=0,column=3,padx=5)
labelG.grid(row=0,column=4,padx=5)
labelH.grid(row=0,column=5,padx=5)
labelJ.grid(row=0,column=6,padx=5)
labelK.grid(row=0,column=7,padx=5)
labelL.grid(row=0,column=8,padx=5)

frameztol=Frame(keyboard_frame)
frameztol.grid(row=3,column=0,pady=3)
labelZ=Label(frameztol,text="Z",bg="black",fg="white",font=("arial",10,"bold"),width=5,height=2,bd=10,relief=GROOVE)
labelX=Label(frameztol,text="X",bg="black",fg="white",font=("arial",10,"bold"),width=5,height=2,bd=10,relief=GROOVE)
labelC=Label(frameztol,text="C",bg="black",fg="white",font=("arial",10,"bold"),width=5,height=2,bd=10,relief=GROOVE)
labelV=Label(frameztol,text="V",bg="black",fg="white",font=("arial",10,"bold"),width=5,height=2,bd=10,relief=GROOVE)
labelB=Label(frameztol,text="B",bg="black",fg="white",font=("arial",10,"bold"),width=5,height=2,bd=10,relief=GROOVE)
labelN=Label(frameztol,text="N",bg="black",fg="white",font=("arial",10,"bold"),width=5,height=2,bd=10,relief=GROOVE)
labelM=Label(frameztol,text="M",bg="black",fg="white",font=("arial",10,"bold"),width=5,height=2,bd=10,relief=GROOVE)
labelZ.grid(row=0,column=0,padx=5)
labelX.grid(row=0,column=1,padx=5)
labelC.grid(row=0,column=2,padx=5)
labelV.grid(row=0,column=3,padx=5)
labelB.grid(row=0,column=4,padx=5)
labelN.grid(row=0,column=5,padx=5)
labelM.grid(row=0,column=6,padx=5)

spaceFrame= Frame(keyboard_frame)
spaceFrame.grid(row=4,column=0,pady=3)
labelspace=Label(spaceFrame,bg="black",fg="white",font=("arial",10,"bold"),width=40,height=2,bd=10,relief=GROOVE)
labelspace.grid(row=0,column=0)

def changeBG(widget):
    widget.config (bg="blue")
    widget.after(200,lambda :widget.config(bg="black"))

label_numbers = [label1,label2,label3,label4,label5,label6,label7,label8,label9,label0]

label_alphabates = [labelA,labelB,labelC,labelD,labelE,labelF,labelG,labelH,labelI,labelJ,labelK,labelL,labelM,
                    labelN,labelO,labelP,labelQ,labelR,labelS,labelT,labelU,labelV,labelW,labelX,labelY,labelZ]
space_label=[labelspace]

binding_numbers=["1","2","3","4","5","6","7","8","9","0"]

binding_capital_alphabetes=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O",
                            "P","Q","R","S","T","U","V","W","X","Y","Z"]
binding_small_alphabetes=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o",
                          "p","q","r","s","t","u","v","w","x","y","z"]
for numbers in range(len(binding_numbers)):
    root.bind(binding_numbers[numbers], lambda event, label=label_numbers[numbers]:changeBG(label))

for capital_alphabetes in range(len(binding_capital_alphabetes)):
    root.bind(binding_capital_alphabetes[capital_alphabetes], lambda event, label=label_alphabates[capital_alphabetes]:changeBG(label))

for small_alphabetes in range(len(binding_small_alphabetes)):
    root.bind(binding_small_alphabetes[small_alphabetes], lambda event, label=label_alphabates[small_alphabetes]:changeBG(label))

root.bind("<space>", lambda event:changeBG(space_label[0]))


root.mainloop()

