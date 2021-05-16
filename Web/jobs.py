# Program to Find Jobs
from bs4 import BeautifulSoup
import requests,time

unknownskill = input('Enter the Unfamiliar Skills : ')
print(f'Filtering Out {unknownskill}')

def find_jobs():
    htmltext = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python').text
    soup = BeautifulSoup(htmltext,'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    #jobs = soup.find('li', class_ = 'clearfix job-bx wht-shd-bx')
    for index,job in enumerate(jobs):
        pubdate = job.find('span', class_ = 'sim-posted').span.text
        if 'few' in pubdate:
            coname = job.find('h3',class_ = 'joblist-comp-name').text.replace(' ','')
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']
            if unknownskill not in skills:
                with open(f'dbs/{index}.txt','w') as f:
                    f.write(f"Company Name : {coname.strip()} \n")
                    f.write(f"Required Skills : {skills.strip()} \n")
                    f.write(f'More Info : {more_info} \n')
                print(f'File Saved: {index}')

if __name__ == '__main__':
    while True:
        find_jobs()
        break
        '''
        print('Waiting for 10 Minutes')
        time.sleep(600)
        '''
