# -*- coding: utf-8 -*-
"""Romans through Colossians."""
from _lettertpl import note, vid, insert

B = []


def book(**kw):
    B.append(kw)


book(id='romans', num='45', name='Romans',
     sub=u'Paul writes ahead to a church he has never met, and ends up setting out his whole gospel from first principles.',
     cap=u'<b>Events</b> none narrated &mdash; it is a letter, not a story<span class="sep">&middot;</span>'
         u'<b>Written</b> c. AD 57, from Corinth<span class="sep">&middot;</span>'
         u'Carried to Rome by Phoebe, a deacon of Cenchreae',
     genre=u'Epistle &middot; sustained argument',
     author=u'Paul, dictated to Tertius', ch=u'16',
     setting=u'Written in Corinth, addressed to Rome',
     theme=u'The righteousness of God, offered to everyone on the same terms',
     prose=u'Every other letter of Paul&rsquo;s answers a crisis in a church he planted. Romans answers nothing; '
           u'he is writing ahead to a congregation he has never visited, hoping to be sent on from there to Spain, '
           u'and so he lays out the whole argument from the ground up. The first three chapters work like a '
           u'prosecution: the pagan world stands condemned, the moral world stands condemned by the standard it '
           u'applies to others, and the Jewish world stands condemned by the law it was given &mdash; so that every '
           u'mouth is stopped. Then the turn, that God puts people right with himself as a gift, through Jesus, '
           u'received by trust rather than earned; Abraham is produced as the precedent, reckoned righteous before '
           u'he was circumcised. Chapters five to eight follow the consequences: released from condemnation, from '
           u'sin&rsquo;s ownership, from the law&rsquo;s accusation, and finally the great passage on the Spirit, on '
           u'creation groaning like a woman in labour, and on the impossibility of being separated from the love of '
           u'God. Chapters nine to eleven wrestle with the question that hurts him most &mdash; if the message is '
           u'true, why has his own people largely not accepted it &mdash; and he refuses every easy answer, ending '
           u'in a doxology rather than a solution. Only then does he turn to ordinary conduct: honest '
           u'self-assessment, hospitality, paying taxes, and the long argument about the strong and the weak in '
           u'which the person with the freer conscience is asked to yield to the person with the tighter one. The '
           u'last chapter is a list of names, twenty-six of them, a third of them women.',
     extra=note(u'The letter has a courier, and she has a name',
                u'Romans 16 opens by commending Phoebe, &ldquo;a deacon of the church at Cenchreae&rdquo; and a '
                u'<i>prostatis</i> &mdash; patron &mdash; of many, including Paul himself. Letters in the ancient '
                u'world were not posted; they were carried, and the carrier normally read the letter aloud and '
                u'answered questions about it. The first person ever to perform Romans, in all likelihood, was '
                u'Phoebe.'),
     videos=vid('ej_6dVdJSIU', 'Romans 1-4', u'chapters 1&ndash;4: the case that everyone is in the same position',
                head=u'Overview, part one') + u'\n' +
            vid('0SVTl4Xa5fY', 'Romans 5-16',
                u'chapters 5&ndash;16: new humanity, Israel&rsquo;s future, and life in the church',
                head=u'Overview, part two'),
     wiki='Epistle_to_the_Romans', guide='book-of-romans')

