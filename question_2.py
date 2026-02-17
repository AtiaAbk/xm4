mechine = ['runing','Maintenance', 'failure', 'running']
running_count=0
for status in mechine:
    if status == 'Maintenance':
        continue
    elif status == 'failure':
        break
    elif status == 'running':
        running_count += 1

print("mechine running normally ", running_count)