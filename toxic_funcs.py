import re

def Cleaner(input_text):
    
    #@TODO: add curse counter before further cleaning
    #@TODO: address colons, semicolons, parens
    
    #period placeholders
    stops = ['\n', '!', '?', '\r', '\t']
    
    output_text = input_text
    for stop in stops:
        output_text = output_text.replace(stop, '. ')
    
    #lower for further matching
    output_text = output_text.lower()
    
    #@TODO: add smiley detector with replacement by 'smileyemote' or something, would allow simple symbol replacer
    #@TODO: add curse counter before further cleaning
    #@TODO: address colons, semicolons, parens

    
    #symbols to be removed
    junks = "\'$%@#^,[]/><`~|•·" #might want - here
    for junk in junks:
        output_text = output_text.replace(junk, '')
        
    space_junks = "-=+—" #symbols that can/often form word dividers
    for junk in space_junks:
        output_text = output_text.replace(junk, ' ')
        
    output_text = output_text.replace('"', '')
        

    '''#alternative symbol rejector, slower for current number of junk symbols, scales better though
    symbols_to_keep = ' ().:;'
    new_string = ''
    for char in output_text:
        if char.isalpha():
            new_string += char
        elif char in symbols_to_keep:
            new_string += char'''
    
    
    #simple words that have no bearing on analysis
    #march/may is minorly problematic
    words = ['january','february','march','april',' may ','june', ' jun ','july','august','september','october','november','december', '(utc)', 'contribs', '(talk)']
    for word in words:
        output_text = output_text.replace(word, '')
    new_string = ''    
    

    
    #easy regex replacements 
    regexs01 = ['http.*?(\s|$)', '(\d+[.])+\d+', '[(]\S*[)]\s*$', '\d+:\d+', '\d+'] 
    #urls, ip addresses or floats, parentheses at end of string, times ##:##, nums, 
    
    for regex in regexs01:
        output_text, _ = re.subn(r''+ regex, '', output_text)
    
    
    #regexs that are not simple replacements
    regexs02 = [ '(?:\w)(:|;)', '[(]\S\S', '\S\S[)]'] 
    
    output_text, _ = re.subn(r'([.]\s*)+[.]', '. ', output_text) #grouped periods

    
    '''    #removes specific filetypes, "youreanasshole.jpg" would pass without triggering net
    options = '('
    extensions = ['jpg','zip','jpeg','png','tar','mpg', 'svg', 'ogv']
    for extension in extensions:
        options += extension + '|'
    options = options[:-1] #remove last |
    options += ')'
    
    search_string = '\s\S+?[.]' + options
    
    output_text, _ = re.subn(r''+ search_string, '', output_text)'''
    
    #alternate file replacer, might be too general
    #can be stuck into regexs01
    output_text, _ = re.subn(r'\b\S+?[.]\S\S\S\b', '', output_text)
        
    return output_text

def PossibleCombination():
    possibleCombin = ["toxic", "toxicsevere_toxic", "toxicsevere_toxicobscene", "toxicsevere_toxicobscenethreat", "toxicsevere_toxicobscenethreatinsult", "toxicsevere_toxicobscenethreatinsultidentity_hate", "toxicsevere_toxicobscenethreatidentity_hate", "toxicsevere_toxicobsceneinsult", "toxicsevere_toxicobsceneinsultidentity_hate", "toxicsevere_toxicobsceneidentity_hate", "toxicsevere_toxicthreat", "toxicsevere_toxicthreatinsult", "toxicsevere_toxicthreatinsultidentity_hate", "toxicsevere_toxicthreatidentity_hate", "toxicsevere_toxicinsult", "toxicsevere_toxicinsultidentity_hate", "toxicsevere_toxicidentity_hate", "toxicobscene", "toxicobscenethreat", "toxicobscenethreatinsult", "toxicobscenethreatinsultidentity_hate", "toxicobscenethreatidentity_hate", "toxicobsceneinsult", "toxicobsceneinsultidentity_hate", "toxicobsceneidentity_hate", "toxicthreat", "toxicthreatinsult", "toxicthreatinsultidentity_hate", "toxicthreatidentity_hate", "toxicinsult", "toxicinsultidentity_hate", "toxicidentity_hate", "severe_toxic", "severe_toxicobscene", "severe_toxicobscenethreat", "severe_toxicobscenethreatinsult", "severe_toxicobscenethreatinsultidentity_hate", "severe_toxicobscenethreatidentity_hate", "severe_toxicobsceneinsult", "severe_toxicobsceneinsultidentity_hate", "severe_toxicobsceneidentity_hate", "severe_toxicthreat", "severe_toxicthreatinsult", "severe_toxicthreatinsultidentity_hate", "severe_toxicthreatidentity_hate", "severe_toxicinsult", "severe_toxicinsultidentity_hate", "severe_toxicidentity_hate", "obscene", "obscenethreat", "obscenethreatinsult", "obscenethreatinsultidentity_hate", "obscenethreatidentity_hate", "obsceneinsult", "obsceneinsultidentity_hate", "obsceneidentity_hate", "threat", "threatinsult", "threatinsultidentity_hate", "threatidentity_hate", "insult", "insultidentity_hate", "identity_hate", ""]
    return possibleCombin



