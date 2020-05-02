

class CharacterSetUtils:

    def get_character_set(self, base_character_sets, character_set_description):
        base_character_set = base_character_sets[character_set_description.base_character_set]
        redundant_character_set = character_set_description.redundant_character_set
        extra_character_set = character_set_description.mappings.keys()

        if not extra_character_set:
            result = base_character_set
        else:
            result = base_character_set + [k for k in extra_character_set]

        for c in redundant_character_set:
            result.remove(c)

        return result

    def map_words(self, character_set_description, words):
        words_mapped = {}
        for word in words:
            word_mapped = self.map_word(character_set_description, word)
            word_mapped_values = words_mapped.get(word_mapped)
            if word_mapped_values is None:
                word_mapped_values = [word]
            else:
                word_mapped_values.append(word)
            words_mapped.update({word_mapped: word_mapped_values})

        return words_mapped

    def map_word(self, character_set_description, word):
        mappings = character_set_description.mappings
        if not mappings:
            return word

        word_mapped = ""
        for c in word:
            if c in mappings.keys():
                word_mapped += mappings[c]
            else:
                word_mapped += c

        return word_mapped
