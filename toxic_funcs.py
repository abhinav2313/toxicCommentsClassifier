def Cleaner(text):
    stops = ['\n', '...', '!', '?']
    end_text = text
    for stop in stops:
        end_text = end_text.replace(stop, '. ')
    
    junks = "-\'=$%@#^,[]/><:;+"
    for junk in junks:
        end_text = end_text.replace(junk, '')
    
    end_text = end_text.replace('"', '')
    
    regexs = ['http*htm.', ] #
    for regex in regexs:
        pass
    
    return end_text