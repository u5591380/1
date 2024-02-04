# restaurant.py

class Restaurant:
    def __init__(self, name, location, type):
        self.name = name
        self.location = location
        self.type = type
        self.ratings = []
        self.reviews = []

    def add_rating(self, rating):
        self.ratings.append(rating)

    def add_review(self, review):
        self.reviews.append(review)

    def average_rating(self):
        if not self.ratings:
            return 0
        return sum(self.ratings) / len(self.ratings)

    def feedback_count(self):
        return len(self.reviews)

    def display_info(self):
        print(f"餐馆名称: {self.name}")
        print(f"位置: {self.location}")
        print(f"类型: {self.type}")
        print(f"平均评分: {self.average_rating()}")
        print(f"反馈数量: {self.feedback_count()}")
        print("评价:")
        for review in self.reviews:
            print(f"- {review}")
        print("\n")
