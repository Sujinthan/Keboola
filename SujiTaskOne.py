import requests

r = requests.get('https://api.typeform.com/v1/form/PfSNFM?key=ac83034cfa742c0f79c26e9a612b4ba7e2aa0d3d')
data = r.json()

for item in data ['questions']:
    print(item['field_id'])
    for thins in data['responses']:
        print("\n")
        print("question")
        print(item['question'])
        for id in thins['answers'].keys():
            if str(item['field_id']) in str(id):
                print(thins['answers'][id])
