from models import Playlist,Song,PlaylistSong,db
from app import app

db.drop_all()
db.create_all()

song1 = Song(title="Shop Around",artist="Berry Gordy")
song2 = Song(title="Buddy Holly",artist="Rivers Cuomo")
song3 = Song(title="Miss You",artist="Keith Richards")
song4 = Song(title="The Rising",artist="Springsteen")

db.session.add(song1)
db.session.add(song2)
db.session.add(song3)
db.session.add(song4)
db.session.commit()


playlist1 = Playlist(name="workout",description="music that is happen when workout")
playlist2 = Playlist(name="study",description="music listen when study")
playlist3 = Playlist(name="commate",description="music listen when work off")

db.session.add(playlist1)
db.session.add(playlist2)
db.session.add(playlist3)
db.session.commit()


play_song1 = PlaylistSong(playlist_id = 1,song_id=1)
play_song2 = PlaylistSong(playlist_id = 1,song_id=2)
play_song3 = PlaylistSong(playlist_id = 2,song_id=3)
play_song4 = PlaylistSong(playlist_id = 3,song_id=4)

db.session.add(play_song1)
db.session.add(play_song2)
db.session.add(play_song3)
db.session.add(play_song4)
db.session.commit()