book(id='corinthians-1', num='46', name='1 Corinthians',
     sub=u'A brilliant, wealthy, quarrelling church gets a letter that answers its questions one at a time and refuses to flatter it once.',
     cap=u'<b>Events</b> none narrated &mdash; it is a letter, not a story<span class="sep">&middot;</span>'
         u'<b>Written</b> c. AD 55, from Ephesus<span class="sep">&middot;</span>'
         u'Answering both a report from Chloe&rsquo;s household and a letter from the church',
     genre=u'Epistle &middot; pastoral correspondence',
     author=u'Paul, with Sosthenes', ch=u'16',
     setting=u'Written in Ephesus to Corinth, a Roman colony and port',
     theme=u'A cross-shaped community in a status-obsessed city',
     prose=u'Corinth was a rebuilt Roman colony &mdash; rich, transient and obsessed with rank &mdash; and the church '
           u'had absorbed the city&rsquo;s instincts wholesale. Paul works through the damage item by item. They '
           u'have split into fan clubs behind rival teachers, so he argues that the message they were converted by '
           u'was deliberately unimpressive &mdash; a crucified man &mdash; and that admiring the messenger misses '
           u'the point. A man is sleeping with his stepmother and the congregation is proud of its '
           u'broad-mindedness. Believers are suing each other in front of pagan magistrates. Some are visiting '
           u'prostitutes on the theory that the body does not matter. From chapter seven the letter shifts to '
           u'answering their own written questions: about marriage and singleness, about meat that has been through '
           u'a temple, about head coverings, about the Lord&rsquo;s Supper, which they are eating in such a way that '
           u'the rich arrive early and eat well while the poor get nothing. Then the long treatment of spiritual '
           u'gifts, which insists that the body needs the parts it considers least presentable, and which is '
           u'interrupted at its centre by chapter thirteen &mdash; not a wedding reading in origin but the '
           u'argument&rsquo;s hinge, that gifts without love are noise. It closes with the resurrection: if Christ '
           u'was not raised the whole thing is a waste of a life, and if he was, then the body has a future and '
           u'nothing done for God is wasted.',
     extra=note(u'A conversation with half the tape missing',
                u'&ldquo;Now concerning the matters about which you wrote&rdquo; (7:1) marks the point where Paul '
                u'starts answering a letter we do not have. Several famously difficult verses read much better as '
                u'quotations of the Corinthians&rsquo; own slogans that he is about to qualify &mdash; &ldquo;all '
                u'things are lawful for me&rdquo;, &ldquo;food is meant for the stomach&rdquo;. Greek had no '
                u'quotation marks, so where the Corinthians stop speaking and Paul starts is an editorial '
                u'judgement, and translations disagree.'),
     videos=vid('yiHf8klCCc4', '1 Corinthians', u'the letter&rsquo;s structure, question by question'),
     wiki='First_Epistle_to_the_Corinthians', guide='book-of-1-corinthians')

book(id='corinthians-2', num='47', name='2 Corinthians',
     sub=u'The most personal thing Paul wrote: a defence of his own ministry by a man who keeps listing his failures as credentials.',
     cap=u'<b>Events</b> none narrated &mdash; it is a letter, not a story<span class="sep">&middot;</span>'
         u'<b>Written</b> c. AD 56, from Macedonia<span class="sep">&middot;</span>'
         u'After a painful visit and a severe letter, neither of which survives',
     genre=u'Epistle &middot; apologia', author=u'Paul, with Timothy', ch=u'13',
     setting=u'Written in Macedonia after meeting Titus with news from Corinth',
     theme=u'Strength that only shows up inside weakness',
     prose=u'Between the two Corinthian letters something went badly wrong. Paul made a visit he calls painful, '
           u'wrote a letter he wrote with many tears, and then waited in Troas and Macedonia for Titus to bring word '
           u'of how it had landed. Relief runs through the opening chapters: they have responded, and he can '
           u'breathe. But rival teachers have arrived in the meantime &mdash; impressive speakers with letters of '
           u'recommendation &mdash; and they have been undermining him: his speech is contemptible, he takes no '
           u'money, he keeps changing his travel plans, he does not look like a man God is backing. The letter is '
           u'his answer, and it is strange, because he refuses to compete on their terms. He describes the ministry '
           u'as treasure carried in clay pots, so that the obvious explanation for any power is not the pot. He '
           u'describes his own body as wasting away while something else is renewed. Chapters eight and nine turn '
           u'to the collection he is gathering for the poor in Jerusalem and make the most sustained case in the '
           u'New Testament for generosity. Then, in the last four chapters, he does what he calls playing the fool: '
           u'since they want credentials, he will list his &mdash; floggings, shipwreck, sleeplessness, hunger, a '
           u'night and a day adrift at sea, and the anxiety of every church pressing on him daily. He mentions '
           u'being caught up to the third heaven and immediately drops it, preferring to talk about a thorn in the '
           u'flesh that was not taken away, and about the answer he got instead: my grace is enough for you.',
     extra=note(u'Four letters, two of them lost',
                u'Paul refers in 1 Corinthians 5:9 to an earlier letter he had already sent, and in 2 Corinthians '
                u'2:4 to a later one written &ldquo;out of much affliction&rdquo;. Neither survives. Some scholars '
                u'read chapters 10&ndash;13, which change tone abruptly, as that severe letter later bound to the '
                u'end of this one; others hear the shift as a man who has finished being conciliatory and turned to '
                u'face the people undermining him.', hot=True),
     videos=vid('3lfPK2vfC54', '2 Corinthians', u'the argument for a ministry shaped like the cross'),
     wiki='Second_Epistle_to_the_Corinthians', guide='book-of-2-corinthians')

