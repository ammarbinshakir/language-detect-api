from langdetect import detect_langs, DetectorFactory
import langcodes

DetectorFactory.seed = 0  # Ensure consistent results

def detect_language(text: str):
    if not text or len(text.strip()) < 5:
        raise ValueError("Text too short to detect language.")

    langs = detect_langs(text)
    top_lang = langs[0]
    lang_code = top_lang.lang
    confidence = round(top_lang.prob, 2)
    lang_name = langcodes.get(lang_code).display_name()

    return {
        "language_code": lang_code,
        "language_name": lang_name,
        "confidence": confidence
    }
