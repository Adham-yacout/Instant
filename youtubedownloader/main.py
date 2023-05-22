import os
from pytube import YouTube

# Provide the YouTube video URL
try:
    video_url = input('please enter the video link you want to download')
    # Create a YouTube object
    yt = YouTube(video_url)
    # Get the available streams and their resolutions
    streams = yt.streams.filter(progressive=True)
    resolutions = [stream.resolution for stream in streams]
    # Prompt the user to choose a resolution
    print("Available Resolutions:")
    for resolution in resolutions:
        print(f" {resolution}")
    # Validate user input
    resolution_choice = None
    while not resolution_choice:
        try:
            choice = (input("Enter the required resolution: "))
            if choice in resolutions:
                resolution_choice = choice
            else:
                print('invalid resolution')
        except ValueError:
            print("Invalid choice. Please enter a valid number.")
    # Get the selected stream
    selected_stream = None
    for stream in streams:
        if stream.resolution == resolution_choice:
            selected_stream = stream
            break
    if selected_stream is None:
        print("Selected stream not found.")
    else:
        # Download the video
        output_path = os.path.join(os.path.expanduser("~"), "Downloads")
        print("Downloading video...")
        selected_stream.download(output_path=output_path, filename=yt.title + ".mp4")
        print("Download completed!")
except:
    print('invalid link')
