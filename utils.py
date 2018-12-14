import random


def test_seq_rep(l):
    for i in range(len(l) - 2):
        j = i+2
        if l[i:i+2] == l[j:j+2]:
            return True
    return False


def label():
    fo = open('char-rnn.pytorch/sampler_ab2.txt')
    wf = open('label_sample_ab.txt', 'w')
    r = 0
    i = 0
    dr = 0
    for line in fo:
        line = line.strip()
        new_line = line
        if len(list(line)) != len(set(line)):
            new_line += '\tRepeated'
            r += 1
        if test_seq_rep(list(line)):
            dr += 1
            new_line += '\tDoubleRepeated'
        wf.write(new_line + '\n')
        i+=1
    print(r/i)
    print(dr/i)


def generate_ab():
    wf = open('ab.txt', 'w')
    for i in range(10000):
        c = random.choice(['a b', 'b a'])
        wf.write(c + '\n')
    wf.close()


# generate_ab()
label()