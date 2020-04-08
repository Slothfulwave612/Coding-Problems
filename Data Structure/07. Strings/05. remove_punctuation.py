## Removing punctuations from a given string

def remove_punctuations(string):
    '''
    Function removes punctuations from the string.

    Argument:
    string -- str, string having punctuations.

    Return:
    string -- str, string having no punctuations.
    '''
    punctautions = '''!"#$%&'()*+,-./:;?@[]\^_`{}|~'''

    for word in string:
        if word in punctautions:
            string = string.replace(word, '')
        
    return string

string = "Hello!!!, he {said ---and} went."
print(remove_punctuations(string))
