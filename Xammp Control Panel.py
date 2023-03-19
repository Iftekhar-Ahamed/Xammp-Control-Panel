#!/usr/bin/python3
import tkinter as tk
import tkinter.font as tkFont
import  os
import  subprocess

class App:
    def __init__(self, root):
        #setting title
        root.title("XAMMP")
        #setting window size
        width=579
        height=481
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        Start=tk.Button(root)
        Start["bg"] = "#90ee90"
        ft = tkFont.Font(family='Times',size=14,weight='bold')
        Start["font"] = ft
        Start["fg"] = "#000000"
        Start["justify"] = "center"
        Start["text"] = "Start"
        Start.place(x=120,y=250,width=70,height=35)
        Start["command"] = self.Start_command



        Stop=tk.Button(root)
        Stop["bg"] = "#cc0000"
        ft = tkFont.Font(family='Times',size=14,weight='bold')
        Stop["font"] = ft
        Stop["fg"] = "#000000"
        Stop["justify"] = "center"
        Stop["text"] = "Stop"
        Stop.place(x=360,y=250,width=70,height=35)
        Stop["command"] = self.Stop_command

        label1=tk.Label(root)
        ft = tkFont.Font(family='Times',size=26)
        label1["font"] = ft
        label1["fg"] = "#333333"
        label1["justify"] = "center"
        label1["text"] = "XAMMP CONTROL"
        label1.place(x=110,y=65,width=350,height=40)

        label2=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        label2["font"] = ft
        label2["fg"] = "#333333"
        label2["justify"] = "center"
        label2["text"] = "BY"
        label2.place(x=240,y=110,width=70,height=25)

        label3=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        label3["font"] = ft
        label3["fg"] = "#333333"
        label3["justify"] = "center"
        label3["text"] = "IFTEKHAR AHAMED SIDDIQUEE"
        label3.place(x=100,y=150,width=350,height=30)

        labelStatus=tk.Label(root)
        ft = tkFont.Font(family='Times',size=15,weight='bold')
        labelStatus["font"] = ft
        labelStatus["fg"] = "#333333"
        labelStatus["justify"] = "center"
        labelStatus["text"] = "STATUS : UNCHECKED"
        labelStatus.place(x=180,y=350,width=240,height=40)

        Status = tk.Button(root)
        Status["bg"] = "#01aaed"
        ft = tkFont.Font(family='Times', size=14,weight='bold')
        Status["font"] = ft
        Status["fg"] = "#000000"
        Status["justify"] = "center"
        Status["text"] = "Status"
        Status.place(x=240, y=250, width=70, height=35)
        Status["command"] = lambda :self.Status_command(labelStatus)

    def Start_command(self):
        sudoPassword = ''
        command = 'sudo /etc/init.d/apache2 stop'
        output = os.system('echo %s|sudo -S %s' % (sudoPassword, command))
        command = '/etc/init.d/mysqld stop'
        output = os.system('echo %s|sudo -S %s' % (sudoPassword, command))
        command = 'sudo /opt/lampp/lampp restart'
        output = os.system('echo %s|sudo -S %s' % (sudoPassword, command))
        #print(output)


    def Status_command(self,val):
        sudoPassword = ''
        command = 'sudo /opt/lampp/lampp status'
        expected = "Apache is running.\nMySQL is running.\n"
        output = subprocess.check_output('echo %s|sudo -S %s' % (sudoPassword, command),shell=True)
        output_str = output.decode("utf-8")
        val.place(x=220, y=350, width=140, height=40)
        if expected in output_str:
            val["text"] = "STATUS : ON"
        else:
            val["text"] = "STATUS : OFF"
        #print(output)


    def Stop_command(self):
        sudoPassword = ''
        command = 'sudo /opt/lampp/lampp stop'
        output = os.system('echo %s|sudo -S %s' % (sudoPassword, command))
        #print(output)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
