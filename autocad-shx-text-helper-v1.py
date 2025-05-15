import streamlit as st

# Streamlit app configuration
st.set_page_config(page_title="AutoCAD SHX Text Helper", page_icon="📐", layout="wide")

# Title and introduction
st.title("AutoCAD SHX Text Helper")
st.markdown("""
Welcome to the AutoCAD SHX Text Helper! This app explains SHX text in AutoCAD, common issues (e.g., PDF exports, missing fonts), and how to manage them. 
Use the sidebar to explore features like font selection, PDF export simulation, and conversion tips.
""")

# Sidebar for navigation
st.sidebar.header("Navigation")
section = st.sidebar.radio("Choose a section:", 
                          ["What is SHX Text?", "PDF Export Issues", "Edit SHX Text", "Simulate PDF Settings", "SHX to TrueType Converter"])

# Sample SHX fonts for simulation
shx_fonts = ["simplex.shx", "romans.shx", "isocp.shx", "txt.shx", "complex.shx"]
truetype_fonts = ["Arial", "Times New Roman", "Calibri", "Helvetica"]

# Section 1: What is SHX Text?
if section == "What is SHX Text?":
    st.header("What is SHX Text?")
    st.markdown("""
    **SHX Text** in AutoCAD refers to fonts or shapes stored in **SHX (Shape) files**. These are vector-based, lightweight files used for text and symbols in drawings. 
    Unlike TrueType fonts, SHX fonts render quickly but can cause issues in PDF exports or when editing.

    **Key Characteristics:**
    - Compiled from `.SHP` (shape) files into `.SHX` format.
    - Stored in AutoCAD's Fonts folder (e.g., `C:\Program Files\Autodesk\AutoCAD\Fonts`).
    - Common examples: `simplex.shx`, `romans.shx`.
    - Pros: Fast rendering, small file size.
    - Cons: Limited PDF compatibility, non-searchable in exports unless configured.
    """)
    st.info("Tip: Always ensure SHX files are available in your drawing's directory to avoid font substitution.")

# Section 2: PDF Export Issues
elif section == "PDF Export Issues":
    st.header("PDF Export Issues with SHX Text")
    st.markdown("""
    SHX text often causes problems when exporting AutoCAD drawings to PDF because PDFs don’t natively support SHX fonts. Common issues include:

    - **Non-searchable Text**: SHX text converts to geometry (polylines) in PDFs, making it uneditable.
    - **Comments in PDFs**: Since AutoCAD 2016, SHX text may export as searchable text but appears as comments or pop-ups, cluttering the PDF.
    - **Missing Fonts**: If SHX files are missing, AutoCAD substitutes fonts, causing display errors.

    **Solutions:**
    - Set `PDFSHX` to 0 in AutoCAD to exclude SHX text from PDFs.
    - Replace SHX fonts with TrueType fonts before exporting.
    - In Adobe Acrobat, print the PDF with “Document Only” to remove SHX comments.
    """)
    st.warning("Flattening PDFs in tools like Bluebeam Revu can also remove SHX-related comments.")

# Section 3: Edit SHX Text
elif section == "Edit SHX Text":
    st.header("Editing SHX Text in AutoCAD")
    st.markdown("""
    Editing SHX text can be tricky since it’s vector-based geometry. Here’s how to handle it:

    **Steps in AutoCAD:**
    1. Use the **Recognize SHX Text** tool (Insert tab > Recognition Settings).
    2. Adjust settings:
       - Recognition threshold (e.g., 50%).
       - Select SHX fonts to match (e.g., `simplex.shx`).
    3. Convert recognized text to **Mtext**.
    4. Combine Mtext strings using the **Combine Text** tool.

    **In PDFs:**
    - Convert SHX text to TrueType fonts in AutoCAD before exporting.
    - Use AutoCAD’s **PDF Import** tool to import PDFs and convert SHX geometry to Mtext.

    **Best Practice**: Replace SHX fonts with TrueType fonts (e.g., Arial) for easier editing and PDF compatibility.
    """)
    st.success("Pro Tip: Always back up your DWG file before converting text!")

# Section 4: Simulate PDF Settings
elif section == "Simulate PDF Settings":
    st.header("Simulate AutoCAD PDF Export Settings")
    st.markdown("Adjust settings below to simulate how SHX text behaves in PDF exports.")

    # Interactive settings
    pdf_shx = st.checkbox("Enable PDFSHX (Include SHX text as searchable)", value=True)
    selected_shx = st.selectbox("Select SHX Font", shx_fonts)
    combine_text = st.checkbox("Combine Mtext strings after recognition", value=False)

    # Simulate output
    st.subheader("Simulation Result")
    if pdf_shx:
        st.write(f"Exporting with `{selected_shx}` as searchable text.")
        st.warning("SHX text will appear as comments in the PDF, which may clutter the document.")
    else:
        st.write(f"Exporting with `{selected_shx}` as geometry (non-searchable).")
        st.info("Set `PDFSHX` to 0 in AutoCAD to achieve this.")
    if combine_text:
        st.write("Mtext strings will be combined for easier editing.")

    st.markdown("**Recommendation**: For cleaner PDFs, disable PDFSHX or convert to TrueType fonts.")

# Section 5: SHX to TrueType Converter
elif section == "SHX to TrueType Converter":
    st.header("SHX to TrueType Font Converter")
    st.markdown("""
    Converting SHX text to TrueType fonts ensures PDF compatibility and searchability. Follow these steps in AutoCAD:

    1. Select SHX text in the drawing.
    2. Open the **Properties** panel.
    3. Change the font to a TrueType font (e.g., Arial).
    4. Export the drawing using **DWG to PDF.pc3**.
    5. In the PDF options, ensure “Capture fonts” is enabled.

    **Try it below**: Map an SHX font to a TrueType font.
    """)

    # Interactive font mapping
    selected_shx = st.selectbox("Select SHX Font to Convert", shx_fonts)
    selected_truetype = st.selectbox("Map to TrueType Font", truetype_fonts)

    st.subheader("Conversion Preview")
    st.write(f"Converting `{selected_shx}` to `{selected_truetype}`.")
    st.success(f"Text styled with `{selected_shx}` will now use `{selected_truetype}` in your drawing and PDF exports.")
    st.info("Apply this in AutoCAD’s Properties panel for all selected text.")

# Footer
st.markdown("---")
st.markdown("""
**AutoCAD SHX Text Helper** | Built with Streamlit  
For more help, check [AutoCAD Documentation](https://www.autodesk.com/) or ask your question below!
""")

# Optional: User feedback or query
user_query = st.text_input("Have a specific SHX text issue? Ask here:")
if user_query:
    st.write("Thanks for your question! For detailed assistance, please provide more context (e.g., specific error, AutoCAD version).")
