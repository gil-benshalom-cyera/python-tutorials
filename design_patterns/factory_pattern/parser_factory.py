import os.path
import re
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup  # For HTML parsing
from pathlib import Path
import PyPDF2


# 1. Abstract Base Parser
class BaseParser(ABC):
    """Base class for all parsers that adds post-processing functionality."""

    def __init__(self, file_path):
        self.file_path = file_path

    @abstractmethod
    def extract_text(self):
        """Each subclass must implement this method."""
        pass

    def clean_text(self, text):
        """Removes extra spaces, special characters, and normalizes text."""
        text = re.sub(r"\s+", " ", text).strip()  # Remove extra spaces/newlines
        return text

    def count_words(self, text):
        """Counts words in the extracted text."""
        words = re.findall(r"\b\w+\b", text)
        return len(words)

    def parse(self):
        """Runs the parser and applies post-processing."""
        text = self.extract_text()
        cleaned_text = self.clean_text(text)
        word_count = self.count_words(cleaned_text)

        return {
            "raw_text": text,
            "cleaned_text": cleaned_text,
            "word_count": word_count,
        }


# 2. Concrete Parser Classes
class TxtParser(BaseParser):
    """Parser for TXT files."""

    def extract_text(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            return file.read()


class HtmlParser(BaseParser):
    """Parser for HTML files."""

    def extract_text(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            html_content = file.read()
            soup = BeautifulSoup(html_content, "html.parser")
            return soup.get_text()


class PdfParser(BaseParser):
    """Parser for PDF files."""

    def extract_text(self):
        if PyPDF2 is None:
            raise ImportError("PyPDF2 is required to parse PDFs.")

        text = []
        with open(self.file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text.append(page.extract_text() or "")
        return "\n".join(text)


# 3. Factory Class
class ParserFactory:
    """Factory that returns the appropriate parser based on file type."""

    @staticmethod
    def get_parser(file_path):
        extension = Path(file_path).suffix.lower()

        if extension == ".txt":
            return TxtParser(file_path)
        elif extension == ".html":
            return HtmlParser(file_path)
        elif extension == ".pdf":
            return PdfParser(file_path)
        else:
            raise ValueError(f"Unsupported file type: {extension}")


def main():
    # Example files (assumes these files exist in the working directory)
    resources_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resources'))
    file_paths = [os.path.join(resources_dir, f) for f in ["sample1.html", "sample2.txt", "sample3.pdf"]]

    for file_path in file_paths:
        try:
            parser = ParserFactory.get_parser(file_path)
            result = parser.parse()
            print(f"Results for {file_path}:")
            print(f"- Word Count: {result['word_count']}")
            print(f"- Cleaned Text (First 100 chars): {result['cleaned_text'][:100]}...\n")
        except Exception as e:
            print(f"Error processing {file_path}: {e}")


# 4. Usage Example
if __name__ == "__main__":
    main()
