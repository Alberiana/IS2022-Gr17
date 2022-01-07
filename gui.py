import tkinter as tk
 
 
def testVulnerability():
    urlEntered = enterText.get()
    postArgEntered = enterPostArgText.get()

    value = checkIfVunlerable(urlEntered, postArgEntered)

    if value == 1:
        enterText.delete(0, END)
        enterText.insert(0, "Vulnerable")

    else:
        enterText.delete(0, END)
        enterText.insert(0, "Not Vulnerable")

def checkIfVulnerable(url,postArg):
 
    data = {'userid': postArg}
    result = requests.post(url,data)
 
    if float(result.elapsed.total_seconds()) > 1:
        return 1
    else:
        return 0 
 
root = tk.Tk()
root.geometry('400x400')
root.wm_title("First GUI Window")
 
enterURL = tk.Label(root, text="Enter an URL to test:",fg="green")
enterURL.grid(row=0,column=1)
 

enterText = tk.Entry(root)
enterText.grid(row=1,column=1,pady=10, padx=10)
 

enterPostArg = tk.Label(root,text="Enter post argument: ")
enterPostArg.grid(row=2,column=1)
 

 
enterPostArgText = tk.Entry(root)
enterPostArgText.grid(row=3,column=1,pady=10, padx=10)
 
checkIfVunlerable = tk.Button(root,text="Test", command=testVulnerability)
checkIfVunlerable.grid(row=4,column=1,pady=10, padx=10)
 
root.mainloop()