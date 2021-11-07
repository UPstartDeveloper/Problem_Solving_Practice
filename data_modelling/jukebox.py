"""
Cracking the coding Intervew 7.3

Jukebox: Design a musical jukebox using object-oriented principles.

pretend:
    JB = HomePod
    songs db = iTunes
    

1. Scope:
    - who?
        - consumers
        - family activity - using the JB at home
        - ASSUME:
            - Skateboard: only one can access the homepod, 1 speaker
            - Bike: multi-user access, screen
            - Car: multi-speaker access, home annoucementd
    - what?
        - play songs 
        - searching for songs
        - purchase a songs 
        - CRUD of songs ----> RU
        - ASSUME we leave albums, audiobook out of scope
    - why?
        - holiday parties
        - birthdays
        - study music, work music, workout music
    - how?
        - JB: has 1 speaker
        - internet connection
        - sync w/ someone's iTunes account
        - charge w/ a lighting cable
        - volume setting

2. Core objects:

    1. Audio:

        Recording:
            TODO
    
        Song
            TODO

    2. User
        account_id: int --> iTunesAccount
        recordings: List[Audio]
        jb_serial_id: int --> JukeBox

        a) AdminUser
            home_users: List[Homebox]

        b) HomeUser: TODO

    3. JukeBox
        - volume_level: float
        - battery_level: float
        - play(audio: Audio) -> None
        - getInternetStatus() -> response

    4. iTunes Account (leave it out, assume APIs available)

3. Relationships:

    User <-------- JB
     |
     |
     |
     Account ----> Song

    
"""
