import tkinter as tk
import time
import pygame

COLOR = "#40534C" 

pygame.mixer.init()
start_resting=False


start_sound = pygame.mixer.Sound("im_batman.mp3")
end_sound = pygame.mixer.Sound("batman.mp3")

def start_timer():
    global started
    if not started:
        start_sound.play()
        started=True
        update_timer()
    else:
        end_sound.play()
        pause()





def reset_timer():
    global counter,started, time_sec, time_min,started, resting
    started=False
    resting=False
    time_min=0
    time_sec=0
    counter=0
    end_sound.play()
    update_timer()

def pause():
    global started
    started=False
    

def update_timer():
    global counter, resting, time_sec, time_min, TIMER, start,started,mark,start_resting
    if started:
        if not resting:
            if start_resting:
                start_sound.play()
                start_resting=False
            time_sec+=1
            if time_sec > 59:
                time_sec=0
                time_min+=1
            if time_min == 25:
                time.sleep(1)
                time_sec=0
                time_min=0
                resting=True
                counter+=1
                mark.config(text="✓"*counter)
            label_title.config(text="WORK")
        else :
            if not start_resting:
                end_sound.play()
                start_resting=True
            time_sec+=1
            if time_sec > 59:
                time_sec=0
                time_min+=1
            if time_min == 5 and (counter+1)%8 != 0: 
                time.sleep(1)
                time_sec=0
                time_min=0
                resting=False
            if time_min == 25:
                time.sleep(1)
                time_sec=0
                time_min=0
                resting=False
            label_title.config(text="REST")
            

    TIMER.config(text=f"{time_min:02}:{time_sec:02}")
    start.config(text="START" if not started else "PAUSE")
    if started:
        window.after(1000, update_timer)
        


resting=False
counter=0
started=False

time_min=0
time_sec=0


window = tk.Tk()
window.config(padx=10, pady=10, bg=COLOR)
window.title("Pomodora")
window.resizable(False, False)

canvas = tk.Canvas(window, width=200, height=210, bg=COLOR, highlightthickness=0)
bat_img = tk.PhotoImage(file="batsy.png")
circle = canvas.create_oval(1, 10, 198, 190, outline="white", fill="white")
canvas.create_image(100, 103, image=bat_img)

label_title=tk.Label(text="BATSY", bg= COLOR, font=("Cosmic Boy",18))
label_title.grid(row=0, column=1)



canvas.grid(row=1, column=1,pady=30)

start=tk.Button(text="START", command=start_timer if not started else pause,width=5)
start.grid(row=2,column=0)

reset=tk.Button(text="RESET", command=reset_timer)
reset.grid(row=2,column=2)

mark=tk.Label(text="✓"*counter, bg=COLOR)
mark.grid(row=2,column=1)

TIMER=tk.Label(text=f"00:00",font=("Arial",10),bg="white")
TIMER.place(x=130,y=145)









window.mainloop()
