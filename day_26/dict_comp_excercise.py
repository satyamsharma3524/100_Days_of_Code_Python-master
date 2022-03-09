temp_c = {
    'monday': 12,
    'tuesday': 14,
    'wednesday': 15,
    'thursday': 14,
    'friday': 21,
    'saturday': 22,
    'sunday': 24
}

temp_f = {day: (temp*9/5)+32 for (day, temp) in temp_c.items()}
print(temp_f)
