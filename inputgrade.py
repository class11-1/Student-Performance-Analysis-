def inputgrade(score):
    """
    输入5个学生的成绩
    参数：成绩列表 - 存储成绩的列表
    返回：更新后的成绩列表
    """
    print("\n--- 输入学生成绩 ---")
    print("请输入5个学生的成绩（0-100分）")
    
    # 清空原来的成绩
    score = []
    
    # 循环5次，输入5个成绩
    for i in range(5):
        while True:  # 循环直到输入正确的成绩
            try:
                grade = int(input(f"请输入第{i+1}个学生的成绩: "))
                
                # 检查成绩是否在0-100之间
                if 0 <=grade<= 100:
                    score.append(grade)  # 添加到列表
                    break  # 跳出while循环
                else:
                    print("成绩必须在0-100之间，请重新输入！")
                    
            except:  # 如果输入的不是数字
                print("请输入数字！")
    
    print("成绩输入完成！")
    return score  # 返回新的成绩列表
