from pytube import YouTube

# Get the YouTube video URL from user input
url = input("Enter a link: ")

try:
    # Initialize the YouTube object
    yt = YouTube(url)

    # Get the highest resolution stream (fixed typo)
    stream = yt.streams.get_highest_resolution()

    print("Going on...")

    # Download the video
    stream.download()

    print("Completed")

except Exception as e:
    print(f"An error occurred: {e}")
