from collections import defaultdict
def counter():
    i=0
    while True:
        yield i
        i+=1
def solution(genres,plays):
    play_count=defaultdict(int)
    song=defaultdict(list)
    
    for song_id,genre,play in zip(counter(),genres,plays):
        play_count[genre]+=play
        song[genre].append((-play,song_id))
    
    genre_in_order = sorted(play_count.keys(), key=lambda g:play_count[g], reverse=True)
    
    answer=list()
    for genre in genre_in_order:
            print(genre)
            answer.extend([ song_id for minus_play, song_id in sorted(song[genre])[:2]])
    return answer