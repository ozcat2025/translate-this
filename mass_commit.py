#!/usr/bin/env python3
"""
Mass GitHub commits script.

This script generates content 60 times using generate_content.py and commits each file individually.
Usage: python mass_commit.py YYYYMMDDHH
"""

import sys
import os
import subprocess
import time
from datetime import datetime, timedelta

def run_command(command, description=""):
    """
    Run a shell command and return the result.
    """
    try:
        print(f"Running: {command}")
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        if result.stdout:
            print(f"Output: {result.stdout.strip()}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error running '{command}': {e}")
        if e.stderr:
            print(f"Error output: {e.stderr}")
        return False

def generate_content_for_hour(base_datetime):
    """
    Generate content for 60 minutes in the specified hour.
    """
    generated_files = []
    
    for minute in range(60):
        # Create datetime for this minute
        current_time = base_datetime.replace(minute=minute, second=0, microsecond=0)
        
        # Format as YYYYMMDDHHMM for generate_content.py
        time_str = current_time.strftime('%Y%m%d%H%M')
        
        print(f"\n--- Generating content for {time_str} ---")
        
        # Run generate_content.py
        if run_command(f"python generate_content.py {time_str}"):
            # Get the generated filename
            filename = f"{current_time.strftime('%Y%m%d')}-{current_time.strftime('%H%M')}.md"
            filepath = os.path.join("content", filename)
            
            if os.path.exists(filepath):
                generated_files.append(filepath)
                print(f"✓ Generated: {filepath}")
            else:
                print(f"✗ Failed to generate: {filepath}")
        else:
            print(f"✗ Failed to run generate_content.py for {time_str}")
    
    return generated_files

def commit_and_push_files(file_list):
    """
    Commit and push each file individually.
    """
    for i, filepath in enumerate(file_list, 1):
        print(f"\n--- Committing file {i}/{len(file_list)}: {filepath} ---")
        
        # Add the specific file
        if not run_command(f"git add {filepath}"):
            print(f"✗ Failed to add {filepath}")
            continue
        
        # Create commit message
        filename = os.path.basename(filepath)
        commit_msg = f"Add content for {filename.replace('.md', '')}"
        
        # Commit the file
        if not run_command(f'git commit -m "{commit_msg}"'):
            print(f"✗ Failed to commit {filepath}")
            continue
        
        # Push to remote
        if not run_command("git push"):
            print(f"✗ Failed to push {filepath}")
            continue
        
        print(f"✓ Successfully committed and pushed: {filepath}")
        
        # Small delay to avoid overwhelming the system
        time.sleep(1)

def parse_date_input(date_str):
    """
    Parse YYYYMMDDHH format and return datetime object.
    """
    try:
        return datetime.strptime(date_str, '%Y%m%d%H')
    except ValueError:
        raise ValueError(f"Invalid date format. Expected YYYYMMDDHH, got: {date_str}")

def main():
    """
    Main function to handle mass commits.
    """
    if len(sys.argv) != 2:
        print("Usage: python mass_commit.py YYYYMMDDHH")
        print("Example: python mass_commit.py 2025101610")
        print("This will generate content for 2025-10-16 10:00 to 10:59 (60 files)")
        sys.exit(1)
    
    date_input = sys.argv[1]
    
    try:
        # Parse the date input
        base_datetime = parse_date_input(date_input)
        print(f"Starting mass commit for: {base_datetime.strftime('%Y-%m-%d %H:00')}")
        
        # Check if we're in a git repository
        if not os.path.exists('.git'):
            print("Error: Not in a git repository. Please run this script from the repository root.")
            sys.exit(1)
        
        # Generate content for 60 minutes
        print(f"\nGenerating content for 60 minutes starting from {base_datetime.strftime('%Y-%m-%d %H:00')}...")
        generated_files = generate_content_for_hour(base_datetime)
        
        if not generated_files:
            print("No files were generated. Exiting.")
            sys.exit(1)
        
        print(f"\nGenerated {len(generated_files)} files. Starting commits...")
        
        # Commit and push each file
        commit_and_push_files(generated_files)
        
        print(f"\n✓ Mass commit completed! Processed {len(generated_files)} files.")
        
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