book(id='galatians', num='48', name='Galatians',
     sub=u'The angriest letter in the New Testament, written fast, and the one that later split Western Christianity in half.',
     cap=u'<b>Events</b> none narrated &mdash; it is a letter, not a story<span class="sep">&middot;</span>'
         u'<b>Written</b> c. AD 48&ndash;49, possibly the earliest of Paul&rsquo;s letters'
         u'<span class="sep">&middot;</span>On the traditional reading, just before the Jerusalem council of Acts 15',
     genre=u'Epistle &middot; polemic', author=u'Paul', ch=u'6',
     setting=u'To the churches of Galatia in central Asia Minor',
     theme=u'Whether gentile believers must become Jews first',
     prose=u'Paul begins every other letter by thanking God for his readers. Here he skips the thanksgiving entirely '
           u'and goes straight to astonishment: he cannot believe how quickly they are deserting the message. '
           u'Teachers have arrived in Galatia arguing that gentile converts must be circumcised and keep the law to '
           u'be full members of the people of God &mdash; a reasonable position, since the promises were made to '
           u'Abraham&rsquo;s family and circumcision was the sign of that family. Paul&rsquo;s answer runs at speed. '
           u'First his own history: he did not receive the gospel from the Jerusalem apostles, and when he did meet '
           u'them they added nothing, and when Peter came to Antioch and stopped eating with gentiles under '
           u'pressure Paul told him to his face that he was wrong. Then the argument from Abraham, who was declared '
           u'righteous by faith four hundred and thirty years before the law existed, so the law cannot be the '
           u'condition of the promise; the law was a guardian for a period of minority, and that period has ended. '
           u'He is not gentle about it &mdash; there is a line about the circumcision party that most translations '
           u'soften &mdash; but the letter is not merely negative. Its last two chapters describe what actually '
           u'holds a community together once the rulebook is not doing the work: freedom used to serve rather than '
           u'to indulge, gentleness towards someone caught out, carrying each other&rsquo;s burdens, and a list of '
           u'the fruit the Spirit grows, against which, he notes drily, there is no law.',
     extra=note(u'The letter that lit the Reformation',
                u'Luther lectured on Galatians in 1519 and again in 1531, called it &ldquo;my epistle, to which I am '
                u'betrothed&rdquo;, and built his doctrine of justification on it. Whether he read Paul&rsquo;s '
                u'opponents correctly &mdash; as legalists earning salvation, or as Jewish believers arguing about '
                u'how gentiles join a covenant people &mdash; has been the central question of Pauline scholarship '
                u'for the last fifty years.'),
     videos=vid('vmx4UjRFp0M', 'Galatians', u'the argument from Abraham, and what freedom is for'),
     wiki='Epistle_to_the_Galatians', guide='book-of-galatians')

