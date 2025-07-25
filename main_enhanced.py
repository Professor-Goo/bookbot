import sys
import os
from stats import get_comprehensive_stats

def get_book_text(path):
    """Read text file with proper encoding handling."""
    try:
        with open(path, encoding='utf-8') as f:
            return f.read()
    except UnicodeDecodeError:
        try:
            with open(path, encoding='latin-1') as f:
                return f.read()
        except Exception as e:
            print(f"Error: Could not read file with UTF-8 or Latin-1 encoding: {e}")
            sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

def print_comprehensive_report(stats, filename):
    """Print a beautiful, comprehensive analysis report."""
    print("=" * 70)
    print("📚 BOOKBOT ENHANCED ANALYSIS REPORT")
    print("=" * 70)
    print(f"📖 File: {filename}")
    print()
    
    # Basic Statistics
    print("📊 BASIC STATISTICS")
    print("-" * 40)
    print(f"Total Words:          {stats['word_count']:,}")
    print(f"Unique Words:         {stats['unique_words']:,}")
    print(f"Sentences:            {stats['sentence_count']:,}")
    print(f"Paragraphs:           {stats['paragraph_count']:,}")
    print()
    
    # Reading Metrics
    print("📏 READING METRICS")
    print("-" * 40)
    print(f"Average Word Length:  {stats['average_word_length']} characters")
    print(f"Reading Time:         {stats['reading_time_minutes']} minutes")
    
    # Calculate additional metrics
    vocab_richness = (stats['unique_words'] / stats['word_count']) * 100
    words_per_sentence = stats['word_count'] / stats['sentence_count'] if stats['sentence_count'] > 0 else 0
    sentences_per_paragraph = stats['sentence_count'] / stats['paragraph_count'] if stats['paragraph_count'] > 0 else 0
    
    print(f"Vocabulary Richness:  {vocab_richness:.1f}% unique words")
    print(f"Words per Sentence:   {words_per_sentence:.1f}")
    print(f"Sentences per Para:   {sentences_per_paragraph:.1f}")
    print()
    
    # Character Analysis
    print("🔤 CHARACTER FREQUENCY ANALYSIS")
    print("-" * 40)
    print("Top 15 most frequent characters:")
    for i, char_info in enumerate(stats['character_frequency'][:15], 1):
        bar_length = int((char_info['num'] / stats['character_frequency'][0]['num']) * 30)
        bar = "█" * bar_length
        print(f"{i:2d}. '{char_info['char']}' {bar} {char_info['num']:,}")
    print()
    
    # Word Analysis
    print("📝 MOST COMMON WORDS")
    print("-" * 40)
    print("Top 15 most frequent words (3+ characters):")
    for i, (word, count) in enumerate(stats['most_common_words'][:15], 1):
        # Create a simple bar visualization
        max_count = stats['most_common_words'][0][1]
        bar_length = int((count / max_count) * 25)
        bar = "▓" * bar_length
        print(f"{i:2d}. {word:15} {bar} {count:,}")
    print()
    
    # Text Complexity Indicators
    print("🧠 TEXT COMPLEXITY INDICATORS")
    print("-" * 40)
    
    # Classify reading level based on average word length and sentence length
    if words_per_sentence < 10:
        complexity = "Simple"
    elif words_per_sentence < 15:
        complexity = "Moderate"
    elif words_per_sentence < 20:
        complexity = "Complex"
    else:
        complexity = "Very Complex"
    
    print(f"Estimated Complexity: {complexity}")
    
    if vocab_richness < 30:
        vocab_level = "Basic vocabulary"
    elif vocab_richness < 50:
        vocab_level = "Moderate vocabulary"
    elif vocab_richness < 70:
        vocab_level = "Rich vocabulary"
    else:
        vocab_level = "Very rich vocabulary"
    
    print(f"Vocabulary Level:     {vocab_level}")
    print()
    
    print("=" * 70)
    print("📈 TIP: Run 'python bookbot_gui.py' for visual charts and graphs!")
    print("=" * 70)

def main():
    """Main function for enhanced command-line BookBot."""
    if len(sys.argv) != 2:
        print("📚 BookBot Enhanced - Advanced Text Analysis Tool")
        print()
        print("Usage: python main_enhanced.py <path_to_book>")
        print()
        print("Features:")
        print("• Comprehensive text statistics")
        print("• Reading time estimation")
        print("• Character and word frequency analysis")
        print("• Text complexity indicators")
        print("• Vocabulary richness metrics")
        print()
        print("For visual charts and graphs, use: python bookbot_gui.py")
        sys.exit(1)
    
    book_path = sys.argv[1]
    
    # Check if file exists
    if not os.path.exists(book_path):
        print(f"Error: File '{book_path}' not found.")
        sys.exit(1)
    
    print("📚 BookBot Enhanced - Analyzing text...")
    print()
    
    # Read and analyze the text
    text = get_book_text(book_path)
    
    if not text.strip():
        print("Warning: The file appears to be empty.")
        sys.exit(1)
    
    # Get comprehensive statistics
    stats = get_comprehensive_stats(text)
    
    # Print the detailed report
    print_comprehensive_report(stats, os.path.basename(book_path))

if __name__ == "__main__":
    main() 