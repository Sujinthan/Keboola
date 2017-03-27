'''
SujiTaskOne.py
Get submitted response from Typeform api and produces a sing table with all responses.
Missing response are NaN
'''

import requests
import textwrap
import re


def collect_data():
    '''
    Makes a request to typform api, extracts data
    from JSON and stores question and submitted
    response in a list
    :return:
    list, list
        first list has the questions and second
        list has the submitted responses
    '''

    ppl = []  # list to store submitted respnse

    header = []  # list to store questions, later will be used as the header for table

    r = requests.get(
        'https://api.typeform.com/v1/form/PfSNFM?key=ac83034cfa742c0f79c26e9a612b4ba7e2aa0d3d')  # making request to typeform api

    index_of = []  # list to store index of question field_id

    data = r.json()  # Use json data from Response
    for item in data['questions']:
        index_of.append(item['field_id'])  # store question field_id
    for response in data['responses']:
        ans = ["NaN"] * len(index_of)  # create list with size length same as the number of questions
        for id in response['answers']:
            temp = []  # list to stroe id of answers to questions
            for obj in response['answers'].keys():
                temp.append(re.sub('[^0-9]', "", obj))  # remove any char from id. Easier to match question with answer.
            for item in data['questions']:
                temp_index = index_of.index(item['field_id'])  # get index of current question id from list 'index_of'.
                header.append(item['question'])  # store question into list.
                if str(item['field_id']) in str(id):
                    # if the user answered the question, then store the answer in the same index as the current question_id in list 'ans'
                    ans[temp_index] = str(response['answers'][id])
                if str(item['field_id']) not in temp:
                    # if the user did not answer the question then store "NaN" in the same index as the current question_id in list 'ans'
                    ans[temp_index] = "NaN"
                if (bool(response['answers']) == False):
                    # if the user did not answer any question then store "NaN" in the same index as the current question_id in list 'ans'
                    ans[temp_index] = "NaN"
        ppl.append(ans)  # store list 'ans' in list 'ppl'
    return header, ppl


def print_table():
    '''

    print submitted response in a table. Table is in this format:
        question 1       question 2     question3       question 4      question 5
        response11       response12     response13      response14      response15
        response21       response22     response24      response24      response25
        response31       response32     response34      response34      response35

    response11: the frist digit is first submission id, the second digit is the question id
    '''
    header, ppl = collect_data()  # return list of questions and answers
    fmt = '{0:<75}\t{1:<95}\t{2:<110}\t{3:<85}\t{4:<100}'  # format of the table
    print(fmt.format(header[0], header[1], header[2], header[3],
                     header[4]))  # print the questions in list 'header' using the format 'fmt'
    for object in ppl:
        print(fmt.format(textwrap.fill(object[0], 35), textwrap.fill(object[1], 35), textwrap.fill(object[2], 35),
                         textwrap.fill(object[3], 100),
                         textwrap.fill(object[4], 225)))  # print the answers in list 'ppl' using format fmt


if __name__ == "__main__":
    print_table()  # print table
