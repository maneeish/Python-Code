dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3 = {'Sixty': 60}

dict4 = {**dict1, **dict2,**dict3}



print(dict4)