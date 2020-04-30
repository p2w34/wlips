

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

    def map_word(self, character_set, word):
        mappings = character_set.mappings
        if not mappings:
            return word

        word_mapped = ""
        for c in word:
            if c in mappings.keys():
                word_mapped += mappings[c]
            else:
                word_mapped += c

        return word_mapped
