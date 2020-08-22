import re
import requests
from collections import OrderedDict
from enum import Enum


class CategoryStatus(Enum):
    EXISTING_CATEGORY = 0
    NON_EXISTING_CATEGORY = 1
    NON_EXISTING_SUBCATEGORY = 2
    NON_EXISTING_POSITION = 3


def extract_category_status_and_category(raw_page):
    # example of the most important part of the raw page: "tylko wśród haseł należących do kategorii tematycznej:<br/>CZŁOWIEK JAKO ISTOTA FIZYCZNA->Budowa i funkcjonowanie ciała ludzkiego->części ciała, elementy i substancje składowe;</li></ul><br>"
    CATEGORY_STATUS_PATTERN = r'<br/>([^->]*)->([^->]*)->([^<]*);</li>'
    res = re.search(CATEGORY_STATUS_PATTERN, raw_page)

    if res.group(1) == '':
        return CategoryStatus.NON_EXISTING_CATEGORY, 'non existing category'
    if res.group(2) == '':
        return CategoryStatus.NON_EXISTING_SUBCATEGORY, 'non existing subcategory'
    if res.group(3) == '':
        return CategoryStatus.NON_EXISTING_POSITION, 'non existing position'

    return CategoryStatus.EXISTING_CATEGORY, f'{res.group(1)} | {res.group(2)} | {res.group(3)}'

def extract_word_list(raw_page):
    # example of the most important part of the raw page: "<ul class="search_list"><li><a href="index.php?id_hasla=90184&amp;ind=0&amp;w_znacz=5225022">achilles&nbsp;</a></li><li><a href="index.php?id_hasla=18993&amp;ind=0&amp;w_znacz=1859912">adrenalina&nbsp;</a></li><li><a href="index.php?id_hasla=25079&amp;ind=0&amp;w_znacz=4906919">żółć&nbsp;</a></li></ul></div><div class="clear"></div>"
    word_list = []
    for line in raw_page.splitlines():
        if re.search(r'<ul class="search_list"><li>.*</li>', line):
            word_list.extend(re.findall(r'>([^&]+)&nbsp;<', line))
    return word_list

def get_page(category_index, subcategory_index, position_index):
    dictionary_url = get_polish_dictionary_url(category_index, subcategory_index, position_index)
    raw_page = requests.get(dictionary_url).text
    category_status, category = extract_category_status_and_category(raw_page)
    word_list = []
    if category_status is CategoryStatus.EXISTING_CATEGORY:
        print(f'downloaded category: {category}')
        word_list = extract_word_list(raw_page)
    return category_status, category, word_list

def get_polish_dictionary_url(category_index, subcategory_index, position_index):
    dictionary_url = (
        f'https://wsjp.pl/index.php?pwh=0&l=1&ind=0&wz=2&szukaj=&ciag_fh=on&z_przest=bez&kwal_ilub=lub&'
        f'kwal_tem_kat={category_index}&'
        f'&kwal_tem_podkat={subcategory_index}&'
        f'kwal_tem_poz={position_index}&'
        f'podtyp_2=on&podtyp_4=on'
    )
    return dictionary_url

def save_as_preliminary_word_list_seed(word_lists):

    with open("../wlip-0003/preliminary-word-lists/_seed", "w") as f:
        f.write('# created with create_preliminary_word_list_seed.py' + '\n')
        f.write('\n')
        f.write('# groups:' + '\n')

        for category in word_lists.keys():
            f.write(f'# group: {category}' + '\n')

        for category in word_lists.keys():
            f.write('\n')
            f.write(f'# group: {category}' + '\n')
            for word in word_lists[category]:
                f.write(word + '\n')

word_lists = OrderedDict()

CATEGORY_INDEX_START = 2
SUBCATEGORY_INDEX_START = 2
POSITION_INDEX_START = 2
category_index = CATEGORY_INDEX_START
subcategory_index = SUBCATEGORY_INDEX_START
position_index = POSITION_INDEX_START
while True:
    category_status, category, word_list = get_page(category_index, subcategory_index, position_index)
    if category_status is CategoryStatus.NON_EXISTING_POSITION:
        subcategory_index = subcategory_index + 1
        position_index = POSITION_INDEX_START
        continue
    if category_status is CategoryStatus.NON_EXISTING_SUBCATEGORY:
        category_index = category_index + 1
        subcategory_index = SUBCATEGORY_INDEX_START
        position_index = POSITION_INDEX_START
        continue
    if category_status is CategoryStatus.NON_EXISTING_CATEGORY:
        break
    word_lists[category] = word_list
    position_index = position_index + 1

save_as_preliminary_word_list_seed(word_lists)
