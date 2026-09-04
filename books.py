# -*- coding: utf-8 -*-
"""The data: eras, books, divisions, and the few chip labels that contract.

Everything build_spine.py computes, it computes from this file. The prose
lives in index.html and nowhere else; this holds only what has a
coordinate or a count. Change a date here and rerun build_spine.py.

Years are signed: -1406 is 1406 BC, 30 is AD 30.
"""

# ---------------------------------------------------------------- eras
# (short name for locators, long name for the spine, date caption, width, from, to, knee)
#
# `knee` bends a band internally: (year, fraction) puts that year at that
# fraction of the band's width instead of where linear time would place it.
# Return & Second Temple runs 538-5 BC, but everything in it happens before
# 430 BC and the four centuries after are silence — so 430 BC sits at 70%,
# and the empty stretch is squeezed into the last 30%. Splitting it into two
# bands instead gave a 3%-wide band that could not carry a label.
ERAS = [
    ('Creation',    'Creation',              'before c. 2100 BC',  6, None,  -2100, None),
    ('Patriarchs',  'Patriarchs',            '2100&ndash;1876 BC', 7, -2100, -1876, None),
    ('Egypt',       'Egypt &amp; Exodus',    '1876&ndash;1406 BC', 9, -1876, -1406, None),
    ('Judges',      'Conquest &amp; Judges', '1406&ndash;1050 BC', 9, -1406, -1050, None),
    ('Monarchy',    'United Monarchy',       '1050&ndash;930 BC',  9, -1050, -930,  None),
    ('Divided',     'Divided Kingdom',       '930&ndash;586 BC',  12, -930,  -586,  None),
    ('Exile',       'Exile',                 '586&ndash;538 BC',   6, -586,  -538,  None),
    ('Return',      'Return &amp; Second Temple', '538&ndash;5 BC', 10, -538, -5,   (-430, 0.7)),
    ('Jesus',       'Life of Jesus',         '5 BC&ndash;AD 30',  12, -5,     30,   None),
    # Twenty-three books land in this band and seventeen of them inside a single
    # twenty-year stretch, so it takes two percent from the gospels' band and
    # bends the rest: AD 70 sits at 78%, which spreads the letters out and
    # squeezes the last thirty years, where only the Johannine writings remain.
    ('Apostolic',   'Apostolic Age',         'AD 30&ndash;100',   20, 30,    100,   (70, 0.78)),
]
assert sum(e[3] for e in ERAS) == 100, 'era widths must total 100'

# --------------------------------------------------------------- books
# id, canonical no., display name, division, family, events (from, to), written,
# flags: runs_off | prologue (a faded bar back to the left edge)

