import requests
import re
import os

INPUT_FILE = "text/b2b_extracted_text_with_noise.txt"
OUTPUT_FILE = "text/b2b_cleaned_text.txt"
CHUNK_SIZE = 1000
API_URL = "http://127.0.0.1:8000/clean"

def split_into_chunks(text, max_len=1000):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    chunks, chunk = [], ""

    for s in sentences:
        if len(chunk) + len(s) < max_len:
            chunk += s + " "
        else:
            chunks.append(chunk.strip())
            chunk = s + " "
    if chunk:
        chunks.append(chunk.strip())
    return chunks

def clean_text_chunk(chunk):
    resp = requests.post(API_URL, json={"text": chunk})
    return resp.json()["cleaned_text"] if resp.status_code == 200 else ""

def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        text = f.read()

    chunks = split_into_chunks(text, CHUNK_SIZE)
    cleaned = [clean_text_chunk(chunk) for chunk in chunks]

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n\n".join(cleaned))

    print(f"✅ Saved cleaned output to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
