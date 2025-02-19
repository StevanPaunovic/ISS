import re
from collections import Counter

# Dieses Programm zählt die Vorkommnis einer Klasse aus einer Ergebnisdatei und gibt die Top10-Aktivitäten zurück.

def zähle_aktivitäten(text, activity_dict):
    # Extrahiere nur die Klassennamen (Werte) aus dem Dictionary und speichere sie als Set für schnelleren Zugriff
    activities = {v.lower().strip() for v in activity_dict.values()}

    # Regulärer Ausdruck für vorhergesagte Klassen und Top-5-Klassen
    alle_klassen = re.findall(r"Vorhergesagte Klasse:\s*([\w\s]+)\s*\(Label-ID", text)
    top5_klassen = re.findall(r"([\w\s]+): \d+\.\d+", text)

    # Liste aller erkannten Aktivitäten (Normalisierung)
    erkannte_klassen = [k.strip().lower() for k in alle_klassen + top5_klassen]

    # Zähle nur die Aktivitäten, die in activity_dict definiert sind
    counter = Counter(k for k in erkannte_klassen if k in activities)

    return counter.most_common(10)  # Top 10 zurückgeben

# Beispiel-Dictionary mit numerischen Keys und Klassennamen als Werte
activity_dict = {
    0: "abseiling",
    1: "air drumming",
    2: "answering questions",
    3: "applauding",
    4: "applying cream",
    5: "archery",
    6: "arm wrestling",
    7: "arranging flowers",
    8: "assembling computer",
    9: "auctioning",
    10: "baby waking up",
    11: "baking cookies",
    12: "balloon blowing",
    13: "bandaging",
    14: "barbequing",
    15: "bartending",
    16: "beatboxing",
    17: "bee keeping",
    18: "belly dancing",
    19: "bench pressing",
    20: "bending back",
    21: "bending metal",
    22: "biking through snow",
    23: "blasting sand",
    24: "blowing glass",
    25: "blowing leaves",
    26: "blowing nose",
    27: "blowing out candles",
    28: "bobsledding",
    29: "bookbinding",
    30: "bouncing on trampoline",
    31: "bowling",
    32: "braiding hair",
    33: "breading or breadcrumbing",
    34: "breakdancing",
    35: "brush painting",
    36: "brushing hair",
    37: "brushing teeth",
    38: "building cabinet",
    39: "building shed",
    40: "bungee jumping",
    41: "busking",
    42: "canoeing or kayaking",
    43: "capoeira",
    44: "carrying baby",
    45: "cartwheeling",
    46: "carving pumpkin",
    47: "catching fish",
    48: "catching or throwing baseball",
    49: "catching or throwing frisbee",
    50: "catching or throwing softball",
    51: "celebrating",
    52: "changing oil",
    53: "changing wheel",
    54: "checking tires",
    55: "cheerleading",
    56: "chopping wood",
    57: "clapping",
    58: "clay pottery making",
    59: "clean and jerk",
    60: "cleaning floor",
    61: "cleaning gutters",
    62: "cleaning pool",
    63: "cleaning shoes",
    64: "cleaning toilet",
    65: "cleaning windows",
    66: "climbing a rope",
    67: "climbing ladder",
    68: "climbing tree",
    69: "contact juggling",
    70: "cooking chicken",
    71: "cooking egg",
    72: "cooking on campfire",
    73: "cooking sausages",
    74: "counting money",
    75: "country line dancing",
    76: "cracking neck",
    77: "crawling baby",
    78: "crossing river",
    79: "crying",
    80: "curling hair",
    81: "cutting nails",
    82: "cutting pineapple",
    83: "cutting watermelon",
    84: "dancing ballet",
    85: "dancing charleston",
    86: "dancing gangnam style",
    87: "dancing macarena",
    88: "deadlifting",
    89: "decorating the christmas tree",
    90: "digging",
    91: "dining",
    92: "disc golfing",
    93: "diving cliff",
    94: "dodgeball",
    95: "doing aerobics",
    96: "doing laundry",
    97: "doing nails",
    98: "drawing",
    99: "dribbling basketball",
    100: "drinking",
    101: "drinking beer",
    102: "drinking shots",
    103: "driving car",
    104: "driving tractor",
    105: "drop kicking",
    106: "drumming fingers",
    107: "dunking basketball",
    108: "dying hair",
    109: "eating burger",
    110: "eating cake",
    111: "eating carrots",
    112: "eating chips",
    113: "eating doughnuts",
    114: "eating hotdog",
    115: "eating ice cream",
    116: "eating spaghetti",
    117: "eating watermelon",
    118: "egg hunting",
    119: "exercising arm",
    120: "exercising with an exercise ball",
    121: "extinguishing fire",
    122: "faceplanting",
    123: "feeding birds",
    124: "feeding fish",
    125: "feeding goats",
    126: "filling eyebrows",
    127: "finger snapping",
    128: "fixing hair",
    129: "flipping pancake",
    130: "flying kite",
    131: "folding clothes",
    132: "folding napkins",
    133: "folding paper",
    134: "front raises",
    135: "frying vegetables",
    136: "garbage collecting",
    137: "gargling",
    138: "getting a haircut",
    139: "getting a tattoo",
    140: "giving or receiving award",
    141: "golf chipping",
    142: "golf driving",
    143: "golf putting",
    144: "grinding meat",
    145: "grooming dog",
    146: "grooming horse",
    147: "gymnastics tumbling",
    148: "hammer throw",
    149: "headbanging",
    150: "headbutting",
    151: "high jump",
    152: "high kick",
    153: "hitting baseball",
    154: "hockey stop",
    155: "holding snake",
    156: "hopscotch",
    157: "hoverboarding",
    158: "hugging",
    159: "hula hooping",
    160: "hurdling",
    161: "hurling (sport)",
    162: "ice climbing",
    163: "ice fishing",
    164: "ice skating",
    165: "ironing",
    166: "javelin throw",
    167: "jetskiing",
    168: "jogging",
    169: "juggling balls",
    170: "juggling fire",
    171: "juggling soccer ball",
    172: "jumping into pool",
    173: "jumpstyle dancing",
    174: "kicking field goal",
    175: "kicking soccer ball",
    176: "kissing",
    177: "kitesurfing",
    178: "knitting",
    179: "krumping",
    180: "laughing",
    181: "laying bricks",
    182: "long jump",
    183: "lunge",
    184: "making a cake",
    185: "making a sandwich",
    186: "making bed",
    187: "making jewelry",
    188: "making pizza",
    189: "making snowman",
    190: "making sushi",
    191: "making tea",
    192: "marching",
    193: "massaging back",
    194: "massaging feet",
    195: "massaging legs",
    196: "massaging person's head",
    197: "milking cow",
    198: "mopping floor",
    199: "motorcycling",
    200: "moving furniture",
    201: "mowing lawn",
    202: "news anchoring",
    203: "opening bottle",
    204: "opening present",
    205: "paragliding",
    206: "parasailing",
    207: "parkour",
    208: "passing American football (in game)",
    209: "passing American football (not in game)",
    210: "peeling apples",
    211: "peeling potatoes",
    212: "petting animal (not cat)",
    213: "petting cat",
    214: "picking fruit",
    215: "planting trees",
    216: "plastering",
    217: "playing accordion",
    218: "playing badminton",
    219: "playing bagpipes",
    220: "playing basketball",
    221: "playing bass guitar",
    222: "playing cards",
    223: "playing cello",
    224: "playing chess",
    225: "playing clarinet",
    226: "playing controller",
    227: "playing cricket",
    228: "playing cymbals",
    229: "playing didgeridoo",
    230: "playing drums",
    231: "playing flute",
    232: "playing guitar",
    233: "playing harmonica",
    234: "playing harp",
    235: "playing ice hockey",
    236: "playing keyboard",
    237: "playing kickball",
    238: "playing monopoly",
    239: "playing organ",
    240: "playing paintball",
    241: "playing piano",
    242: "playing poker",
    243: "playing recorder",
    244: "playing saxophone",
    245: "playing squash or racquetball",
    246: "playing tennis",
    247: "playing trombone",
    248: "playing trumpet",
    249: "playing ukulele",
    250: "playing violin",
    251: "playing volleyball",
    252: "playing xylophone",
    253: "pole vault",
    254: "presenting weather forecast",
    255: "pull ups",
    256: "pumping fist",
    257: "pumping gas",
    258: "punching bag",
    259: "punching person (boxing)",
    260: "push up",
    261: "pushing car",
    262: "pushing cart",
    263: "pushing wheelchair",
    264: "reading book",
    265: "reading newspaper",
    266: "recording music",
    267: "riding a bike",
    268: "riding camel",
    269: "riding elephant",
    270: "riding mechanical bull",
    271: "riding mountain bike",
    272: "riding mule",
    273: "riding or walking with horse",
    274: "riding scooter",
    275: "riding unicycle",
    276: "ripping paper",
    277: "robot dancing",
    278: "rock climbing",
    279: "rock scissors paper",
    280: "roller skating",
    281: "running on treadmill",
    282: "sailing",
    283: "salsa dancing",
    284: "sanding floor",
    285: "scrambling eggs",
    286: "scuba diving",
    287: "setting table",
    288: "shaking hands",
    289: "shaking head",
    290: "sharpening knives",
    291: "sharpening pencil",
    292: "shaving head",
    293: "shaving legs",
    294: "shearing sheep",
    295: "shining shoes",
    296: "shooting basketball",
    297: "shooting goal (soccer)",
    298: "shot put",
    299: "shoveling snow",
    300: "shredding paper",
    301: "shuffling cards",
    302: "side kick",
    303: "sign language interpreting",
    304: "singing",
    305: "situp",
    306: "skateboarding",
    307: "ski jumping",
    308: "skiing (not slalom or crosscountry)",
    309: "skiing crosscountry",
    310: "skiing slalom",
    311: "skipping rope",
    312: "skydiving",
    313: "slacklining",
    314: "slapping",
    315: "sled dog racing",
    316: "smoking",
    317: "smoking hookah",
    318: "snatch weight lifting",
    319: "sneezing",
    320: "sniffing",
    321: "snorkeling",
    322: "snowboarding",
    323: "snowkiting",
    324: "snowmobiling",
    325: "somersaulting",
    326: "spinning poi",
    327: "spray painting",
    328: "spraying",
    329: "springboard diving",
    330: "squat",
    331: "sticking tongue out",
    332: "stomping grapes",
    333: "stretching arm",
    334: "stretching leg",
    335: "strumming guitar",
    336: "surfing crowd",
    337: "surfing water",
    338: "sweeping floor",
    339: "swimming backstroke",
    340: "swimming breast stroke",
    341: "swimming butterfly stroke",
    342: "swing dancing",
    343: "swinging legs",
    344: "swinging on something",
    345: "sword fighting",
    346: "tai chi",
    347: "taking a shower",
    348: "tango dancing",
    349: "tap dancing",
    350: "tapping guitar",
    351: "tapping pen",
    352: "tasting beer",
    353: "tasting food",
    354: "testifying",
    355: "texting",
    356: "throwing axe",
    357: "throwing ball",
    358: "throwing discus",
    359: "tickling",
    360: "tobogganing",
    361: "tossing coin",
    362: "tossing salad",
    363: "training dog",
    364: "trapezing",
    365: "trimming or shaving beard",
    366: "trimming trees",
    367: "triple jump",
    368: "tying bow tie",
    369: "tying knot (not on a tie)",
    370: "tying tie",
    371: "unboxing",
    372: "unloading truck",
    373: "using computer",
    374: "using remote controller (not gaming)",
    375: "using segway",
    376: "vault",
    377: "waiting in line",
    378: "walking the dog",
    379: "washing dishes",
    380: "washing feet",
    381: "washing hair",
    382: "washing hands",
    383: "water skiing",
    384: "water sliding",
    385: "watering plants",
    386: "waxing back",
    387: "waxing chest",
    388: "waxing eyebrows",
    389: "waxing legs",
    390: "weaving basket",
    391: "welding",
    392: "whistling",
    393: "windsurfing",
    394: "wrapping present",
    395: "wrestling",
    396: "writing",
    397: "yawning",
    398: "yoga",
    399: "zumba",
}

