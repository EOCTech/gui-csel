#!/usr/bin/env python

from Tkinter import *



def callback():
  fw = 'checkFirewall=(y)\ncheckFirewallValue=(' + checkFirewallValue.get() + ')\n'
  bd = 'checkBackdoor=(y)\ncheckBackdoorValue=(' + checkBackdoorValue.get() + ')\n'
  sd = 'secureSudoers=(y)\nsecureSudoersValue=(' + secureSudoersValue.get() + ')\n'
  f = open('test.txt','w')
  if fwEnabled.get() == 1:
    f.write(fw)
  if bdEnabled.get() == 1:
    f.write(bd)
  if sdEnabled.get() == 1:
    f.write(sd)

root = Tk()

#Create variables to enable/disable status
fwEnabled = IntVar()
sdEnabled = IntVar()
bdEnabled = IntVar()

root.title('Vulnerabilities')

#Create some checkbuttons and entry boxes
checkFirewall = Checkbutton(root,text='Firewall',variable=fwEnabled)
checkFirewallValue = Entry(root)
secureSudoers = Checkbutton(root,text='Sudoers',variable=sdEnabled)
secureSudoersValue = Entry(root)
checkBackdoor = Checkbutton(root,text='Backdoor',variable=bdEnabled)
checkBackdoorValue = Entry(root)
submit = Button(root,text='Submit',command=callback)


#Let's make a table!!!!
head1 = Label(root,text="Enabled?")
head2 = Label(root,text="Point Value")
head1.grid(row=0,column=1)
head2.grid(row=0,column=2)
vulns = [checkFirewall,secureSudoers,checkBackdoor,]
values = [checkFirewallValue,secureSudoersValue,checkBackdoorValue]

i=1
for label in vulns:
  label.grid(row=i,column=1,sticky=W)
  i+=1

j=1
for val in values:
  val.grid(row=j,column=2)
  j+=1
  
submit.grid(row=99,column=2)

root.mainloop()