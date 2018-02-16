## 3. Introduction To The Data ##

import pandas as pd
import matplotlib.pyplot as plt

women_degrees = pd.read_csv('percent-bachelors-degrees-women-usa.csv')

plt.plot(women_degrees["Year"], women_degrees["Biology"])
         
plt.show()

## 4. Visualizing The Gender Gap ##

plt.plot(women_degrees["Year"], women_degrees["Biology"], c = "blue", label = "Women")

plt.plot(women_degrees["Year"], 100 - women_degrees["Biology"], c = "green", label = "Men")

plt.title("Percentage of Biology Degrees Awarded By Gender")

plt.legend(loc = "upper right")

plt.show()

## 6. Hiding Tick Marks ##

plt.plot(women_degrees["Year"], women_degrees["Biology"], c = "blue", label = "Women")

plt.plot(women_degrees["Year"], 100 - women_degrees["Biology"], c = "green", label = "Men")

plt.tick_params(bottom = "off", top = "off", left = "off", right = "off")

plt.title("Percentage of Biology Degrees Awarded By Gender")

plt.legend(loc = "upper right")

plt.show()

## 7. Hiding Spines ##

fig, ax = plt.subplots()
ax.plot(women_degrees['Year'], women_degrees['Biology'], label='Women')
ax.plot(women_degrees['Year'], 100-women_degrees['Biology'], label='Men')
ax.tick_params(bottom="off", top="off", left="off", right="off")
# Add your code here
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)

ax.legend(loc='upper right')
ax.set_title('Percentage of Biology Degrees Awarded By Gender')
plt.show()

## 8. Comparing Gender Gap Across Degree Categories ##

major_cats = ['Biology', 'Computer Science', 'Engineering', 'Math and Statistics']
fig = plt.figure(figsize=(12, 12))

for sp in range(0,4):
    ax = fig.add_subplot(2,2,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[major_cats[sp]], c='blue', label='Women')
    ax.plot(women_degrees['Year'], 100-women_degrees[major_cats[sp]], c='green', label='Men')
    # Add your code here.
    
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0, 100)
    
    ax.tick_params(bottom="off", top="off", left="off", right="off")
    
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    
    ax.set_title(major_cats[sp])
    
# Calling pyplot.legend() here will add the legend to the last subplot that was created.
plt.legend(loc='upper right')
plt.show()