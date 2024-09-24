"""
owner:
data: 2023-07-29
description:
"""
import json

# t = 0
# f = 0
# hallu = 0
# no_ref = 0
# hallu0, hallu1 = 0, 0
# with open('hallucination_0.9.json', 'w') as outfile:
#     with open('cls_0.9.jsonl') as file:
#         for line in file:
#             data = json.loads(line)
#             answer = data[1]['choices'][0]['message']['content']
#             question = data[0]['messages'][0]['content']
#             claim = data[0]['messages'][0]['content'].split('Claim:')[1].split('Reference:')[0]
#             reference = data[0]['messages'][0]['content'].split('Reference:')
#             if len(reference) == 1:
#                 reference = reference[0]
#             elif len(reference) == 2:
#                 reference = reference[1]
#             else:
#                 reference = reference[2]
#             if "true" in answer or "True" in answer or "TRUE" in answer:
#                 t += 1
#                 with open('dataset/climate/climate_true_or_false.json') as file1:
#                     for line1 in file1:
#                         data1 = json.loads(line1)
#                         claim1 = data1['claim']
#                         if claim.strip() == claim1:
#                             if data1['claim_label'] == 'REFUTES':
#                                 hallu += 1
#                                 hallu0 += 1
#                                 outfile.write(json.dumps(data) + "\n")
#             elif "False" in answer or "false" in answer:
#                 f += 1
#                 with open('dataset/climate/climate_true_or_false.json') as file1:
#                     for line1 in file1:
#                         data1 = json.loads(line1)
#                         claim1 = data1['claim']
#                         if claim.strip() == claim1:
#                             if data1['claim_label'] == 'SUPPORTS':
#                                 outfile.write(json.dumps(data) + "\n")
#                                 hallu += 1
#                                 hallu1 += 1
#             else:
#                 no_ref += 1
#                 print(no_ref)
#                 print(claim)
#                 print(reference)
#                 print(answer)
# print('\n', t, f, hallu)
# print(hallu0, hallu1)
#
# num=0
# with open('non_hallucination_0.9.json', 'w') as outfile:
#     with open('cls_0.9.jsonl') as file:
#         for line in file:
#             data = json.loads(line)
#             answer = data[1]['choices'][0]['message']['content']
#             question = data[0]['messages'][0]['content']
#             claim = data[0]['messages'][0]['content'].split('Claim:')[1].split('Reference:')[0]
#             reference = data[0]['messages'][0]['content'].split('Reference:')
#             if len(reference)==1:
#                 reference = reference[0]
#             elif len(reference)==2:
#                 reference = reference[1]
#             else:
#                 reference = reference[2]
#             if "true" in answer or "True" in answer or "TRUE" in answer:
#                 with open('dataset/climate/climate_true_or_false.json') as file1:
#                     for line1 in file1:
#                         data1 = json.loads(line1)
#                         claim1 = data1['claim']
#                         if claim.strip() == claim1:
#                             if data1['claim_label'] == 'SUPPORTS':
#                                 num+=1
#                                 outfile.write(json.dumps(data)+"\n")
#             elif "False" in answer or "false" in answer:
#                 with open('dataset/climate/climate_true_or_false.json') as file1:
#                     for line1 in file1:
#                         data1 = json.loads(line1)
#                         claim1 = data1['claim']
#                         if claim.strip() == claim1:
#                             if data1['claim_label'] == 'REFUTES':
#                                 num+=1
#                                 outfile.write(json.dumps(data)+"\n")
#             if num==175:
#                 break
#
# with open('dataset_0.9.jsonl', 'w') as outfile:
#     with open('hallucination_0.9.json') as file:
#         for line in file:
#             data = json.loads(line)
#             data[0]["label"] = "true"
#             outfile.write(json.dumps(data) + "\n")
#     with open('non_hallucination_0.9.json') as file:
#         for line in file:
#             data = json.loads(line)
#             data[0]["label"] = "false"
#             outfile.write(json.dumps(data) + "\n")

# t = 0
# f = 0
# hallu = 0
# no_ref = 0
# hallu0, hallu1 = 0, 0
# with open('hallucination_0.9.json', 'w') as outfile:
#     with open('cls_0.9.jsonl') as file:
#         for line in file:
#             claim = line.split("Reference: ")[0].split("Claim: ")[1]
#             answer = line.split("\"\"> Assistant: ")[1]
#             # reference = line.split("\"\"> Assistant: ")[-1][0:-1]
#             if "true" in answer or "True" in answer or "TRUE" in answer:
#                 t += 1
#                 with open('dataset/wice/wice_true_or_false.json') as file1:
#                     for line1 in file1:
#                         data1 = json.loads(line1)
#                         claim1 = data1['claim']
#                         if claim.strip() == claim1:
#                             if data1['label'] == 'not_supported':
#                                 hallu += 1
#                                 hallu0 += 1
#                                 outfile.write(line)
#             elif "False" in answer or "false" in answer or "FALSE" in answer:
#                 f += 1
#                 with open('dataset/wice/wice_true_or_false.json') as file1:
#                     for line1 in file1:
#                         data1 = json.loads(line1)
#                         claim1 = data1['claim']
#                         if claim.strip() == claim1:
#                             if data1['label'] == 'supported':
#                                 outfile.write(line)
#                                 hallu += 1
#                                 hallu1 += 1
#             else:
#                 no_ref += 1
#                 print(no_ref)
#                 print(claim)
#                 # print(reference)
#                 print(answer)
# print('\n', t, f, hallu)
# print(hallu0, hallu1)

