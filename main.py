# main.py
from restaurant import Restaurant

def main():
    # 示例餐馆对象列表
    restaurants = [
        Restaurant(name='餐馆1', location='位置1', type='餐馆'),
        Restaurant(name='餐馆2', location='位置2', type='咖啡馆'),
        # 添加其他餐馆对象
    ]

    # 学生评分和评价
    for restaurant in restaurants:
        student_rating = input(f"请给{restaurant.name}评分（按Enter跳过则默认5分）：")
        if not student_rating:
            student_rating = 5.0  # 默认好评
        else:
            student_rating = float(student_rating)

        student_review = input(f"请发表你对{restaurant.name}的评价：")

        # 添加评分和评价到餐馆对象
        restaurant.add_rating(student_rating)
        restaurant.add_review(student_review)

    # 排序并显示排名
    print("\n按评分由高到低排名:")
    sorted_by_rating_high_to_low = sorted(restaurants, key=lambda x: x.average_rating(), reverse=True)
    for idx, restaurant in enumerate(sorted_by_rating_high_to_low, start=1):
        print(f"{idx}. {restaurant.name} - 平均评分: {restaurant.average_rating()}")

    print("\n按评分由低到高排名:")
    sorted_by_rating_low_to_high = sorted(restaurants, key=lambda x: x.average_rating())
    for idx, restaurant in enumerate(sorted_by_rating_low_to_high, start=1):
        print(f"{idx}. {restaurant.name} - 平均评分: {restaurant.average_rating()}")

    print("\n按受欢迎程度（反馈数量）排名:")
    sorted_by_feedback_count = sorted(restaurants, key=lambda x: x.feedback_count(), reverse=True)
    for idx, restaurant in enumerate(sorted_by_feedback_count, start=1):
        print(f"{idx}. {restaurant.name} - 反馈数量: {restaurant.feedback_count()}")

if __name__ == "__main__":
    main()
