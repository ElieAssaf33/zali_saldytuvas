def songInfo(song, lenght):
    songs[song] = length
    return songs
songs = {}
while True:
    print("""  
        Welcome back!

What would you like to do?
0 - exit
1 - add album
2 - add song
3 - display album information

""")
    choise = input("Please enter a number: ")
    if choise.startswith('0'):
        print("See you next time!")
        break
    elif choise.startswith('1'):
        group = input("Enter the name of the group: ")
        album = input("Enter the name of the album: ")
    elif choise.startswith('2'):
        song = input("Enter the name of the song: ")
        length = input("Enter the length of the song: ")
        length = float(length)
        songs = songInfo(song,length)
    elif choise.startswith('3'):
        print(f"""
Group name: {group}
Album name: {album}
Songs: {songs}
""")

   
