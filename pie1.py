
import matplotlib.pyplot as plt

# ডেটা সেট তৈরি করা
labels = ['Python', 'Java', 'C++', 'JavaScript']  # প্রোগ্রামিং ভাষার নাম
sizes = [40, 30, 20, 10]  # প্রতিটি সেকশনের মান
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']  # রংগুলোর তালিকা
explode = (0.1, 0, 0, 0)  # প্রথম সেকশন (Python) কে আলাদা করে দেখানোর জন্য 'explode' ব্যবহার করা হয়েছে

# Pie Chart তৈরি করা
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=90)

# লিজেন্ড যুক্ত করা, যা Pie Chart এর বাইরে দেখাবে
plt.legend(labels, title="Programming Languages", loc="upper right", bbox_to_anchor=(1, 0, 0.5, 1))

# Plot দেখানো
plt.axis('equal')  # Pie Chart কে গোলাকার দেখানোর জন্য সমান অক্ষ ব্যবহার করা
plt.show()
