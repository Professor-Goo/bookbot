import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np
from collections import Counter
try:
    from wordcloud import WordCloud
    WORDCLOUD_AVAILABLE = True
except ImportError:
    WORDCLOUD_AVAILABLE = False

def create_character_frequency_chart(char_data, top_n=15):
    """Create a bar chart of character frequencies."""
    if not char_data:
        return None
    
    # Take only top N characters
    top_chars = char_data[:top_n]
    characters = [item['char'] for item in top_chars]
    frequencies = [item['num'] for item in top_chars]
    
    fig, ax = plt.subplots(figsize=(12, 6))
    bars = ax.bar(characters, frequencies, color='skyblue', edgecolor='navy', alpha=0.7)
    
    ax.set_xlabel('Characters', fontsize=12)
    ax.set_ylabel('Frequency', fontsize=12)
    ax.set_title(f'Top {len(characters)} Most Frequent Characters', fontsize=14, fontweight='bold')
    ax.grid(axis='y', alpha=0.3)
    
    # Add value labels on bars
    for bar, freq in zip(bars, frequencies):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + max(frequencies)*0.01,
                f'{freq:,}', ha='center', va='bottom', fontsize=10)
    
    plt.xticks(rotation=0)
    plt.tight_layout()
    return fig

def create_word_frequency_chart(word_data, top_n=10):
    """Create a horizontal bar chart of most common words."""
    if not word_data:
        return None
    
    words = [item[0] for item in word_data[:top_n]]
    frequencies = [item[1] for item in word_data[:top_n]]
    
    fig, ax = plt.subplots(figsize=(10, 8))
    y_pos = np.arange(len(words))
    
    bars = ax.barh(y_pos, frequencies, color='lightcoral', edgecolor='darkred', alpha=0.7)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(words)
    ax.invert_yaxis()  # Labels read top-to-bottom
    ax.set_xlabel('Frequency', fontsize=12)
    ax.set_title(f'Top {len(words)} Most Common Words', fontsize=14, fontweight='bold')
    ax.grid(axis='x', alpha=0.3)
    
    # Add value labels on bars
    for i, (bar, freq) in enumerate(zip(bars, frequencies)):
        width = bar.get_width()
        ax.text(width + max(frequencies)*0.01, bar.get_y() + bar.get_height()/2.,
                f'{freq:,}', ha='left', va='center', fontsize=10)
    
    plt.tight_layout()
    return fig

def create_statistics_overview(stats):
    """Create a visual overview of text statistics."""
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))
    
    # 1. Basic Stats
    basic_stats = ['Words', 'Unique Words', 'Sentences', 'Paragraphs']
    basic_values = [stats['word_count'], stats['unique_words'], 
                   stats['sentence_count'], stats['paragraph_count']]
    
    bars1 = ax1.bar(basic_stats, basic_values, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4'])
    ax1.set_title('Text Structure Statistics', fontweight='bold')
    ax1.set_ylabel('Count')
    
    # Add value labels
    for bar, value in zip(bars1, basic_values):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + max(basic_values)*0.01,
                f'{value:,}', ha='center', va='bottom')
    
    # 2. Reading Metrics
    metrics = ['Avg Word Length', 'Reading Time (min)']
    metric_values = [stats['average_word_length'], stats['reading_time_minutes']]
    
    bars2 = ax2.bar(metrics, metric_values, color=['#F7B731', '#5F27CD'])
    ax2.set_title('Reading Metrics', fontweight='bold')
    ax2.set_ylabel('Value')
    
    for bar, value in zip(bars2, metric_values):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + max(metric_values)*0.01,
                f'{value}', ha='center', va='bottom')
    
    # 3. Top Characters (pie chart)
    top_chars = stats['character_frequency'][:8]
    char_labels = [f"'{item['char']}'" for item in top_chars]
    char_sizes = [item['num'] for item in top_chars]
    
    ax3.pie(char_sizes, labels=char_labels, autopct='%1.1f%%', startangle=90)
    ax3.set_title('Character Distribution (Top 8)')
    
    # 4. Vocabulary Richness
    vocab_richness = (stats['unique_words'] / stats['word_count']) * 100
    ax4.pie([vocab_richness, 100-vocab_richness], labels=['Unique', 'Repeated'], 
            autopct='%1.1f%%', colors=['#FF6B6B', '#E0E0E0'])
    ax4.set_title(f'Vocabulary Richness\n({vocab_richness:.1f}% unique words)')
    
    plt.tight_layout()
    return fig

def create_word_cloud(text, width=800, height=400):
    """Create a word cloud visualization."""
    if not WORDCLOUD_AVAILABLE:
        print("WordCloud package not available. Install with: pip install wordcloud")
        return None
    
    # Clean the text for word cloud
    import re
    words = re.findall(r'\b\w+\b', text.lower())
    words = [word for word in words if len(word) > 3]  # Filter short words
    clean_text = ' '.join(words)
    
    wordcloud = WordCloud(width=width, height=height, 
                         background_color='white',
                         max_words=100,
                         colormap='viridis').generate(clean_text)
    
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    ax.set_title('Word Cloud - Most Common Words', fontsize=16, fontweight='bold', pad=20)
    
    plt.tight_layout()
    return fig

def save_all_visualizations(stats, text, output_dir='visualizations'):
    """Save all visualizations to files."""
    import os
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    saved_files = []
    
    # Character frequency chart
    char_fig = create_character_frequency_chart(stats['character_frequency'])
    if char_fig:
        char_path = os.path.join(output_dir, 'character_frequency.png')
        char_fig.savefig(char_path, dpi=300, bbox_inches='tight')
        saved_files.append(char_path)
        plt.close(char_fig)
    
    # Word frequency chart
    word_fig = create_word_frequency_chart(stats['most_common_words'])
    if word_fig:
        word_path = os.path.join(output_dir, 'word_frequency.png')
        word_fig.savefig(word_path, dpi=300, bbox_inches='tight')
        saved_files.append(word_path)
        plt.close(word_fig)
    
    # Statistics overview
    stats_fig = create_statistics_overview(stats)
    if stats_fig:
        stats_path = os.path.join(output_dir, 'statistics_overview.png')
        stats_fig.savefig(stats_path, dpi=300, bbox_inches='tight')
        saved_files.append(stats_path)
        plt.close(stats_fig)
    
    # Word cloud
    if WORDCLOUD_AVAILABLE:
        cloud_fig = create_word_cloud(text)
        if cloud_fig:
            cloud_path = os.path.join(output_dir, 'word_cloud.png')
            cloud_fig.savefig(cloud_path, dpi=300, bbox_inches='tight')
            saved_files.append(cloud_path)
            plt.close(cloud_fig)
    
    return saved_files 