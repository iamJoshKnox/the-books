# -*- coding: utf-8 -*-
"""1 Thessalonians through Hebrews."""
from _lettertpl import note, vid, insert

B = []


def book(**kw):
    B.append(kw)


book(id='thessalonians-1', num='52', name='1 Thessalonians',
     sub=u'Possibly the oldest surviving Christian document, written weeks after Paul was run out of town.',
     cap=u'<b>Events</b> none narrated &mdash; it is a letter, not a story<span class="sep">&middot;</span>'
         u'<b>Written</b> c. AD 50&ndash;51, from Corinth<span class="sep">&middot;</span>'
         u'Within months of the church being founded',
     genre=u'Epistle &middot; pastoral', author=u'Paul, with Silvanus and Timothy', ch=u'5',
     setting=u'Written in Corinth to Thessalonica, capital of Macedonia',
     theme=u'Holding on under pressure, and what happens to those who die first',
     prose=u'Paul was in Thessalonica for a matter of weeks before a riot forced him out, and he left with no idea '
           u'whether the handful of new believers would survive. This letter is written after Timothy came back with '
           u'news that they had, and the relief is audible: he keeps returning to how much he wanted to come himself '
           u'and could not. Two things are on his mind. The first is that they are under social pressure from their '
           u'own neighbours, and he wants them to know that suffering was always in the job description rather than '
           u'a sign that something has gone wrong. The second is a question they have sent him, and it is a question '
           u'that can only arise once: some of the congregation have died, and the church is grieving on the '
           u'assumption that those people have missed the return of Christ altogether. Paul&rsquo;s answer is the '
           u'passage that has shaped Christian funerals ever since &mdash; that the dead in Christ will rise first, '
           u'that the living will not precede them, and that the point of knowing this is not speculation but that '
           u'they should grieve differently from people with no hope. He is unbothered about timing, tells them the '
           u'day will come like a thief, and then gives the practical instructions this church apparently needed: '
           u'work with your hands, mind your own business, respect the people doing the hard work among you, and do '
           u'not put out the Spirit&rsquo;s fire.',
     extra=note(u'The earliest page in the New Testament',
                u'On the traditional dating only Galatians competes with it, and most reckonings place 1 '
                u'Thessalonians around AD 50 &mdash; roughly twenty years after the crucifixion, and some fifteen '
                u'years before the first gospel was written down. Whatever else it is, it is the oldest Christian '
                u'writing anyone has.', hot=True),
     videos=vid('No7Nq6IX23c', '1 Thessalonians', u'a young church under pressure, and the question about the dead'),
     wiki='First_Epistle_to_the_Thessalonians', guide='book-of-1-thessalonians')

book(id='thessalonians-2', num='53', name='2 Thessalonians',
     sub=u'A follow-up written because the first letter was misread, and someone may have forged a second one.',
     cap=u'<b>Events</b> none narrated &mdash; it is a letter, not a story<span class="sep">&middot;</span>'
         u'<b>Written</b> c. AD 51&ndash;52, from Corinth<span class="sep">&middot;</span>'
         u'Months after 1 Thessalonians, to the same church',
     genre=u'Epistle &middot; corrective', author=u'Paul, with Silvanus and Timothy', ch=u'3',
     setting=u'Written in Corinth to Thessalonica',
     theme=u'The day has not already come, so go back to work',
     prose=u'Something has gone wrong with the first letter. A report is circulating in Thessalonica &mdash; by '
           u'prophecy, by word of mouth, or by a letter claiming to be from Paul &mdash; that the day of the Lord '
           u'has already arrived. Some in the congregation have responded by giving up work altogether and living '
           u'off everyone else, and the church is fraying. Paul writes to shut the rumour down. He argues that the '
           u'day cannot have come, because certain things have not happened first: a rebellion, and the revealing of '
           u'a figure he calls the man of lawlessness, currently held back by something or someone he declines to '
           u'name, because the Thessalonians already know what he means and we do not. It is the most cryptic '
           u'passage he ever wrote, and centuries of interpreters have filled the gap with everything from the '
           u'Roman empire to the papacy to a future antichrist. Then he turns to the practical damage, and is blunt '
           u'about it: anyone unwilling to work should not eat, and the busybodies should settle down and earn their '
           u'own living. He signs the last lines in his own handwriting and points out the signature as the mark of '
           u'a genuine letter &mdash; which is the clearest evidence in the New Testament that forged apostolic '
           u'letters were already circulating.',
     extra=note(u'&ldquo;See what large letters I make&rdquo;',
                u'Paul dictated his letters to a secretary &mdash; Tertius names himself in Romans 16:22 &mdash; and '
                u'then took the pen for a closing line. In 2 Thessalonians 3:17 he calls that signature &ldquo;the '
                u'mark in every letter of mine&rdquo;, and in Galatians 6:11 he remarks on the size of his own '
                u'handwriting. Both make a good deal more sense once you notice that 2:2 has just warned them about '
                u'a letter &ldquo;seeming to be from us&rdquo;.'),
     videos=vid('kbPBDKOn1cc', '2 Thessalonians', u'the rumour, the restrainer, and the instruction to work'),
     wiki='Second_Epistle_to_the_Thessalonians', guide='book-of-2-thessalonians')

