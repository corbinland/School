import string

# Triple-quoted passage from *The Fellowship of the Ring*
text = """\
All we have to decide is what to do with the time that is given us."""

def analyze_text(text):
    # Remove punctuation
    text_no_punct = text.translate(str.maketrans('', '', string.punctuation))
    
    # Split into words
    words = text_no_punct.split()
    
    # Count total words and words containing 'e'
    total_words = len(words)
    e_words = [word for word in words if 'e' in word.lower()]
    num_e_words = len(e_words)
    
    # Calculate percentage
    percentage = (num_e_words / total_words) * 100 if total_words > 0 else 0
    
    # Print result
    print(f'Your text contains {total_words} words, of which {num_e_words} ({percentage:.1f}%) contain an "e".')

# Analyze the LOTR quote
analyze_text(text)
