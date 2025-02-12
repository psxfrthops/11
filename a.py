import randomذ

def guess_the_number():
    # انتخاب عدد تصادفی بین 1 تا 100
    number_to_guess = random.randint(1, 100)
    guesses = []  # لیست برای ذخیره حدس‌ها
    attempts = 0  # شمارش تعداد حدس‌ها

    print("به بازی حدس عدد خوش آمدید!")
    print("عدد تصادفی بین 1 تا 100 انتخاب شده است. تلاش کنید آن را حدس بزنید!")

    while True:
        try:
            # گرفتن ورودی از کاربر
            user_guess = int(input("حدس خود را وارد کنید: "))
            attempts += 1
            guesses.append(user_guess)  # ذخیره حدس در لیست

            # بررسی اینکه حدس درست است یا نه
            if user_guess < number_to_guess:
                print("عدد حدس شما کمتر از عدد صحیح است.")
            elif user_guess > number_to_guess:
                print("عدد حدس شما بیشتر از عدد صحیح است.")
            else:
                print(f"تبریک! عدد صحیح {number_to_guess} بود.")
                break  # بازی تمام می‌شود

        except ValueError:
            print("لطفاً یک عدد صحیح وارد کنید.")

    # نمایش تاریخچه حدس‌ها و تعداد تلاش‌ها
    print("\nتاریخچه تمام حدس‌های شما:")
    print(f"تعداد تلاش‌ها: {attempts}")
    print("حدس‌ها:", guesses) 