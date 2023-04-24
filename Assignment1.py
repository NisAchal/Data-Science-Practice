text=''' Data science combines math and statistics, specialized programming, advanced analytics, artificial intelligence (AI), and machine learning with specific subject matter expertise to uncover actionable insights hidden in an organization’s data. These insights can be used to guide decision making and strategic planning.
The accelerating volume of data sources, and subsequently data, has made data science is one of the fastest growing field across every industry. As a result, it is no surprise that the role of the data scientist was dubbed the “sexiest job of the 21st century” by Harvard Business Review (link resides outside of IBM). Organizations are increasingly reliant on them to interpret data and provide actionable recommendations to improve business outcomes.
The data science lifecycle involves various roles, tools, and processes, which enables analysts to glean actionable insights. Typically, a data science project undergoes the following stages Data ingestion: The lifecycle begins with the data collection--both raw structured and unstructured data from all relevant sources using a variety of methods. These methods can include manual entry, web scraping, and real-time streaming data from systems and devices. Data sources can include structured data, such as customer data, along with unstructured data like log files, video, audio, pictures, the Internet of Things (IoT), social media, and more.
 '''

list=text.split() 
print(f"\nThe total number of words are: {len(list)}\n")                 #Counts word
print(f"Lists of words: \n\n{list}\n\n")                               #1. Create the list of words(all)

Uniqueset=set(list)                                                  #3. set of unique words

list=[]
for i in Uniqueset:
    i=i.strip(",.?'():")
    list.append(i)
print(f"sets of unique words: \n\n{set(list)}")                             #3. set of unique words without symbol

from collections import Counter
count=Counter(list)
ex=count.items()
print(f"\neach unique word with their frequency:\n")
for i in ex:
     print(i)                                                               #2. unique words with frequency
# print(set(count.keys()))                                                  #3. another way to find set of unique words without symbol

print("\n\nCommon five words and their frequency:\n")
sort_orders = sorted(count.items(), key=lambda x: x[1], reverse=True)
j=0
for i in sort_orders:
    if j==5:
        break
    else:
	    print(f"word: {i[0]} \t\t\t\t frequency:{i[1]}")                    #4. five most common words based on frequency
j = j+1               