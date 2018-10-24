from pydub import AudioSegment
from os import system
from wiki_fetch import fetch_page_content
from text_manip import clean_article, count_syllables, delete_duplicates
from rap import rap
import subprocess
from nltk.tokenize import sent_tokenize
from translate_back import translate_back
from threading import Thread
from time import sleep
import profiles
from random import choice
from audio_manip import *


def record_rap(wiki_page):
    ADLIBS = ["yo", "ayy", "yah", "okay", "grah"]
    title, page = fetch_page_content(wiki_page)
    title = clean_article(title)
    sentences = [clean_article(sent).strip() for sent in sent_tokenize(page)]
    print(title)
    couplets = rap(sentences)
    delete_duplicates(couplets)
    # title = "cats"
    # couplets = [('The company built or renovated skyscrapers, hotels, casinos, and golf courses.', 'His first two marriages ended in widely publicized divorces.'), ('He managed the company until his 2017 inauguration.', 'due in part to its opposition to multiculturalism and immigration.'), ('His election and policies have sparked numerous protests.', 'He uses Twitter as a direct means of communication with the public, sidelining the press.'), ('Trump grew up in Jamaica, Queens, and attended the Kew-Forest School from kindergarten through seventh grade.', 'At age 18 in 1930, she immigrated to New York, where she worked as a maid.'), ('While at Wharton, he worked at the family business, Elizabeth Trump & Son.', 'This transformed his 2016 election committee into a 2020 reelection one.'), ('In 1971, Donald Trump was made president of the company, which was later renamed the Trump Organization.', 'As a child, he attended the First Presbyterian Church in Jamaica, Queens, where he had his confirmation.'), ('As a child, he attended the First Presbyterian Church in Jamaica, Queens, where he had his confirmation.', 'By March 2016, Trump became poised to win the Republican nomination.'), ('The Trumps sold the property in 1972, with vacancy on the rise.', 'In general, news organizations have been hesitant to label these statements as lies.'), ("They sold it in 1995, by which time Ivana was no longer involved in the hotel's day-to-day operations.", "Trump's early policies have favored rollback and dismantling of government regulations."), ('He intended to rename it Trump Empire State Building Tower Apartments if he had been able to boost his share.', 'In 1999, Trump told Larry King Live: I believe in universal healthcare.'), ('In order to join, prospective members had to pay an initiation fee and annual dues.', 'Trump called the report fake news.'), ('leaving Trump with 50 percent ownership.', 'His interactions with the press turned into what some sources called a love-hate relationship.'), ('The pageants include Miss USA and Miss Teen USA.', 'After repeated questioning by reporters, Trump said that he disavowed David Duke and the KKK.'), ('Trump later named Linda McMahon as Administrator of the Small Business Administration.', 'Trump is the wealthiest president in U.S. history, even after adjusting for inflation.'), ('and falsely claimed that the rumors had been started by Hillary Clinton during her 2008 campaign.', 'He also announced his campaign slogan: Make America Great Again.'), ('Throughout his career, Trump has sought media attention.', 'However, North Korea accelerated their missile and nuclear tests leading to increased tension.'), ('On July 15, 2016, Trump announced his selection of Indiana Governor Mike Pence as his running mate.', "I don't even wait."), ('due in part to its opposition to multiculturalism and immigration.', 'By March 2016, Trump became poised to win the Republican nomination.'), ('Trump is the wealthiest president in U.S. history, even after adjusting for inflation.', 'As a child, he attended the First Presbyterian Church in Jamaica, Queens, where he had his confirmation.'), ('could impact $2\xa0trillion in global trade.', 'At age 18 in 1930, she immigrated to New York, where she worked as a maid.'), ('The administration then clarified that visitors with a green card were exempt from the ban.', "reversing Trump's pre-election position critical of further involvement in Afghanistan."), ('and South Carolina Governor Nikki Haley as Ambassador to the United Nations.', "Trump's early policies have favored rollback and dismantling of government regulations.")]
    # couplets = [('Cats have a high breeding rate.', 'The males will fight over her, and the victor wins the right to mate.'), ('Within this family, domestic cats .', 'Herodotus expressed astonishment at the domestic cats in Egypt, because he had only ever seen wildcats.'), ('Two main theories are given about how cats were domesticated.', 'However, the ecological role of introduced cats can be more complicated.'), ("The extra lumbar and thoracic vertebrae account for the cat's spinal mobility and flexibility.", 'Their excellent sense of balance allows cats to move with great stability.'), ('Within the jaw, cats have teeth adapted for killing prey and tearing meat.', 'The claws on the fore feet are typically sharper than those on the hind feet.'), ('Like almost all members of the Felidae, cats have protractable and retractable claws.', 'Cats can voluntarily extend their claws on one or more paws.'), ('The claws on the fore feet are typically sharper than those on the hind feet.', 'After about 20 to 30 minutes, once the female is finished grooming, the cycle will repeat.'), ('which they use to communicate through urine spraying and marking with scent glands.', 'The French kings often witnessed these spectacles and even lit the bonfire with their own hands.'), ('Their excellent sense of balance allows cats to move with great stability.', 'have also contributed to their susceptibility.'), ('The average lifespan of pet cats has risen in recent years.', 'At 10–12 days, implantation occurs.'), ('Domestic cats, especially young kittens, are known for their love of play.', 'Cats have seven cervical vertebrae, as do almost all mammals; 13 thoracic vertebrae .'), ('Multiple males will be attracted to a female in heat.', 'The claws on the fore feet are typically sharper than those on the hind feet.'), ('Feral cats are domestic cats that were born in or have reverted to a wild state.', 'The males will fight over her, and the victor wins the right to mate.')]
    if title.lower() == "cat":
        del couplets[1]
    p = profiles.beat2
    song = AudioSegment.from_file("audio/beat2.mp3") - 4
    full_ranges = []
    couplet_counter = 0
    for c_range in p["couplet"]:
        if couplet_counter >= len(couplets):
            break
        couplet = couplets[couplet_counter]
        couplet_counter += 1
        save_wav(couplet[0], "audio/c1")
        save_wav(couplet[1], "audio/c2")
        system("ffmpeg -i audio/c1.wav audio/c1.wav -y")
        system("ffmpeg -i audio/c2.wav audio/c2.wav -y")
        l1 = get_duration_wav("audio/c1.wav") * 1000
        l2 = get_duration_wav("audio/c2.wav") * 1000
        if l1 > c_range[0][1] - c_range[0][0]:
            range_len = c_range[0][1] - c_range[0][0]
            speedup = float(l1) / range_len
            stretch("audio/c1.wav", "audio/c1.wav", speedup)
        if l2 > c_range[1][1] - c_range[1][0]:
            range_len = c_range[0][1] - c_range[0][0]
            speedup = float(l2) / range_len
            stretch("audio/c2.wav", "audio/c2.wav", speedup)

        c1_a = AudioSegment.from_file("audio/c1.wav")
        c2_a = AudioSegment.from_file("audio/c2.wav")
        song = song.overlay(c1_a, position=c_range[0][1] - l1)
        full_ranges.append([c_range[0][1] - l1, c_range[0][1]])
        full_ranges.append([c_range[1][1] - l2, c_range[1][1]])
        song = song.overlay(c2_a, position=c_range[1][1] - l2)
    print(full_ranges)
    if full_ranges:
        for i, a in enumerate(p["adlib"]):
            valid = True
            for r in full_ranges:
                if (r[0] - 500 < a and a < r[1]) or a > full_ranges[
                    len(full_ranges) - 1
                ][1]:
                    valid = False
                    break
            if valid:
                # save_wav(choice(ADLIBS), "audio/a" + str(i))
                print("ad")

                lib = AudioSegment.from_file("audio/" + choice(ADLIBS) + ".wav")
                song = song.overlay(lib, position=a)

        save_wav(title, "audio/title")
        print("tite")
        title_wav = AudioSegment.from_file("audio/title" + ".wav")
        song = song.overlay(title_wav, position=p["title"])
        song = song[: full_ranges[len(full_ranges) - 1][1] + 2000]

        song.export("productions/" + title + ".mp3")
        for couplet in couplets:
            print(couplet[0])
            print(couplet[1])
            print()
        for i in range(1, len(full_ranges)):
            cur = full_ranges[i]
            prev = full_ranges[i - 1]
            if cur[0] < prev[1]:
                full_ranges[i][0] = prev[1] + 1
        return (title, full_ranges, couplets[:len(full_ranges) // 2])
    else:
        return None
