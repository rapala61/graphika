import json
import math
import os
import pprint
import typing

from flashtext import KeywordProcessor
from time import perf_counter
from termcolor import colored

pp = pprint.PrettyPrinter(indent=2)
t_start = perf_counter()
script_dir = os.path.dirname(__file__)

# Run a binary search against a sorted list of nids that make up a group set
# in order to confirm membership
def is_in_group(nid: int, group: list) -> bool:
    found = False
    size = len(group)
    if size == 0: return found
    pivot_idx = 0 if size == 1 else math.floor(size / 2) - 1
    if nid == group[pivot_idx]:
        found = True
    elif size > 1:
        if nid > group[pivot_idx]:
            found = is_in_group(nid, group[pivot_idx+1:])
        else:
            found = is_in_group(nid, group[:pivot_idx])
    return found

# Returns a sorted list of all node ids in a group
def get_nids(f: typing.TextIO) -> list:
    # Using a set to prevent any duplicate nid
    nids=set()
    with f as nid_lines:
        for line in nid_lines:
            nid = line.strip()
            if nid:
                nids.add(int(nid))
    return sorted(nids)

# Returns keywords search tree 
def get_search_tree(f: typing.TextIO) -> KeywordProcessor:
    kw_tree = KeywordProcessor()
    with f as kw_lines:
        kw_tree.add_keywords_from_list([kw.strip() for kw in kw_lines])
    return kw_tree
        
# Outputs the matched terms to the message id that contains them
def output_results(nodes: dict) -> None:
    for key in nodes:
        kws = nodes[key].get('keywords')
        if len(kws):
            print(*kws)

# Read in terms1
kw_tree_1 = get_search_tree(open(os.path.join(script_dir, '../data/terms1.txt')))
# Read in terms2
kw_tree_2 = get_search_tree(open(os.path.join(script_dir, '../data/terms2.txt')))
# Read in nodes1
group_1_nids = get_nids(open(os.path.join(script_dir, '../data/nodes1.txt')))
# Read in nodes2
group_2_nids = get_nids(open(os.path.join(script_dir, '../data/nodes2.txt')))

# Memoize tweets to cut on searching time
nodes = {}
kw_trees = {1:kw_tree_1, 2:kw_tree_2}

# Read tweets
with open(os.path.join(script_dir, '../data/tweets.jsonl')) as tweets:
    for twt_str in tweets:
        twt = json.loads(twt_str)
        msg_id = twt.get('message_id')
        txt = twt.get('text')
        nid = int(twt.get('node_id'))
        in_mem_tw = nodes.get(nid)
        group = 0
        # If the tweet is in memory let's just append the messages.
        # No need re-check group membership
        if in_mem_tw:
            group = in_mem_tw.get('group')
        else:
            # Check if Twitter user is member of either group #1 or #2.
            # TODO: Refactor into declarative searching in all groups
            if is_in_group(nid, group_1_nids):
                group = 1
            elif is_in_group(nid, group_2_nids):
                group = 2
            # store messages 
            nodes[nid] = { 'group': group, 'keywords': []}
        kw_tree = kw_trees.get(group)
        if kw_tree:
            results = [(kw, msg_id) for kw in kw_tree.extract_keywords(txt)]
            for match in results:
                nodes[nid]['keywords'].append(match)
            
# pp.pprint([ (key, nodes[key]) for key in nodes if len(nodes[key].get('keywords'))])

output_results(nodes)

t_end = perf_counter()
t_total = (t_end-t_start)*1000
print(colored('Elapsed Time, ', 'green'), '{:.2f} ms'.format(t_total))
