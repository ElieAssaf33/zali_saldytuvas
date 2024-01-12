def group_album(info, group, album):
    info[group] = album
    return info
def song(song_name, song_length, songs):
    songs[song_name] = song_length
    return songs
def remove_song(track, songs):
    del songs[track]
    return songs
def change_album_name(info, album, group, new_album):
    del album
    info[group] = new_album
    return info
def change_group_name(info, album, group, new_group):
    del group
    info[new_group] = album
    return info
def remove_album_name(info, album):
    del album
    info[group] = "Group/artist has no albums"
    return info
def remove_group_name(info, group):
    del group
    info["You dont have any groups/artists"]= "You dont have any albums"
    return info

songs = {}
info = {}
track = 
while True:
    print("""

|Meniu for album|

0 - exit
1 - add album
2 - add song
3 - remove song
4 - change album name
5 - change group name
6 - remove album
7 - remove group
8 - print album information
""")

    choice = input("Enter a number: ")
    if choice.startswith('0'):
        ("Bye bye! have a nice day :)")
        break
    elif choice.startswith('1'):
        group = input("Please enter the name of the group or artist: ")
        album = input("Pleae enter name of the album: ")
        info = group_album(info, group, album)
    elif choice.startswith('2'):
        song_name = input("Enter song: ")
        song_length = input("Enter the length of the song: ")
        songs = song(song_name, song_length, songs)
    elif choice.startswith('3'):
        print(songs)
        track = input("Choose song number from above: ")
        songs = remove_song(track, songs)
    elif choice.startswith('4'):
        print(info)
        album = input("Choose an album from above: ")
        new_album = input("Enter the changed name of the album: ")
        info = change_album_name(info, album, group, new_album)
    elif choice.startswith('5'):
        print(group)
        group = input("Choose a group from above: ")
        new_group = input("Enter the changed name of the group: ")
        info = change_group_name(info, album, group, new_group)
    elif choice.startswith('6'):
        print(album)
        album = input("Choose a album you would like to remove from above")
        info = remove_album_name(info, album)
    elif choice.startswith('7'):
        print(group)
        group = input("Choose a group or artist you would like to delete from above: ")
        info = remove_group_name(info, group)
    elif choice.startswith('8'):
        for key, value in info.items():
            print(f"""\n
            |Album info|\n
Group/Artist: {key}\n
Album: {value}""")              
        print("Songs:\n")
        for key, value in songs.items():
            print(f"{track}{key} {value}")


"""
         
      
            
       