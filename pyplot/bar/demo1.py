import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({
    'subjects': ['english', 'kannada', 'hindi', 'maths', 'social_science', 'science'],
    'marks': [87, 45, 56, 91, 55, 67]
})

plt.bar(df['subjects'], df['marks'])
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.title('Student marks for each subject')
plt.show()
