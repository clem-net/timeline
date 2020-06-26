import wikipedia

ford = wikipedia.page(pageid=645042)
# 645042
# print(ford.summary)
# print("\n", ford.pageid)

for i in range(1, 999):
    try:
        page = wikipedia.page(pageid=i)
        print(page.title)
    except wikipedia.exceptions.PageError as e:
        
        print(str(e))
