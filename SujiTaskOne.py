import requests

r = requests.get('https://api.typeform.com/v1/form/PfSNFM?key=ac83034cfa742c0f79c26e9a612b4ba7e2aa0d3d')
data = r.json()
question_id =[]
answer_dic = None
for item in data ['questions']:
    print("\n")
    print(item['question'])
    '''for id in question_id:'''
    for response in data['responses']:
        for id in response['answers']:
            if str(item['field_id']) in str(id):
                print(response['answers'][id])
