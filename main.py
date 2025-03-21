
#chatgpt
import matplotlib.pyplot as plt
import numpy as np

# Data তৈরি করা
x = np.linspace(0, 10, 100)  # 0 থেকে 10 পর্যন্ত 100টি পয়েন্ট
y = np.sin(x)  # y হলো x এর sine ফাংশন

# গ্রাফ প্লট করা
plt.plot(x, y, label='sin(x)', color='blue', linewidth=2)

# লেবেল ও শিরোনাম যোগ করা
plt.xlabel('X Value')
plt.ylabel('Y Value')
plt.title('Sine Wave Plot')

# লিজেন্ড যোগ করা
plt.legend()

# গ্রাফ দেখানো
plt.show()
