import requests
import random
from datetime import datetime

def getallsolved(participants):
    set_ofallsolvedproblems=[]
    for handle in participants : 
        url = f"https://codeforces.com/api/user.status?handle={handle}&from=1&count=10000"
        response = requests.get(url).json()
        for problem in response['result']:
            problemdata = problem['problem']
            set_ofallsolvedproblems.append(problemdata)
            # print(problemdata)
    res = []
    [res.append(x) for x in set_ofallsolvedproblems if x not in res]
    return res



def getRandomProblemByRating(num,min_rating,max_rating,participants):
    url = "https://codeforces.com/api/problemset.problems"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        if data['status'] == 'OK':
            problems = data['result']['problems']
            filtered_problems = []
            for p in problems:
                if(p.get('rating')>= min_rating and p.get('rating')<=max_rating):
                    filtered_problems.append(p)

            if filtered_problems:
                done_problems = getallsolved(participants)
                final_list = []
                for p in filtered_problems:
                    if(p not in done_problems):
                        final_list.append(p)
            
                final_list = random.sample(final_list,num)
                url_list = []
                for p in final_list:
                    link = f"https://codeforces.com/contest/{p['contestId']}/problem/{p['index']}"
                    url_list.append(link)
                return {
                    "status": "OK",
                    "url": url_list,

                }
            else:
                return {"status": "Error", "message": "No problems found with the given rating."}
        else:
            return {"status": "Error", "message": "Error in fetching data from the API."}
    else:
        return {"status": "Error", "message": f"HTTP Error: {response.status_code}"}

def getprob(url_list):
    problem_list = []
    for link in url_list:
        link = link.split('/')
        contest_id = int(link[4])
        index = link[6]
        item = { 'contest_id' : contest_id , 'index' : index}
        problem_list.append(item)
    return problem_list

def check_solved(users , problem):
    fact = False
    contest_id = problem['contest_id']
    index = problem['index']
    ws = 0
    tim = 0
    for i in users:
        if i :
            url = f"https://codeforces.com/api/user.status?handle={i}&from=1&count=100"
            response = (requests.get(url).json())['result']
            for p in response:
                prob = p['problem']
                if(prob['contestId']==contest_id and prob['index']== index):
                    if(p['verdict'] == "OK"):
                        fact = True
                        tim = int(p['creationTimeSeconds'])
                        tim = datetime.fromtimestamp(ts)
                    else : 
                        ws+=1
    return ws , fact , tim

