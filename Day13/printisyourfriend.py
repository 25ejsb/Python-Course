pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages + word_per_page
print(total_words)

# Hmm, why is it only printing out the number of pages?
# lets try printing out both of them

print(pages)
print(word_per_page)

# Hmm why is word_per_page 0?
# Ohh! I put == instead of =

pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages + word_per_page
print(total_words)

# There we go!