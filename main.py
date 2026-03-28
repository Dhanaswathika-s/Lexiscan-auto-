import re
import unicodedata
from nltk.tokenize import sent_tokenize


#  Read File
def read_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


#  Unicode Normalization
def normalize_unicode(text):
    return unicodedata.normalize("NFKC", text)


#  Remove Headers & Footers
def remove_headers_footers(text):
    lines = text.split("\n")
    cleaned = [line for line in lines if len(line.strip()) > 20]
    return "\n".join(cleaned)


#  Remove Redactions ***
def remove_redactions(text):
    return re.sub(r"\*+", "", text)


#  Fix Spacing
def fix_spacing(text):
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\s([?.!,])", r"\1", text)
    return text.strip()


#  Sentence Segmentation
def segment_sentences(text):
    return sent_tokenize(text)


#  Save Output
def save_output(sentences, filepath):
    with open(filepath, "w", encoding="utf-8") as f:
        for sentence in sentences:
            f.write(sentence + "\n")


#  Full Pipeline
def ocr_pipeline(input_path, output_path):
    text = read_file(input_path)
    text = normalize_unicode(text)
    text = remove_headers_footers(text)
    text = remove_redactions(text)
    text = fix_spacing(text)
    sentences = segment_sentences(text)
    save_output(sentences, output_path)


# Run
if __name__ == "__main__":
    ocr_pipeline("sample.txt", "output.txt")
    print("OCR Cleaning Completed ")

