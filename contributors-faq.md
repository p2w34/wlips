# Contribution FAQ

## How can I contribute?
Currently this repository is still in it's infancy.
Contributors are asked to focus on extending [preliminary word list](wlip-0003/preliminary-word-lists/english_us).
Let's first add ~5k words (they should be manually chosen):
  - length does not matter here - a word might be too long for English list, but it might be appropriate for other lists,
  - common nouns and adjectives known to everyone;
  they should come from some kind of widely accepted source (well known dictionaries)
  - it does not matter that some words might be less known in some of the countries (for example animals or fruits),
  - avoid words from groups like: religion, i.e. words which might lead to some unnecessary discussions
  - it is OK if some people especially children would not understand some of them,
  but it should not 'put in trouble' (no embarrassing words) people who know the meaning and are asked for explanation.
  This is a vague definition but there really is no point to try to better define such words.
  When in doubt, please simply come up with another word.
  - hopefully grouping them by category will help; let's keep order (may be simply alphabetical) within each such group;
    feel free to add more groups.

Preliminary word list creation is a prerequisite to start work on the word lists.

## Is there any roadmap? How can I add a word list for a new language?
Again, this repo is still in its infancy. The work should progress as follows:
- finishing [preliminary word list](wlip-0003/preliminary-word-lists/english_us)
- for each language:
    - translate preliminary_word_list
    - create a draft of the word list by extracting words fulfilling requirements; this can be automated using the script:
      `/home/pawel/priv/wlips/scripts/create_word_list.py -l translated_preliminaroy_word_list`
    - manually polish the list
