def get_num_words(text):
  return len(text.split())

def get_character_count(text):
    results = {}
    for character in text:
        character = character.lower()

        if character in results:
            results[character] += 1
        else:
            results[character] = 1
    return results




def get_sorted_list(text):
    char_dict = get_character_count(text)
    

    char_list = [{"letter": key, "amount": value} for key,value in char_dict.items()]

    char_list.sort(reverse=True, key=lambda items: items["amount"])
    
    return char_list
 
