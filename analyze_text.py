def analyze_text(text,target_word):    
    words = text.split()
    word_count = len(words)
    max_len = 0
    longest_word = ""
    target_count=0
    for word in words:
        if len(word) > max_len:
            max_len = len(word)
            longest_word = word
        if word.lower()== target_word.lower():
            target_count +=1
    return word_count,target_count, longest_word
result=list(analyze_text("Hello0000000 world davaleba N8 davaleba დავალება N8",'davaleba'))

print(result)
print(result[2])