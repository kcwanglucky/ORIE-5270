import requests
import pandas as pd
import re
import matplotlib.pyplot as plt

url = "https://files.oakland.edu/users/grossman/enp/Erdos0.html"
page = requests.get(url)
page_text = page.text

author_info = page_text.split("http://www.oakland.edu/enp\n\n")[1] # extract all the name and info
author_list = author_info.split("\n")[:-1]	# the last index contains <\pre> tag which should be discarded

data = []	# store all the information
for author in author_list:
    name_index = author.index("   ")
    if author[name_index - 1] == "*":
        name = author[:name_index - 1]
    else:    
        name = author[:name_index]
    
    year = int(author[40:44])   
    
    if author[44] != ":":
        freq = 1
    else:   
        freq = int(re.search("[0-9]+", author[45:]).group())
    data.append([name, year, freq])

df = pd.DataFrame(data, columns=['Name','Year','Frequency'])
print(df.head(10))

# Question 2
max_ind = df['Frequency'].idxmax()
f_name, f_year, f_freq = df.iloc[max_ind]
print("{} has collaborate with Erdos most Often and his frequency is {}.".format(f_name, f_freq))

# Question 3
latest_ind = df['Year'].idxmax()
l_name, l_year, l_freq = df.iloc[latest_ind]
print("{} is the one who last collaborate with Erdos and his year is {}.".format(l_name, l_year))

# Question 4
plt.figure(figsize=(14, 7))
plt.subplot(1, 2, 1)
df['Year'].plot.hist()
plt.title("Histogram of the Year Column")
plt.xlabel("Year")
plt.subplot(1, 2, 2)
df['Frequency'].plot.hist()
plt.title("Histogram of the Frequency Column")
plt.xlabel("Frequency Column")
plt.subplots_adjust(wspace = 0.4)
plt.savefig('histogram.pdf')
