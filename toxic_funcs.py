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

def PossibleCombination():
    return ["toxic", "toxicsevere_toxic", "toxicsevere_toxicobscene", "toxicsevere_toxicobscenethreat", "toxicsevere_toxicobscenethreatinsult", "toxicsevere_toxicobscenethreatinsultidentity_hate", "toxicsevere_toxicobscenethreatidentity_hate", "toxicsevere_toxicobsceneinsult", "toxicsevere_toxicobsceneinsultidentity_hate", "toxicsevere_toxicobsceneidentity_hate", "toxicsevere_toxicthreat", "toxicsevere_toxicthreatinsult", "toxicsevere_toxicthreatinsultidentity_hate", "toxicsevere_toxicthreatidentity_hate", "toxicsevere_toxicinsult", "toxicsevere_toxicinsultidentity_hate", "toxicsevere_toxicidentity_hate", "toxicobscene", "toxicobscenethreat", "toxicobscenethreatinsult", "toxicobscenethreatinsultidentity_hate", "toxicobscenethreatidentity_hate", "toxicobsceneinsult", "toxicobsceneinsultidentity_hate", "toxicobsceneidentity_hate", "toxicthreat", "toxicthreatinsult", "toxicthreatinsultidentity_hate", "toxicthreatidentity_hate", "toxicinsult", "toxicinsultidentity_hate", "toxicidentity_hate", "severe_toxic", "severe_toxicobscene", "severe_toxicobscenethreat", "severe_toxicobscenethreatinsult", "severe_toxicobscenethreatinsultidentity_hate", "severe_toxicobscenethreatidentity_hate", "severe_toxicobsceneinsult", "severe_toxicobsceneinsultidentity_hate", "severe_toxicobsceneidentity_hate", "severe_toxicthreat", "severe_toxicthreatinsult", "severe_toxicthreatinsultidentity_hate", "severe_toxicthreatidentity_hate", "severe_toxicinsult", "severe_toxicinsultidentity_hate", "severe_toxicidentity_hate", "obscene", "obscenethreat", "obscenethreatinsult", "obscenethreatinsultidentity_hate", "obscenethreatidentity_hate", "obsceneinsult", "obsceneinsultidentity_hate", "obsceneidentity_hate", "threat", "threatinsult", "threatinsultidentity_hate", "threatidentity_hate", "insult", "insultidentity_hate", "identity_hate", ""]

