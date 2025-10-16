# Generate Content Script

A Python script that generates Vietnamese content based on date/time input formats.

## Installation

### Prerequisites

- Python 3.9 (using `/opt/homebrew/bin/python3.9`)
- `uv` package manager

### Setup Python Environment

1. Install `uv` if you haven't already:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Create a virtual environment named `.venv` using Python 3.9:
   ```bash
   uv venv .venv --python /opt/homebrew/bin/python3.9
   ```

3. Activate the virtual environment:
   ```bash
   source .venv/bin/activate
   ```

4. Install dependencies (if any):
   ```bash
   uv pip install -r requirements.txt
   ```

## Usage

The script supports multiple date/time formats:

### Syntax

```bash
python generate_content.py YYYYMM
python generate_content.py YYYYMMDD
python generate_content.py YYYYMMDDHH
python generate_content.py YYYYMMDDHHMM
```

### Examples

1. **Generate content for a month (YYYYMM):**
   ```bash
   python generate_content.py 202510
   ```
   Creates: `content/20251001-0000.md`

2. **Generate content for a specific day (YYYYMMDD):**
   ```bash
   python generate_content.py 20251016
   ```
   Creates: `content/20251016-0000.md`

3. **Generate content for a specific hour (YYYYMMDDHH):**
   ```bash
   python generate_content.py 2025101610
   ```
   Creates: `content/20251016-1000.md`

4. **Generate content for a specific minute (YYYYMMDDHHMM):**
   ```bash
   python generate_content.py 202510161000
   ```
   Creates: `content/20251016-1000.md`

### Output

- Each run generates a single file in the `content/` directory
- Filename format: `YYYYMMDD-HHMM.md`
- Content: A single sentence in Vietnamese about anything
- The script creates the `content/` directory automatically if it doesn't exist

### Example Output

File: `content/20251016-1000.md`
```
Hôm nay trời đẹp và nắng ấm.
```

## Features

- Supports 4 different date/time input formats
- Generates random Vietnamese sentences
- Automatic directory creation
- UTF-8 encoding support
- Error handling for invalid date formats

## Requirements

- Python 3.9+
- No external dependencies (uses only standard library)
