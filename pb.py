import matplotlib.pyplot as plt
from matplotlib.pyplot import title

# ডেটা সেট তৈরি করা
categories = ['Python', 'Java', 'C++', 'JavaScript']
values = [40, 30, 20, 10]
"""
# Subplot 1: Bar Chart
plt.subplot(2, 1, 1)  # 2 row, 1 column এর মধ্যে প্রথম subplot
plt.bar(categories, values, color=['blue', 'green', 'red', 'purple'])
plt.title('Popularity of Programming Languages')
plt.xlabel('Languages')
plt.ylabel('Popularity (%)')
plt.grid(True)
"""
# Subplot 2: Pie Chart
plt.subplot(2, 1, 2)  # 2 row, 1 column এর মধ্যে দ্বিতীয় subplot
explode = (0.1, 0.2, 0, 0)  # প্রথম সেকশনকে কিছুটা আলাদা করে দেখানো হচ্ছে
plt.pie(values, labels=categories, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('Popularity Distribution')
plt.legend(title= "Programming Languages",loc="right",bbox_to_anchor=(1,1.5))
# প্রদর্শন করা
#plt.tight_layout()
plt.axis('equal')# layout adjust করা
plt.show()
