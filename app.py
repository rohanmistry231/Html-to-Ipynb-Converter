import streamlit as st
from bs4 import BeautifulSoup
import json
import re
import os

# Set page configuration
st.set_page_config(
    page_title="Jupyter HTML to IPYNB Converter",
    page_icon="📓",
    layout="centered"
)

st.title("Jupyter HTML to IPYNB Converter")

# File uploader for HTML
uploaded_file = st.file_uploader("Upload your Jupyter HTML file", type=["html", "htm"])

if uploaded_file is not None:
    try:
        # Get the uploaded file name and change extension to .ipynb
        file_name = os.path.splitext(uploaded_file.name)[0] + ".ipynb"
        
        # Read the uploaded HTML file
        html_content = uploaded_file.read().decode("utf-8")
        
        # Parse the HTML with BeautifulSoup
        soup = BeautifulSoup(html_content, 'lxml')
        
        # Initialize the ipynb structure (nbformat 4 is standard)
        notebook = {
            "nbformat": 4,
            "nbformat_minor": 5,
            "metadata": {
                "kernelspec": {
                    "display_name": "Python 3",
                    "language": "python",
                    "name": "python3"
                },
                "language_info": {
                    "codemirror_mode": {"name": "ipython", "version": 3},
                    "file_extension": ".py",
                    "mimetype": "text/x-python",
                    "name": "python",
                    "nbconvert_exporter": "python",
                    "pygments_lexer": "ipython3",
                    "version": "3.9.0"
                }
            },
            "cells": []
        }
        
        # Find all cell divs with class 'jp-Cell'
        for cell_div in soup.find_all("div", class_="jp-Cell"):
            if "jp-MarkdownCell" in cell_div["class"]:
                # Extract markdown content
                markdown_div = cell_div.find("div", class_="jp-RenderedMarkdown")
                if markdown_div:
                    # Get the raw HTML content and convert to markdown-compatible text
                    markdown_content = markdown_div.decode_contents().strip()
                    # Handle images by converting to markdown syntax
                    for img in markdown_div.find_all("img"):
                        src = img.get("src", "")
                        alt = img.get("alt", "Image")
                        markdown_content = markdown_content.replace(str(img), f'![{alt}]({src})')
                    cell = {
                        "cell_type": "markdown",
                        "metadata": {},
                        "source": markdown_content.splitlines(keepends=True)
                    }
                    notebook["cells"].append(cell)
            
            elif "jp-CodeCell" in cell_div["class"]:
                # Extract code content
                code_div = cell_div.find("div", class_="jp-CodeMirrorEditor")
                if code_div:
                    code_text = code_div.get_text().strip()
                    # Skip empty code cells (only whitespace)
                    if code_text and not re.match(r'^\s*$', code_text):
                        cell = {
                            "cell_type": "code",
                            "execution_count": None,
                            "metadata": {},
                            "source": code_text.splitlines(keepends=True),
                            "outputs": []
                        }
                        notebook["cells"].append(cell)
        
        if notebook["cells"]:
            # Convert to JSON string
            ipynb_json = json.dumps(notebook, indent=2)
            
            # Provide download button with uploaded file name (changed to .ipynb)
            st.download_button(
                label="Download as .ipynb",
                data=ipynb_json,
                file_name=file_name,
                mime="application/json"
            )
            st.success("Conversion complete! Download the .ipynb file above.")
        else:
            st.error("No valid cells found in the HTML. Ensure it's a valid JupyterLab-exported HTML file.")
    
    except Exception as e:
        st.error(f"An error occurred while processing the file: {str(e)}")
else:
    st.info("Please upload a Jupyter HTML file to convert.")