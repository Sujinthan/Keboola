import requests
import textwrap
import re

from tabulate import tabulate

r = requests.get('https://api.typeform.com/v1/form/PfSNFM?key=ac83034cfa742c0f79c26e9a612b4ba7e2aa0d3d')
data = r.json()

question_answer = []
answer_dic = None
i = 0

ppl = []
header = []
index_of  = []
fmt = '| {:<35}|{:<35}|{:<35}|{:>35}|{:>35}|'

for item in data['questions']:
    index_of.append(item['field_id'])

for response in data['responses']:
    ans =[""]*5
    for id in response['answers']:
        temp = []
        for obj in response['answers'].keys():
            temp.append(re.sub('[^0-9]', "", obj))
        for item in data['questions']:
            temp_index = index_of.index(item['field_id'])
            header.append(item['question'])
            if str(item['field_id']) in str(id):
                ans[temp_index] = str(response['answers'][id])
            if str(item['field_id']) not in temp:
                ans[temp_index]="NaN"
            elif (bool(response['answers']) == False):
                ans[temp_index]="NaN"
    ppl.append(ans)
print(fmt.format(textwrap.fill(header[0],100),header[1], header[2],header[3], header[4]))

for object in ppl:
    print("----"*(75))
    print(fmt.format(object[0],object[1], object[2],object[3], object[4]))


'''
for item in data ['questions']:
    question_answer.append([])
    question_answer[i].append(str(item['question']))
    header.append(str(item['question']))
    answer = []
    for response in data['responses']:
        for id in response['answers']:
            temp = []
            for obj in response['answers'].keys():
                temp.append(re.sub('[^0-9]', "", obj))
            if str(item['field_id']) in str(id):
                answer.append(response['answers'][id])
        if str(item['field_id']) not in temp:
            answer.append("NaN")
        elif(bool(response['answers']) == False):
            answer.append("NaN")
    question_answer[i].append(answer)
    i += 1

print(tabulate(question_answer))'''

'''fmt = '{:<50}{:<100}'
print(fmt.format("Question", "Answers"))
for item in question_answer:
    new_str = textwrap.fill(str(item[0]),35)
    print("----"*(35))
    print("\t")
    print(fmt.format(new_str,""))
    for answer in item[1]:
        new_answer = textwrap.fill(str(answer), 75)
        print(fmt.format("", new_answer) )
        print("\t")'''
