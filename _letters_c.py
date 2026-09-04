# -*- coding: utf-8 -*-
"""1 Peter through Jude &mdash; the six letters that follow James."""
from _lettertpl import note, vid, insert

B = []


def book(**kw):
    B.append(kw)


book(id='peter-1', num='60', name='1 Peter',
     sub=u'A letter to people who have become foreigners in the towns they were born in.',
     cap=u'<b>Events</b> none narrated &mdash; it is a letter, not a story<span class="sep">&middot;</span>'
         u'<b>Written</b> c. AD 62&ndash;64, from &ldquo;Babylon&rdquo;<span class="sep">&middot;</span>'
         u'Circulated around five provinces of northern Asia Minor',
     genre=u'Epistle &middot; circular', author=u'Peter, written down by Silvanus', ch=u'5',
     setting=u'Written from Rome to scattered believers in Asia Minor',
     theme=u'Living well as a permanent minority',
     prose=u'Peter writes to believers spread across five Roman provinces and calls them exiles and resident aliens '
           u'&mdash; legal terms for people living somewhere they do not belong, with no civic standing and no '
           u'protection from the crowd. That is his diagnosis of their situation and also his instruction for '
           u'handling it. They are not being executed; they are being talked about, excluded, insulted for no longer '
           u'joining in, and the letter takes that ordinary social pain entirely seriously. His answer runs on two '
           u'tracks at once. On one, the language of enormous privilege: a chosen race, a royal priesthood, a holy '
           u'nation, a people for God&rsquo;s own possession &mdash; every phrase lifted from what was said to '
           u'Israel at Sinai and applied to a scattered gentile minority. On the other, a strategy of conspicuous '
           u'decency: live such good lives among the pagans that the accusations fail on inspection, honour the '
           u'emperor, do good and suffer for it if you must, and always be ready to give a reason for the hope you '
           u'have &mdash; but with gentleness and respect. Running underneath is the example of Jesus, who when '
           u'insulted did not retaliate, and the promise that the suffering is brief. It closes with greetings from '
           u'&ldquo;she who is in Babylon&rdquo; and from Mark, whom Peter calls his son.',
     extra=note(u'Babylon means Rome',
                u'Peter sends greetings from &ldquo;Babylon&rdquo; (5:13), a city he had no known connection with '
                u'and which was by then largely deserted. Early Christian writers read it as code for Rome &mdash; '
                u'the empire that had destroyed the temple standing in for the empire that destroyed the first one '
                u'&mdash; and Revelation uses the same substitution for the same city a generation later.'),
     videos=vid('WhP7AZQlzCg', '1 Peter', u'exile as a status, and what to do with it'),
     wiki='First_Epistle_of_Peter', guide='book-of-1-peter')

book(id='peter-2', num='61', name='2 Peter',
     sub=u'A last testament against teachers who have worked out that a delayed promise is hard to defend.',
     cap=u'<b>Events</b> none narrated &mdash; it is a letter, not a story<span class="sep">&middot;</span>'
         u'<b>Written</b> c. AD 65&ndash;67<span class="sep">&middot;</span>'
         u'Shares most of a chapter of material with Jude',
     genre=u'Epistle &middot; testament', author=u'Peter', ch=u'3',
     setting=u'Written knowing his death is close',
     theme=u'The promise has not failed; it is being patient',
     prose=u'Peter writes as a man putting his affairs in order &mdash; he says he knows the putting off of his body '
           u'is imminent, and wants this on record so it can be recalled after he is gone. The threat he is '
           u'addressing is teachers inside the community who deny the coming judgement, and whose argument is '
           u'straightforward and rather good: everything has carried on exactly as it always has since the '
           u'ancestors died, so where is this promised arrival? Peter answers on three fronts. First, testimony: he '
           u'was on the mountain, he heard the voice, this is not a cleverly devised myth. Second, precedent: the '
           u'flood is proof that the world is not in fact a closed system that carries on regardless. Third, and '
           u'most memorably, a change of scale &mdash; with the Lord one day is like a thousand years and a thousand '
           u'years like one day, and what looks like slowness is patience, God not wanting anyone to be lost. The '
           u'central chapter is a sustained assault on the teachers themselves, in language of real disgust, '
           u'comparing them to irrational animals, waterless springs, and a dog returning to its vomit. At the very '
           u'end comes an aside of enormous consequence: our brother Paul writes about these things in all his '
           u'letters, in which there are some things hard to understand, which the ignorant twist as they do the '
           u'other scriptures.',
     extra=note(u'Paul&rsquo;s letters, already called scripture',
                u'2 Peter 3:16 refers to a collection of Paul&rsquo;s letters as circulating, difficult, and being '
                u'distorted &ldquo;as they do the other scriptures&rdquo; &mdash; grouping them with the Hebrew '
                u'Bible. It is the earliest hint that Paul&rsquo;s correspondence was being gathered and read as '
                u'authoritative, and one of the main reasons much scholarship dates this letter late and attributes '
                u'it to a follower of Peter rather than to Peter himself.', hot=True),
     videos=vid('wWLv_ITyKYc', '2 Peter', u'the scoffers&rsquo; argument, and the answer about time'),
     wiki='Second_Epistle_of_Peter', guide='book-of-2-peter')

