from Slack_Intigrater import *
from database import *

def Delete_Downvoted(Dislike_Ratio=10):
    Black_List_ID=[]
    for data in Reaction_Feedback(Prev_Time_Channel()):
        if data[-1] > Dislike_Ratio*data[-2]:
            Delete_Previous([[data[0], data[1]]])
            Black_List_ID.append(data[2])
    return Black_List_ID


Remove_Black_List(Delete_Downvoted(1))