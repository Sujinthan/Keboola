import requests
import textwrap
r = requests.get('https://api.typeform.com/v1/form/PfSNFM?key=ac83034cfa742c0f79c26e9a612b4ba7e2aa0d3d')
data = r.json()
print(data)
question_answer =[]
answer_dic = None
i = 0
for item in data ['questions']:
    print("\n")
    question_answer.append([])
    question_answer[i].append(str(item['question'].encode('utf-8').strip()))
    answer = []
    for response in data['responses']:
        for id in response['answers']:
            if str(item['field_id']) in str(id):
                answer.append(response['answers'][id].encode('utf-8').strip())
        if(bool(response['answers'])== False):
            answer.append("NaN")
    question_answer[i].append(answer)
    i += 1

fmt = '{:<50}{:<50}'
print(fmt.format("Question", "Answers"))
for item in question_answer:
    new_str = textwrap.fill(item[0],35)
    print("\t")
    print("----"*(50))
    print("\t")
    print(fmt.format(new_str,""))
    for answer in item[1]:
        new_answer = textwrap.fill("{:<8}".format(answer))
        print(fmt.format("", new_answer))
        print("\t")
