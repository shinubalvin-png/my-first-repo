from plyer import notification
import time

while True:
    notification.notify(
         title="Hydration Reminder 💧",
        message="पानी पी लो and stay hydrated!",
        timeout=5  # notification कितनी देर दिखेगा (seconds)
    )
    time.sleep(1600)  # हर 1 घंटे बाद reminder (3600 seconds)

