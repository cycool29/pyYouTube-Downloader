import pytube as pt
from sty import *


# User search what video they want

print(fg.red + 'Search Query:' + fg.rs)
user_input = input("")
yt = pt.Search(user_input)

# Filter and show user the results
results_name = yt.completion_suggestions
results_length = len(results_name)

number = 0
new_results_name = ""
options_name = ""

if results_name == "None":
    print("Sorry, no results found")
    exit(0)

for string in results_name:
    number += 1
    options_name = str(number) + ". " + string + " \n"
    new_results_name = new_results_name + options_name
    new_results_name = new_results_name.title()


print(f"\nFound {results_length} results.\n")

print(new_results_name)

# Filter video ID
new_results_id = []

for string in yt.results:
    new_string = str(string).replace(
        "<pytube.__main__.YouTube object: videoId=", "")
    new_string = new_string.replace(">", "")
    new_results_id.append(new_string)

choose = input("Which one you want? ")
choose = int(choose) - 1
video_url = "https://www.youtube.com/watch?v=" + new_results_id[choose]
print(video_url)

# Choose resolution
resolutions_type = "360p", "720p", "1080p"
resolution = input("Which resolution you'd like to download? ")
if resolution not in resolutions_type:
    print("That is not a valid option.")
    exit(1)


# Download video
video = pt.YouTube(video_url)
where_to_save = input("\nWhere you want to save the video? [same folder] ")
video.streams.filter(res=resolution).first().download(where_to_save)
print("Downloaded.")
