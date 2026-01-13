def xsmaxmin(maxx,minn):
    """
    显示最高分和最低分
    参数：最高分, 最低分
    """
    print("\n" + "="*30)
    print("成绩分析结果")
    print("="*30)
    print(f"最高分：{maxx}分")
    print(f"最低分：{minn}分")
    print("="*30)

def xsaver(av):
    """
    显示平均分
    参数：平均分
    """
    print("\n" + "="*30)
    print("平均分统计")
    print("="*30)
    print(f"班级平均分：{av}分")
    
    # 简单评价
    if av >= 90:
        print("评价：非常优秀！")
    elif av >= 80:
        print("评价：良好")
    elif av >= 70:
        print("评价：中等")
    elif av >= 60:
        print("评价：及格")
    else:
        print("评价：需要努力")
    print("="*30)

def xsall(score):
    """
    显示所有成绩，并用简单图表表示
    参数：成绩列表
    """
    print("\n" + "="*40)
    print("所有学生成绩")
    print("="*40)
    
    # 显示每个学生的成绩
    for i in range(len(score)):
        print(f"学生{i+1}：{score[i]}分")
    
    print("-"*40)
    
    # 用星号画出简单图表
    print("成绩图表（每个*表示10分）：")
    for i in range(len(score)):
        # 计算星号数量（每10分一个星号）
        count = score[i] // 10
        xh = "*" * count
        
        # 显示图表
        print(f"学生{i+1}：{xh} ({score[i]}分)")
    
    print("="*40)

