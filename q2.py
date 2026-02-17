running_count = 0

while(status := input("enter the status : ")) !="stop":
    if status == 'maintenence' :
        continue
    if status == 'failure':
        break 
    if status == 'running':
        running_count +=1
print("mechine running nirmally ", running_count)
