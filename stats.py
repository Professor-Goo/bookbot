import re
from collections import Counter

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(dict_item):
    return dict_item["num"]

def get_chars_report(chars_dict):
    chars_list = []
    for char in chars_dict:
        if char.isalpha():
            chars_list.append({"char": char, "num": chars_dict[char]})
    
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list

# NEW ENHANCED STATISTICS FUNCTIONS

def get_sentence_count(text):
    """Count sentences based on sentence-ending punctuation."""
    sentences = re.split(r'[.!?]+', text)
    # Filter out empty strings and very short fragments
    sentences = [s.strip() for s in sentences if s.strip() and len(s.strip()) > 1]
    return len(sentences)

def get_paragraph_count(text):
    """Count paragraphs based on double newlines."""
    paragraphs = text.split('\n\n')
    # Filter out empty paragraphs
    paragraphs = [p.strip() for p in paragraphs if p.strip()]
    return len(paragraphs)

def get_unique_word_count(text):
    """Count unique words (case-insensitive)."""
    words = re.findall(r'\b\w+\b', text.lower())
    return len(set(words))

def get_average_word_length(text):
    """Calculate average word length."""
    words = re.findall(r'\b\w+\b', text)
    if not words:
        return 0
    total_length = sum(len(word) for word in words)
    return round(total_length / len(words), 2)

def get_reading_time(text, wpm=200):
    """Estimate reading time in minutes (default 200 words per minute)."""
    word_count = get_num_words(text)
    minutes = word_count / wpm
    return round(minutes, 1)

def get_most_common_words(text, top_n=10):
    """Get the most common words with their frequencies."""
    words = re.findall(r'\b\w+\b', text.lower())
    # Filter out very short words (like 'a', 'an', 'the')
    words = [word for word in words if len(word) > 2]
    word_counts = Counter(words)
    return word_counts.most_common(top_n)

def get_comprehensive_stats(text):
    """Get all statistics in one convenient function."""
    stats = {
        'word_count': get_num_words(text),
        'unique_words': get_unique_word_count(text),
        'sentence_count': get_sentence_count(text),
        'paragraph_count': get_paragraph_count(text),
        'average_word_length': get_average_word_length(text),
        'reading_time_minutes': get_reading_time(text),
        'character_frequency': get_chars_report(get_chars_dict(text)),
        'most_common_words': get_most_common_words(text)
    }
    return stats