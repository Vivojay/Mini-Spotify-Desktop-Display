# Mini-Spotify-Desktop-Display

Mini Desktop Display for displaying the currently playing Spotify song.

This is a **mini widget/window** which displays the currently playing Spotify **song** along with the **artist's name**. It also shows a small, excessively-wide (*working on it*) non-interactable **progress bar** and a cute little art cover image taken directly from the **[spotipy api](https://developer.spotify.com/)** (Yup, that wasn't a spelling error).

By default this widget has some transparency effect which can be tweaked in the settings along with other personal touches.

## Settings

This app contains some working and some non-operational settings as of now.

List of working settings are as follows:

| Setting                    | Valid Values                                                 | Description                                                  |
| -------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **classicColorSchemeOnly** | **0** or **1**<br /><br />*Default value: 1*                 | Does nothing when set to **0**.<br />Forces the default classic color scheme if set to **1**.<br /><br />*Reports an error if set to anything else*<br />(Overrides colorScheme) |
| **colorScheme**            | Name of a predefined color scheme taken from "**Themes.json**" file<br />*(or the bespoke "**colorSchemeFile**" defined in the settings)* (SEE NEXT) | Sets color scheme to the provided value if it is [valid](color_scheme_validation).<br />(Only valid if *classicColorSchemeOnly = 0*) |
| **colorSchemeFile**        | Any file path as long as it is valid<br />**(Always put path in double-quotes)** | This is the *[relative path](relative_path)* of the **themes file**.<br /><br />*Default value: "Themes.json"* |
| **alwaysOnTop**            | **0** or **1**<br /><br />*Default value: 1*                 | Sets display to **Always-On-Top** if set to **1**.           |
| **overrideOpacity**        | **allow**: **0** or **1**<br />**value**: Any [whole number](whole_number_footnote) from **0 to 100** (Only valid if *allow = 1*)<br /><br />*Default value: 0* | Set custom opacity<br />100%** makes widget **opaque**,<br />**0%** makes it fully **transparent**.<br /><br />(Default is 40% opacity for all color schemes except "Classic" for which it is 60%)<br /> |
| **windowDimensions**       | **"(width)x(height)"**. E.g. **"200x300"** sets width to 200 pixels and height to 300 pixels <br /><br />*Default value: "204x350"* | Sets dimensions of the widget's window.                      |
| **imageSize**              | Any number (preferably between 100 to 400, but **depends on windowDimensions**)<br /><br />*Default value: 200* | Sets the size of the image (Spotify track's art cover) in **pixels** (Preferably smaller than the width of the window in pixels) |



## Some ambitious future goals and unimplemented features

Ok, actually a LOT of them...

Here's a list of them:

- Features:
    - For the user (Appearance):
        - Display
            - Artist Name
            - Song Name
            - Track Cover
            - Toggleable Dynamic BgColor (Inherits Color theme from current track's cover art)
            - Toggleable Dyamic TextColor = Complement of Current [So that it is clearly visible]
            - A visualizer of sorts
            - Release Year [Possibly, exact date]
            - Volume value display (Probably not reqd., will be replaced by on-widget volume controller)
            - Background Blur/Gradient Background (Toggleable (in settings))
            - Progress time display ("Remaining" and "Elapsed")

        - Controls
            - Playback Seek
            - Play/Pause/Next/Prev
            - Like/Unlike
            - Song/Album/Playlist Repeat Toggle
            - Volume Control (Slider/Knob)
            - Double-Click/Play-Pause Button on window = play/pause

        - Others:
            - Listening Habits from Scrobbled songs/artist [Get from both lastFM and Spotify...]
            - Quicker Image Load [If possible]
            - Option to start on boot (Some registry setting?)

- Keep log of (Only if user allows):
    - Artist,
    - Song Name,
    - Song ID,
    - Artist ID,
    - Date,
    - Time,
    - Genre,

          \# The following is perceived as sensitive information by a lot of OSS users
        - Location of listener's device (Using IP location services like ipinfo.io, etc...),
        - Established location of artist

- Calculations/Analysis:
    - Total Songs heard overall
    - Total Songs heard per Artist
    - For a given timeframe (E.g. Day, Month, Year, All Time):
        - Total Songs heard
        - Total Songs heard per Artist

    - Show max play count of:
        - Artist
        - Song

    - Average time spent listening to (per day):
        - Artist
        - Song
        - Location's Songs/Artist