# Beispielaufruf mit deinem Text
text = """Top 5 Klassen mit Wahrscheinlichkeiten:
punching person (boxing): 0.3875
slapping: 0.1062
shaking hands: 0.0669
rock scissors paper: 0.0246
hugging: 0.0187



Top 5 Klassen mit Wahrscheinlichkeiten:
punching person (boxing): 0.2305
slapping: 0.0967
texting: 0.0718
rock scissors paper: 0.0517
shaking hands: 0.0387




Top 5 Klassen mit Wahrscheinlichkeiten:
slapping: 0.4074
texting: 0.1276
hugging: 0.0406
jogging: 0.0380
shaking hands: 0.0293



Top 5 Klassen mit Wahrscheinlichkeiten:
shaking hands: 0.6140
rock scissors paper: 0.0094
dancing charleston: 0.0040
hammer throw: 0.0038
slapping: 0.0034




Top 5 Klassen mit Wahrscheinlichkeiten:
side kick: 0.5375
high kick: 0.0734
swinging legs: 0.0570
stretching leg: 0.0150
drop kicking: 0.0113




Top 5 Klassen mit Wahrscheinlichkeiten:
high kick: 0.4740
side kick: 0.0890
swinging legs: 0.0277
drop kicking: 0.0245
stretching leg: 0.0141



Top 5 Klassen mit Wahrscheinlichkeiten:
tango dancing: 0.2687
kissing: 0.1798
hugging: 0.0584
tai chi: 0.0188
dancing charleston: 0.0148



Top 5 Klassen mit Wahrscheinlichkeiten:
hugging: 0.2525
kissing: 0.1801
tango dancing: 0.0435
headbutting: 0.0242
tai chi: 0.0233



Top 5 Klassen mit Wahrscheinlichkeiten:
slapping: 0.4804
hugging: 0.0762
shaking hands: 0.0611
jumpstyle dancing: 0.0275
kissing: 0.0253




Top 5 Klassen mit Wahrscheinlichkeiten:
slapping: 0.5192
punching person (boxing): 0.0673
hugging: 0.0369
jumpstyle dancing: 0.0288
shaking hands: 0.0202
"""
top10_ergebnisse = zähle_aktivitäten(text, activity_dict)

# Ergebnisse ausgeben
print("\nTop 10 Aktivitäten:")
for i, (klasse, anzahl) in enumerate(top10_ergebnisse, 1):
    print(f"{i}. {klasse}: {anzahl} Vorkommen")
