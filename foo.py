file_name = 'contacts.txt'
names = []
emails = []


with open(file_name, mode='r', encoding='utf-8') as user_file:
    for user_info in user_file:
        names.append(user_info.split()[0])
        emails.append(user_info.split()[1])

print(names)
print('='*80)
print(emails)