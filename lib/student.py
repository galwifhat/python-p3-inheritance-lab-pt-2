import re
class Student:
    def hello(self):
        print("Hey there! I'm so excited to learn stuff.")
    def raise_hand(self):
        print("Pick me!")

class ChattyStudent(Student):
    def hello(self):
        super().hello()
        print("How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died...")
        # paragraph = "How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died..."
        # sentences = re.split(r'(?<=[.!?])\s+', paragraph.strip()) #looks for whitespace that comes after a punctuation mark/punc stays in the sen
        # for sentence in sentences:
        #     print(sentence)

    def raise_hand(self):
        for a in range(10):
         super().raise_hand()

chat1 = Student()
chat1.hello()
chat1.raise_hand()

chat2 = ChattyStudent()
chat2.hello()
chat2.raise_hand()