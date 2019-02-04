import csv


N = input('What line do you need? > ')
i = 0
for j in range(1,15):
    trial=str(j)+'.csv'
    the_file = open(trial, 'r')
    reader = csv.reader(the_file)

    for row in reader:
        if i == N:
            print("This is the line.")
            print(row)
            break

        i += 1

the_file.close()
