import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
import collections
from plotly.subplots import make_subplots
from nltk.corpus import stopwords
import plotly.graph_objects as go

import numpy as np
np.random.seed(1)

raw_n_words = [
     'abhorrent', 'abjectabrupt', 'absurdabysmal', 'acerbic', 'acrimonious', 'adverse', 'aggressive', 'agonizing',
     'aimless', 'alarming', 'angry', 'annoying', 'appalling', 'arrogant', 'awful', 'awkward', 'bad', 'barbarous',
     'battered', 'biting', 'bizarre', 'blank', 'blasphemous', 'bloated', 'bloodthirsty', 'blue', 'blundering',
     'blurred', 'boastful', 'boorish', 'bored', 'boring', 'bossy', 'brainless', 'brash', 'brisk', 'broken', 'bruised',
     'brutal', 'bulky', 'bum', 'bumpy', 'bungling', 'caged', 'callous', 'cancelled', 'cancerous', 'cantankerous',
     'capricious', 'careless', 'catastrophic', 'chauvinistic', 'cheap', 'cheerless', 'choppy', 'clammy', 'clinical',
     'clogged', 'clownish', 'clueless', 'clumsy', 'cluttered', 'coarse', 'cocky', 'cold', 'coldhearted', 'colorless',
     'commercial', 'common', 'complacent', 'complaining', 'complicated', 'compulsive', 'compulsory', 'conceited',
     'conflicted', 'confounded', 'contemptuous', 'contradictory', 'controllable', 'controversial', 'costly', 'cowardly',
     'crabby', 'crafty', 'crass', 'crazy', 'criminal', 'critical', 'crooked', 'crowded', 'cruel', 'crumbly', 'crushed',
     'cursed', 'cynical', 'damaged', 'dangerous', 'dark', 'daunting', 'deadly', 'decayed', 'deceitful', 'deceivable',
     'decimated', 'declining', 'defeated', 'defective', 'defenseless', 'deficient', 'deformed', 'degenerative',
     'delinquent', 'deluded', 'demented', 'demonic', 'dependent', 'deplorable', 'depraved', 'depressed', 'depressing',
     'deprived', 'derogatory', 'desolate', 'despairing', 'despicable', 'despondent', 'destroyed', 'destructive',
     'detestable', 'detrimental', 'devastated', 'devious', 'diabolical', 'difficult', 'digressive', 'dilapidated',
     'dim', 'diminishing', 'diminutive', 'dingy', 'dire', 'dirty', 'disadvantaged', 'disadvantageous', 'disaffected',
     'disagreeable', 'disappearing', 'disappointed', 'disappointing', 'disastrous', 'discarded', 'disconnected',
     'discouraging', 'discourteous', 'disdainful', 'diseased', 'disgraceful', 'disgusting', 'disheartened', 'dishonest',
     'dishonorable', 'disillusioned', 'disingenuous', 'disjointed', 'dislikeable', 'disloyal', 'dismal', 'disobedient',
     'disorganized', 'displeasing', 'disreputable', 'disrespectful', 'disruptive', 'distraught', 'distressed',
     'doubtful', 'dramatic', 'dreaded', 'dreary', 'dull', 'duplicitous', 'eerie', 'egotistical', 'emaciated',
     'embittered', 'emotional', 'empty', 'envious', 'errant', 'erroneous', 'estranged', 'evil', 'exasperated',
     'excruciating', 'extraneous', 'faded', 'failed', 'fallacious', 'fatal', 'faulty', 'fearful', 'fearsome', 'feeble',
     'feigned', 'flawed', 'foolish', 'frayed', 'frightening', 'frivolous', 'furious', 'futile', 'fuzzy', 'gawky',
     'ghoulish', 'gnarly', 'goofy', 'grueling', 'gruesome', 'gruff', 'grumpy', 'hard', 'harmful', 'harsh', 'hated',
     'heartless', 'heavy', 'heinous', 'hideous', 'hopeless', 'horrible', 'horrid', 'horrifying', 'hostile', 'hurt',
     'icky', 'idiotic', 'ill', 'illogical', 'immature', 'immoral', 'imperfect', 'impersonal', 'impolite', 'impossible',
     'impractical', 'improper', 'imprudent', 'impure', 'inaccurate', 'inadmissible', 'inadvisable', 'inane',
     'inappropriate', 'inarticulate', 'incapable', 'incompatible', 'incomplete', 'inconceivable', 'inconvenient',
     'incorrect', 'inferior', 'insane', 'insipid', 'irksome', 'irrational', 'loathsome', 'lowly', 'manipulative',
     'messy', 'nasty', 'negligent', 'odd', 'parasitic', 'pathological', 'pessimistic', 'pitiful', 'poor', 'putrid',
     'redundant', 'repugnant', 'rotten', 'rubbish', 'rude', 'sickening', 'shoddy',
     'substandart', 'squalid', 'tasteless', 'terrible', 'toxic', 'upsetting', 'useless', 'unpleasant', 'wretched'
]

