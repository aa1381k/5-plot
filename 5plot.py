import matplotlib.pyplot as plt
figure, axes = plt.subplots(nrows=3, ncols=2)
bad_chars=["barcode={","right={","bottom={","left={","top={","};"]
file1=open("sensor.mat","r")
lines=file1.readlines()

def Convert(string): 
    li = list(string.split(","))
    return li 

def ploty(p1):
    y=lines[p1]
    for sub in bad_chars: 
        y = y.replace(sub,'')
    y=list(map(int, Convert(y)))
    return y

for i in range (9):

    if i==0:
        axes[0, 0].plot(ploty(0))
        print(ploty(0))
    elif i==2:
        axes[0, 1].plot(ploty(2))
        
    elif i==4:
        axes[1, 0].plot(ploty(4))
    
    elif i==6:
        axes[1, 1].plot(ploty(6))
        
    elif i==8:
        axes[2, 0].plot(ploty(8))
        

plt.show()
 