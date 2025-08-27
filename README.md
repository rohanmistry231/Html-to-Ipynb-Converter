# 📓 Jupyter HTML to IPYNB Converter

![Streamlit App](https://img.shields.io/badge/Streamlit-Powered-red.svg)
![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

Transform JupyterLab-exported HTML files back into editable `.ipynb` notebooks with this sleek, user-friendly Streamlit app! Designed for data science students, educators, and professionals, this tool bridges the gap between static HTML exports and dynamic Jupyter notebooks, making it perfect for course assignments, collaborative projects, or archival recovery.

---

## 🚀 Features

- **Seamless Conversion**: Convert JupyterLab HTML exports to `.ipynb` files with accurate markdown and code cell extraction.
- **Image Support**: Preserves images in markdown cells as markdown syntax (e.g., `![alt](src)`).
- **Dynamic File Naming**: Downloads the converted `.ipynb` file with the same name as the uploaded HTML file.
- **Robust Error Handling**: Gracefully handles invalid files and provides clear user feedback.
- **Streamlit-Powered UI**: Intuitive web interface for easy file uploads and downloads.
- **JupyterLab Compatibility**: Tailored for modern JupyterLab HTML exports, supporting `jp-MarkdownCell` and `jp-CodeCell` structures.
- **Lightweight & Fast**: Built with minimal dependencies for quick deployment and execution.

---

## 🎯 Why Use This Tool?

Ever received a Jupyter notebook as an HTML file from a course instructor or colleague? Converting it back to an editable `.ipynb` file can be a hassle. This app simplifies the process, enabling you to:

- **Edit Assignments**: Convert static HTML handouts into editable Jupyter notebooks for coursework.
- **Recover Notebooks**: Restore `.ipynb` files from HTML exports for further analysis or modification.
- **Streamline Workflows**: Save time by automating the conversion process with a clean, web-based interface.

Whether you're a data science student tackling NumPy assignments or a professional reviving old notebook exports, this tool is your go-to solution!

---

## 🛠 Installation (Local Setup)

Follow these steps to run the app locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/jupyter-html-converter.git
   cd jupyter-html-converter
   ```

2. **Set Up a Virtual Environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` includes:
   ```
   streamlit==1.31.0
   beautifulsoup4==4.12.3
   lxml==5.2.2
   ```

4. **Run the App**:
   ```bash
   streamlit run app.py
   ```

5. **Access the App**:
   Open your browser to `http://localhost:8501` and upload your Jupyter HTML file!

---

## 📖 Usage

1. **Launch the App**:
   - Run locally or access the deployed version on Streamlit Community Cloud.
   
2. **Upload HTML File**:
   - Click the file uploader and select a JupyterLab-exported `.html` or `.htm` file.
   - Ensure the file is a valid JupyterLab HTML export containing `jp-Cell` divs.

3. **Download .ipynb**:
   - After uploading, the app processes the file and offers a download button.
   - The downloaded `.ipynb` file will have the same name as the uploaded file (e.g., `numpy_lesson.html` → `numpy_lesson.ipynb`).

4. **Open in Jupyter**:
   - Save the downloaded `.ipynb` file and open it in JupyterLab or Jupyter Notebook.
   - Note: If the notebook contains images (e.g., `list.png`), ensure those files are in the same directory as the `.ipynb` file.

---

## ☁️ Deploying to Streamlit Community Cloud

Host your app online for free with Streamlit Community Cloud! Follow these steps:

1. **Push to GitHub**:
   - Create a public GitHub repository (e.g., `jupyter-html-converter`).
   - Add the following files:
     ```
     ├── app.py
     ├── requirements.txt
     ├── README.md
     ├── .gitignore
     ```
   - Push to GitHub:
     ```bash
     git add .
     git commit -m "Initial commit for Streamlit app"
     git push origin main
     ```

2. **Deploy on Streamlit**:
   - Log in to [Streamlit Community Cloud](https://share.streamlit.io).
   - Click “New app” and select your GitHub repository.
   - Set the main file path to `app.py` and deploy.
   - Your app will be live at a URL like `https://your-app-name.streamlit.app`.

3. **Update Automatically**:
   - Any changes pushed to your GitHub repository’s main branch will trigger automatic redeployment.

---

## 📸 Screenshots

| Upload Interface | Successful Conversion |
|------------------|-----------------------|
| ![Upload Screen](https://via.placeholder.com/400x200.png?text=Upload+Screen) | ![Download Screen](https://via.placeholder.com/400x200.png?text=Download+Screen) |

*(Replace placeholder images with actual screenshots after testing locally or deploying!)*

---

## 🧑‍💻 Example Input/Output

**Input HTML** (JupyterLab-exported):
```html
<div class="jp-Cell jp-MarkdownCell">
  <div class="jp-RenderedMarkdown">
    <h1>NumPy</h1>
  </div>
</div>
<div class="jp-Cell jp-CodeCell">
  <div class="jp-CodeMirrorEditor">
    <pre>import numpy as np</pre>
  </div>
</div>
```

**Output .ipynb**:
```json
{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": ["<h1>NumPy</h1>"]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "source": ["import numpy as np"],
      "outputs": []
    }
  ],
  "metadata": {...},
  "nbformat": 4,
  "nbformat_minor": 5
}
```

---

## ⚠️ Notes & Limitations

- **Image Files**: The app converts `<img>` tags to markdown syntax (e.g., `![Image](list.png)`). Ensure referenced image files are available in your Jupyter working directory.
- **Outputs**: Currently, code cell outputs are not extracted (set to `[]`). If your HTML includes outputs (e.g., in `jp-OutputArea`), contact the developer for an enhanced version.
- **File Size**: For large HTML files, consider adding a size limit (e.g., 10MB) to avoid memory issues on Streamlit Cloud.
- **Compatibility**: Optimized for JupyterLab HTML exports. Older Jupyter Notebook formats may require adjustments.

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create