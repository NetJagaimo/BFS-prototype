import os
import csv
import requests
import re
from bs4 import BeautifulSoup

def craw_data(out_file, target_file=None, target=None):
    targets = []
    if target:
        targets.append(target)
    else:
        with open(target_file, encoding='utf-8') as f:
            targets = list(csv.DictReader(f))

    data = []
    error = 0
    pdf = 0

    for i, target in enumerate(targets):
        print(i)
        
        # skip pdf, cannot hadle pdf now
        if re.search(".pdf$", target['url']):
            pdf += 1
            continue

        try:
            r = requests.get(target['url'])
            if r.status_code == requests.codes.ok:
                soup = BeautifulSoup(r.text, 'lxml')
                if soup.body != None:
                    for s in soup(["script", "style", "nav", "button"]):
                        s.extract()
                    plain_text = soup.body.get_text()
                    plain_text = re.sub(r' {2,}', " ", plain_text)
                    plain_text = re.sub(r'[\t\n]', "", plain_text)
            
            data.append({'title': target['title'], 'url': target['url'], 'plain_text': plain_text})
        except:
            error += 1
        
        # if i >= 100:
        #     break

    if not os.path.isfile(out_file) and len(data) > 0:
        with open(out_file, "w", encoding='utf-8') as outfile:
            fieldnames = ['title', 'url', 'plain_text']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
    else:
        with open(out_file, "a", encoding='utf-8') as outfile:
            fieldnames = ['title', 'url', 'plain_text']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writerows(data)

    print("done with {} errors in {} data. skip with {} pdf".format(error, len(targets), pdf))