"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""

    # ADD THE NECESSARY CODE HERE
    __tablename__ = "playlist"

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)

    name = db.Column(db.Text,nullable=False)

    description = db.Column(db.Text,nullable=True)

    def __repr__(self):
        return f"playlist id {self.id} and name: {self.name}"


class Song(db.Model):
    """Song."""

    # ADD THE NECESSARY CODE HERE
    __tablename__ = "songs"

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)

    title = db.Column(db.Text,nullable=False)

    artist = db.Column(db.Text,nullable=False)

    def __repr__(self):
        return f"song id {self.id} and it's title: {self.title}"

    playlists = db.relationship("Playlist",secondary="playlist_song",backref="songs")


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    # ADD THE NECESSARY CODE HERE

    __tablename__ = "playlist_song"

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)

    playlist_id = db.Column(db.Integer,db.ForeignKey("playlist.id"),primary_key=True)

    song_id = db.Column(db.Integer,db.ForeignKey("songs.id"),primary_key=True)


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)
