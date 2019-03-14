# make the categories for which I have to retrieve data in an array
import json
import logging
import os
import requests
import threading
import time
from multiprocessing.pool import ThreadPool

BASE_URL = "https://www.hackerrank.com/rest/contests/master/"   
logging.basicConfig(filename="logs.txt")

class Scrapper:

    PREFIX = "_"
    def __init__(self, conf):
        self.submissions = None
        self.HEADERS = {
            'x-csrf-token': conf["CSRF_TOKEN"],
            'cookie': conf["COOKIE"]
        }
        self.file_extensions = {
            'java': '.java',
            'java7': '.java',
            'java8': '.java',
            'python': '.py',
            'python3': '.py',
            'python2': '.py',
            'text': '.txt'
        } 
        self.created_files = 0
    
    def get_all_submissions(self):
        limit = 1000
        submissions_url = BASE_URL + "submissions"
        PARAMS = {
            'limit': limit
        }
        
        response = requests.get(url=submissions_url, params=PARAMS, headers=self.HEADERS)
        submissions = response.json()
        return submissions['models']
    
    def set_submissions(self):
        # sort by highest score, then latest submission
        raw_submissions = self.get_all_submissions()
        # create dictionary based on challenge ID
        self.submissions = {}
        for submission in raw_submissions:
            challenge_id = submission['challenge_id']
            cur_submission = {
                "sub_id": submission["id"],
                "score": float(submission['score']),
                "time": submission["inserttime"]
            }
            if challenge_id not in self.submissions:
                self.submissions[challenge_id] = list()
        
            self.submissions[challenge_id].append(cur_submission)

        # sort by score, then by latest time (both descending)
        for challenge in self.submissions:
            self.submissions[challenge].sort(key=lambda sub: (sub['score'], sub['time']), reverse=True)
    
    
    def create_file(self, sub_id):
        # generate code file for the submission 
        submission_url = BASE_URL + "submissions/{}".format(sub_id)
        res = requests.get(url=submission_url, headers=self.HEADERS).json()
        response = res['model']
        code = response['code']

        if code:
            challenge_name = response['challenge_slug']
            track = response['track']
            track_name = track['track_slug']
            subdomain_name = track['slug']
            language = response['language']
        
            extension = self.file_extensions[language]     
            filename = challenge_name + extension    
            dir = os.path.join(self.PREFIX+track_name, subdomain_name)
            file_path = os.path.join(dir, filename)
            print("Saving to {}".format(file_path))
            if not os.path.exists(dir): #os.path.isdir(dir):
                os.makedirs(dir)
                if not os.path.isfile(file_path):
                    print("New file: {}".format(file_path))
                print(code, file=open(file_path, 'w'))
            else:
                print(code, file=open(file_path, 'w'))
            self.created_files += 1   
    
    def scrape(self):
        self.set_submissions()
        # now, pull out for each challenge the sub_id associated
        # with the most successful, most recent submission
        recent_submissions = list()
        for challenge in self.submissions:
            challenge_submissions = self.submissions[challenge]
            recent_submissions.append(challenge_submissions[0]['sub_id'])
        
        print("found submissions for {} challenges".format(len(recent_submissions)))
        
        pool = ThreadPool()
        pool.map(lambda sub_id: self.create_file(sub_id), recent_submissions)
        # for sub_id in recent_submissions:
            # self.create_file(sub_id)

        print("created {} files".format(self.created_files))
        
if __name__ == "__main__":
    
    start = time.time()
    conf = {}
    with open("credentials.json", "r") as f:
        conf = json.load(f)

    scrapper = Scrapper(conf)
    try:    
        scrapper.scrape()
        
    except Exception as e:
        print('Exception:', str(e))
        logging.warning(e)
        
    end = time.time()
    
    print("Took {} seconds".format(int(end-start)))

