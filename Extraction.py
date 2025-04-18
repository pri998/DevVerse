import re
import spacy
from collections import defaultdict
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from project_status import project_status
from datetime import datetime

#Preprocess full text
def preprocess_text(text):
    if not text:
        return ""
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s.,;:()\-\'\"]+', '', text)
    return text

#Clean individual requirement
def clean_requirement(req):
    cleaned = re.sub(r'^\s*[\•\-\*\○\◦\▪\▫\□\◆\◇\■\#\d+\.\)]+\s*', '', req)
    return cleaned.strip()

# 3. Identify business requirements
def identify_requirements(text):
    try:
        nlp = spacy.load("en_core_web_sm")
    except OSError:
        import subprocess
        subprocess.call(["python", "-m", "spacy", "download", "en_core_web_sm"])
        nlp = spacy.load("en_core_web_sm")

    doc = nlp(text)
    requirements = []

    req_patterns = [
        r"(?i)(?:shall|must|will be required to|is required to) .{10,200}?[.?!]",
        r"(?i)(?:requirement|requirements)[:;]? .{10,200}?[.?!]",
        r"(?i)(?:the system|the solution|the product|the website|the vendor|the contractor) (?:shall|must|will|should) .{10,200}?[.?!]",
        r"(?i)(?:deliverable|deliverables)[:;]? .{10,200}?[.?!]",
        r"(?i)(?:functional requirement|business requirement|technical requirement)[:;]? .{10,200}?[.?!]",
        r"(?i)(?:integration|implementation) (?:of|with) .{10,200}?[.?!]",
        r"(?i)(?:is|are) (?:required|necessary|needed|essential) .{10,200}?[.?!]",
        r"(?i)(?:should be|must be|shall be) .{10,200}?[.?!]",
        r"(?i)(?:development of|creation of|provision of) .{10,200}?[.?!]"
    ]

    for pattern in req_patterns:
        matches = re.finditer(pattern, text)
        for match in matches:
            req = clean_requirement(match.group(0).strip())
            if req not in requirements and len(req) > 20:
                requirements.append(req)

    key_phrases = [
        "provide", "support", "enable", "allow", "implement", "maintain",
        "ensure", "deliver", "comply", "include", "integrate", "offer",
        "manage", "process", "handle", "deploy", "develop", "design",
        "create", "build", "configure", "secure", "optimize", "establish"
    ]

    key_contexts = [
        "system", "solution", "product", "website", "application", "platform",
        "vendor", "e-commerce", "commerce", "online", "portal",
        "database", "user", "customer", "interface", "payment", "security",
        "feature", "functionality", "service", "component", "module", "design"
    ]

    for sent in doc.sents:
        sent_text = sent.text.strip()
        if len(sent_text.split()) < 5:
            continue
        sent_lower = sent_text.lower()
        if any(f" {phrase} " in sent_lower for phrase in key_phrases):
            if any(context in sent_lower for context in key_contexts):
                cleaned_sent = clean_requirement(sent_text)
                if cleaned_sent not in requirements and len(cleaned_sent) > 20:
                    requirements.append(cleaned_sent)

    bullet_req_pattern = r'o\s+([A-Z][^o]{10,200}?[.?!])'
    matches = re.finditer(bullet_req_pattern, text)
    for match in matches:
        req = clean_requirement(match.group(1).strip())
        if req not in requirements and len(req) > 20:
            requirements.append(req)

    return requirements

#Vectorize requirements using TF-IDF
def vectorize_requirements(requirements):
    processed_reqs = [re.sub(r'[^\w\s]', '', req.lower()) for req in requirements]
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(processed_reqs).toarray()
    return vectors

#Wrapper function for Streamlit
def process_pdf_text(text):
    processed_text = preprocess_text(text)
    requirements = identify_requirements(processed_text)
    tfidf_vectors = vectorize_requirements(requirements) if requirements else []


    return requirements, tfidf_vectors
