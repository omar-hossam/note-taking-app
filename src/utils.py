def greeting(hour, fname):
        if hour > 4 and hour < 12:
                return f"Good Morning {fname} ☀️"
        elif hour >= 12 and hour < 17:
                return f"Good Afternoon {fname} ❤️"
        elif hour >= 17 and hour < 20:
                return f"Good Evening {fname} ☺️"
        else:
                return f"Good Night {fname} 🥰"