# num=0
# with open('non_hallucination_0.9.json', 'w') as outfile:
#     with open('cls_0.9.jsonl') as file:
#         for line in file:
#             claim = line.split("Reference: ")[0].split("Claim: ")[1]
#             answer = line.split("\"\"> Assistant: ")[1]
#             if "true" in answer or "True" in answer or "TRUE" in answer:
#                 with open('dataset/wice/wice_true_or_false.json') as file1:
#                     for line1 in file1:
#                         data1 = json.loads(line1)
#                         claim1 = data1['claim']
#                         if claim.strip() == claim1:
#                             if data1['label'] == 'supported':
#                                 num+=1
#                                 outfile.write(line)
#             elif "False" in answer or "false" in answer or "FALSE" in answer:
#                 with open('dataset/wice/wice_true_or_false.json') as file1:
#                     for line1 in file1:
#                         data1 = json.loads(line1)
#                         claim1 = data1['claim']
#                         if claim.strip() == claim1:
#                             if data1['label'] == 'not_supported':
#                                 num+=1
#                                 outfile.write(line)
#             if num==261:
#                 break
#
# with open('dataset_0.9.jsonl', 'w') as outfile:
#     with open('hallucination_0.9.json') as file:
#         for line in file:
#             outfile.write(json.dumps(line) + "label: true\n")
#     with open('non_hallucination_0.9.json') as file:
#         for line in file:
#             outfile.write(json.dumps(line) + "label: false\n")

# t = 0
# f = 0
# hallu = 0
# no_ref = 0
# hallu0, hallu1 = 0, 0
# with open('hallucination_0.5.json', 'w') as outfile:
#     with open('cls_0.5.jsonl') as file:
#         for line in file:
#             claim = line.split("Reference: ")[0].split("Claim: ")[1]
#             answer = line.split("Response: ")[1]
#             if "true" in answer or "True" in answer or "TRUE" in answer:
#                 t += 1
#                 with open('dataset/pubhealth/pubhealth_dev.json') as file1:
#                     for line1 in file1:
#                         data1 = json.loads(line1)
#                         claim1 = data1['claim']
#                         if claim1 in claim.strip():
#                             if data1['label'] == 'false':
#                                 hallu += 1
#                                 hallu0 += 1
#                                 outfile.write(line)
#             elif "False" in answer or "false" in answer or "FALSE" in answer:
#                 f += 1
#                 with open('dataset/pubhealth/pubhealth_dev.json') as file1:
#                     for line1 in file1:
#                         data1 = json.loads(line1)
#                         claim1 = data1['claim']
#                         if claim1 in claim.strip():
#                             if data1['label'] == 'true':
#                                 outfile.write(line)
#                                 hallu += 1
#                                 hallu1 += 1
#             else:
#                 no_ref += 1
#                 print(no_ref)
#                 print(claim)
#                 print(answer)
# print('\n', t, f, hallu)
# print(hallu0, hallu1)

num = 0
with open('non_hallucination_0.5.json', 'w') as outfile:
    with open('cls_0.5.jsonl') as file:
        for line in file:
            claim = line.split("Reference: ")[0].split("Claim: ")[1]
            answer = line.split("Response: ")[1]
            pre=num
            if "true" in answer or "True" in answer or "TRUE" in answer:
                with open('dataset/pubhealth/pubhealth_dev.json') as file1:
                    for line1 in file1:
                        data1 = json.loads(line1)
                        claim1 = data1['claim']
                        if claim1 in claim.strip():
                            if data1['label'] == 'true':
                                num += 1
                                outfile.write(line)
            elif "False" in answer or "false" in answer or "FALSE" in answer:
                with open('dataset/pubhealth/pubhealth_dev.json') as file1:
                    for line1 in file1:
                        data1 = json.loads(line1)
                        claim1 = data1['claim']
                        if claim1 in claim.strip():
                            if data1['label'] == 'false':
                                num += 1
                                outfile.write(line)
            if num == 207:
                break

with open('dataset_0.5.jsonl', 'w') as outfile:
    with open('hallucination_0.5.json') as file:
        for line in file:
            outfile.write(json.dumps(line) + "label: true\n")
    with open('non_hallucination_0.5.json') as file:
        for line in file:
            outfile.write(json.dumps(line) + "label: false\n")
