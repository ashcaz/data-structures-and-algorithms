from code_challenges.hashtable.hashtable import Hashtable


def repeat_word(paragraph: str) -> str:
    # create new hastable
    hashtable = Hashtable()

    # split paragraph into an array of words
    words_list = paragraph.split()

    # loop through words
    for i in range(len(words_list)):
        # check to see if it already exists in hashtable
        if hashtable.contains(i):
            # hash the key
            ht_index = hashtable._hash(i)
            # check to see if value is the same
            ht_node = hashtable._buckets[ht_index]

            if ht_node:
                return words_list[i]
            # if value is the same return

        hashtable.set(i, words_list[i])
