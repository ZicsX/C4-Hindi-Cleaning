import sys
import jsonlines
import gzip
import json
from clean import clean_text


PATH ="/home/yeb/oscar_nl"

def main(file):
    with gzip.open(f"cleaned_{file}", mode='wb') as writer:
        with gzip.open(f'{PATH}/{file}') as f:
            for line in f:
                obj = json.loads(line)
                cleaned = clean_text(obj['text'])
                if cleaned is not None:
                    obj['text'] = cleaned
                    writer.write(str.encode(json.dumps(obj)))
                    writer.write('\n'.encode("utf-8"))

if __name__ == '__main__':
    file = sys.argv[1]
    main(file)