book(id='timothy-1', num='54', name='1 Timothy',
     sub=u'Instructions to a young man left behind to sort out a church, from the man who left him there.',
     cap=u'<b>Events</b> none narrated &mdash; it is a letter, not a story<span class="sep">&middot;</span>'
         u'<b>Written</b> c. AD 63&ndash;64<span class="sep">&middot;</span>'
         u'After a release from the imprisonment Acts ends with, on the traditional reckoning',
     genre=u'Epistle &middot; pastoral manual', author=u'Paul', ch=u'6',
     setting=u'To Timothy in Ephesus',
     theme=u'How a household of God is supposed to conduct itself',
     prose=u'Paul has left Timothy in Ephesus with an unenviable job: stop certain people teaching a mixture of '
           u'speculative genealogies and law-keeping that produces arguments rather than anything useful. The letter '
           u'is a working manual, and it moves quickly between very different registers. There is prayer for kings '
           u'and everyone in authority, on the grounds that God wants everyone saved. There is a passage on how men '
           u'and women should conduct themselves in the assembly that contains one of the most fiercely contested '
           u'sentences in the New Testament. There are the qualifications for overseers and deacons, which are '
           u'almost entirely about character and household management rather than ability &mdash; not a drunkard, '
           u'not violent, not a lover of money, able to manage his own house. There are instructions about widows '
           u'that reveal an organised welfare register with an age threshold and eligibility rules. And there is a '
           u'sustained attack on the love of money, including the line that is almost always misquoted: not that '
           u'money is the root of all evil, but that the love of it is a root of all kinds of evil, and that some '
           u'people, reaching for it, have wandered away and pierced themselves with many pangs. Throughout, Paul '
           u'writes as a man handing something over, and the repeated instruction is to guard what has been '
           u'entrusted.',
     extra=note(u'Written by Paul, or written in his name?',
                u'The three pastoral letters share a vocabulary and a settled church structure that the undisputed '
                u'letters do not, which is why much modern scholarship treats them as written by a follower in '
                u'Paul&rsquo;s name &mdash; a recognised practice in antiquity. The traditional view, followed by '
                u'the dating used here, takes them as genuine and late: after a release from the Roman custody Acts '
                u'leaves him in, and before a second arrest.'),
     videos=vid('7RoqnGcEjcs', '1 Timothy', u'a church being ordered, and the false teaching behind it'),
     wiki='First_Epistle_to_Timothy', guide='book-of-1-timothy')

