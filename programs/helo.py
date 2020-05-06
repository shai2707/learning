from pytube import YouTube

def main():
    youtube_url = input("Please enter url of youtube video of your choice:- ")
    yt_streams = YouTube(youtube_url).streams
    for index, st in enumerate(yt_streams):
        print(f'{index}) {st.mime_type} - {st.abr} - {st.resolution} - {st.type} - {st.video_codec}')
    selected_stream = int(input("Please enter your choice of format to download:- "))
    yt_streams[selected_stream].download()

main()
