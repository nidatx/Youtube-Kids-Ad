from googleapiclient.discovery import build
from json import loads,dumps
import time


def GetVideosFromChannel(api_key,channel_id):
    # This function gets the 10 most popular videos from the channel and writes them into a text file 'videos.txt'
    # Arguments: 
    #           api_key (string): Your api key to be used to make requests
    #           channel_id (string): The channel id of the Youtube Channel
    youtube = build('youtube','v3',developerKey=api_key)
    
    request = youtube.search().list(
        part="snippet",
        channelId=channel_id,
        maxResults=10,
        order="viewCount",
        regionCode="US",
        type = "video"
    )
    response = request.execute()
    
    # print(dumps(response,sort_keys=True,indent=4))
    
    
    file_name = "vidoes.txt"
    file = open(file_name,'a')

    count = 0
    for vid in response["items"]:
        videoID = (vid['id']['videoId'])
        count=count+1
        
        if count ==10:
            file.write(videoID)
        else:
            file.write(videoID+',')
        
    
    file.write('\n')
    file.write('\n')
    
def GetChannelName(api_key,channelID):
    # This function gets the channel name given the channel ID and writes it into the videos.txt file
    # (Intermediate function for formatting purposes)
    # Arguments: 
    #           api_key (string): Your api key to be used to make requests
    #           channel_id (string): The channel id of the Youtube Channel
    youtube = build('youtube','v3',developerKey=api_key)
    
    request = youtube.channels().list(
        part="snippet",
        id = channelID
    )
    response = request.execute()
    
    
    channel_title = response['items'][0]['snippet']['title']
    
    file_name = "vidoes.txt"
    file = open(file_name,'a')
    file.write(channel_title+" : "+channelID)
    file.write('\n')


def main():
    
    key = "your api key"
    
    # populate this list with the channel IDs
    channel_list = [
        
    ]
    
    for i in range(0,5):
        GetChannelName(key,channel_list[i])
        GetVideosFromChannel(key,channel_list[i])
        time.sleep(2)
        
    
    
        

if __name__ == "__main__":
    main()