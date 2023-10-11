import re

def solution(new_id):
    renewal = new_id.lower()
    clean_id = re.sub(r'[^a-z0-9-_.]','', renewal)
    clean_new_id = re.sub(r'\.{2,}','.',clean_id)
    
    if clean_new_id:
        if clean_new_id[0] == '.':
            clean_new_id = clean_new_id[1:]

        if clean_new_id and clean_new_id[-1] == '.':
            clean_new_id = clean_new_id[:-1]

    if clean_new_id == '':
        clean_new_id = 'a'
        
    if len(clean_new_id) >= 16:
        clean_new_id = clean_new_id[:15]
        if clean_new_id[-1] == '.':
            clean_new_id = clean_new_id[:14]
        
    if len(clean_new_id) <= 2:
        clean_new_id = clean_new_id + clean_new_id[-1] * (3 - len(clean_new_id))
        
    return clean_new_id