BOOKS = [
 ('genesis',      '01', 'Genesis',      1, 'torah',          (None, -1805), -1440, ''),
 ('exodus',       '02', 'Exodus',       1, 'torah',          (-1876, -1445), -1440, ''),
 ('leviticus',    '03', 'Leviticus',    1, 'torah',          (-1445, -1445), -1440, ''),
 ('numbers',      '04', 'Numbers',      1, 'torah',          (-1445, -1406), -1406, ''),
 ('deuteronomy',  '05', 'Deuteronomy',  1, 'torah',          (-1406, -1406), -1406, ''),
 ('joshua',       '06', 'Joshua',       2, 'historical',     (-1406, -1375), -1375, ''),
 ('judges',       '07', 'Judges',       2, 'historical',     (-1375, -1050), -1043, ''),
 ('ruth',         '08', 'Ruth',         2, 'historical',     (-1100, -1095), -1000, ''),
 ('samuel-1',     '09', '1 Samuel',     2, 'historical',     (-1105, -1010), -1000, ''),
 ('samuel-2',     '10', '2 Samuel',     2, 'historical',     (-1010, -970),  -960,  ''),
 ('kings-1',      '11', '1 Kings',      2, 'historical',     (-970,  -853),  -560,  ''),
 ('kings-2',      '12', '2 Kings',      2, 'historical',     (-853,  -586),  -560,  ''),
 ('chronicles-1', '13', '1 Chronicles', 2, 'historical',     (-1010, -970),  -430,  'prologue'),
 ('chronicles-2', '14', '2 Chronicles', 2, 'historical',     (-970,  -538),  -430,  ''),
 ('ezra',         '15', 'Ezra',         2, 'historical',     (-538,  -457),  -440,  ''),
 ('nehemiah',     '16', 'Nehemiah',     2, 'historical',     (-445,  -430),  -430,  ''),
 ('esther',       '17', 'Esther',       2, 'historical',     (-483,  -473),  -460,  ''),
 ('job',          '18', 'Job',          3, 'wisdom',         (-2000, -1950), -1400, ''),
 ('psalms',       '19', 'Psalms',       3, 'wisdom',         (-1440, -430),  -430,  ''),
 ('proverbs',     '20', 'Proverbs',     3, 'wisdom',         (-950,  -700),  -700,  ''),
 ('ecclesiastes', '21', 'Ecclesiastes', 3, 'wisdom',         (-940,  -935),  -935,  ''),
 ('song-of-songs','22', 'Song of Songs',3, 'wisdom',         (-970,  -965),  -965,  ''),
 ('isaiah',       '23', 'Isaiah',       3, 'prophets-major', (-740,  -681),  -681,  ''),
 ('jeremiah',     '24', 'Jeremiah',     3, 'prophets-major', (-627,  -580),  -580,  ''),
 ('lamentations', '25', 'Lamentations', 3, 'prophets-major', (-586,  -586),  -586,  ''),
 ('ezekiel',      '26', 'Ezekiel',      3, 'prophets-major', (-593,  -571),  -571,  ''),
 ('daniel',       '27', 'Daniel',       3, 'apocalyptic',    (-605,  -536),  -530,  ''),
 ('hosea',        '28', 'Hosea',        3, 'prophets-minor', (-755,  -715),  -715,  ''),
 ('joel',         '29', 'Joel',         3, 'prophets-minor', (-835,  -830),  -830,  ''),
 ('amos',         '30', 'Amos',         3, 'prophets-minor', (-760,  -750),  -750,  ''),
 ('obadiah',      '31', 'Obadiah',      3, 'prophets-minor', (-586,  -585),  -585,  ''),
 ('jonah',        '32', 'Jonah',        3, 'prophets-minor', (-780,  -778),  -760,  ''),
 ('micah',        '33', 'Micah',        3, 'prophets-minor', (-735,  -700),  -700,  ''),
 ('nahum',        '34', 'Nahum',        3, 'prophets-minor', (-663,  -640),  -640,  ''),
 ('habakkuk',     '35', 'Habakkuk',     3, 'prophets-minor', (-610,  -605),  -605,  ''),
 ('zephaniah',    '36', 'Zephaniah',    3, 'prophets-minor', (-640,  -630),  -630,  ''),
 ('haggai',       '37', 'Haggai',       3, 'prophets-minor', (-520,  -520),  -520,  ''),
 ('zechariah',    '38', 'Zechariah',    3, 'prophets-minor', (-520,  -480),  -480,  ''),
 ('malachi',      '39', 'Malachi',      3, 'prophets-minor', (-433,  -430),  -430,  ''),
 ('matthew',      '40', 'Matthew',      4, 'gospels',        (-5,     30),    60,   ''),
 ('mark',         '41', 'Mark',         4, 'gospels',        (27,     30),    55,   ''),
 ('luke',         '42', 'Luke',         4, 'gospels',        (-5,     30),    62,   ''),
 ('john',         '43', 'John',         4, 'gospels',        (27,     30),    90,   'prologue'),
 ('acts',         '44', 'Acts',         5, 'acts',           (30,     62),    62,   ''),
 ('romans',       '45', 'Romans',       5, 'epistles',       (57,     57),    57,   ''),
 ('corinthians-1','46', '1 Corinthians',5, 'epistles',       (55,     55),    55,   ''),
 ('corinthians-2','47', '2 Corinthians',5, 'epistles',       (56,     56),    56,   ''),
 ('galatians',    '48', 'Galatians',    5, 'epistles',       (48,     49),    48,   ''),
 ('ephesians',    '49', 'Ephesians',    5, 'epistles',       (60,     62),    60,   ''),
 ('philippians',  '50', 'Philippians',  5, 'epistles',       (61,     62),    61,   ''),
 # Colossians and Philemon went to the same town in the same hand, carried by
 # Tychicus and Onesimus together, so they share a span and split the lane
 ('colossians',   '51', 'Colossians',   5, 'epistles',       (60,     61),    60,   ''),
 ('thessalonians-1','52','1 Thessalonians',5,'epistles',     (50,     51),    50,   ''),
 ('thessalonians-2','53','2 Thessalonians',5,'epistles',     (51,     52),    51,   ''),
 ('timothy-1',    '54', '1 Timothy',    5, 'epistles',       (63,     64),    63,   ''),
 ('timothy-2',    '55', '2 Timothy',    5, 'epistles',       (66,     67),    66,   ''),
 ('titus',        '56', 'Titus',        5, 'epistles',       (63,     64),    63,   ''),
 ('philemon',     '57', 'Philemon',     5, 'epistles',       (60,     61),    60,   ''),
 ('hebrews',      '58', 'Hebrews',      5, 'epistles',       (65,     68),    65,   ''),
 ('james',        '59', 'James',        5, 'epistles',       (45,     46),    45,   ''),
 ('peter-1',      '60', '1 Peter',      5, 'epistles',       (62,     64),    62,   ''),
 # 2 Peter and Jude share most of a chapter of material as well as a decade
 ('peter-2',      '61', '2 Peter',      5, 'epistles',       (65,     67),    65,   ''),
 ('john-1',       '62', '1 John',       5, 'epistles',       (85,     95),    90,   ''),
 ('john-2',       '63', '2 John',       5, 'epistles',       (90,     95),    90,   ''),
 ('john-3',       '64', '3 John',       5, 'epistles',       (90,     95),    90,   ''),
 ('jude',         '65', 'Jude',         5, 'epistles',       (65,     67),    65,   ''),
 ('revelation',   '66', 'Revelation',   5, 'apocalyptic',    (95,    100),    95,   'runs_off'),
]

