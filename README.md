# Word Lists Improvement Proposals

Contributions are very much welcome - please check [Contributors FAQ](contributors-faq.md).

## Abstract
Aim of this work is to create [BIP0039](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) word lists
for various languages.

## Motivation
There is not much progress in internationalization of BIP0039 word lists. This is definitely one of the obstacles
on the road to widespread adoption.
There have been already submitted some [BIP0039](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) PRs
for several languages, but most of them hang unreviewed for a long time.
What is more, different word lists are created by different authors, with different objectives in mind.
There is no common denominator. Work on Word List Improvement Proposals aims to clarify the objectives and provide help
for lists creation.

## Description

All work is gathered as proposals in the table below. Any help from community is appreciated, especially work
on WLIP-0001 and WLIP-0003.

There are two key observations:  
1) Various languages might be grouped based on the character set they use. They are ofter very similar.
It brings many benefits, including common set of requirements for such group of languages.  
2) Creation of list for particular language does not have to start from the scratch!
The main idea is that lists creation is based on the provided [preliminary word list](wlip-0003/english_us/preliminary-word-list)
consisting of a few thousand commonly used words. It is way easier to translate such 'master list' and then polish it.
Plus, very often, some of the common words sound very similar in various languages.

|Number|Title|Type|Status|
|---|---|---|---|
|[WLIP-0000](wlip-0000.md)|WLIP Template|Informational|Accepted|
|[WLIP-0001](wlip-0001.md)|Word lists requirements|Standard|Draft|
|[WLIP-0002](wlip-0002.md)|Word list file format|Standard|Draft|
|[WLIP-0003](wlip-0003.md)|Word lists|Standard|Draft|














