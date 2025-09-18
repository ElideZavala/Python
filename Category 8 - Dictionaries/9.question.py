# Get the key of a minimum value from the following dictionary

sample_dict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}

# get_minimun = {k: v for (k,v) in sample_dict.items() if v == min(v)}
get_minimun = min(sample_dict.values())
get_key = {k: v for (k,v) in sample_dict.items() if v == get_minimun}

get_key2 = {k: v for (k,v) in sample_dict.items() if v == min(sample_dict.values())}

print(get_key2)
print(get_key)

