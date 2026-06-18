import streamlit as st
import os
import json
from dotenv import load_dotenv

from parser.pdf_parser import extract_pdf_text
from parser.image_parser import extract_image_text

from prompts.classify_prompt import CLASSIFY_PROMPT
from prompts.summary_prompt import SUMMARY_PROMPT
from prompts.risk_prompt import RISK_PROMPT

from langchain_google_genai import ChatGoogleGenerativeAI

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="AI Intelligent Document Analyzer",
    page_icon="📄",
    layout="wide"
)

# =========================
# LOAD ENV
# =========================

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

.main-title{
    text-align:center;
    font-size:42px;
    font-weight:bold;
    color:#1E88E5;
}

.sub-title{
    text-align:center;
    color:gray;
    font-size:18px;
    margin-bottom:20px;
}

.block-container{
    padding-top:2rem;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================

st.markdown(
"""
<div class="main-title">
📄 AI Intelligent Document Analyzer
</div>

<div class="sub-title">
Document Classification • Entity Extraction • Risk Analysis • Structured Reporting
</div>
""",
unsafe_allow_html=True
)

# =========================
# SIDEBAR
# =========================

with st.sidebar:

    st.title("🤖 AI Analyzer")

    st.markdown("---")

    st.write("### Supported Formats")

    st.write("📄 PDF")
    st.write("🖼 PNG")
    st.write("🖼 JPG")
    st.write("🖼 JPEG")

    st.markdown("---")

    st.caption("Powered by Gemini AI")

# =========================
# FILE UPLOAD
# =========================

uploaded_file = st.file_uploader(
    "Upload Document",
    type=["pdf", "png", "jpg", "jpeg"]
)

# =========================
# PROCESS DOCUMENT
# =========================

if uploaded_file:

    with st.spinner("Analyzing document..."):

        extension = uploaded_file.name.split(".")[-1].lower()

        # Extract Text

        if extension == "pdf":
            text = extract_pdf_text(uploaded_file)
        else:
            text = extract_image_text(uploaded_file)

        # Document Type

        doc_type = llm.invoke(
            CLASSIFY_PROMPT.format(text=text)
        )

        # Summary

        summary = llm.invoke(
            SUMMARY_PROMPT.format(text=text)
        )

        # Entities

        entity_prompt = f"""
Extract key entities from the document.

Return JSON only.

{{
  "name":"",
  "date":"",
  "amount":"",
  "organization":"",
  "email":"",
  "phone":""
}}

Document:

{text}
"""

        entities = llm.invoke(entity_prompt)

        # Risk Analysis

        risk = llm.invoke(
            RISK_PROMPT + "\n\n" + text
        )

    st.success("Document Processed Successfully")

    # =========================
    # METRICS
    # =========================

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Document Type",
            doc_type.content.strip()
        )

    with col2:
        st.metric(
            "Status",
            "Processed"
        )

    with col3:
        st.metric(
            "Size (KB)",
            round(uploaded_file.size / 1024, 2)
        )

    st.markdown("---")

    # =========================
    # TABS
    # =========================

    tab1, tab2, tab3 = st.tabs([
        "📋 Summary",
        "🔍 Entities",
        "⚠ Risk Analysis"
    ])

    # =========================
    # SUMMARY
    # =========================

    with tab1:

        st.subheader("Executive Summary")

        st.info(summary.content)

    # =========================
    # ENTITIES
    # =========================

    with tab2:

        st.subheader("Extracted Entities")

        try:

            entity_json = json.loads(
                entities.content.replace("```json", "")
                                .replace("```", "")
            )

            st.json(entity_json)

        except:

            st.write(entities.content)

    # =========================
    # RISK
    # =========================

    with tab3:

        st.subheader("Risk Assessment")

        st.warning(risk.content)

    st.markdown("---")

    # =========================
    # RAW TEXT
    # =========================

    with st.expander("📜 View Extracted Text"):

        st.text_area(
            "Extracted Text",
            text,
            height=250
        )

    # =========================
    # DOWNLOAD REPORT
    # =========================

    report = {
        "document_type": doc_type.content,
        "summary": summary.content,
        "entities": entities.content,
        "risk_analysis": risk.content
    }

    st.download_button(
        label="⬇ Download JSON Report",
        data=json.dumps(report, indent=4),
        file_name="document_report.json",
        mime="application/json"
    )