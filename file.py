import re

def Cleaner(input_text):
    
    #period placeholders
    stops = ['\n', '!', '?']
    
    output_text = input_text
    for stop in stops:
        output_text = output_text.replace(stop, '. ')
    
    
    #symbols to be removed
    junks = "-\'=$%@#^,[]/><+—`~"
    for junk in junks:
        output_text = output_text.replace(junk, '')
    output_text = output_text.replace('"', '')
    
    
    #lower for further matching
    output_text = output_text.lower()
    
    
    #@TODO: add curse counter before further cleaning
    
    
    #simple words that have no bearing on analysis
    #march/may is minorly problematic
    words = ['january','february','march','april',' may ','june','july','august','september','october','november','december', '(utc)', 'contribs', '(talk)']
    for word in words:
        output_text = output_text.replace(word, '')

    
    #easy regex replacements
    regexs01 = ['http.*?(\s|$)', '(\d+[.])+\d+', '(\S*)\s*$', '\d+:\d+', '\d+'] 
    #urls, ip addresses or floats, parentheses at end of string, times ##:##, nums
    
    for regex in regexs01:
        output_text, _ = re.subn(r''+ regex, '', output_text)
    
    
    #regexs that are not simple replacements
    regexs02 = [ '(?:\w)(:|;)', '[(]\S\S', '\S\S[)]', '([.]\s*)+[.]'] 
    
    output_text, _ = re.subn(r'([.]\s*)+[.]', '.', output_text) #grouped periods

    
    #remove filenames, "youreanasshole.jpg" would pass without triggering net
    #could be replaced by \s\S+?[.]\w\w\w\b
    options = '('
    extensions = ['jpg','zip','jpeg','png','tar','mpg','jpeg', 'svg']
    for extension in extensions:
        options += extension + '|'
    options = options[:-1]
    options += ')'
    
    search_string = '\s\S+?[.]' + options
    
    output_text, _ = re.subn(r''+ search_string, '', output_text)
        
    return output_text