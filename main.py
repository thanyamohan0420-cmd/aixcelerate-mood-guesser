Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
... 
... train_data = [
...     ("I got full marks in the test today!", "Happy"),
...     ("We won the college cricket match", "Happy"),
...     ("My friends planned a surprise party for me", "Happy"),
...     ("The food in the canteen was really tasty", "Happy"),
...     ("I am so excited for the weekend trip", "Happy"),
...     ("Our project got selected for the exhibition", "Happy"),
...     ("I finally learned how to ride a bicycle", "Happy"),
...     ("Mom made my favourite sweets today", "Happy"),
...     ("I lost my phone on the bus", "Sad"),
...     ("I failed in the mathematics exam", "Sad"),
...     ("My best friend is moving to another city", "Sad"),
...     ("It rained and our picnic was cancelled", "Sad"),
...     ("I missed the last bus and felt very upset", "Sad"),
...     ("My laptop stopped working before the submission", "Sad"),
...     ("I felt lonely during the long holidays", "Sad"),
... ]
... 
... practice_data = [
...     ("I won a medal in the sports meet", "Happy"),
...     ("I lost my notebook before the exam", "Sad"),
...     ("My friends gave me a lovely surprise", "Happy"),
...     ("The train was late and I felt upset", "Sad"),
...     ("Today was a great day", "Happy"),
... ]
... 
... 
... def count_moods(data):
...     happy = 0
...     sad = 0
...     for sentence, mood in data:
...         if mood == "Happy":
...             happy += 1
...         elif mood == "Sad":
...             sad += 1
    return happy, sad



happy_words = ["won", "surprise", "great", "excited"]
sad_words = ["lost", "upset", "failed", "lonely"]


def clean(sentence):
    """Make everything lowercase, drop punctuation, split into words."""
    kept = ""
    for ch in sentence.lower():
        if ch.isalpha() or ch == " ":
            kept += ch
    return kept.split()


def guess_mood(sentence):
    happy_score = 0
    sad_score = 0
    for word in clean(sentence):
        if word in happy_words:
            happy_score += 1
        if word in sad_words:
            sad_score += 1

    if happy_score > sad_score:
        return "Happy"
    if sad_score > happy_score:
        return "Sad"
    
    return "Happy"



def accuracy(data, guesser):
    correct = 0
    for sentence, real_mood in data:
        guess = guesser(sentence)
        print(f"{sentence!r} -> guessed {guess}, real {real_mood}")
        if guess == real_mood:
            correct += 1
    return correct / len(data) * 100


def learn_scores(data):
    scores = {}
    for sentence, mood in data:
        for word in clean(sentence):
            if mood == "Happy":
                scores[word] = scores.get(word, 0) + 1
            else:
                scores[word] = scores.get(word, 0) - 1
    return scores


learned_scores = learn_scores(train_data)


def guess_mood_learned(sentence):
    total = 0
    for word in clean(sentence):
        total += learned_scores.get(word, 0)  
    return "Happy" if total > 0 else "Sad"


print("Mood counts (Happy, Sad):", count_moods(train_data))

print("\nLevel 2 on practice data:")
acc = accuracy(practice_data, guess_mood)
print(f"Accuracy: {acc:.0f}%")

print("\nBonus (learned scores) on practice data:")
acc2 = accuracy(practice_data, guess_mood_learned)
