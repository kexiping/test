def make_album(singer_name, album_name, song_number=None):
    """创建一个包含专辑信息的字典"""
    album_dict ={"singer_name": singer_name.title(),
                 "album_name": album_name.title()
                 }
    if song_number:
        album_dict['song_number'] = song_number
    return album_dict

#生成提示语
album_prompt = "\n What album are you thinking of?"
singer_prompt = "Who's the singer?"

 #让用户知道如何退出
print("Enter 'q' at any time to stop.")

while True:
    album_name = input(album_prompt)
    if album_name == 'q':
        break
    
    singer_name = input(singer_prompt)
    if singer_name == 'q':
        break
    
    album = make_album(singer_name, album_name)
    print(album)
    
print("\nThanks for responding!")
    