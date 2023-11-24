def to_minutes(hours):
    return int(hours * 60)

def to_hours(minutes):
    return 0 if minutes == 0 else round(minutes / 60, 4)