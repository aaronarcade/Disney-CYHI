import os

# Get a list of directories in the current directory
directories = [d for d in os.listdir() if os.path.isdir(d)]

# Create a Markdown list of directories with links
markdown_list = ""
for d in directories:
    markdown_list += f"- [{d}]({d})\n"

    # List .md files in the subdirectory
    subdirectory = os.path.join(os.getcwd(), d)
    md_files = [f for f in os.listdir(subdirectory) if f.endswith(".md")]

    if md_files:
        for md_file in md_files:
            markdown_list += f"    - [{md_file}]({os.path.join(d, md_file)})\n"

# Save the Markdown list to a file or print it to the console
with open("folder_list.md", "w") as file:
    file.write("# List of Folders in the Current Directory\n\n")
    file.write(markdown_list)

print("List of folders and Markdown files with links saved to folder_list.md")
