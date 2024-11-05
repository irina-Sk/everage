students = {'Sasha', 'Patrik', 'Yasmina', 'Amir', 'Musation'}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3, 3, 4], [4, 5, 5, 2], [4, 5, 5], [5, 5, 4, 5 ]]
# print(grades[2])
eve_0 = (sum(grades[0]) / len(grades[0]))
eve_1 = round(sum(grades[1]) / len(grades[1]),2)
eve_2 = (sum(grades[2]) / len(grades[2]))
eve_3 = round(sum(grades[3]) / len(grades[3]),2)
eve_4 = (sum(grades[4]) / len(grades[4]))
#print(eve_0)
print(f'Sasha: {eve_0}, Patrik: {eve_1}, Yasmina: {eve_2}, Amir: {eve_3}, Musation: {eve_4}')
