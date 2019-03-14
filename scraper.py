# make the categories for which I have to retrieve data in an array
import requests
import logging
import threading

# Instead, could implement using my 'self.submissions' object
# build self.submissions from raw submissions
# track -> subdomain -> name -> most recent maximal submission (id, code, score)
# can still use threading after build submissions object so can get each track 
# separately

        
# t1 = threading.Thread(target=hr_scrap.get_track, args=(i,))
# t1.start();

CSRF_TOKEN = '+k8VWcejIevBfnDAqv14Hoi3VQ8CBnHkGnrR6dCH+HxTlgoQih0jJ/iN5pIxZ2bzgZbjytUfOvI7q/vXDwEp7w=='
COOKIE = 'hackerrank_mixpanel_token=5da4f9c0-7cb1-4953-ac9d-df9239d9d545; h_v=_default; optimizelyEndUserId=oeu1530840012384r0.695090859698549; optimizelySegments=%7B%221709580323%22%3A%22false%22%2C%221717251348%22%3A%22gc%22%2C%221719390155%22%3A%22direct%22%2C%222308790558%22%3A%22none%22%7D; optimizelyBuckets=%7B%7D; _biz_uid=5ac680d5cd194998bb10dd0ea29a8b0b; hacker_editor_theme=light; enableIntellisenseUserPref=true; moodys-analytics-2018-university-codesprint_crp=*nil*; _hp2_id.547804831=%7B%22userId%22%3A%225259965638745528%22%2C%22pageviewId%22%3A%220537651805653669%22%2C%22sessionId%22%3A%228624142995341047%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; h_r=submissions; h_l=_default; hourrank-31_crp=*nil*; show_cookie_banner=false; hourrank-30_crp=*nil*; _hp2_id.698647726=%7B%22userId%22%3A%227668729448631156%22%2C%22pageviewId%22%3A%220556813660754875%22%2C%22sessionId%22%3A%227941301582454007%22%2C%22identity%22%3A%225da4f9c0-7cb1-4953-ac9d-df9239d9d545%22%2C%22trackerVersion%22%3A%224.0%22%2C%22identityField%22%3Anull%2C%22isIdentified%22%3A1%7D; _hp2_id.3318504451=%7B%22userId%22%3A%224077452746086965%22%2C%22pageviewId%22%3A%225364204197316697%22%2C%22sessionId%22%3A%221349050163803418%22%2C%22identity%22%3A%225da4f9c0-7cb1-4953-ac9d-df9239d9d545%22%2C%22trackerVersion%22%3A%224.0%22%2C%22identityField%22%3Anull%2C%22isIdentified%22%3A1%7D; amplitude_id_f73efeaeb49336eb6e9608d1c0cb0600hackerrank.com=eyJkZXZpY2VJZCI6IjIxMDUxYzM3LWMyYTktNDMxZS1hZTBiLWJhNDM3ZWE2M2I5NFIiLCJ1c2VySWQiOiI1ZGE0ZjljMC03Y2IxLTQ5NTMtYWM5ZC1kZjkyMzlkOWQ1NDUiLCJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOjE1NDQ4OTA5MDQzMDQsImxhc3RFdmVudFRpbWUiOjE1NDQ4OTMzNzYxMTAsImV2ZW50SWQiOjc2NSwiaWRlbnRpZnlJZCI6Nywic2VxdWVuY2VOdW1iZXIiOjc3Mn0=; __utmc=74197771; hrc_l_i=T; _hrank_session=cfbe8a5379566b0c455761190beeba7f5216a39d75aab34734c6d9a9d317602cd8d858a434af754d5e45217d6eb244035aeb55fbe9ed9a5b3d4f098b7d8333cd; _mkto_trk=id:487-WAY-049&token:_mch-hackerrank.com-1549942376167-85012; _ga=GA1.2.905029814.1530840012; PHPSESSID=ogu67m4f8iqskk58joaq3k1qt1; pagination_per_page_limit=100; user_type=hacker; react_var=true__trm2; react_var2=true__trm2; metrics_user_identifier=42e42b-63109ce8a270ee97a14d702cac8e300cded9789f; fileDownload=true; hackerrankx_mixpanel_token=5da4f9c0-7cb1-4953-ac9d-df9239d9d545; session_referrer=https%3A%2F%2Fwww.google.com%2F; session_referring_domain=www.google.com; __zlcmid=rHi510evvaQA8C; session_id=lqmorf4i-1552359734027; __utma=74197771.905029814.1530840012.1552151511.1552359736.156; __utmz=74197771.1552359736.156.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); session_landing_url=https%3A%2F%2Fwww.hackerrank.com%2Fapi%2Fdocs; _biz_dfsA=%5B%5D; _biz_nA=50; _biz_pendingA=%5B%22m%2Fipv%3F_biz_r%3D%26_biz_h%3D-1719903975%26_biz_u%3D5ac680d5cd194998bb10dd0ea29a8b0b%26_biz_s%3D493e02%26_biz_l%3Dhttps%253A%252F%252Fwww.hackerrank.com%252Fcontests%252Falgorithms%252Fchallenges%26_biz_t%3D1552360081473%26_biz_i%3DSolve%2520algorithms%2520Questions%2520%257C%2520Contests%2520%257C%2520HackerRank%26_biz_n%3D49%26rnd%3D1650%22%5D; mp_dcd74fdb7c65d92ce5d036daddac0a25_mixpanel=%7B%22distinct_id%22%3A%20%225da4f9c0-7cb1-4953-ac9d-df9239d9d545%22%2C%22%24device_id%22%3A%20%221696fd924863ff-0d8b7767bb4728-10346654-fa000-1696fd924878be%22%2C%22%24user_id%22%3A%20%225da4f9c0-7cb1-4953-ac9d-df9239d9d545%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%7D; mp_bcb75af88bccc92724ac5fd79271e1ff_mixpanel=%7B%22distinct_id%22%3A%20%225da4f9c0-7cb1-4953-ac9d-df9239d9d545%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22%24user_id%22%3A%20%225da4f9c0-7cb1-4953-ac9d-df9239d9d545%22%2C%22%24had_persisted_distinct_id%22%3A%20true%2C%22%24device_id%22%3A%20%225da4f9c0-7cb1-4953-ac9d-df9239d9d545%22%2C%22%24search_engine%22%3A%20%22google%22%7D; mp_86cf4681911d3ff600208fdc823c5ff5_mixpanel=%7B%22distinct_id%22%3A%20%221646d2cd8e6561-0c83a5f6a5e204-16396952-fa000-1646d2cd8e7891%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22%24search_engine%22%3A%20%22google%22%7D5'
BASE_URL = "https://www.hackerrank.com/rest/contests/master/"   
   
logging.basicConfig(filename="logs.txt")

class Scrapper:

    PREFIX = "_"
    def __init__(self):
        self.submissions = None
        self.HEADERS = {
        'x-csrf-token': CSRF_TOKEN,
        'cookie': COOKIE
    }

    def get_all_submissions(self):
        limit = 1000
        submissions_url = BASE_URL + "submissions"
        PARAMS = {
            'limit': limit
        }
        
        submissions = requests.get(url=submissions_url, params=PARAMS, headers=self.HEADERS)
        return submissions
    
    def set_submissions(self):
        # sort by highest score, then latest submission
        self.submissions = self.get_all_submissions()
        print("Got submissions")
        
    def scrape(self):
        self.set_submissions()
        

if __name__ == "__main__":
  
    scrapper = Scrapper()
    try:    
        scrapper.scrape()
        
    except Exception as e:
        print('Something went wrong::', str(e))
        logging.warning(e)
        pass
    
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
        pass
