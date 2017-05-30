# drEdsby
For years, the Edsby interface has had the same old, drab, and non-responsive interface that is unintuitive to use. I've set out to create a better version of the Edsby interface, relying heavily on the PyEdsby project (credit: @ctrezevant for starting the project) which I am a part of.  
The goal of this project is to revitalize the Edsby interface while retaining all existing functionality of the native Edsby interface.  
## Security
- For security purposes, the Django SECRET\_KEY has been excluded from `settings.py`. A file called `settings_secret.py` must be created in the same directory as `settings.py`. All files/directories containing _secret_ are excluded from git for this very purpose.  
- As an login interface does not yet exist in drEdsby, the Edsby instance URL, username, and password must be added to the `config.ini` that is created in the project's root the first time it is run. As these are stored in plaintext, all *.ini files are also excluded from git.
## To-Do
- [ ] Main view
    - [ ] Activity feed
        - [ ] Full compatibility with attendance
        - [ ] Assignment preview
        - [ ] Assignment download
            - [ ] Proxy
        - [ ] Assignment submission
        - [ ] Assignment of assignments
    - [ ] Schedule
        - [x] Color-coding for attendance
        - [x] Collapsible to allow for calendar/events to be included in the same area
        - [ ] Fixed persistently to side
    - [ ] Class quick-view
        - Class menu items expand to show more information about the class, including average, teacher, room number, etc. (perhaps the most recent post)
- [ ] Class view
    - [ ] Class feed
        - More to come...  

_The Edsby trademark and brand are property of CoreFour, Inc. This software is unofficial and not supported by CoreFour in any way. I am not affiliated with CoreFour._