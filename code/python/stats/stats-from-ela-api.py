import sys
import argparse
import requests
import json
import csv
from pathlib import Path

parser = argparse.ArgumentParser(
                    prog='stats.py',
                    description='Genera semplici statistiche del corpus di documenti TEI (parole e caratteri spazi esclusi)',
                    epilog='')
parser.add_argument('output_file', nargs = '?', default="./stats.json", type=Path)
args = parser.parse_args()

result = []
if args.output_file.exists():
    with args.output_file.open('r') as fp:
        result = json.load(fp)
already_processed_ids = [item['documentId'] for item in result]

url = 'https://ela.unisi.it/DasMemo/api/search/search'

headers = {
    'Content-Type' : 'application/json'
}
data = {
    'plainText' : '',
    'lemmasText' : '', 
    'tags' :[]
}

resp = requests.post(url, None, headers = headers, json = data) 
data = resp.json()
# print (data)
for document in data['value']['results']:
    documentId = document['documentId']
    if not documentId in already_processed_ids:
        url = 'https://ela.unisi.it/DasMemo/api/cltk/document/' + documentId
        print (url)
        document_cltk = requests.get(url).json()
        document = document | {key : value for key, value in document_cltk['response']['statistics'].items() if key in ('words_number','types_number','lemmas_number')}
        result.append(document)
        with args.output_file.open('w') as fp:
            json.dump(result, fp)

fieldnames=['documentId','author','title','words_number','types_number','lemmas_number']
writer = csv.DictWriter(sys.stdout, fieldnames = fieldnames)
writer.writeheader()
writer.writerows(({key : value for key, value in item.items() if key in fieldnames} for item in result))