def make_album(singer_name, album_name, song_number= None):
    """歌手的名字和专辑名"""
    album_dict = {"singer_name": singer_name.title(),
                  "album_name": album_name.title(),
                  }
    if song_number:
        album_dict['song_number'] = song_number
    return album_dict

album = make_album('lifei','wangfei')
print(album)


album = make_album('zhang','tell','7')
print(album)