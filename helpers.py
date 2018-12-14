# https://github.com/spro/char-rnn.pytorch

import unidecode
import string
import random
import time
import math
import torch

# Reading and un-unicode-encoding data
all_characters = 'ab#'
n_characters = len(all_characters)

def read_file(filename):
    # file = unidecode.unidecode(open(filename).read().split())
    file = open(filename).read().split()
    return file, len(file)

# Turning a string into a tensor

def char_tensor(string):
    tensor = torch.zeros(len(string)).long()
    for c in range(len(string)):
        try:
            tensor[c] = all_characters.index(string[c])
        except:
            continue
    return tensor

# Readable time elapsed

def time_since(since):
    s = time.time() - since
    m = math.floor(s / 60)
    s -= m * 60
    return '%dm %ds' % (m, s)
# Reading and un-unicode-encoding data

# all_characters = string.ascii_lowercase + '#' + '^'
def get_total_data(f, num):
    fo = open(f)
    data = []
    for line in fo:
        line = line.strip()
        seq = line.split(' ')[:num]
        seq.extend('#')
        data.append(seq)
    return data
