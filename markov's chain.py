# -*- coding: cp1252 -*-
#!/usr/bin/env python
import string
import random

s = """We're here for your gold, not your heads, so don’t nobody decide to be a hero."

Malcolm Graves is a wanted man in every realm, city-state, and empire he has visited. Tough, strong-willed, and above all, relentless, through his life of crime he has amassed (then invariably lost) a small fortune.

Raised in the wharf alleys of Bilgewater, Malcolm quickly learned how to fight and how to steal, skills that have served him very well over the years. Smuggling himself to the mainland in the bilge of an outgoing cargo ship as a youth, he stole, lied, and gambled his way from place to place. But it was across the table of a high-stakes card game that Malcolm met the man who would change his life: the trickster now known as TwistedFateSquare.png Twisted Fate. Both men saw the same reckless love of danger and adventure in the other, and a dysfunctional partnership that lasted nearly a decade was born.

Combining their unique skills, Graves and Twisted Fate were an effective team, pulling off scores of heists. They stole from and swindled the rich and foolish for cash, fame, and the sheer thrill. Adventure became as much of a lure as the payoff.

On the borderlands of Noxus, they set two renowned houses at each other's throats as cover for the rescue of an heir apparent being held hostage. That they pocketed the reward money only to ransom the vile young man to the highest bidder should have come as no surprise to their employer. In Piltover, they hold the distinction of being the only thieves ever to crack the supposedly impenetrable Clockwork Vault. Not only did the two empty the vault of its treasures, but they tricked its guards into loading it onto their hijacked cargo ship. Only once the pair were over the horizon was the theft discovered, along with Fate's trademark playing card.

But eventually their luck ran out. During a heist that went wrong, Twisted Fate seemingly betrayed and abandoned his partner. Graves was taken alive and thrown in the infamous prison known as the Locker.

Years of imprisonment and torture followed, during which time Graves nursed his hatred for his former partner. A lesser man would surely have broken, but Malcolm Graves endured it all and finally escaped. He clawed his way to freedom and began his pursuit of Twisted Fate, the man whose treachery consigned him to a decade of unspeakable misery.

Holed up in an empty bar, bleeding from a dozen wounds and surrounded by armed men who wanted him dead, Malcolm Graves had seen better days. He’d seen worse ones, too, so he wasn’t worried yet. Graves leaned over the smashed bar and helped himself to a bottle, sighing as he read the label.

"Demacian wine? That all you got?"

"It's the most expensive bottle I have..." said the innkeeper, cowering below the bar in a glittering ocean of broken glass.

Graves looked around the bar and grinned.

"I reckon it's the only bottle you got left."

The man had panic written all over him. He clearly wasn't used to being in the middle of a gunfight. This wasn't Bilgewater, where fatal brawls broke out ten times a day. Piltover was regarded a more civilized city than Graves's hometown. In some ways, at least.

He yanked the cork free with his teeth and spat it to the floor before taking a swig. He swilled it around his mouth like he’d seen rich folks do before swallowing it.

"Pisswater," he said, "but beggars can't be choosers, huh?"

A voice shouted through the broken windows, buoyed with confidence it hadn't earned and the false bravado of numbers.

"Give it up, Graves. There's seven of us to one of you. This ain't going to end well."

"Damn straight it ain't," hollered Graves in return. “If you want to walk away from this, you best go fetch more men!"

He took another swig from the bottle, then put it down on the bar.

"Time to get to work," he said, lifting his one-of-a-kind shotgun from the bar.

Graves reloaded, pushing fresh shells home. The weapon snapped together with a satisfyingly lethal sound, loud enough to carry to the men outside. Anyone who knew him would know that sound and what it meant.

The outlaw slid off the barstool and made his way to the door, glass crunching beneath his boot heels. He stooped to glance through a cracked window. Four men crouched behind makeshift cover: two on the upper floor of a fancy workshop, another two in shadowed doorways to either side. All held crossbows or muskets at the ready.

"We tracked you halfway across the world, you son of a bitch," shouted the same voice. "Bounty didn't say nothin' about you being alive or dead. Walk out now with that cannon of yours held high and there don't need to be no more bloodshed."

"Oh, I'm comin' out," shouted Graves. "Don't you worry none about that."

He drew a silver serpent from his pocket and flipped it onto the bar, where it spun through a pool of spilled rum before landing heads up. A trembling hand reached up to take it. Graves grinned.

"That's for the door," he said.

"What about the door?" asked the innkeeper.

Graves hammered his boot into the inn's front door, smashing it from its hinges. He dived through the splintered frame, rolling to one knee, gun blasting from the hip.

"Alright, you bastards!" he roared. "Let's finish this!"""

def split_string(s):
    #TODO: deal with situations like "lol??...??,/.,/./../,"
    string_ls = s.split(" ")
    for i in range(len(string_ls)):
        w = string_ls[i]
        #If word has a punctuation mark at the end and isn't the mark itself
        if w not in string.punctuation:
            if w[-1] in string.punctuation:
                #Split them apart
                string_ls.append(w[-1])
                string_ls[i] = w[:-1]
    return string_ls

def markov_chain(string_ls):
    probability_dict = {}
    #First word
    probability_dict["[BEGIN]"] = {string_ls[0]: 1}
    for i in range(len(string_ls)):
        #If not last word
        if i != len(string_ls) - 1:
            #If current word hasn't been registered
            if string_ls[i] not in probability_dict:
                probability_dict[string_ls[i]] = {string_ls[i + 1]: 1}
            else:
                #If next word hasn't been registered
                if string_ls[i + 1] not in probability_dict[string_ls[i]]:
                    probability_dict[string_ls[i]][string_ls[i + 1]] = 1
                                                  
                #Next word is already registered
                else:
                    probability_dict[string_ls[i]][string_ls[i + 1]] += 1
        else:
            if string_ls[i] not in probability_dict:
                probability_dict[string_ls[i]] = {"[END]" : 1}
            else:
                probability_dict[string_ls[i]]["[END]"] = 1
    return probability_dict

def markov_generate(word_dict):
    #dict should follow the format: {"Word": {"Next_word1": prob, "Next_word2": prob}}
    
    def choose_randomly(probability_dict):
        #dict should follow the format: {item1: prob, item2: prob}
        prob_sum = 0
        for v in probability_dict.values():
            prob_sum += v
        r = random.randrange(prob_sum)
        sum_so_far = 0
        for k, v in probability_dict.iteritems():
            sum_so_far += v
            if(r < sum_so_far):
                return k
            
    last_word = "[BEGIN]"
    result = ""
    while last_word != "[END]":
        last_word = choose_randomly(word_dict[last_word])
        result += last_word + " "
    result = result[:-6]
    return result

                

s = split_string(s)
print s
m = markov_chain(s)
print m
mg = markov_generate(m)
print mg

