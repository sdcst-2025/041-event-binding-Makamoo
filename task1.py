
import tkinter as tk
import playsound as p

def playsound(event):
    print(event)
    p.playsound("ytmp3free.cc_old-car-horn-sound-effecthd-youtubemp3free.org.mp3",block=False)

def mine(craft):
    print(craft)
    p.playsound("ytmp3free.cc_minecraft-eating-sound-effect-hd-youtubemp3free.org.mp3",block=False)

def get(out):
    print(out)
    p.playsound("tuco-get-out.mp3",block=False)

def rizz(sound):
    print(sound)
    p.playsound("rizz-sound-effect.mp3",block=False)

def are(yousure):
    print(yousure)
    p.playsound("omni-man-are-you-sure.mp3",block=False)

def metal(pipe):
    print(pipe)
    p.playsound("metal-pipe-clang.mp3",block=False)

def flash(bang):
    print(bang)
    p.playsound("flashbanggg.mp3",block=False)

def freddy(FNAF):
    print(FNAF)
    p.playsound("five-nights-at-freddys-full-scream-sound_2.mp3",block=False)

def modern(horn):
    print(horn)
    p.playsound("goofy-ahh-car-horn-sound-effect.mp3",block=False)

def prowler(noise):
    print(noise)
    p.playsound("prowler-sound-effect_6bXErot.mp3",block=False)

def goku(drip):
    print(drip)
    p.playsound("drip-goku-meme-song-original-dragon-ball-super-music-clash-of-gods-in-description.mp3",block=False)

def horn(blare):
    print(blare)
    p.playsound("giudok-poezda.mp3",block=False)


win = tk.Tk()
win.attributes('-topmost',True)

b1 =  tk.Button(win,text="Old Car Horn")
b1.bind("<Button>",playsound)

b2 =  tk.Button(win,text="Minecraft")
b2.bind("<Button>",mine)

b3 =  tk.Button(win,text="Get Out")
b3.bind("<Button>",get)

b4 =  tk.Button(win,text="Rizz")
b4.bind("<Button>",rizz)

b5 =  tk.Button(win,text="Are You Sure?")
b5.bind("<Button>",are)

b6 =  tk.Button(win,text="Metal Pipe")
b6.bind("<Button>",metal)

b7 =  tk.Button(win,text="Flashbang")
b7.bind("<Button>",flash)

b8 =  tk.Button(win,text="Jumpscare")
b8.bind("<Button>",freddy)

b9 =  tk.Button(win,text="Modern Car Horn")
b9.bind("<Button>",modern)

b10 =  tk.Button(win,text="Prowler")
b10.bind("<Button>",prowler)

b11 =  tk.Button(win,text="Goku Drip")
b11.bind("<Button>",goku)

b12 =  tk.Button(win,text="Horn Blare")
b12.bind("<Button>",horn)

b1.grid(row=1,column=1)
b2.grid(row=2,column=1)
b3.grid(row=3,column=1)
b4.grid(row=4,column=1)
b5.grid(row=1,column=2)
b6.grid(row=2,column=2)
b7.grid(row=3,column=2)
b8.grid(row=4,column=2)
b9.grid(row=1,column=3)
b10.grid(row=2,column=3)
b11.grid(row=3,column=3)
b12.grid(row=4,column=3)

win.mainloop()