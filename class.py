#!/usr/bin/env python

from Tkinter import *

class Vuln:
    def __init__(self, name, value, enabled):
        self.name = name
        self.value = value
        self.enabled = enabled

v1 = Vuln("checkFirewall","10","1")
v2 = Vuln("secureSudoers","4","1")
v3 = Vuln("checkBackdoor","0","0")

def callback():
  for items,tkVars in vulnList:
      item.enabled = 
      if item.enabled != "0":
          print item.name,"for",item.value,"points"
      else:
          print item.name,"is Disabled"
  v1.enabled = cb01.get()
  v1.value = en01.get()
  print v1.name,v1.enabled,v1.value

root = Tk()
cb01 = IntVar()
en01 = IntVar()

root.title('Vulnerabilities')

#Create some checkbuttons and entry boxes
checkbox01 = Checkbutton(root,text=v1.name,variable=cb01)
entry01 = Entry(root,textvariable=en01)
submit = Button(root,text='Submit',command=callback)


#Let's make a table!!!!
head1 = Label(root,text="Enabled?")
head2 = Label(root,text="Point Value")
head1.grid(row=0,column=1)
head2.grid(row=0,column=2)
checkbox01.grid(row=1,column=1)
entry01.grid(row=1,column=2)
#vulns = [checkFirewall,secureSudoers,checkBackdoor,]
#values = [checkFirewallValue,secureSudoersValue,checkBackdoorValue]

#i=1
#for label in vulns:
#  label.grid(row=i,column=1,sticky=W)
#  i+=1
#
#j=1
#for val in values:
#  val.grid(row=j,column=2)
#  j+=1
  
submit.grid(row=99,column=2)

root.mainloop()