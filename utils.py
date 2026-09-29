def print_loop():
    for i in range(3):
        print(f'这是第{i+1}次循环')
def print_multiplication_table():
    for i in range(1,10):
        for j in range(1,i+1):
            print(f'{j}*{i}={i*j}',end='\t')
        print()