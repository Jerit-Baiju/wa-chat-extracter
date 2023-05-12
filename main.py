from datetime import datetime
import os

def fmt_date(fmt):
    return datetime.strptime(fmt, "%d/%m/%y")


def eval_date(content):
    if fmt_date(content):
        return True
    return False

with open('chat.txt', 'r') as file:
    lines = file.readlines()

dates = []
chats = []

for line in lines:
    day = line.split(',')[0]
    if day not in dates:
        try:
            if eval_date(day):
                dates.append(day)
        except:
            pass

for date in dates:
    chat = []
    for line in lines:
        if date == line.split(',')[0]:
            chat.append(line)
    chats.append(chat)

for chat in chats:
    date = fmt_date(chat[0].split(',')[0])
    file_name = f"exports/{(date).strftime('%B')}/{date.strftime('%d-%B-%Y')}.txt"
    folder_path = os.path.dirname(file_name)
    os.makedirs(folder_path, exist_ok=True)
    with open(file_name, 'w') as file:
        file.writelines(chat)
        file.close()
