import csv

with open('data.csv', mode='w') as csvfile:
    fieldnames = ['name', 'email', 'contact', 'profession', 'country', 'keycode']
    writes =csv.DictWriter(csvfile, fieldnames=fieldnames)
    writes.writeheader()
    writes.writerow({"name": "john", "email": "john123@gmail.com", "contact": 3434343, "profession": "Tech", "country": "India", "keycode": "08"})
    writes.writerow({"name": "ron", "email": "ron123@gmail.com", "contact": 478348378, "profession": "Tech", "country": "Us", "keycode": "03"})
    writes.writerow({"name": "nehonz", "email": "neo123@gmail.com", "contact": 2903030, "profession": "Software Developer", "country": "Canada", "keycode": "05"})