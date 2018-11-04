from timeit import repeat


print(repeat("new_list=list(filter(None, your_list))",
                    'your_list= 100*["a", "b", "", "", "c", "", "d", "e", "f", "", "g"]',
                    repeat=3,number = 100000))

print(repeat("your_list=[x for x in your_list if x != '']",
                    'your_list= 100*["a", "b", "", "", "c", "", "d", "e", "f", "", "g"]',
                    repeat=3,number = 100000))

print(repeat("while '' in your_list: your_list.remove('')",
                    'your_list= 100*["a", "b", "", "", "c", "", "d", "e", "f", "", "g"]',
                    repeat=3,number = 100000))



'''
result:
[1.26160959, 1.26600539, 1.2595593159999998]
[2.6536732560000003, 2.6442194679999993, 2.663753957999999]
[0.6465177769999997, 0.6435874330000004, 0.6530912820000001]

'''