DIVISIONS = {1: ('Pentateuch', 5), 2: ('Historical Books', 12),
             3: ('Writings and Prophets', 22), 4: ('Gospels', 4),
             5: ('Acts, Letters and Revelation', 23)}

# Chip labels only. Acts, Letters and Revelation is twenty-three books and
# wrapped to three rows, which took the floating header to ~220px and left
# almost no clearance above an anchored title. Contracting the six longest
# names buys back a row. Everywhere else -- section headings, spine tooltips,
# the table of contents -- keeps the full name, and the chip carries it as an
# aria-label so nothing is lost to a screen reader.
SHORT = {
    'corinthians-1':   '1 Cor.',
    'corinthians-2':   '2 Cor.',
    'thessalonians-1': '1 Thess.',
    'thessalonians-2': '2 Thess.',
    'timothy-1':       '1 Tim.',
    'timothy-2':       '2 Tim.',
}

# ---------------------------------------------------------- reads with
# Which books belong side by side, and why, in a phrase that reads the same
# from either end. Every edge is rendered under both books' spec blocks.
# Every book appears at least once; verify.py checks both properties.
PAIRS = [
    ('genesis',      'exodus',        'ends with Joseph&rsquo;s coffin; Exodus carries it out'),
    ('exodus',       'deuteronomy',   'the law given, then the law retold forty years on'),
    ('exodus',       'numbers',       'the tabernacle built, then carried'),
    ('leviticus',    'hebrews',       'the sacrificial system, and the letter that reads it as a sketch'),
    ('deuteronomy',  'joshua',        'the speech on the plains, then the crossing'),
    ('judges',       'ruth',          'the same lawless decades, one household wide'),
    ('samuel-1',     'samuel-2',      'one scroll, cut in two by its Greek translators'),
    ('samuel-1',     'psalms',        'the headings that point back to the cave and the flight'),
    ('samuel-2',     'chronicles-1',  'David&rsquo;s reign told twice, once with the failures and once without'),
    ('kings-1',      'kings-2',       'one scroll, cut in two by its Greek translators'),
    ('kings-1',      'chronicles-2',  'Solomon and the kings of Judah, from a priest&rsquo;s side of the aisle'),
    ('kings-2',      'chronicles-2',  'the same kings to the same end, from a priest&rsquo;s side of the aisle'),
    ('kings-2',      'isaiah',        'Hezekiah&rsquo;s crisis, 2 Kings 18&ndash;20 and Isaiah 36&ndash;39, nearly word for word'),
    ('kings-2',      'jeremiah',      'the last kings of Judah from outside the city and from inside it'),
    ('chronicles-1', 'chronicles-2',  'one scroll, cut in two by its Greek translators'),
    ('ezra',         'nehemiah',      'one book in the Hebrew Bible; the return, in two waves'),
    ('ezra',         'haggai',        'the prophet who got the temple built in Ezra 5&ndash;6'),
    ('ezra',         'zechariah',     'the prophet who got the temple built in Ezra 5&ndash;6'),
    ('ezra',         'esther',        'Esther falls in the gap between Ezra 6 and Ezra 7'),
    ('nehemiah',     'malachi',       'the same abuses, found on Nehemiah&rsquo;s second visit'),
    ('job',          'proverbs',      'what happens when the rules of Proverbs stop holding'),
    ('proverbs',     'ecclesiastes',  'wisdom, and the case against it'),
    ('ecclesiastes', 'song-of-songs', 'the two Solomon books the rabbis argued over keeping'),
    ('isaiah',       'micah',         'contemporaries; Isaiah 2 and Micah 4 share a passage'),
    ('jeremiah',     'lamentations',  'the fall Jeremiah foretold, wept over'),
    ('jeremiah',     'obadiah',       'a dozen verses on Edom in common, Jeremiah 49 and Obadiah'),
    ('ezekiel',      'daniel',        'the exile from Babylon, from the canal and from the palace'),
    ('ezekiel',      'revelation',    'the throne, the scroll, the measured city &mdash; Revelation&rsquo;s furniture'),
    ('daniel',       'revelation',    'the visions Revelation reuses'),
    ('hosea',        'amos',          'the northern kingdom in its last good years, from two directions'),
    ('joel',         'acts',          'the passage Peter quoted at Pentecost'),
    ('jonah',        'nahum',         'Nineveh spared, then Nineveh finished'),
    ('habakkuk',     'romans',        'the righteous shall live by faith &mdash; Paul&rsquo;s text, and where he found it'),
    ('zephaniah',    'kings-2',       'Josiah&rsquo;s reform, and the prophet preaching just before it'),
    ('haggai',       'zechariah',     'the same two months in 520 BC'),
    ('matthew',      'mark',          'nine tenths of Mark is in Matthew'),
    ('mark',         'luke',          'half of Mark is in Luke'),
    ('matthew',      'luke',          'the sayings the two share that Mark does not have'),
    ('john',         'john-1',        'the same voice and the same vocabulary, in a letter'),
    ('luke',         'acts',          'volume two: same author, same addressee, same first sentence'),
    ('acts',         'galatians',     'Acts 15 and Galatians 2: the same meeting, from two chairs'),
    ('acts',         'philippians',   'the jail in Acts 16, and the church that came out of it'),
    ('romans',       'galatians',     'the same argument, once in a hurry and once at leisure'),
    ('romans',       'james',         'faith and works: two answers to two different questions'),
    ('corinthians-1', 'corinthians-2', 'a painful visit and a lost letter between them'),
    ('ephesians',    'colossians',    'twin letters; a third of Ephesians is in Colossians'),
    ('colossians',   'philemon',      'carried in the same bag to the same town'),
    ('thessalonians-1', 'thessalonians-2', 'the second corrects what the first was taken to mean'),
    ('timothy-1',    'titus',         'the same instructions for two men in two places'),
    ('timothy-1',    'timothy-2',     'the first is a handover; the second is a farewell'),
    ('peter-1',      'peter-2',       'the same name, a very different letter'),
    ('peter-2',      'jude',          'share most of a chapter'),
    ('john-1',       'john-2',        'the same hand, one sheet'),
    ('john-2',       'john-3',        'the same hand, one sheet each'),
]

