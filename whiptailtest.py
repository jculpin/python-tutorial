import whiptail as wt

#from whiptail import *

#wt = Whiptail()
#wt.title = "Hello"
#wt.alert("Hello")

newone = wt.Whiptail()
newone.title = "Choose"
#newone.height = 20
val = newone.confirm("Is that correct?")

newmenu = wt.Whiptail()
newmenu.title = "Menu"
newmenu.height= 15
menuval = newmenu.menu("Choose one",("first","second","third"))
print(menuval)

