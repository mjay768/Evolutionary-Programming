# ([[-3, -5, 34],[-3, 0, 9],
#  [3, -2, 13],
#  [1, 4, 17],
#  [-3 ,-4 ,25]])
best_index = 1
worst_index = 0
best_data = [-3 ,0, 9]
worst_data = [-3 ,-5, 34]
import numpy as np
import random

a = np.array([[-3, -5, 34],[-3, 0, 9],
 [3, -2, 13],
 [1, 4, 17],
 [-3 ,-4 ,25]])
new_data = np.array([])
for data in a[:,range(0,len(a[0])-1)]:
    #print(data)
    temp = np.array([])
    for i in data:
        count = 0
        rand_1 = 0
        rand_2 = 0

        if count != len(a[0])+1:
            rand_1 = (float("{0:.2f}".format(random.uniform(0,1))))
            rand_2 = (float("{0:.2f}".format(random.uniform(0,1))))
            print("rand 1 = "  + str(rand_1) + " rand_2 = " + str(rand_2))
            print("best_data = " + str(best_data[count]) + " worst_data = " + str(worst_data[count]))
            print("i = " + str(i))
            part1 = rand_1 * (best_data[count] - (abs(i)))
            part2 = rand_2 * (worst_data[count] - (abs(i)))
            print("part 1 = "+ str(part1) + " part 2 = "+ str(part2))
            res = (float("{0:.2f}".format(i + (part1 - part2))))
            print(str(res))

            count = count + 1
            temp = np.append(temp, res)
            print(temp)
    new_data = np.append(new_data , temp)

print(str(new_data))
