import subprocess
import time

def get_safari_tabs():
    """Uses AppleScript to get the titles of active tabs in all open Safari windows and close tabs with YouTube Shorts."""
    safari_script = """
    tell application "Safari"
        set window_count to count of windows
        if window_count > 0 then
            repeat with i from 1 to window_count
                set tab_url to URL of current tab of window i
                if tab_url contains "youtube.com/shorts" then
                    close window i
                    return "Closed Safari window " & i & " with YouTube Shorts"
                else
                    set window_name to name of current tab of window i
                    return "Safari - Window " & i & ": " & window_name & " (" & tab_url & ")"
                end if
            end repeat
        else
            return "no safari"
        end if
    end tell
    """
    
    try:
        result = subprocess.run(['osascript', '-e', safari_script], capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        return f"Error in Safari tracking: {str(e)}"


def get_chrome_tabs():
    """Uses AppleScript to get the titles of active tabs in all open Chrome windows and close tabs with YouTube Shorts."""
    chrome_script = """
    tell application "Google Chrome"
        set window_count to count of windows
        if window_count > 0 then
            repeat with i from 1 to window_count
                set tab_url to URL of active tab of window i
                if tab_url contains "youtube.com/shorts" then
                    close window i
                    return "Closed Chrome window " & i & " with YouTube Shorts"
                else
                    set window_name to get title of active tab of window i
                    return "Chrome - Window " & i & ": " & window_name & " (" & tab_url & ")"
                end if
            end repeat
        else
            return "No crhome bro"
        end if
    end tell
    """
    
    try:
        result = subprocess.run(['osascript', '-e', chrome_script], capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        return f"Error in Chrome tracking: {str(e)}"



def track_browsers():
    """GSTEALS UR FUCKING INFORMATION BITCH"""
    while True:
        # Check Safai for yt 
        safari_tabs = get_safari_tabs()
        print(safari_tabs)
        
        # Check Chrome for YouTube Shorts
        chrome_tabs = get_chrome_tabs()
        print(chrome_tabs)

        
        
        
        time.sleep(5)  # Wait for 2 seconds before checking again



if __name__ == "__main__":
    track_browsers()