book(id='ephesians', num='49', name='Ephesians',
     sub=u'A prison letter with no crisis to solve, written in enormous sentences about one new humanity made out of two old ones.',
     cap=u'<b>Events</b> none narrated &mdash; it is a letter, not a story<span class="sep">&middot;</span>'
         u'<b>Written</b> c. AD 60&ndash;62, from imprisonment<span class="sep">&middot;</span>'
         u'The oldest manuscripts do not contain the words &ldquo;in Ephesus&rdquo;',
     genre=u'Epistle &middot; circular', author=u'Paul, in prison', ch=u'6',
     setting=u'Written in custody, probably in Rome, to churches in Asia Minor',
     theme=u'The church as the place where the divided world is put back together',
     prose=u'Ephesians has no quarrel in it. Nobody is being corrected, no crisis is being managed, and the first '
           u'three chapters are a single sustained act of praise that includes, in the Greek, one sentence running '
           u'twelve verses. God&rsquo;s plan, Paul says, was always to gather everything in heaven and on earth into '
           u'one under Christ, and the church is where that gathering has started to show. Then the pivot the letter '
           u'is built on: you gentiles were outsiders, without hope and without God in the world, and Christ has '
           u'made the two groups one by demolishing the dividing wall of hostility &mdash; a phrase that would have '
           u'carried a physical charge for anyone who had seen the barrier in the Jerusalem temple beyond which no '
           u'gentile could pass on pain of death. The result is not a merger of one group into the other but one new '
           u'humanity in place of both. Chapters four to six work out what that costs in practice: speaking '
           u'truthfully because we are parts of each other, working in order to have something to give away, and '
           u'the household code, in which the startling line is the one addressed to husbands and to masters rather '
           u'than to wives and slaves. It closes with the armour of God, a picture assembled out of Isaiah, in which '
           u'the only offensive weapon is a word and the enemy is explicitly not the human being in front of you.',
     extra=note(u'A letter to nobody in particular',
                u'The phrase &ldquo;in Ephesus&rdquo; in 1:1 is missing from the earliest and best manuscripts, and '
                u'the letter contains no personal greetings at all &mdash; odd for a city where Paul spent three '
                u'years. The likeliest explanation is that it was a circular, carried around the province with the '
                u'address left blank and filled in as it went, which is also why it reads more like a sermon than a '
                u'piece of correspondence.'),
     videos=vid('Y71r-T98E2Q', 'Ephesians', u'one new humanity, and the household code'),
     wiki='Epistle_to_the_Ephesians', guide='book-of-ephesians')

