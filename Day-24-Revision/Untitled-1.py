class Song:
    def __init__(self, title: str, artist: str, duration_sec: int):
        self.title = title
        self.artist = artist
        self.duration_sec = duration_sec

    # Magic Method for printing readable info
    def __str__(self):
        minutes = self.duration_sec // 60
        seconds = self.duration_sec % 60
        return f"🎵 {self.title} - {self.artist} ({minutes}:{seconds:02d})"


class Playlist:
    def __init__(self, name: str):
        self.name = name
        self.songs = []

    def add_song(self, song: Song):
        self.songs.append(song)
        print(f"[+] Added: {song.title}")

    # Magic Method to use len(playlist)
    def __len__(self):
        return len(self.songs)

    # Magic Method to print the whole playlist nicely
    def __str__(self):
        header = f"\n=== Playlist: {self.name} ({len(self)} songs) ===\n"
        song_list = "\n".join(str(song) for song in self.songs)
        return header + (song_list if self.songs else "Playlist is empty.")


if __name__ == "__main__":
    my_playlist = Playlist("Coding Vibes")

    s1 = Song("Midnight City", "M83", 243)
    s2 = Song("Starboy", "The Weeknd", 230)

    my_playlist.add_song(s1)
    my_playlist.add_song(s2)

    # Direct print because of __str__
    print(my_playlist)

    # Direct len() because of __len__
    print(f"\nTotal songs count: {len(my_playlist)}")