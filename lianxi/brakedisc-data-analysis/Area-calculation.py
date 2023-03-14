def print_table(data, row_width, col_width):
    # 打印表格头部
    print(f'+{"-" * (col_width+2)}+' * (row_width+1))

    # 打印表格内容
    for i, row in enumerate(data):
        print('|', end=' ')
        for j, cell in enumerate(row):
            cell = str(cell)
            print(f'{cell:{col_width}}', end=' | ')
        # 如果不是最后一行，打印分隔线
        if i != len(data)-1:
            print('\n' + f'+{"-" * (col_width+2)}+' * (row_width+1))
    # 打印表格底部
    print('\n' + f'+{"-" * (col_width+2)}+' * (row_width+1))

# 测试打印
data = [
    [3, 15, 7, 2],
    ['hello', 'world', 'python', 'code'],
    [1.23, 4.567, 8.9, 12.345],
]

print_table(data, len(data[0]), 8)