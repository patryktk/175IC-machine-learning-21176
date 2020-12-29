# 8.Praca z danymi w formacie JSON i CSV

## Working With JSON Data in Python

Zapisywanie danych w formacie JSON, serializacja danych
```
data = {
    "student":{
        "name":"Patryk Tkaczyk",
        "species":"cos"
    }
}
```

Zapisywanie danych do pliku data_file.json
```

with open("data_file.json","w") as write_file:
  json.dump(data,write_file)

```
Dodawanie wcięć w liście
```
json_string = json.dumps(data, indent=4)
json_string
```

Możemy zakodować wiadomośc, ale po odkowaniu nie zawsze otrzymamy ten sam wynik
```
blackjack_hand = (8, "Q")
encoded_hand = json.dumps(blackjack_hand)
decoded_hand = json.loads(encoded_hand)

print(blackjack_hand == decoded_hand)

print(type(blackjack_hand))

print(type(decoded_hand))

blackjack_hand == tuple(decoded_hand)
```
Deserializacja z pliku czyli odczyt danych
```
with open("data_file.json", "r") as read_file:
    data = json.load(read_file)
```
Deserializacja z URL
```
response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)
```
Wyświetlanie ukończnych zadań oraz osób które je ukończyły
```
todos_by_user = {}

for todo in todos:
  if todo["completed"]:
    try:
      todos_by_user[todo["userId"]] += 1
    except KeyError:
      todos_by_user[todo["userId"]] = 1

top_users = sorted(todos_by_user.items(), 
                   key=lambda x: x[1], reverse=True)

print(f'Top postów: {top_users}')

max_complete = top_users[0][1]
users = []
for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))

max_users = " and ".join(users)

print(f'Osoby które ukończyły wszystkie taski: {max_users}')
```
Funkcja która wyszykuje użykowników z ukończonymi wszystkimi zadaniami
```
def keep(todo):
    is_complete = todo["completed"]
    has_max_count = str(todo["userId"]) in users
    return is_complete and has_max_count


with open("json_file/filtered_data_file.json", "w") as data_file:
    filtered_todos = list(filter(keep, todos))
    json.dump(filtered_todos, data_file, indent=2)

filtered_todos
```
Kodowanie i dekodowanie niestandardowych obiektów PYTHON
```
def encode_complex(z):
    if isinstance(z, complex):
        return (z.real, z.imag)
    else:
        type_name = z.__class__.__name__
        raise TypeError(f"Object of type '{type_name}' is not JSON serializable")
json.dumps(9 + 5j, default=encode_complex)
```
Kodowanie z pomocą JSONEncoder'a
```
class ComplexEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, complex):
            return (z.real, z.imag)
        else:
            return super().default(z)

#Przykładowe wywołania kodowania powyżej
print(f'json.dumps: {json.dumps(2 + 6j, cls=ComplexEncoder)}')
encoder = ComplexEncoder()
print(f'encoder.encode: {encoder.encode(3 + 6j)}')

#Dekodowanie typów niestandardowych
complex_json = json.dumps(4 + 17j, cls=ComplexEncoder)
print(f'json.loads: {json.loads(complex_json)}')
```
Dekodowanie klucza 
```
def decode_complex(dct):
    if "__complex__" in dct:
        return complex(dct["real"], dct["imag"])
    return dct

with open("json_file/complex_data.json") as complex_data:
     data = complex_data.read()
     z = json.loads(data, object_hook=decode_complex)

print(z)
```

## Reading and Writing CSV Files in Python

Czytanie plików CSV
```
with open('employee_birthday.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
```
Pisanie plików CSV
```
with open('employee_file.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])

with open('employee_file.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
```
Odczyt danych csv za pomocą pandas
```
df = pd.read_csv('hrdata.csv', index_col = 'Name')
print(df)
```
Pisanie plików .csv z pomocą biblioteki pandas ze zmianą indexu oraz parsowaniem dat
```
import pandas
df = pandas.read_csv('hrdata.csv', 
            index_col='Employee', 
            parse_dates=['Hired'],
            header=0, 
            names=['Employee', 'Hired', 'Salary', 'Sick Days'])
df.to_csv('hrdata_modified.csv')

df = pd.read_csv('hrdata_modified.csv')
print(df)
```
