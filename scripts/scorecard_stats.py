#!/usr/bin/env python3
"""Print the numbers docs/scorecard.md quotes, straight from data/.

    python3 scripts/scorecard_stats.py
"""
import csv, re, statistics, collections, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
bets = {r['bet_id']: r for r in csv.DictReader(open(ROOT/'data/bets.csv'))}
out = collections.defaultdict(dict)
for r in csv.DictReader(open(ROOT/'data/outcomes.csv')):
    out[r['bet_id']][r['question']] = r
RANK = {'astro2010': 2010, 'p5-2014': 2014}

def kv(s):
    d = {}
    for part in s.split(';'):
        i = part.find('=')
        if i >= 0: d[part[:i].strip()] = part[i+1:].strip()
    return d
def num(s):
    m = re.search(r'-?\d+(\.\d+)?', s or ''); return float(m.group()) if m else None
def year(s):
    if re.match(r'\s*(none|never|n/a)', s or '', re.I): return None
    m = re.search(r'(19|20)\d\d', s or ''); return int(m.group()) if m else None

print('== Q1 built ==')
for rep in ['astro2010', 'p5-2014', 'all']:
    c = collections.Counter(out[b]['built']['result'] for b in bets if rep == 'all' or bets[b]['source_report'] == rep)
    n = sum(c.values()); print(rep, n, dict(c))
pt = collections.Counter(out[b]['built']['pt_category'] or 'blank' for b in bets)
print('pt categories, all:', dict(pt))
for rep in ['astro2010', 'p5-2014']:
    print(' ', rep, dict(collections.Counter(out[b]['built']['pt_category'] or 'blank' for b in bets if bets[b]['source_report'] == rep)))

print('\n== Q2 cost ==')
cs = {b: out[b]['cost-schedule'] for b in bets if 'cost-schedule' in out[b]}
print('cost-schedule rows:', len(cs), dict(collections.Counter(r['result'] for r in cs.values())))
rat = []
for b, r in cs.items():
    k = kv(r['value'])
    if 'delivered' in k or 'recommended' in k: continue
    x = num(k.get('ratio'))
    if x is None: continue
    rat.append((b, x, r['result'], bets[b]['agency'], bets[b]['source_report']))
rat.sort(key=lambda t: -t[1])
for t in rat: print(f'  {t[0]:32} {t[1]:5.2f} {t[2]:9} {t[3]:9} {t[4]}')
fin = [t for t in rat if t[2] != 'building']
print('finished with ratio:', len(fin), 'over 1.15:', sum(1 for t in fin if t[1] > 1.15), 'median', statistics.median(t[1] for t in fin))
print('all with ratio:', len(rat), 'median', statistics.median(t[1] for t in rat))
for grp, f in [('P5 2014 DOE-baselined', lambda t: t[4] == 'p5-2014'), ('Astro2010 appraisals', lambda t: t[4] == 'astro2010')]:
    s = [t for t in rat if f(t)]
    print(f'  {grp}: n={len(s)} median={statistics.median(t[1] for t in s):.2f} over1.15={sum(1 for t in s if t[1]>1.15)} max={max(s,key=lambda t:t[1])}')
for ag in ['DOE', 'NASA', 'NSF']:
    s = [t for t in rat if ag in t[3].split('+')]
    print(f'  involves {ag}: n={len(s)} median={statistics.median(t[1] for t in s):.2f} over1.15={sum(1 for t in s if t[1]>1.15)}')
s = [t for t in rat if t[3] == 'DOE']
print(f'  DOE-only bets: n={len(s)} median={statistics.median(t[1] for t in s):.2f} over1.15={sum(1 for t in s if t[1]>1.15)}')

print('\n== Q2 schedule ==')
lag = []
for b, r in cs.items():
    k = kv(r['value'])
    if 'delivered' in k or 'recommended' in k: continue
    fd = k.get('first_data', '')
    y = year(fd)
    proj = bool(re.search(r'projected|planned|expected', fd[:45], re.I))
    tgt = k.get('target') or bets[b]['target_date']
    te = None
    ys = re.findall(r'(?:19|20)\d\d', re.sub(r'\(.*?\)', '', tgt or ''))
    if ys: te = int(ys[-1])
    lag.append((b, y, proj, RANK[bets[b]['source_report']], te, r['result']))
for t in lag: print(f'  {t[0]:32} first={t[1]} proj={t[2]} ranked={t[3]} target_end={t[4]} late={(t[1]-t[4]) if t[1] and t[4] else None} wait={(t[1]-t[3]) if t[1] else None} {t[5]}')
arr = [t for t in lag if t[1] and not t[2]]
w = sorted(t[1]-t[3] for t in arr)
print('arrived (not projected):', len(arr), 'wait years:', w, 'median', statistics.median(w))
built_yes = [t for t in arr if out[t[0]]['built']['result'] == 'yes']
w2 = sorted(t[1]-t[3] for t in built_yes)
print('arrived and built=yes:', len(built_yes), w2, 'median', statistics.median(w2))
lt = [t for t in arr if t[4]]
print('with target: ', len(lt), 'late:', sum(1 for t in lt if t[1] > t[4]), 'late years:', sorted(t[1]-t[4] for t in lt))
pj = [t for t in lag if t[1] and t[2]]
print('projected:', [(t[0], t[1], t[1]-t[3]) for t in pj])

print('\n== Q3 science ==')
for b in bets:
    if 'science' in out[b]: print(f"  {b:20} {out[b]['science']['result']:9} {out[b]['science']['confidence']}")
