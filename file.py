def Cleaner(text):
    stops = ['\n', '...', '!', '?']
    end_text = text

    for stop in stops:
        end_text = end_text.replace(stop, '. ')
    
    junks = "-\'=$%@#^,[]/><:;+"
    nums="0123456789"
    
    for junk in junks:
        end_text = end_text.replace(junk, '')
    
    for num in nums:
        end_text = end_text.replace(num, '')


    end_text = end_text.replace('"', '')
    
    regexs = ['http*htm.', ]
    for regex in regexs:
        pass
    
    return end_text