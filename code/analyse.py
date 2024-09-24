"""
owner:
data: 2023-09-12
description:
"""
import json

# num=0
# num1=0
# with open('dataset/climate/climate_true_or_false.json') as file1:
#     for line1 in file1:
#         data1 = json.loads(line1)
#         claim1 = data1['claim']
#         num+=1
#         if data1['claim_label'] == 'SUPPORTS':
#             num1 += 1
# print(num,num1,num-num1,(num-num1)/num*100)
#
# num=0
# num1=0
# with open('dataset/pubhealth/pubhealth_dev.json') as file1:
#     for line1 in file1:
#         data1 = json.loads(line1)
#         claim1 = data1['claim']
#         num+=1
#         if data1['label'] == 'true':
#             num1 += 1
# print(num,num1,num-num1,(num-num1)/num*100)
#
# num=0
# num1=0
# with open('dataset/wice/wice_true_or_false.json') as file1:
#     for line1 in file1:
#         data1 = json.loads(line1)
#         claim1 = data1['claim']
#         num+=1
#         if data1['label'] == 'supported':
#             num1 += 1
# print(num,num1,num-num1,(num-num1)/num*100)

# t = 0
# f = 0
# hallu = 0
# no_ref = 0
# hallu0, hallu1 = 0, 0
# with open('dataset/wice/cls_0.9.jsonl') as file:
#     for line in file:
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
#                 with open('dataset/wice/wice_true_or_false.json') as file1:
#                     for line1 in file1:
#                         data1 = json.loads(line1)
#                         claim1 = data1['claim']
#                         if claim.strip() == claim1:
#                             if data1['label'] == 'not_supported':
#                                 hallu += 1
#                                 hallu0 += 1
#             elif "False" in answer or "false" in answer:
#                 f += 1
#                 with open('dataset/wice/wice_true_or_false.json') as file1:
#                     for line1 in file1:
#                         data1 = json.loads(line1)
#                         claim1 = data1['claim']
#                         if claim.strip() == claim1:
#                             if data1['label'] == 'supported':
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

