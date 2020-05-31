import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

scope=['https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('Client_Secret.json', scope)
client = gspread.authorize(creds)

sheets = client.open('Slack_Bots').sheet1
sheets_2 = client.open('Slack_Bots').worksheet("Sheet2")

pp = pprint.PrettyPrinter()
# Scraped = sheets.col_values(3)                          #Note the index starts from 1
# pp.pprint(Scraped)

def Add_to_Sheets(data,index = 2):
    for i in data:
        new_row = i
        sheets.insert_row(new_row, index)

def Prev_Time_Channel():
        Message_Data = []
        Message_ID = sheets.col_values(3)
        Time_Stamp = sheets.col_values(4)
        Channel_ID = sheets.col_values(5)
        for i in range(1, len(Time_Stamp)):
                if Time_Stamp[i]:
                        Message_Data.append([Time_Stamp[i], Channel_ID[i], Message_ID[i]])
        return Message_Data

def Remove_Black_List(data):
        Message_ID = sheets.col_values(3)
        index= []
        for i in range(len(Message_ID)):
                if Message_ID[i] in data:
                        Add_Black_List_URL(sheets.row_values(i+1))
                        index.append(i)
        index.reverse()
        for i in index:
                sheets.delete_rows(i+1)

def Add_Black_List_URL(value):                  ## In Future add just main domomain
        sheets_2.insert_row(value,2)