raw_p_words = [
     'acceptable', 'accomplished', 'ace', 'adept', 'admirable', 'adorable', 'adroit', 'affable',
     'agreeable', 'alluring', 'altruistic', 'amazing', 'amiable', 'amusing', 'angelical', 'appealing', 'approving',
     'attractive', 'awesome', 'beautiful', 'beneficent', 'benign', 'best', 'big', 'bighearted', 'blessed', 'blest',
     'bounteous', 'brill', 'brilliant', 'calming', 'captivating', 'charitable', 'charming', 'clean', 'clear', 'clever',
     'comfortable', 'commendable', 'committed', 'compassionate', 'compelling', 'congenial', 'considerate', 'convincing',
     'correct', 'creditable', 'cunning', 'cute', 'dainty', 'darling', 'dear', 'delicate', 'delightful', 'deluxe',
     'devoted', 'dishy', 'dutiful', 'ecstatic', 'ethical', 'elegant', 'enchanting', 'engaging', 'enjoyable', 'euphoric',
     'excellent', 'exceptional', 'exhilarating', 'expedient', 'fair', 'faithful', 'faultless', 'felicitous', 'fine',
     'rate', 'fit', 'flawless', 'fun', 'friendly', 'genial', 'gentle','glad', 'glossy', 'good', 'goodhearted',
     'goody', 'gorgeous', 'graceful', 'grateful', 'great', 'high', 'grade', 'quality', 'holy', 'honorable',
     'hospitable', 'hot', 'incredible', 'inculpable', 'indefectible', 'inoffensive', 'intact', 'kind', 'kindhearted',
     'likable', 'lovely', 'loyal', 'magic', 'magnanimous', 'marvelous', 'mild', 'moralistic', 'neat', 'nice', 'nifty',
     'normal', 'ok', 'perfect', 'pleasant', 'pleasing', 'praiseworthy', 'pretty', 'prime', 'prized', 'proficient',
     'profitable', 'pure', 'real', 'reliable', 'reputable', 'respected', 'safe', 'satisfactory', 'satisfying',
     'shipshape', 'skilled', 'smart', 'snazzy', 'solid', 'spanking', 'special', 'spotless', 'stable', 'standard',
     'stunning', 'sublime', 'super', 'supreme', 'sweet', 'swell', 'tasteful', 'thorough', 'tip', 'top', 'unblamable',
     'unspoiled', 'unswerving', 'valuable', 'weighty', 'well', 'wonderful', 'worthy', 'zingy'
]

stop = stopwords.words('english')
file = open('comments.txt')
text = file.read()
clean = [word for word in text.split() if word not in stop]

c = collections.Counter()
for word in clean:
    c[word] += 1

n_words_result = []
n_counts_result = []
p_words_result = []
p_counts_result = []

for key, val in c.items():
    for nw in raw_p_words:
        if nw == key:
            p_words_result.append(key)
            p_counts_result.append(val)

for key, val in c.items():
    for nw in raw_n_words:
        if nw == key:
            n_words_result.append(key)
            n_counts_result.append(val)

# df = pd.DataFrame({
#     "РЎР»РѕРІРѕ": n_words_result,
#     "Р§Р°СЃС‚РѕС‚Р°": n_counts_result
# })

fig = make_subplots(rows=2, cols=1, subplot_titles=('Plot 1', 'Plot 2'))
fig.add_histogram(x=n_words_result, y=n_counts_result, row=1, col=1)
fig.add_histogram(x=p_words_result, y=p_counts_result, row=2, col=1)
# fig = px.bar(df, x="РЎР»РѕРІРѕ", y="Р§Р°СЃС‚РѕС‚Р°", height=900)
fig.show()