book(id='timothy-2', num='55', name='2 Timothy',
     sub=u'The last thing Paul wrote: cold, alone, asking for a coat and his notebooks.',
     cap=u'<b>Events</b> none narrated &mdash; it is a letter, not a story<span class="sep">&middot;</span>'
         u'<b>Written</b> c. AD 66&ndash;67, from a Roman prison<span class="sep">&middot;</span>'
         u'Traditionally the last of Paul&rsquo;s letters, shortly before his execution',
     genre=u'Epistle &middot; farewell', author=u'Paul', ch=u'4',
     setting=u'Written in Rome, in chains, to Timothy in Ephesus',
     theme=u'Hold the line, and hand it on',
     prose=u'The tone changes completely. Paul is in custody again, and this time he does not expect to be released; '
           u'he says his life is already being poured out like a drink offering. He writes to Timothy as a father to '
           u'a son, remembering the faith he first saw in the boy&rsquo;s grandmother Lois and mother Eunice, and '
           u'telling him to fan into flame what is in him, because God did not give a spirit of timidity. The '
           u'instruction that runs through the letter is about transmission: what you heard from me, entrust to '
           u'reliable people who will be able to teach others &mdash; four generations in a single sentence. He '
           u'warns that people will accumulate teachers to tell them what their ears itch to hear. He describes '
           u'scripture as God-breathed and useful, which is where that phrase comes from. And then, near the end, '
           u'the letter stops being theological altogether and becomes unbearably specific. Demas has deserted him, '
           u'in love with this present world. Only Luke is with him. Bring Mark, he is useful. When you come, bring '
           u'the cloak I left at Troas with Carpus, and the books, especially the parchments. At his first defence '
           u'no one stood by him. He asks that it not be held against them. Come before winter.',
     extra=note(u'A cloak, some scrolls, and the parchments',
                u'2 Timothy 4:13 is the most human sentence in the New Testament and one of the most argued-over: a '
                u'cold man in a stone cell asking for a coat, some books, and &ldquo;especially the parchments&rdquo; '
                u'&mdash; <i>membranae</i>, the expensive material used for documents worth keeping. Nobody knows '
                u'what they were. Guesses have run from Hebrew scriptures to his Roman citizenship papers to blank '
                u'notebooks for the next letter.', hot=True),
     videos=vid('urlvnxCaL00', '2 Timothy', u'a final charge, and the loneliness underneath it'),
     wiki='Second_Epistle_to_Timothy', guide='book-of-2-timothy')

book(id='titus', num='56', name='Titus',
     sub=u'Appoint elders, silence the talkers, and remember what these people were like before &mdash; including us.',
     cap=u'<b>Events</b> none narrated &mdash; it is a letter, not a story<span class="sep">&middot;</span>'
         u'<b>Written</b> c. AD 63&ndash;64<span class="sep">&middot;</span>'
         u'Alongside 1 Timothy, to a colleague in the same situation',
     genre=u'Epistle &middot; pastoral manual', author=u'Paul', ch=u'3',
     setting=u'To Titus on Crete',
     theme=u'Sound teaching that shows up as ordinary decency',
     prose=u'Titus has been left on Crete to finish what was unfinished and appoint elders town by town, and the '
           u'letter is the shortest of the three pastorals and the most concentrated. The qualifications repeat 1 '
           u'Timothy&rsquo;s emphasis on character over talent, with one addition suited to the island: an elder '
           u'must hold firmly to the message so as to be able to answer back, because there are plenty of people '
           u'there talking nonsense for money. Paul then quotes a Cretan poet&rsquo;s line about Cretans always '
           u'being liars, agrees with it, and moves on &mdash; a joke with an edge that has embarrassed commentators '
           u'for centuries. The middle chapter is a household code addressed by age and station, and it is followed '
           u'by the reason for all of it, put twice in the letter as compact creedal statements: the grace of God '
           u'has appeared, training us to renounce godlessness and to live sensibly in the present age while we '
           u'wait; and he saved us, not because of works done by us in righteousness, but according to his own '
           u'mercy. The instruction that closes it is characteristically down to earth &mdash; avoid stupid '
           u'controversies and genealogies and quarrels about the law, because they are unprofitable and futile '
           u'&mdash; and there is a last, practical line about making sure Zenas the lawyer and Apollos lack nothing '
           u'for their journey.',
     extra=note(u'&ldquo;Cretans are always liars&rdquo;',
                u'Titus 1:12 quotes the Cretan seer Epimenides, and does it knowingly: a Cretan saying all Cretans '
                u'lie is the classic form of the liar paradox, which logicians still call the Epimenides paradox. '
                u'Paul&rsquo;s comment &mdash; &ldquo;this testimony is true&rdquo; &mdash; may be the only joke in '
                u'the pastoral letters.'),
     videos=vid('PUEYCVXJM3k', 'Titus', u'appointing elders, and grace that trains behaviour'),
     wiki='Epistle_to_Titus', guide='book-of-titus')

