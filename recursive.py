# The recursive of algorithm
def count_down(i):
    """basic recursive func """
    print(i)
    # 基线条件
    if i <= 0:
        return
    else:
    # 递归条件
        count_down(i-1)


count_down(5)