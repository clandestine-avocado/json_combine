import json
import os
from pathlib import Path

def combine_json_files(root_dir, output_file):
    combined_data = []

    # Walk through all subdirectories
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.json'):
                file_path = Path(dirpath) / filename
                relative_path = file_path.relative_to(root_dir)

                try:
                    with open(file_path, 'r') as f:
                        file_data = json.load(f)

                        # Extract the 5-digit number from the filename
                        unique_id = filename[:-5]  # Remove the '.json' extension
                        if not unique_id.isdigit() or len(unique_id) != 5:
                            print(f"Warning: Filename {filename} does not match expected format (5 digits). Using full filename as ID.")
                            unique_id = filename[:-5]  # Use filename without extension as fallback

                            # Add file path information and unique ID to the JSON object
                            file_data['_original_file_path'] = str(relative_path)
                            file_data['_unique_id'] = unique_id

                            combined_data.append(file_data)
                            except json.JSONDecodeError:
                                print(f"Error reading {file_path}. Skipping this file.")

                                # Write combined data to output file
                                with open(output_file, 'w') as f:
                                    json.dump(combined_data, f, indent=2)

                                    print(f"Combined {len(combined_data)} JSON files into {output_file}")

                                    # Usage
                                    root_directory = r'C:\Users\kroy2\Documents\python\projects\json_generate_test_files\nested_data'
                                    output_file = 'combined_output.json'
                                    combine_json_files(root_directory, output_file)
