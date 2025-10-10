import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import os
from stats import get_comprehensive_stats
from visualization import (create_character_frequency_chart, create_word_frequency_chart, 
                          create_statistics_overview, create_word_cloud, save_all_visualizations)

class BookBotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("📚 BookBot - Advanced Text Analysis Tool")
        self.root.geometry("1200x800")
        self.root.configure(bg='#f0f0f0')
        
        # Variables
        self.current_file = tk.StringVar()
        self.current_text = ""
        self.current_stats = None
        
        # Set up the GUI
        self.setup_styles()
        self.create_widgets()
        
    def setup_styles(self):
        """Configure custom styles for the GUI."""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure custom styles
        style.configure('Title.TLabel', font=('Arial', 16, 'bold'), background='#f0f0f0')
        style.configure('Subtitle.TLabel', font=('Arial', 12, 'bold'), background='#f0f0f0')
        style.configure('Info.TLabel', font=('Arial', 10), background='#f0f0f0')
        
    def create_widgets(self):
        """Create and layout all GUI widgets."""
        # Main container
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(1, weight=1)
        
        # Header
        self.create_header(main_frame)
        
        # Main content area with notebook (tabs)
        self.create_notebook(main_frame)
        
        # Status bar
        self.create_status_bar(main_frame)
        
    def create_header(self, parent):
        """Create the header section with file selection."""
        header_frame = ttk.LabelFrame(parent, text="File Selection", padding="10")
        header_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        header_frame.columnconfigure(1, weight=1)
        
        # File selection
        ttk.Label(header_frame, text="Select Book:").grid(row=0, column=0, sticky=tk.W, padx=(0, 10))
        
        file_entry = ttk.Entry(header_frame, textvariable=self.current_file, state='readonly')
        file_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 10))
        
        ttk.Button(header_frame, text="Browse...", command=self.select_file).grid(row=0, column=2)
        ttk.Button(header_frame, text="Analyze", command=self.analyze_text, 
                  style='Accent.TButton').grid(row=0, column=3, padx=(10, 0))
        
    def create_notebook(self, parent):
        """Create the main notebook with tabs for different views."""
        self.notebook = ttk.Notebook(parent)
        self.notebook.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Tab 1: Statistics Overview
        self.create_stats_tab()
        
        # Tab 2: Character Analysis
        self.create_char_tab()
        
        # Tab 3: Word Analysis
        self.create_word_tab()
        
        # Tab 4: Visualizations
        self.create_viz_tab()
        
    def create_stats_tab(self):
        """Create the statistics overview tab."""
        stats_frame = ttk.Frame(self.notebook)
        self.notebook.add(stats_frame, text="📊 Statistics Overview")
        
        # Create scrollable text widget for stats
        self.stats_text = scrolledtext.ScrolledText(stats_frame, height=20, width=60, 
                                                   font=('Courier', 11), state='disabled')
        self.stats_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Add initial content
        self.stats_text.config(state='normal')
        self.stats_text.insert(tk.END, "📚 Welcome to BookBot!\n\n")
        self.stats_text.insert(tk.END, "Select a text file and click 'Analyze' to see comprehensive statistics.\n\n")
        self.stats_text.insert(tk.END, "Features:\n")
        self.stats_text.insert(tk.END, "• Word count and unique word analysis\n")
        self.stats_text.insert(tk.END, "• Sentence and paragraph counting\n")
        self.stats_text.insert(tk.END, "• Character frequency analysis\n")
        self.stats_text.insert(tk.END, "• Reading time estimation\n")
        self.stats_text.insert(tk.END, "• Most common words identification\n")
        self.stats_text.insert(tk.END, "• Beautiful data visualizations\n")
        self.stats_text.config(state='disabled')
        
    def create_char_tab(self):
        """Create the character analysis tab."""
        char_frame = ttk.Frame(self.notebook)
        self.notebook.add(char_frame, text="🔤 Character Analysis")
        
        # Create matplotlib figure for character chart
        self.char_fig, self.char_ax = plt.subplots(figsize=(10, 6))
        self.char_canvas = FigureCanvasTkAgg(self.char_fig, char_frame)
        self.char_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Add toolbar
        char_toolbar = NavigationToolbar2Tk(self.char_canvas, char_frame)
        char_toolbar.update()
        
    def create_word_tab(self):
        """Create the word analysis tab."""
        word_frame = ttk.Frame(self.notebook)
        self.notebook.add(word_frame, text="📝 Word Analysis")
        
        # Create matplotlib figure for word chart
        self.word_fig, self.word_ax = plt.subplots(figsize=(10, 6))
        self.word_canvas = FigureCanvasTkAgg(self.word_fig, word_frame)
        self.word_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Add toolbar
        word_toolbar = NavigationToolbar2Tk(self.word_canvas, word_frame)
        word_toolbar.update()
        
    def create_viz_tab(self):
        """Create the comprehensive visualizations tab."""
        viz_frame = ttk.Frame(self.notebook)
        self.notebook.add(viz_frame, text="📈 Advanced Visualizations")
        
        # Create matplotlib figure for overview
        self.viz_fig, self.viz_axes = plt.subplots(2, 2, figsize=(12, 10))
        self.viz_canvas = FigureCanvasTkAgg(self.viz_fig, viz_frame)
        self.viz_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Add toolbar and export button frame
        control_frame = ttk.Frame(viz_frame)
        control_frame.pack(fill=tk.X, padx=10, pady=5)
        
        viz_toolbar = NavigationToolbar2Tk(self.viz_canvas, control_frame)
        viz_toolbar.pack(side=tk.LEFT)
        
        ttk.Button(control_frame, text="Export All Visualizations", 
                  command=self.export_visualizations).pack(side=tk.RIGHT, padx=(10, 0))
        
    def create_status_bar(self, parent):
        """Create the status bar."""
        self.status_var = tk.StringVar()
        self.status_var.set("Ready - Select a file to begin analysis")
        
        status_bar = ttk.Label(parent, textvariable=self.status_var, relief=tk.SUNKEN, 
                              style='Info.TLabel')
        status_bar.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(10, 0))
        
    def select_file(self):
        """Open file dialog to select a text file."""
        file_path = filedialog.askopenfilename(
            title="Select a text file to analyze",
            filetypes=[
                ("Text files", "*.txt"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            self.current_file.set(file_path)
            self.status_var.set(f"File selected: {os.path.basename(file_path)}")
            
    def read_file(self, file_path):
        """Read the selected file with proper encoding handling."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except UnicodeDecodeError:
            try:
                with open(file_path, 'r', encoding='latin-1') as f:
                    return f.read()
            except Exception as e:
                raise Exception(f"Could not read file with UTF-8 or Latin-1 encoding: {e}")
        except Exception as e:
            raise Exception(f"Error reading file: {e}")
            
    def analyze_text(self):
        """Analyze the selected text file."""
        if not self.current_file.get():
            messagebox.showwarning("No File Selected", "Please select a text file first.")
            return
            
        try:
            self.status_var.set("Analyzing text...")
            self.root.update_idletasks()
            
            # Read the file
            self.current_text = self.read_file(self.current_file.get())
            
            if not self.current_text.strip():
                messagebox.showwarning("Empty File", "The selected file appears to be empty.")
                return
                
            # Get comprehensive statistics
            self.current_stats = get_comprehensive_stats(self.current_text)
            
            # Update all displays
            self.update_stats_display()
            self.update_character_chart()
            self.update_word_chart()
            self.update_visualization_overview()
            
            self.status_var.set(f"Analysis complete - {self.current_stats['word_count']:,} words analyzed")
            
        except Exception as e:
            messagebox.showerror("Analysis Error", f"An error occurred during analysis:\n\n{str(e)}")
            self.status_var.set("Analysis failed")
            
    def update_stats_display(self):
        """Update the statistics text display."""
        if not self.current_stats:
            return
            
        stats = self.current_stats
        filename = os.path.basename(self.current_file.get())
        
        # Build the stats text
        stats_text = f"📚 BOOKBOT ANALYSIS REPORT\n"
        stats_text += f"{'='*50}\n\n"
        stats_text += f"📖 File: {filename}\n\n"
        
        stats_text += f"📊 BASIC STATISTICS\n"
        stats_text += f"{'-'*30}\n"
        stats_text += f"Total Words:      {stats['word_count']:,}\n"
        stats_text += f"Unique Words:     {stats['unique_words']:,}\n"
        stats_text += f"Sentences:        {stats['sentence_count']:,}\n"
        stats_text += f"Paragraphs:       {stats['paragraph_count']:,}\n\n"
        
        stats_text += f"📏 READING METRICS\n"
        stats_text += f"{'-'*30}\n"
        stats_text += f"Average Word Length:  {stats['average_word_length']} characters\n"
        stats_text += f"Estimated Reading Time: {stats['reading_time_minutes']} minutes\n"
        
        # Vocabulary richness
        vocab_richness = (stats['unique_words'] / stats['word_count']) * 100
        stats_text += f"Vocabulary Richness:  {vocab_richness:.1f}%\n\n"
        
        stats_text += f"🔤 TOP CHARACTER FREQUENCIES\n"
        stats_text += f"{'-'*30}\n"
        for i, char_info in enumerate(stats['character_frequency'][:10], 1):
            stats_text += f"{i:2d}. '{char_info['char']}' - {char_info['num']:,} occurrences\n"
            
        stats_text += f"\n📝 MOST COMMON WORDS\n"
        stats_text += f"{'-'*30}\n"
        for i, (word, count) in enumerate(stats['most_common_words'], 1):
            stats_text += f"{i:2d}. '{word}' - {count:,} occurrences\n"
        
        # Update the text widget
        self.stats_text.config(state='normal')
        self.stats_text.delete(1.0, tk.END)
        self.stats_text.insert(tk.END, stats_text)
        self.stats_text.config(state='disabled')
        
    def update_character_chart(self):
        """Update the character frequency chart."""
        if not self.current_stats:
            return
            
        self.char_ax.clear()
        
        # Get character data
        char_data = self.current_stats['character_frequency'][:15]
        characters = [item['char'] for item in char_data]
        frequencies = [item['num'] for item in char_data]
        
        # Create the chart
        bars = self.char_ax.bar(characters, frequencies, color='skyblue', edgecolor='navy', alpha=0.7)
        self.char_ax.set_xlabel('Characters', fontsize=12)
        self.char_ax.set_ylabel('Frequency', fontsize=12)
        self.char_ax.set_title('Character Frequency Analysis', fontsize=14, fontweight='bold')
        self.char_ax.grid(axis='y', alpha=0.3)
        
        # Add value labels on bars
        for bar, freq in zip(bars, frequencies):
            height = bar.get_height()
            self.char_ax.text(bar.get_x() + bar.get_width()/2., height + max(frequencies)*0.01,
                             f'{freq:,}', ha='center', va='bottom', fontsize=9)
        
        self.char_fig.tight_layout()
        self.char_canvas.draw()
        
    def update_word_chart(self):
        """Update the word frequency chart."""
        if not self.current_stats:
            return
            
        self.word_ax.clear()
        
        # Get word data
        word_data = self.current_stats['most_common_words'][:10]
        words = [item[0] for item in word_data]
        frequencies = [item[1] for item in word_data]
        
        # Create horizontal bar chart
        y_pos = range(len(words))
        bars = self.word_ax.barh(y_pos, frequencies, color='lightcoral', edgecolor='darkred', alpha=0.7)
        self.word_ax.set_yticks(y_pos)
        self.word_ax.set_yticklabels(words)
        self.word_ax.invert_yaxis()
        self.word_ax.set_xlabel('Frequency', fontsize=12)
        self.word_ax.set_title('Most Common Words', fontsize=14, fontweight='bold')
        self.word_ax.grid(axis='x', alpha=0.3)
        
        # Add value labels
        for i, (bar, freq) in enumerate(zip(bars, frequencies)):
            width = bar.get_width()
            self.word_ax.text(width + max(frequencies)*0.01, bar.get_y() + bar.get_height()/2.,
                             f'{freq:,}', ha='left', va='center', fontsize=9)
        
        self.word_fig.tight_layout()
        self.word_canvas.draw()
        
    def update_visualization_overview(self):
        """Update the comprehensive visualization overview."""
        if not self.current_stats:
            return
            
        # Clear all subplots
        for ax in self.viz_axes.flat:
            ax.clear()
            
        stats = self.current_stats
        
        # 1. Basic Stats (top-left)
        ax1 = self.viz_axes[0, 0]
        basic_stats = ['Words', 'Unique\nWords', 'Sentences', 'Paragraphs']
        basic_values = [stats['word_count'], stats['unique_words'], 
                       stats['sentence_count'], stats['paragraph_count']]
        
        bars1 = ax1.bar(basic_stats, basic_values, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4'])
        ax1.set_title('Text Structure Statistics', fontweight='bold')
        ax1.set_ylabel('Count')
        
        # Add value labels
        for bar, value in zip(bars1, basic_values):
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height + max(basic_values)*0.01,
                    f'{value:,}', ha='center', va='bottom', fontsize=8)
        
        # 2. Reading Metrics (top-right)
        ax2 = self.viz_axes[0, 1]
        metrics = ['Avg Word\nLength', 'Reading Time\n(minutes)']
        metric_values = [stats['average_word_length'], stats['reading_time_minutes']]
        
        bars2 = ax2.bar(metrics, metric_values, color=['#F7B731', '#5F27CD'])
        ax2.set_title('Reading Metrics', fontweight='bold')
        ax2.set_ylabel('Value')
        
        for bar, value in zip(bars2, metric_values):
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., height + max(metric_values)*0.01,
                    f'{value}', ha='center', va='bottom', fontsize=8)
        
        # 3. Top Characters (bottom-left)
        ax3 = self.viz_axes[1, 0]
        top_chars = stats['character_frequency'][:8]
        char_labels = [f"'{item['char']}'" for item in top_chars]
        char_sizes = [item['num'] for item in top_chars]
        
        ax3.pie(char_sizes, labels=char_labels, autopct='%1.1f%%', startangle=90)
        ax3.set_title('Character Distribution (Top 8)')
        
        # 4. Vocabulary Richness (bottom-right)
        ax4 = self.viz_axes[1, 1]
        vocab_richness = (stats['unique_words'] / stats['word_count']) * 100
        ax4.pie([vocab_richness, 100-vocab_richness], labels=['Unique', 'Repeated'], 
                autopct='%1.1f%%', colors=['#FF6B6B', '#E0E0E0'])
        ax4.set_title(f'Vocabulary Richness\n({vocab_richness:.1f}% unique words)')
        
        self.viz_fig.tight_layout()
        self.viz_canvas.draw()
        
    def export_visualizations(self):
        """Export all visualizations to files."""
        if not self.current_stats:
            messagebox.showwarning("No Data", "Please analyze a text file first.")
            return
            
        try:
            output_dir = filedialog.askdirectory(title="Select output directory for visualizations")
            if not output_dir:
                return
                
            self.status_var.set("Exporting visualizations...")
            self.root.update_idletasks()
            
            saved_files = save_all_visualizations(self.current_stats, self.current_text, output_dir)
            
            self.status_var.set(f"Exported {len(saved_files)} visualizations")
            messagebox.showinfo("Export Complete", 
                              f"Successfully exported {len(saved_files)} visualizations to:\n{output_dir}")
            
        except Exception as e:
            messagebox.showerror("Export Error", f"An error occurred during export:\n\n{str(e)}")
            self.status_var.set("Export failed")

def main():
    """Run the BookBot GUI application."""
    root = tk.Tk()
    app = BookBotGUI(root)
    
    # Center the window
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")
    
    root.mainloop()

if __name__ == "__main__":
    main() 