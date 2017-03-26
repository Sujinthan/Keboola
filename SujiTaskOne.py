import requests
import textwrap
import re
r = requests.get('https://api.typeform.com/v1/form/PfSNFM?key=ac83034cfa742c0f79c26e9a612b4ba7e2aa0d3d')
data = r.json()

question_answer =[]
answer_dic = None
i = 0
for item in data ['questions']:
    question_answer.append([])
    question_answer[i].append(str(item['question']))
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



fmt = '{:<50}{:<100}'
print(fmt.format("Question", "Answers"))
for item in question_answer:
    new_str = textwrap.fill(str(item[0]),35)
    print("----"*(35))
    print("\t")
    print(fmt.format(new_str,""))
    for answer in item[1]:
        new_answer = textwrap.fill(str(answer), 75)
        print(fmt.format("", new_answer))
        print("\t")
