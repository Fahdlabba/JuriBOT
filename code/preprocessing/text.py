
def preprocessText(text):
    #remove any special characters
    text = ''.join(e for e in text if e.isalnum() or e.isspace())
    return text