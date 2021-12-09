with open(r'name.json','w') as json:
    
    for i in range(1,101):
        print(f'Heet {i}',file=json)
        print(f'Adit {i}',file=json)