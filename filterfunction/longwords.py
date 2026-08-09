words=["elephant","cat","gorilla","tiger","ant","hippopotamus"]

long_wors=list(filter(lambda words : len(words) > 4, words))

print("long words:", long_wors)
