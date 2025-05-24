time_str = '1h 45m,36s,25m,30m 120s,2h 60s'
total_minutes = 0

for part in time_str.split(','):
    part = part.strip()
    for subpart in part.split():
        if 'h' in subpart:
            hours = int(subpart.replace('h', ''))
            total_minutes += hours * 60
        elif 'm' in subpart:
            minutes = int(subpart.replace('m', ''))
            total_minutes += minutes
        elif 's' in subpart:
            seconds = int(subpart.replace('s', ''))
            total_minutes += seconds // 60

print(total_minutes)