from Scrapper import *
from Slack_Intigrater import *
from database import *

Message_Data = contain_url(get_updates())

Serve_Slack(Message_Data)

Add_to_Sheets(Message_Data)                 ## Adds the message and metadata to google sheet
