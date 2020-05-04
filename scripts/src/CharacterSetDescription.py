import re


class CharacterSetDescription:
    BASE_CHARACTER_SET_NAME_PATTERN = r"([a-z]*)"
    REDUNDANT_CHARACTER_SET_PATTERN = r"(-[a-z]+)?"
    EXTRA_CHARACTER_SET_PATTERN = r"((\+\w:\w)+)*"

    def __init__(self, character_set_description):

        regex = r"(?:.*)(\[{}{}{}\])(?:.*)".format(self.BASE_CHARACTER_SET_NAME_PATTERN,
                                       self.REDUNDANT_CHARACTER_SET_PATTERN,
                                       self.EXTRA_CHARACTER_SET_PATTERN)
        result = re.match(regex, character_set_description)
        if result is None or result.group(2) is None:
            raise Exception("invalid character set description")

        base_character_set_name = result.group(2)

        redundant_character_set = []
        if result.group(3) is not None:
            redundant_character_set = list(result.group(3)[1:])

        mappings = {}
        if result.group(4) is not None:
            mappings_candidates = result.group(4).split('+')[1:]
            mappings = dict(zip([k[0] for k in mappings_candidates], [v[2] for v in mappings_candidates]))

        self.description = result.group(1)
        self.base_character_set = base_character_set_name
        self.redundant_character_set = redundant_character_set
        self.mappings = mappings

    def __eq__(self, other):

        return self.description == other.description \
               and self.base_character_set == other.base_character_set \
               and self.redundant_character_set == other.redundant_character_set \
               and self.mappings == other.mappings
