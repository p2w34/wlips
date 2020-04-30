from scripts.src.CharacterSetDescription import CharacterSetDescription


CHARACTER_SET_ENGLISH = list("abcdefghijklmnopqrstuvwxyz")
CHARACTER_SET_POLISH = list("abcdefghijklmnoprstuwyząćęłńóśźż")
CHARACTER_SETS = {"english": CHARACTER_SET_ENGLISH}

CHARACTER_SET_DESCRIPTION_ENGLISH = CharacterSetDescription("[english]")
CHARACTER_SET_DESCRIPTION_POLISH = CharacterSetDescription("[english-qvx+ą:a+ć:c+ę:e+ł:l+ń:n+ó:o+ś:s+ź:z+ż:z]")
CHARACTER_SET_DESCRIPTION_EMPTY = CharacterSetDescription("[]")