book(id='john-1', num='62', name='1 John',
     sub=u'Written after a split, for the people who stayed, in a vocabulary of about three hundred words.',
     cap=u'<b>Events</b> none narrated &mdash; it is a letter, not a story<span class="sep">&middot;</span>'
         u'<b>Written</b> c. AD 85&ndash;95, from Ephesus<span class="sep">&middot;</span>'
         u'After a group had already left the community',
     genre=u'Epistle &middot; homily', author=u'John the Elder', ch=u'5',
     setting=u'To the churches around Ephesus, after a schism',
     theme=u'How to tell whether it is real',
     prose=u'Something has already happened before this letter starts: a group has left. &ldquo;They went out from '
           u'us, but they were not of us&rdquo; is the wound the whole thing is written around, and what they took '
           u'with them was a teaching that Christ did not truly come in the flesh. The letter never argues the point '
           u'in a systematic way. Instead it circles, repeating a small set of words &mdash; light, darkness, love, '
           u'truth, life, know, abide &mdash; in a Greek so simple it is the passage beginning readers are usually '
           u'given first, and so slippery that its pronouns have defeated commentators for two thousand years. What '
           u'it offers the people who stayed is a set of tests they can apply to themselves without needing to win '
           u'an argument. Do you keep his commands. Do you love your brother, or only say you do &mdash; because '
           u'anyone who claims to love the God he has not seen while hating the brother he has seen is lying. Do you '
           u'confess that Jesus came in the flesh. The letter is unsparing about self-deception and then '
           u'unexpectedly gentle: if we confess our sins he is faithful and just to forgive them, and if our own '
           u'heart condemns us, God is greater than our heart. It contains the flattest statement about God in the '
           u'New Testament &mdash; God is love &mdash; and immediately defines the word by pointing at a specific '
           u'death rather than at a feeling.',
     extra=note(u'A verse that was added, and then removed again',
                u'Some older English Bibles carry a trinitarian sentence at 1 John 5:7&ndash;8 &mdash; the '
                u'&ldquo;Johannine Comma&rdquo; &mdash; about three that bear witness in heaven. It appears in no '
                u'Greek manuscript before the fourteenth century, entered the printed text through a promise Erasmus '
                u'is said to have regretted, and travelled from there into the King James Version. Modern '
                u'translations omit it or footnote it.'),
     videos=vid('l3QkE6nKylM', '1-3 John', u'one video covering all three Johannine letters'),
     wiki='First_Epistle_of_John', guide='book-of-1-john')

book(id='john-2', num='63', name='2 John',
     sub=u'Thirteen verses to a congregation about who to let through the door.',
     cap=u'<b>Events</b> none narrated &mdash; it is a letter, not a story<span class="sep">&middot;</span>'
         u'<b>Written</b> c. AD 90&ndash;95, from Ephesus<span class="sep">&middot;</span>'
         u'One of the two shortest books in the Bible',
     genre=u'Epistle &middot; private note', author=u'John the Elder', ch=u'1',
     setting=u'To &ldquo;the elect lady and her children&rdquo;',
     theme=u'Hospitality has a limit',
     prose=u'This is a real letter of the ordinary ancient kind &mdash; one sheet of papyrus, thirteen verses, about '
           u'as long as a page would allow &mdash; addressed to &ldquo;the elect lady and her children&rdquo;, '
           u'almost certainly a church and its members rather than an individual. The elder is glad to have found '
           u'some of them walking in the truth, and repeats the commandment that was there from the beginning, which '
           u'is to love one another. Then he comes to the point. Travelling teachers are circulating who do not '
           u'confess that Jesus Christ has come in the flesh, and because early Christian mission ran entirely on '
           u'hospitality &mdash; a visiting teacher stayed in a member&rsquo;s house and was fed and sent on with '
           u'supplies &mdash; taking such a person in was not a private courtesy but a public endorsement, and '
           u'funded the next stop. So: do not receive him into the house or give him any greeting. It is a hard '
           u'instruction from the letters most associated with love, and it is aimed narrowly, at teachers on a '
           u'circuit rather than at neighbours. He ends by saying he has much more to write but would rather not use '
           u'paper and ink, and hopes to come and talk face to face.',
     extra=note(u'Why the shortest books are the shortest',
                u'2 and 3 John are each about the length of a single sheet of papyrus, roughly 20 by 25 centimetres '
                u'&mdash; the standard unit of ancient correspondence. Both end by saying the writer has more to say '
                u'and would rather say it in person. They are not summaries of anything; they are simply as long as '
                u'the paper was.'),
     videos=vid('l3QkE6nKylM', '1-3 John', u'one video covering all three Johannine letters'),
     wiki='Second_Epistle_of_John', guide='book-of-2-john')

