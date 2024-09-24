"""
owner:
data: 2023-09-15
description:
"""
import json

# classList = ["Education", "Technology", "Literature", "Geography", "Business", "Culture", "Sports", "Politics", "Music",
#              "History", "Science", "Law", "Entertainment"]
# numList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# numList1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# hallList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# hallList1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# num = 0
# with open('results.jsonl') as file:
#     for line in file:
#         num += 1
#         data = json.loads(line)
#         claim = data[0]['messages'][0]['content'].split('Claim:')[1]
#         answer = data[1]['choices'][0]['message']['content']
#         for c in classList:
#             if c in answer:
#                 numList1[classList.index(c)] += 1
#                 with open('dataset/wice/dataset_0.9.jsonl') as file1:
#                     for line1 in file1:
#                         data1 = json.loads(line1)
#                         # .encode().decode('unicode_escape')
#                         claim1 = data1[0]['messages'][0]['content'].split('Claim:')[1].split('Reference:')[0]
#                         if claim1.strip() == claim.strip():
#                             if data1[0]['label'] == 'true':
#                                 hallList[classList.index(c)] += 1
#                             numList[classList.index(c)] += 1
#                             break
#                 break
#
# print(classList)
# print(numList,numList1)
# print(hallList)

classList = ["Technology", "Geography", "Business", "Culture", "Sports", "Politics", "Music", "History"]
numList = [0, 0, 0, 0, 0, 0, 0, 0]
numList1 = [0, 0, 0, 0, 0, 0, 0, 0]
hallList = [0, 0, 0, 0, 0, 0, 0, 0]
hallList1 = [0, 0, 0, 0, 0, 0, 0, 0]
num = 0
# with open('results_1.jsonl') as file:
#     for line in file:
#         num += 1
#         data = json.loads(line)
#         claim = data[0]['messages'][0]['content'].split('Claim:')[1]
#         answer = data[1]['choices'][0]['message']['content']
#         for c in classList:
#             if c in answer:
#                 numList1[classList.index(c)] += 1
#                 with open('dataset/wice/dataset_0.9.jsonl') as file1:
#                     for line1 in file1:
#                         data1 = json.loads(line1)
#                         # .encode().decode('unicode_escape')
#                         claim1 = data1[0]['messages'][0]['content'].split('Claim:')[1].split('Reference:')[0]
#                         if claim1.strip() == claim.strip():
#                             if data1[0]['label'] == 'true':
#                                 hallList[classList.index(c)] += 1
#                             numList[classList.index(c)] += 1
#                             break
#                 break
# print(classList)
# print(hallList)

# x = 0
# with open('results_wice_1.jsonl') as file:
#     for line in file:
#         num += 1
#         data = json.loads(line)
#         claim = data[0]['messages'][0]['content'].split('Claim:')[1]
#         answer = data[1]['choices'][0]['message']['content']
#         flag = False
#         for c in classList:
#             if c in answer:
#                 flag = True
#                 numList1[classList.index(c)] += 1
#                 with open('dataset/wice/dataset_0.9.jsonl') as file1:
#                     for line1 in file1:
#                         data1 = json.loads(line1)
#                         # .encode().decode('unicode_escape')
#                         claim1 = data1[0]['messages'][0]['content'].split('Claim:')[1].split('Reference:')[0]
#                         if claim1.strip() == claim.strip():
#                             if data1[0]['label'] == 'true':
#                                 hallList1[classList.index(c)] += 1
#                             hallList[classList.index(c)] += 1  # 数据集中
#                             break
#                 break
#         if not flag:
#             x += 1
#             if "Science" in answer:
#                 numList1[0] += 1
#             print(answer)
# print(classList)
# print(sum(numList1), numList1)
# print(sum(hallList), hallList, hallList1)

x=0
with open('dataset/wice/dataset_0.9.jsonl') as file:
     for line in file:
         data = json.loads(line)
         claim = data[0]['messages'][0]['content'].split('Claim:')[1].split('Reference:')[0]
         if data[0]['label'] == 'true':
         #claim=line.split("Reference:")[0].split("Claim:")[1]
         #label=line.split("label:")[1]
         #if "true" in label: # 幻觉
             with open('results_wice.jsonl') as file1:
                 for line1 in file1:
                     data1 = json.loads(line1)
                     claim1 = data1[0]['messages'][0]['content'].split('Claim:')[1]
                     answer1 = data1[1]['choices'][0]['message']['content']
                     if claim.strip()==claim1.strip():
                         x+=1
                         flag=False
                         for c in classList:
                            if c in answer1:
                                flag=True
                                hallList[classList.index(c)] += 1
                                break
                         if not flag:
                            print(claim)
                         break
print(x)
print(hallList)
