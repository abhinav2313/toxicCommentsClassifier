import re

def Cleaner(input_text):
    
    
    stops = ['\n', '!', '?']
    
    output_text = input_text
    for stop in stops:
        output_text = output_text.replace(stop, '. ')
    
    junks = "-\'=$%@#^,[]/><+—`~"
    for junk in junks:
        output_text = output_text.replace(junk, '')
    
    output_text = output_text.replace('"', '')
    
    output_text = output_text.lower()
    
    #march/may is minorly problematic
    words = ['january','february','march','april',' may ','june','july','august','september','october','november','december', '(utc)', 'contribs', '(talk)']
    for word in words:
        output_text = output_text.replace(word, '')
    #problem with regex: "asshole.jpg" would pass
    
    regexs01 = ['http.*?(\s|$)', '(\d+[.])+\d+', '(\S*)\s*$', '\d+:\d+'] 
    #urls, ip addresses or floats, parentheses at end of string, times ##:##, 
    
    for regex in regexs01:
        output_text, _ = re.subn(r''+ regex, '', output_text)
    
    #regexs that are not simple replacements
    regexs02 = [ '(?:\w)(:|;)', '[(]\S\S', '\S\S[)]', '([.]\s*)+[.]'] 
    
    output_text, _ = re.subn(r'([.]\s*)+[.]', '.', output_text) #grouped periods
    #output_text, _ = re.subn(r'(?:\w)(:|;)', '', output_text) #text: -> text

    
    #remove filenames, "youreanasshole.jpg" would pass without triggering net
    options = '('
    extensions = ['jpg','zip','jpeg','png','tar','mpg','jpeg', 'svg']
    for extension in extensions:
        options += extension + '|'
    options = options[:-1]
    options += ')'
    
    search_string = '\s\S+?[.]' + options
    
    output_text, _ = re.subn(r''+ search_string, '', output_text)
        
    return output_text