# ------------------------------------------------------------ read it
# USFM book codes, as bible.com uses them: https://www.bible.com/bible/59/GEN.1.ESV
# is Genesis 1 in the ESV (version 59). The same https link is a universal
# link, so on a phone with the YouVersion app installed it opens there.
USFM = {
    'genesis': 'GEN', 'exodus': 'EXO', 'leviticus': 'LEV', 'numbers': 'NUM', 'deuteronomy': 'DEU',
    'joshua': 'JOS', 'judges': 'JDG', 'ruth': 'RUT', 'samuel-1': '1SA', 'samuel-2': '2SA',
    'kings-1': '1KI', 'kings-2': '2KI', 'chronicles-1': '1CH', 'chronicles-2': '2CH',
    'ezra': 'EZR', 'nehemiah': 'NEH', 'esther': 'EST', 'job': 'JOB', 'psalms': 'PSA',
    'proverbs': 'PRO', 'ecclesiastes': 'ECC', 'song-of-songs': 'SNG', 'isaiah': 'ISA',
    'jeremiah': 'JER', 'lamentations': 'LAM', 'ezekiel': 'EZK', 'daniel': 'DAN', 'hosea': 'HOS',
    'joel': 'JOL', 'amos': 'AMO', 'obadiah': 'OBA', 'jonah': 'JON', 'micah': 'MIC', 'nahum': 'NAM',
    'habakkuk': 'HAB', 'zephaniah': 'ZEP', 'haggai': 'HAG', 'zechariah': 'ZEC', 'malachi': 'MAL',
    'matthew': 'MAT', 'mark': 'MRK', 'luke': 'LUK', 'john': 'JHN', 'acts': 'ACT', 'romans': 'ROM',
    'corinthians-1': '1CO', 'corinthians-2': '2CO', 'galatians': 'GAL', 'ephesians': 'EPH',
    'philippians': 'PHP', 'colossians': 'COL', 'thessalonians-1': '1TH', 'thessalonians-2': '2TH',
    'timothy-1': '1TI', 'timothy-2': '2TI', 'titus': 'TIT', 'philemon': 'PHM', 'hebrews': 'HEB',
    'james': 'JAS', 'peter-1': '1PE', 'peter-2': '2PE', 'john-1': '1JN', 'john-2': '2JN',
    'john-3': '3JN', 'jude': 'JUD', 'revelation': 'REV',
}
ESV = 59
