#Word Counting in text

text = """
Lorenz has spent her life proving those people wrong. She expects a lot—not only from her life, but from herself. And as a senior accessibility specialist at Amazon, she works to make sure that the latest technology is accessible to everyone.

“I always want to push the envelope in my own life, but also in my role here at Amazon,” she said.

Lorenz works on a team developing features for Alexa Shopping, one of the many teams working on Alexa, Amazon’s voice AI. Looking for ways to help people with disabilities—that often also benefit everyone else—her team recently launched features like Amazon Pharmacy on Alexa and “Alexa, send my shopping list.”

“I look at where the gaps are for people, figure out how we can make things better, and then we go innovate and launch new features that do those things,” she said. “In my experience, the awesome thing about working at Amazon is that accessibility is a priority. But while we can be proud of what we’ve built, at the same time, we need to keep pushing.”
"""
print(text)
print("Characters num:",len(text))

print("Words:", len(text.split()))

#Word counting in dictinoray 
text = """
a b c a a b
"""

print(text.split())

word_count = {}

for word in text.split():
  if word in word_count:
    word_count[word] += 1
  else:
    word_count[word] = 1

print(word_count)
