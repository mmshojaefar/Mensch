from main_window import Main_Window
from first_window import First_Window
from game import Game

# fqjklwerjr23e
mensch = Game(24)
colors = ['green', 'yellow', 'blue', 'red']
obj = First_Window(colors, mensch)
if len(colors) == 3:
    mensch.sort_turns()
    # obj.root.destroy()
    # print(mensch.turns)
    mw = Main_Window(colors, mensch, obj.usr)
    mw.create_first()
    mw.root.mainloop()