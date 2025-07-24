import fitz  # PyMuPDF
import json

def process_pdf(path):
    doc = fitz.open(path)
    headings = []
    title = ""
    sizes = {}

    for page_num, page in enumerate(doc):
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:
            if "lines" in b:
                for l in b["lines"]:
                    for span in l["spans"]:
                        size = round(span["size"], 1)
                        text = span["text"].strip()
                        if len(text) < 3: continue
                        sizes[size] = sizes.get(size, 0) + 1

    largest_size = max(sizes, key=sizes.get)
    for page_num, page in enumerate(doc):
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:
            if "lines" in b:
                for l in b["lines"]:
                    for span in l["spans"]:
                        text = span["text"].strip()
                        if not text: continue
                        size = round(span["size"], 1)
                        if size == largest_size and not title:
                            title = text
                        elif size > largest_size * 0.8:
                            level = "H1"
                        elif size > largest_size * 0.6:
                            level = "H2"
                        elif size > largest_size * 0.4:
                            level = "H3"
                        else:
                            continue
                        headings.append({
                            "level": level,
                            "text": text,
                            "page": page_num + 1
                        })

    return json.dumps({
        "title": title,
        "outline": headings
    }, indent=2)
