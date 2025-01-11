# Импортируем библиотеку для выполнения HTTP-запросов в интернет
import requests

target_word = 'человек'
target_chapter = 15

# Читаем текстовый файл по url-ссылке
data = requests.get("https://raw.githubusercontent.com/SkillfactoryDS/Datasets/master/war_peace_processed.txt").text
# Предобрабатываем текстовый файл
data = data.split('\n')
data.remove('')
data = data + ['[new chapter]']
#print(data[:100])

word_set=set(data)
word_set.discard('[new chapter]')
#print('Общее количество слов: {}'.format(len(data)))
#print('Общее количество уникальных слов: {}'.format(len(word_set)))

word_counts={} #пустой словарь
count_chapter=0 #подсчет количества глав
for word in data:
    if word=='[new chapter]':
        count_chapter+=1
        continue
    if word not in word_counts:
        word_counts[word]=1
    else:
        word_counts[word]+=1
#print('Количество глав: {}'.format(count_chapter))

for i, key in enumerate(word_counts):
    if i==10:
       break
    #print(key, word_counts[key])

chapter_data=[]
chapter_words=[]

for word in data:
    if word=='[new chapter]':
        chapter_data.append(chapter_words)
        chapter_words=[]
    else:
        chapter_words.append(word)
#print('Вложенный список содержит {} внутренних списка'.format(len(chapter_data)))
#print(chapter_data[0][:100])
#print(chapter_data[15][100])

chapter_words_count=[]

for chapter_words in chapter_data:
    temp={}
    for word in chapter_words:
        if word not in temp:
            temp[word]=1
        else:
            temp[word]+=1
    chapter_words_count.append(temp)
#print(chapter_words_count)

for chapter_number, chapter_dict in enumerate(chapter_words_count):
    if chapter_number==5:
        break
    #print('-'*40)
    #print('Chapter: {}'.format(chapter_number))
    #print('-'*40)
    for j, word in enumerate(chapter_dict):
        if j==10:
            break
        #print(word, chapter_dict[word])

words_count_chapter = {}

j=0
for i in chapter_data:
    words_count_chapter[j] = len(chapter_data[j])
    j+=1

tf_word_array = []


for chapter_number, chapter_dict in enumerate(chapter_words_count):
    tf_word = {}
    for word in chapter_dict:
        tf_word[word] = chapter_dict[word] / words_count_chapter[chapter_number]
    tf_word_array.append(tf_word)

tf_check = tf_word_array[target_chapter]
print(tf_check[target_word])


df_word = {}
n_word = {}

# n_word=0
i=0

for word in word_set:
    if word not in n_word:
        n_word[word] = 0
    i=0
    while i<count_chapter:
        for word_chapter in chapter_data[i]:
            if word==word_chapter:
                n_word[word]+=1
                break
        i+=1

for word in n_word:
    df_word[word] = n_word[word]/count_chapter
# while i<count_chapter:
#     for word in chapter_data[i]:
#         if word==target_word:
#             n_word+=1
#             break
#     i+=1
# df_word=n_word/count_chapter
        
print(df_word[target_word])