book(id='philippians', num='50', name='Philippians',
     sub=u'A thank-you note from prison that turns into the earliest Christian hymn we possess.',
     cap=u'<b>Events</b> none narrated &mdash; it is a letter, not a story<span class="sep">&middot;</span>'
         u'<b>Written</b> c. AD 61&ndash;62, from imprisonment<span class="sep">&middot;</span>'
         u'To the first church Paul planted in Europe',
     genre=u'Epistle &middot; letter of friendship', author=u'Paul, with Timothy', ch=u'4',
     setting=u'Written in custody to Philippi, a Roman colony in Macedonia',
     theme=u'Joy that is not dependent on circumstances',
     prose=u'Philippi was a Roman colony full of retired soldiers, proud of its citizenship, and the church there had '
           u'sent Paul money more than once &mdash; the only church he let do it. This letter is partly a receipt '
           u'and partly a report on how he is: in custody, chained to a rotating guard, and pleased about it, '
           u'because the whole praetorium now knows why he is there. He genuinely cannot decide whether he would '
           u'rather live or die, and says so. Two women in the congregation, Euodia and Syntyche, have fallen out '
           u'badly enough for it to reach him, and the letter&rsquo;s central appeal is aimed at that. To make it, '
           u'he quotes what appears to be an existing hymn: that Christ, being in the form of God, did not treat '
           u'equality with God as something to exploit, but emptied himself, took the form of a slave, and became '
           u'obedient to the point of death &mdash; even death on a cross &mdash; and that God therefore exalted '
           u'him and gave him the name above every name. It is the highest thing said about Jesus anywhere in Paul, '
           u'and it is deployed to settle an argument between two church members. The rest follows from it. He '
           u'lists his own impeccable credentials and calls them refuse. He tells them to think about whatever is '
           u'true, honourable, just, pure, lovely. And he says he has learned to be content, which he presents as a '
           u'skill acquired rather than a temperament possessed.',
     extra=note(u'A hymn older than the letter quoting it',
                u'Philippians 2:6&ndash;11 has a rhythm and vocabulary unlike Paul&rsquo;s surrounding prose &mdash; '
                u'several words appear nowhere else in his writing &mdash; which is why most scholars read it as an '
                u'existing hymn he is citing rather than composing. If so, it is a window onto what Christians were '
                u'singing about Jesus within roughly two decades of his death.', hot=True),
     videos=vid('oE9qqW1-BkU', 'Philippians', u'the hymn at the centre, and the argument it settles'),
     wiki='Epistle_to_the_Philippians', guide='book-of-philippians')

book(id='colossians', num='51', name='Colossians',
     sub=u'Written to a town Paul had never visited, against a teaching we can only see through his answer to it.',
     cap=u'<b>Events</b> none narrated &mdash; it is a letter, not a story<span class="sep">&middot;</span>'
         u'<b>Written</b> c. AD 60&ndash;61, from imprisonment<span class="sep">&middot;</span>'
         u'Carried by Tychicus alongside Philemon, to the same town',
     genre=u'Epistle &middot; corrective', author=u'Paul, with Timothy', ch=u'4',
     setting=u'Written in custody to Colossae in the Lycus valley',
     theme=u'Christ as sufficient, with nothing needing to be added',
     prose=u'Paul had never been to Colossae; the church was planted by Epaphras, one of his converts, who has now '
           u'come to him with a problem. Something is being taught there that combines Jewish observance with '
           u'ascetic practice and some kind of angelic devotion &mdash; we cannot reconstruct it properly, because '
           u'we only have Paul&rsquo;s reply. What we can see is his strategy, which is not to refute the teaching '
           u'point by point but to make it look small. He answers with another hymn: Christ is the image of the '
           u'invisible God, the firstborn of all creation, in whom all things were created, things visible and '
           u'invisible, thrones and dominions and rulers and powers &mdash; the very categories the new teachers are '
           u'worried about, listed and placed under him. All the fullness of God was pleased to dwell in him. So the '
           u'festivals and food rules are a shadow, and the substance has arrived; and the ascetic regime, with its '
           u'do-not-handle and do-not-taste, has the appearance of wisdom but no power against self-indulgence at '
           u'all. What replaces it is not another regime but a change of clothes: strip off anger, malice, slander, '
           u'filthy language; put on compassion, kindness, humility, patience, and above all love, which binds '
           u'everything together. The closing greetings are unusually warm, and include a note to a man named '
           u'Archippus telling him to finish the job he was given.',
     extra=note(u'A shadow of the thing that casts it',
                u'Colossians 2:17 calls the sabbaths and food laws &ldquo;a shadow of what is to come, but the '
                u'substance belongs to Christ&rdquo;. The image is precise rather than dismissive: a shadow is '
                u'genuine evidence of a real body, correctly shaped and cast by the thing itself. Paul is not saying '
                u'the practices were false, but that they were the outline of someone who has since walked into the '
                u'room.'),
     videos=vid('pXTXlDxQsvc', 'Colossians', u'the hymn of chapter one, and what it makes unnecessary'),
     wiki='Epistle_to_the_Colossians', guide='book-of-colossians')

insert(B, before='james')
