#!/usr/bin/env python3
"""
Generate Vietnamese content based on date/time input.
Supports formats: YYYYMM, YYYYMMDD, YYYYMMDDHH, YYYYMMDDHHMM
"""

import sys
import os
import re
from datetime import datetime
import random

# Vietnamese sentences for content generation
VIETNAMESE_SENTENCES = [
    "Hôm nay trời đẹp và nắng ấm.",
    "Tôi đang học tiếng Việt mỗi ngày.",
    "Cà phê sáng là thứ tôi thích nhất.",
    "Gia đình là điều quan trọng nhất trong cuộc sống.",
    "Thành phố này rất đông đúc và nhộn nhịp.",
    "Tôi thích đọc sách vào buổi tối.",
    "Món phở này rất ngon và đậm đà.",
    "Hôm nay tôi cảm thấy rất hạnh phúc.",
    "Công việc hôm nay khá bận rộn.",
    "Tôi đang lên kế hoạch cho chuyến du lịch.",
    "Thời tiết hôm nay mát mẻ và dễ chịu.",
    "Tôi thích nghe nhạc khi làm việc.",
    "Bữa tối hôm nay rất ngon miệng.",
    "Tôi đang học một kỹ năng mới.",
    "Cuối tuần này tôi sẽ nghỉ ngơi.",
    "Tôi thích đi dạo trong công viên.",
    "Hôm nay tôi gặp một người bạn cũ.",
    "Tôi đang suy nghĩ về tương lai.",
    "Công việc này thú vị và bổ ích.",
    "Tôi thích ngắm hoàng hôn trên biển."
]

def parse_date_input(date_str):
    """
    Parse date input string and return datetime object.
    Supports formats: YYYYMM, YYYYMMDD, YYYYMMDDHH, YYYYMMDDHHMM
    """
    # Validate input format
    if not re.match(r'^\d{6,12}$', date_str):
        raise ValueError("Invalid date format. Use YYYYMM, YYYYMMDD, YYYYMMDDHH, or YYYYMMDDHHMM")
    
    length = len(date_str)
    
    try:
        if length == 6:  # YYYYMM
            return datetime.strptime(date_str, '%Y%m')
        elif length == 8:  # YYYYMMDD
            return datetime.strptime(date_str, '%Y%m%d')
        elif length == 10:  # YYYYMMDDHH
            return datetime.strptime(date_str, '%Y%m%d%H')
        elif length == 12:  # YYYYMMDDHHMM
            return datetime.strptime(date_str, '%Y%m%d%H%M')
        else:
            raise ValueError("Invalid date format length")
    except ValueError as e:
        raise ValueError(f"Invalid date: {e}")

def generate_filename(dt):
    """
    Generate filename in format YYYYMMDD-HHMM.md
    """
    return f"{dt.strftime('%Y%m%d')}-{dt.strftime('%H%M')}.md"

def get_random_vietnamese_sentence():
    """
    Get a random Vietnamese sentence from the predefined list.
    """
    return random.choice(VIETNAMESE_SENTENCES)

def create_content_directory():
    """
    Create content directory if it doesn't exist.
    """
    content_dir = "content"
    if not os.path.exists(content_dir):
        os.makedirs(content_dir)
        print(f"Created directory: {content_dir}")

def main():
    """
    Main function to handle command line arguments and generate content.
    """
    if len(sys.argv) != 2:
        print("Usage: python generate_content.py YYYYMM[DD[HH[MM]]]")
        print("Examples:")
        print("  python generate_content.py 202510")
        print("  python generate_content.py 20251016")
        print("  python generate_content.py 2025101610")
        print("  python generate_content.py 202510161000")
        sys.exit(1)
    
    date_input = sys.argv[1]
    
    try:
        # Parse the date input
        dt = parse_date_input(date_input)
        
        # Create content directory
        create_content_directory()
        
        # Generate filename
        filename = generate_filename(dt)
        filepath = os.path.join("content", filename)
        
        # Generate random Vietnamese sentence
        vietnamese_sentence = get_random_vietnamese_sentence()
        
        # Write content to file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(vietnamese_sentence)
        
        print(f"Generated content: {filepath}")
        print(f"Content: {vietnamese_sentence}")
        
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
