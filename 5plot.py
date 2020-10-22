#Draw a data file diagram project
import matplotlib.pyplot as plt
figure, axes = plt.subplots(nrows=3, ncols=2)
bad_chars=["barcode={","right={","bottom={","left={","top={","};"]
#read data file
file1=open("sensor.mat","r")
lines=file1.readlines()
#Convert str to list func
def Convert(string): 
    li = list(string.split(","))
    return li 
#Remove extra characters func
def ploty(p1):
    y=lines[p1]
    for sub in bad_chars: 
        y = y.replace(sub,'')
    y=list(map(int, Convert(y)))
    return y
#Specify the coordinates of each graph
axes[0, 0].plot(ploty(0))
axes[0, 1].plot(ploty(2))       
axes[1, 0].plot(ploty(4))   
axes[1, 1].plot(ploty(6))       
axes[2, 0].plot(ploty(8))
#show graph     
plt.show()
 