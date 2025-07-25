# 📚 BookBot - Advanced Text Analysis Tool

BookBot is a comprehensive text analysis tool that provides detailed statistics, beautiful visualizations, and both command-line and GUI interfaces for analyzing books and text files.

## ✨ Features

### 📊 **Enhanced Text Statistics**
- **Word Analysis**: Total words, unique words, average word length
- **Structure Analysis**: Sentence count, paragraph count  
- **Reading Metrics**: Estimated reading time, vocabulary richness
- **Complexity Indicators**: Text complexity level, vocabulary assessment

### 📈 **Data Visualizations**
- **Character Frequency Charts**: Beautiful bar charts of most common characters
- **Word Frequency Analysis**: Horizontal bar charts of frequent words
- **Statistical Overview**: Multi-panel visualization with pie charts and metrics
- **Word Clouds**: Visual representation of most common words (optional)

### 🖥️ **Multiple Interfaces**
- **GUI Application**: Modern tabbed interface with embedded charts
- **Enhanced CLI**: Beautiful formatted reports with ASCII charts
- **Original CLI**: Simple command-line version

## 📸 Screenshots

### GUI Interface
![BookBot GUI Interface](docs/bookbot-gui-screenshot.png)

*The modern GUI interface features a clean, tabbed design with:*
- **File Selection Area**: Easy browse and analyze workflow
- **Statistics Overview Tab**: Comprehensive text analysis with formatted reporting
- **Character Analysis Tab**: Interactive bar charts of character frequencies  
- **Word Analysis Tab**: Horizontal bar charts of most common words
- **Advanced Visualizations Tab**: Multi-panel dashboard with pie charts and metrics
- **Export Functionality**: Save all visualizations as high-quality images

## 🚀 Quick Start

### Installation

1. **Clone or download** the repository
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

#### 🖼️ GUI Version (Recommended)
```bash
python bookbot_gui.py
```

**Features:**
- File browser to select text files
- 4 tabs: Statistics Overview, Character Analysis, Word Analysis, Advanced Visualizations
- Interactive charts with zoom/pan capabilities
- Export visualizations to PNG files
- Modern, user-friendly interface

#### 📊 Enhanced Command Line
```bash
python main_enhanced.py path/to/your/book.txt
```

**Features:**
- Comprehensive formatted report
- ASCII bar charts for visual representation
- Text complexity analysis
- Reading level assessment

#### 🔧 Original Command Line
```bash
python main.py path/to/your/book.txt
```

**Features:**
- Basic word count and character frequency
- Simple output format

## 📁 File Support

BookBot supports various text file formats:

- **✅ Plain Text Files** (`.txt`) - Full support
- **✅ Markdown Files** (`.md`) - Full support  
- **✅ Any text-based file** - Full support

**Unicode Support:** Automatically handles UTF-8 and Latin-1 encodings for international characters.

## 📊 Sample Output

### GUI Interface
The GUI provides 4 comprehensive tabs:

1. **📊 Statistics Overview**: Detailed text metrics with beautiful formatting
2. **🔤 Character Analysis**: Interactive bar chart of character frequencies
3. **📝 Word Analysis**: Horizontal bar chart of most common words
4. **📈 Advanced Visualizations**: Multi-panel dashboard with:
   - Text structure statistics
   - Reading metrics
   - Character distribution (pie chart)
   - Vocabulary richness analysis

### Enhanced Command Line
```
======================================================================
📚 BOOKBOT ENHANCED ANALYSIS REPORT
======================================================================
📖 File: frankenstein.txt

📊 BASIC STATISTICS
----------------------------------------
Total Words:          78,045
Unique Words:         13,847
Sentences:            3,324
Paragraphs:           878

📏 READING METRICS
----------------------------------------
Average Word Length:  4.5 characters
Reading Time:         390.2 minutes
Vocabulary Richness:  17.7% unique words
Words per Sentence:   23.5
Sentences per Para:   3.8

🔤 CHARACTER FREQUENCY ANALYSIS
----------------------------------------
Top 15 most frequent characters:
 1. 'e' ████████████████████████████████ 46,043
 2. 't' ████████████████████████ 30,365
 3. 'a' ████████████████████ 26,743
 ...

📝 MOST COMMON WORDS
----------------------------------------
Top 15 most frequent words (3+ characters):
 1. the            ██████████████████████████ 4,083
 2. and            ████████████████████ 2,976
 3. was            ███████████████ 2,187
 ...

🧠 TEXT COMPLEXITY INDICATORS
----------------------------------------
Estimated Complexity: Very Complex
Vocabulary Level:     Basic vocabulary
```

## 🛠️ Project Structure

```
bookbot/
├── main.py                 # Original simple CLI version
├── main_enhanced.py        # Enhanced CLI with comprehensive stats
├── bookbot_gui.py         # GUI application
├── stats.py               # Text analysis functions
├── visualization.py       # Chart and graph generation
├── requirements.txt       # Python dependencies
├── README.md             # This documentation
├── books/                # Directory for text files
│   └── your-books.txt    # Your text files go here
└── visualizations/       # Generated charts (when exported)
    ├── character_frequency.png
    ├── word_frequency.png
    ├── statistics_overview.png
    └── word_cloud.png
```

## 🔧 Dependencies

- **matplotlib** (≥3.5.0): Chart generation and visualization
- **numpy** (≥1.21.0): Numerical operations for charts
- **wordcloud** (≥1.9.0): Word cloud generation (optional)

## 📈 Advanced Features

### Vocabulary Analysis
- **Vocabulary Richness**: Percentage of unique words
- **Word Length Distribution**: Analysis of word complexity
- **Reading Level Assessment**: Estimated text difficulty

### Text Complexity
- **Sentence Structure**: Average words per sentence
- **Paragraph Analysis**: Structure and organization metrics
- **Complexity Classification**: Simple → Moderate → Complex → Very Complex

### Export Capabilities
- **PNG Export**: Save all visualizations as high-quality images
- **Batch Export**: Generate all charts at once
- **Custom Directory**: Choose where to save visualizations

## 🎯 Use Cases

- **Academic Research**: Analyze literature for patterns and complexity
- **Content Analysis**: Evaluate readability and structure of documents
- **Writing Assessment**: Get insights into your own writing style
- **Comparative Analysis**: Compare multiple texts side-by-side
- **Educational Tools**: Teaching text analysis and statistics

## 🔮 Future Enhancements

Possible additions for even more functionality:
- PDF and EPUB file support
- Sentiment analysis
- Language detection
- Batch processing multiple files
- Web interface version
- Reading level (Flesch-Kincaid) scoring
- Export to CSV/JSON formats

## 📚 Example Usage

1. **Download a book** from Project Gutenberg:
   ```bash
   curl https://www.gutenberg.org/files/84/84-0.txt -o books/frankenstein.txt
   ```

2. **Analyze with GUI**:
   ```bash
   python bookbot_gui.py
   # Select the file and click "Analyze"
   ```

3. **Analyze with CLI**:
   ```bash
   python main_enhanced.py books/frankenstein.txt
   ```

## 🤝 Contributing

BookBot is a learning project that demonstrates:
- Text processing and analysis
- Data visualization with matplotlib
- GUI development with tkinter
- Clean, modular Python code structure
- Unicode handling and file encoding

Feel free to fork, modify, and enhance for your own projects!

## 📄 License

This project was created as part of the [Boot.dev](https://www.boot.dev) learning curriculum. Use it for learning and educational purposes.
