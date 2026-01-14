def maxmin(score):
    """
    找出最高分和最低分
    参数：成绩列表 - 存储成绩的列表
    返回：最高分, 最低分
    """
    # 检查列表是否为空
    if len(score) == 0:
        return 0, 0
    
    # 假设第一个成绩是最高分和最低分
    maxx = score[0]
    minn = score[0]
    
    # 遍历列表中的每个成绩
    for i in score:
        # 如果找到更高的成绩，更新最高分
        if i> maxx:
            maxx = i
        
        # 如果找到更低的成绩，更新最低分
        if i < minn:
            minn = i
    
    return maxx,minn

def aver(score):
    """
    计算平均分
    参数：成绩列表 - 存储成绩的列表
    返回：平均分
    """
    # 检查列表是否为空
    if len(score) == 0:
        return 0
    
    # 计算总分
    s = 0
    for i in score:
        s += i  # 累加每个成绩
    
    # 计算平均分
    av= s/ len(score)
    
    # 保留2位小数
    return round(av, 2)
