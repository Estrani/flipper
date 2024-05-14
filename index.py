from tkinter import Tk, Canvas, Button

# taille plateau w= 595 h= 842
xMinP= 0
xMaxP= 595
yMinP= 0
yMaxP= 842

root=Tk()
canvas=Canvas(root, width=xMaxP, height=yMaxP, bg="ivory")
canvas.pack(side='left', padx=5, pady=5)

# position bille
xb=276
yb=632
# vitesse bille
vx= +20
vy= +10

#  variable.create_ovale(position x, y, position x + diametre, y+ diametre)

#bille
bille = canvas.create_oval((xb, yb), (xb + 43, yb + 43), fill='light gray', outline='black', width=2)

def deplacement_bille():
    global xb, yb, vx, vy

    xb = xb + vx
    yb = yb + vy

    canvas.coords(bille, xb, yb, xb + 43, yb + 43)

    if xb < xMinP or xb > xMaxP :
        vx =-vx
    if yb < yMinP or yb > yMaxP :
        vy =-vy
    '''if xb > 200 and yb > 127 or xb < 374 and yb > 127 or xb > 222 and yb < 279 or xb < 374 and yb < 279 :
        vx =-vx
        vy =-vy '''
    if xb < 276 and yb > 680 or xb > 319 and yb > 680 :
        vx = 0
        vy = 0
   

    canvas.after(50, deplacement_bille)
    return

#  variable.create_rectangle(1point diagonale x, y, 2point diagonale x, y)
batG = canvas.create_rectangle((0, 722), (276, 751), fill='gray', outline='dark gray', width=2)
batD = canvas.create_rectangle((319, 722), (595, 751), fill='gray', outline='dark gray', width=2)


def action_batteur(event):
    touche = event.keysym
    #print(batG)
    global xb, yb, vx, vy

    xb = xb + vx
    yb = yb + vy

    canvas.coords(bille, xb, yb, xb + 43, yb + 43)

    if touche == "Left" :
        canvas.itemconfigure(batG,fill='red')
    else:
        canvas.itemconfigure(batG,fill='gray')
    if touche == "Left" and xb < 276 and yb > 680 :
        vx =+20
        vy =-10
        
    if touche == "Right" :
        canvas.itemconfigure(batD,fill='red')
    else:
        canvas.itemconfigure(batD,fill='gray')
    if touche == "Right" and xb > 319 and yb > 680 :
        vx =+20
        vy =-10
        
    return

#bumper
canvas.create_rectangle((222, 127), (374, 279), fill='light blue', outline='red', width=2)

def action_bumper():
    global xb, yb, vx, vy

    xb = xb + vx
    yb = yb + vy

    canvas.coords(bille, xb, yb, xb + 43, yb + 43)

    if xb > 222+152 and yb > 127+152 :
        vx =-vx
        vy =-vy
   
    canvas.after(50, deplacement_bille)
    return

def action_deplacer():
    deplacement_bille()
    return

bouton = Button(root, text="Déplacer", width=20, command=action_deplacer)
bouton.pack(side='top', padx=5, pady=5)





root.bind("<Key>", action_batteur)
root.mainloop()


