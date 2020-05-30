from Slack_Intigrater import *
from database import *

def Delete_Downvoted(Dislike_Ratio=10):
    for data in Reaction_Feedback(Prev_Time_Channel()):
        print(data)
        if data[-1] > Dislike_Ratio*data[-2]:
            Delete_Previous([[data[0], data[1]]])

Delete_Downvoted(1)