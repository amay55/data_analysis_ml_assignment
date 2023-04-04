import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

pd.options.display.float_format = "{:,.2f}".format
sns.set_theme(style='darkgrid')

m_df = pd.read_csv('ghealth_gender_male.csv')
f_df = pd.read_csv('ghealth_gender_female.csv')

fig, ax = plt.subplots(1, 2)
sns.regplot(data=m_df, x="HEALTH BIN", ax=ax[0], y="PA1MIN_", scatter_kws={'s': 2}, ci=None, color='black', line_kws={"color": "red"}).set_title(
    'Male')
sns.regplot(data=f_df, x="HEALTH BIN", ax=ax[1], y="PA1MIN_", scatter_kws={'s': 2}, ci=None, color='black', line_kws={"color": "red"}).set_title(
    'Female')
fig.suptitle('Relationship between minutes of physical activity per week and general health, split by gender', fontsize='medium')
# fig, ax = plt.subplots()
ax[0].set_xlim(-0.5, 4.5)
ax[0].set_xticks(range(0, 5))
ax[1].set_xlim(-0.5, 4.5)
ax[1].set_xticks(range(0, 5))

ax[0].set_ylim(-100, 7100)
ax[0].set_yticks(range(0, 7001, 1000))
ax[1].set_ylim(-100, 7100)
ax[1].set_yticks(range(0, 7001, 1000))

ax[0].set(xlabel='General Health Rating', ylabel='Minutes of physical activity per week')
ax[1].set(xlabel='General Health Rating', ylabel='Minutes of physical activity per week')
# sns.scatterplot(data=df, x="HEALTH BIN", y="PA1MIN_", hue='Gender', marker="o", s=8)

fig.show()
plt.show()

print('done')