book(id='philemon', num='57', name='Philemon',
     sub=u'A single page about one runaway slave, which never quite says what it is asking for.',
     cap=u'<b>Events</b> none narrated &mdash; it is a letter, not a story<span class="sep">&middot;</span>'
         u'<b>Written</b> c. AD 60&ndash;61, from imprisonment<span class="sep">&middot;</span>'
         u'Carried to Colossae with Colossians, by Onesimus himself',
     genre=u'Epistle &middot; private letter', author=u'Paul, with Timothy', ch=u'1',
     setting=u'Written in custody to Philemon, a householder in Colossae',
     theme=u'What the gospel does to a relationship it has not abolished',
     prose=u'The shortest thing Paul wrote is a single sheet about one man. Onesimus was Philemon&rsquo;s slave; he '
           u'ran, somehow reached Paul in custody, and became a believer there. Paul is sending him back &mdash; '
           u'which he must, since harbouring a runaway was itself a crime &mdash; carrying this letter, and the '
           u'letter is a masterpiece of pressure applied without ever being named. Paul says he could command, but '
           u'appeals instead. He puns on the name: Onesimus means useful, and he was formerly useless to you but now '
           u'he is useful to both of us. He asks Philemon to receive him no longer as a slave but as more than a '
           u'slave, a beloved brother. He offers to cover any debt in his own hand, and then mentions, in passing, '
           u'that Philemon owes him his very self. He says he is confident of Philemon&rsquo;s obedience, knowing he '
           u'will do even more than asked. And he adds that he hopes to visit soon, so prepare a guest room. What he '
           u'never does is state the request. Whether he is asking for forgiveness, for manumission, or for Onesimus '
           u'to be sent back to him as a co-worker is left for Philemon to work out &mdash; in front of the whole '
           u'church, since the letter is addressed to them too.',
     extra=note(u'The letter that was used on both sides',
                u'Philemon was cited by American defenders of slavery as proof that Paul returned a fugitive to his '
                u'owner, and by abolitionists for verse 16 &mdash; no longer as a slave, but more than a slave, a '
                u'beloved brother &mdash; on the argument that a relationship redefined like that cannot survive as '
                u'property. The letter itself neither endorses the institution nor demands its end; it puts one man '
                u'inside it and asks what is now possible.', hot=True),
     videos=vid('aW9Q3Jt6Yvk', 'Philemon', u'a private letter read to a whole congregation'),
     wiki='Epistle_to_Philemon', guide='book-of-philemon')

book(id='hebrews', num='58', name='Hebrews',
     sub=u'An anonymous sermon in the finest Greek in the New Testament, arguing that the old arrangement was always a sketch.',
     cap=u'<b>Events</b> none narrated &mdash; it is a letter, not a story<span class="sep">&middot;</span>'
         u'<b>Written</b> c. AD 65&ndash;68<span class="sep">&middot;</span>'
         u'Before AD 70: it discusses the temple sacrifices as still being offered',
     genre=u'Homily &middot; sustained exposition', author=u'Unknown', ch=u'13',
     setting=u'To Jewish believers under pressure to return to the synagogue',
     theme=u'Better &mdash; a better priest, a better covenant, a better sacrifice',
     prose=u'Hebrews does not open like a letter. There is no author, no addressee, no greeting &mdash; it begins '
           u'with a sentence of formal Greek rhetoric about God having spoken in many ways through the prophets and '
           u'now speaking through a Son, and it ends, thirteen chapters later, with a note that reads like a '
           u'postscript stapled on. In between is a sermon, and its argument is comparative. The Son is better than '
           u'the angels; Moses was faithful in the house, but Jesus is the Son over it. The priesthood is better, '
           u'because it belongs to the order of Melchizedek, who appears for three verses in Genesis without '
           u'genealogy and is used here to argue for a priest whose qualification is not descent but an '
           u'indestructible life. The covenant is better, on the authority of Jeremiah, who said God would make a '
           u'new one. And the sacrifice is better, because the old one had to be repeated &mdash; the very '
           u'repetition being the proof that it never finished anything &mdash; while this one was made once. '
           u'Cutting across the argument are five warnings, sharp enough that the church spent centuries arguing '
           u'about them, urging readers not to drift, not to fall away, not to give up meeting together. Then '
           u'chapter eleven, the roll call of people who lived by faith without receiving what was promised, and '
           u'chapter twelve&rsquo;s image of that crowd as spectators in a stadium while the reader runs.',
     extra=note(u'Nobody knows who wrote it',
                u'The Greek is the most polished in the New Testament and the author is a superb rhetorician who '
                u'quotes the Old Testament in Greek throughout, which makes Paul unlikely; the writer also says the '
                u'message came &ldquo;to us&rdquo; from those who heard the Lord, which Paul would never say. '
                u'Suggestions have included Barnabas, Apollos, Luke, Clement and Priscilla. Origen, in the third '
                u'century, wrote that who actually composed it God alone knows.', hot=True),
     videos=vid('1fNWTZZwgbs', 'Hebrews', u'the comparative argument, and the five warnings inside it'),
     wiki='Epistle_to_the_Hebrews', guide='book-of-hebrews')

insert(B, before='james')
