#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

def team_topics(mem1, mem2):
    #return sum(1 if mem1[i]=='1' or mem2[i]=='1' else 0 for i in range(len(mem1)))
    return bin(int(mem1,2) | int(mem2,2)).count("1")

def determine_ncombos(ntopics, topic_count_members):
    ncombos = 0
    for smaller_topic_count in set.intersection(set(range(1, ntopics)), set(topic_count_members.keys())):
        smaller_members = topic_count_members.get(smaller_topic_count, [])
        if smaller_members:
            #print("smaller_topic_count: {}".format(smaller_topic_count))
            min_larger_topic_count = max(ntopics-smaller_topic_count, smaller_topic_count)
            #print("larger topic range: {} - {}".format(min_larger_topic_count, ntopics))
            for larger_topic_count in set.intersection(set(range(min_larger_topic_count, ntopics)), set(topic_count_members.keys())):
                larger_members = topic_count_members.get(larger_topic_count, [])
                if larger_members:
                    #print("larger_topic_count: {}".format(larger_topic_count))
                    # NEED TO optimize so don't double count if smaller_members == larger_members
                    if smaller_topic_count == larger_topic_count:
                        # smaller_members = larger_members
                        for mem1_ind in range(len(smaller_members)-1):
                            for mem2_ind in range(mem1_ind+1, len(smaller_members)):
                                mem1 = smaller_members[mem1_ind]
                                mem2 = smaller_members[mem2_ind]
                                cur_team_topics = team_topics(mem1, mem2)
                                if cur_team_topics == ntopics:
                                    #print("Incrementing ncombos with mem1 = {} and mem2 = {}".format(mem1, mem2))
                                    ncombos += 1
                    else:
                        for mem1, mem2 in itertools.product(smaller_members, larger_members):
                            cur_team_topics = team_topics(mem1, mem2)
                            if cur_team_topics == ntopics:
                                #print("Incrementing ncombos with mem1 = {} and mem2 = {}".format(mem1, mem2))
                                ncombos += 1

    return ncombos

def ntopics_possible(cur_cand, topic_count_members):
    # start with most likely
    topic_counts = sorted(topic_count_members.keys(), reverse=True)
    for larger_count_ind in range(len(topic_counts)):
        for smaller_count_ind in range(larger_count_ind, len(topic_counts)):
            larger_count = topic_counts[larger_count_ind]
            smaller_count = topic_counts[smaller_count_ind]
            larger_members = topic_count_members[larger_count]
            smaller_members = topic_count_members[smaller_count]
            for mem1 in larger_members:
                for mem2 in smaller_members:
                    cur_team_topics = team_topics(mem1, mem2)
                    if cur_team_topics >= cur_cand:
                        return True
                    
    return False 
            
def determine_max_topics(topic_count_members, ntopics):
    topic_count_possibilities = sorted(topic_count_members.keys())
    max_possible_topics = min(2*topic_count_possibilities[-1], ntopics)
    #print(max_possible_topics)
    min_possible_topics = topic_count_possibilities[0]
    target = None
    cur_max = max_possible_topics
    cur_min = min_possible_topics
    while not target:
        #print("cur max: {}, cur_min: {}".format(cur_max, cur_min))
        cur_cand = cur_min + int(math.ceil((cur_max - cur_min)/2))
        #print("cur cand: {}".format(cur_cand))
        if ntopics_possible(cur_cand, topic_count_members):
            #print("{} is possible".format(cur_cand))
            cur_min = cur_cand
        else:            
            #print("{} is not possible".format(cur_cand))
            cur_max = cur_cand - 1
            
        if cur_max == cur_min:
            target = cur_max
    
    return target

def acmTeam(topic):
    
    # first do O(n) split of members into ntopics they know.  
    ntopics = len(topic[0]) 
    nmembers = len(topic)
    topic_count_members = dict()
    # for each combination, record the ntopics they know
    for mem in topic:
        mem_count = sum(1 if int(mem[i]) else 0 for i in range(ntopics))
        if mem_count == ntopics:
            return [ntopics, int(nmembers*(nmembers-1)/2)]
        if mem_count in topic_count_members:
            topic_count_members[mem_count].append(mem)
        else:
            topic_count_members[mem_count] = [mem]
   
    #print(sorted(topic_count_members.keys()))
    
    max_topics = determine_max_topics(topic_count_members, ntopics)
    #print("max possible topics is: {}".format(max_topics))
    # Then go down from max possible to min, checking only the real candidates
    
    ncombos = determine_ncombos(max_topics, topic_count_members)
    
    return [max_topics, ncombos]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])

    topic = []
    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()

