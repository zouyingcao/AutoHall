import json

with open('multi_ref_7.json', 'w') as outfile:
    with open('dataset/wice/dataset_0.9.jsonl') as file:
        for line in file:
            data = json.loads(line)
            question = data[0]['messages'][0]['content']
            claim = question.split('Claim:')[1].split('Reference:')[0]
            reference = question.split('Reference:')[-1]
            outfile.write(json.dumps(reference.strip()) + "\n")
            n=0
            with open('reference_7.jsonl') as file1:
                for line1 in file1:
                    data1 = json.loads(line1)
                    answer1 = data1[1]['choices'][0]['message']['content']
                    question1 = data1[0]['messages'][0]['content']
                    claim1 = question1.split('Claim:')[1]
                    if claim.strip() == claim1.strip():
                        n+=1
                        outfile.write(json.dumps(answer1.strip()) + "\n")
            if n!=1:
                print(n)
                print(claim)
