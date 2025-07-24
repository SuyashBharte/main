import os
from extractor import process_pdf

INPUT_DIR = "/app/input"
OUTPUT_DIR = "/app/output"

def main():
    for file in os.listdir(INPUT_DIR):
        if file.endswith(".pdf"):
            input_path = os.path.join(INPUT_DIR, file)
            output_filename = file.replace(".pdf", ".json")
            output_path = os.path.join(OUTPUT_DIR, output_filename)
            data = process_pdf(input_path)
            with open(output_path, "w") as f:
                f.write(data)

if __name__ == "__main__":
    main()
