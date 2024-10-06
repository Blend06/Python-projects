import pytube
import os

try:
    link = input('Enter the YouTube video link: ')
    print(f"Link provided: {link}") 
    
    yt = pytube.YouTube(link)

    # Get the highest resolution stream available
    stream = yt.streams.get_highest_resolution()

    # Get the desktop path
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

    # Download the video to the desktop
    stream.download(output_path=desktop_path)

    print(f'Downloaded: {yt.title} to {desktop_path}')
except pytube.exceptions.RegexMatchError:
    print("Invalid YouTube URL. Please try again.")
except Exception as e:
    print(f"An error occurred: {e}")
