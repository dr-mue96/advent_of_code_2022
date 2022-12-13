import pandas as pd
data = pd.read_csv('input.csv', sep=' ', header=None, names=['opponent', 'me'])

def calc_score1(o, m):
    scores = []   
    for opp, me in zip(o,m):
        score = 0
        if me == 'X':
            score += 1
            if opp == 'A':
                score += 3
            elif opp == 'C':
                score += 6
        elif me == 'Y':
            score += 2
            if opp == 'B':
                score += 3
            elif opp == 'A':
                score += 6
        elif me == 'Z':
            score += 3
            if opp == 'B':
                score += 6
            elif opp == 'C':
                score += 3
        scores.append(score)            
    return scores

data['score1'] = calc_score1(data['opponent'], data['me'])
print('Total Score if second column is shape:', data['score1'].sum())

def calc_score2(o, r):
    scores = []   
    for opp, res in zip(o,r):           
        score = 0
        if res == 'X':
            if opp == 'A':
                score += 3
            elif opp == 'B':
                score += 1
            elif opp == 'C':
                score += 2
        elif res == 'Y':
            score += 3
            if opp == 'A':
                score += 1
            elif opp == 'B':
                score += 2
            elif opp == 'C':
                score += 3
        elif res == 'Z':
            score += 6
            if opp == 'A':
                score += 2
            elif opp == 'B':
                score += 3
            elif opp == 'C':
                score += 1
        scores.append(score)            
    return scores

data['score2'] = calc_score2(data['opponent'], data['me'])
print('Total Score if second column is outcome:', data['score2'].sum())