book(id='john-3', num='64', name='3 John',
     sub=u'A note about a man named Diotrephes, who likes to put himself first.',
     cap=u'<b>Events</b> none narrated &mdash; it is a letter, not a story<span class="sep">&middot;</span>'
         u'<b>Written</b> c. AD 90&ndash;95, from Ephesus<span class="sep">&middot;</span>'
         u'The only New Testament book that never mentions Jesus by name',
     genre=u'Epistle &middot; private note', author=u'John the Elder', ch=u'1',
     setting=u'To Gaius, a member of one of the churches',
     theme=u'A local power struggle, preserved',
     prose=u'The companion piece to 2 John, and its mirror image: where that letter says refuse hospitality to the '
           u'wrong teachers, this one says extend it to the right ones. It is written to a man named Gaius, praised '
           u'for looking after travelling brothers who were strangers to him, and asked to send them on their way in '
           u'a manner worthy of God, since they set out for the sake of the Name and accept nothing from '
           u'non-believers. Then the letter turns to the actual problem, and it is startlingly small and '
           u'startlingly familiar. A man named Diotrephes, who likes to put himself first, refuses to acknowledge '
           u'the elder&rsquo;s authority, spreads malicious talk about him, will not welcome the travelling '
           u'brothers, and throws out of the church anyone who does. The elder says that if he comes he will bring '
           u'it up. Set against him is Demetrius, who is well spoken of by everyone. That is the whole letter &mdash; '
           u'a first-century congregational dispute over who controls the guest room &mdash; and it survived because '
           u'someone in that community thought it was worth copying.',
     extra=note(u'No mention of Jesus anywhere in it',
                u'3 John is the only book in the New Testament that never names Jesus, and one of only two in the '
                u'Bible &mdash; with Esther &mdash; not to name God directly either; it refers instead to '
                u'&ldquo;the Name&rdquo;. Both it and 2 John were slow to be accepted into the canon, and Eusebius '
                u'in the fourth century still lists them among the disputed books.', hot=True),
     videos=vid('l3QkE6nKylM', '1-3 John', u'one video covering all three Johannine letters'),
     wiki='Third_Epistle_of_John', guide='book-of-3-john')

book(id='jude', num='65', name='Jude',
     sub=u'Twenty-five verses of controlled fury, quoting two books that never made it into the Bible.',
     cap=u'<b>Events</b> none narrated &mdash; it is a letter, not a story<span class="sep">&middot;</span>'
         u'<b>Written</b> c. AD 65&ndash;67<span class="sep">&middot;</span>'
         u'Shares most of its material with 2 Peter 2',
     genre=u'Epistle &middot; polemic', author=u'Jude, brother of James', ch=u'1',
     setting=u'To an unnamed church that has been infiltrated',
     theme=u'Contend for the faith, and pity the doubters',
     prose=u'Jude says outright that he meant to write a different letter. He had been intending something warm '
           u'about their common salvation and found he had to write this instead, urging them to contend for the '
           u'faith once for all entrusted to God&rsquo;s people, because certain people have slipped in among them '
           u'&mdash; turning grace into licence and denying the master. What follows is twenty-five verses of '
           u'accumulating examples, delivered in threes: the wilderness generation, the angels who left their proper '
           u'place, Sodom and Gomorrah; Cain, Balaam, Korah. He calls the intruders blemishes at the love feasts, '
           u'shepherds feeding only themselves, waterless clouds, autumn trees without fruit and twice dead, wild '
           u'waves foaming up their own shame, wandering stars for whom the deepest darkness has been reserved. It '
           u'is the most concentrated invective in the New Testament. And then, having spent the whole letter '
           u'condemning, he turns at the last moment to the congregation itself with something completely different '
           u'in tone: build yourselves up, pray, keep yourselves in the love of God &mdash; and have mercy on those '
           u'who doubt, snatch others out of the fire, and show mercy to still others mixed with fear. The closing '
           u'doxology, to him who is able to keep you from stumbling, is read at the end of services to this day.',
     extra=note(u'Quoting books that are not in the Bible',
                u'Verses 14&ndash;15 quote 1 Enoch by name as prophecy, and verse 9 &mdash; the archangel Michael '
                u'disputing with the devil over the body of Moses &mdash; appears to come from the Assumption of '
                u'Moses. Neither is in any Jewish or Protestant canon. It is the clearest case in the New Testament '
                u'of a writer drawing on literature his readers evidently knew well, and it made Jude one of the '
                u'last books to be accepted.', hot=True),
     videos=vid('6UoCmakZmys', 'Jude', u'the triads, the invective, and the turn at the end'),
     wiki='Epistle_of_Jude', guide='book-of-jude')

insert(B, before='revelation')
