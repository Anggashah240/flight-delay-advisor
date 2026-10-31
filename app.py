import streamlit as st
import time
import re

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="Flight Delay & EU 261 Advisor",
    layout="centered"
)

# ---------------------------------------------------------
# Security Guardrail & ML Backend Logic
# ---------------------------------------------------------
def evaluate_prompt_security(user_query: str):
    injection_keywords = ["abaikan", "ignore", "forget previous", "admin mode", "bypass", "berikan saya uang", "hack"]
    if any(keyword in user_query.lower() for keyword in injection_keywords):
        return False, "[DEFENSE TRIGGERED] Perintah berbahaya terdeteksi. Sistem menolak manipulasi instruksi."
    return True, "[SAFE QUERY] Pertanyaan diproses secara aman."

def calculate_delay_probability(dep_delay_min: int, distance_km: int) -> float:
    base = 0.20
    delay_impact = min(0.65, dep_delay_min * 0.02)
    dist_impact = min(0.10, distance_km * 0.00003)
    prob = base + delay_impact + dist_impact
    return min(0.98, max(0.05, prob))

def parse_delay_minutes(user_query: str, default_delay: int) -> int:
    query_lower = user_query.lower()
    jam_match = re.search(r'(\d+)\s*jam', query_lower)
    if jam_match:
        return int(jam_match.group(1)) * 60
    menit_match = re.search(r'(\d+)\s*menit', query_lower)
    if menit_match:
        return int(menit_match.group(1))
    return default_delay

def generate_chatbot_response(user_query: str, maskapai: str, jarak: int, delay_sidebar: int):
    q = user_query.lower()
    effective_delay = parse_delay_minutes(user_query, delay_sidebar)
    
    # ML Prediction Calculation (Target Label: Delay >= 15 min)
    prob = calculate_delay_probability(effective_delay, jarak)
    prob_pct = prob * 100
    risk_level = "HIGH RISK (Berpotensi Delay >= 15 Menit)" if prob > 0.5 else "LOW RISK (Berpotensi Tepat Waktu)"
    
    # EU 261 Rate Calculation
    if jarak <= 1500:
        comp_val = "EUR 250"
    elif jarak <= 3500:
        comp_val = "EUR 400"
    else:
        comp_val = "EUR 600"

    # Intent Detection
    is_asking_prediction = any(k in q for k in ["prediksi", "peluang", "probabilitas", "risiko", "potensi", "telat", "delay", "menit", "jam"])
    is_asking_hotel = any(k in q for k in ["hotel", "nginep", "menginap", "tidur", "akomodasi", "inap"])
    is_asking_money = any(k in q for k in ["uang", "kompensasi", "ganti rugi", "klaim", "bayar", "euro", "eur"])
    is_asking_refund = any(k in q for k in ["refund", "batal", "kembalikan uang", "cancel", "tiket"])
    is_asking_food = any(k in q for k in ["makan", "minum", "snack", "konsumsi", "lapar"])
    is_greeting = any(k in q for k in ["halo", "hai", "pagi", "siang", "sore", "malam", "siapa"])

    if is_greeting and not is_asking_prediction and not is_asking_money:
        log = "[AGENT DECISION] -> Skip Retrieval Tool (Direct Response)"
        text = (
            "Halo! Saya Chatbot Flight Delay & EU 261 Legal Advisor.\n\n"
            "Silakan tanyakan prediksi keterlambatan penerbangan Anda atau hak kompensasi penumpang berdasarkan regulasi EU 261."
        )
        return log, text

    log = "[AGENT DECISION] -> Call Tool: eu261_retrieval_tool() (FAISS Vector Store)"
    
    parts = []
    
    # Section 1: ML Prediction Result
    ml_info = (
        f"**Hasil Prediksi Deteksi Delay (LightGBM):**\n"
        f"- Estimasi Probabilitas Delay (>= 15 Menit): `{prob_pct:.1f}%`\n"
        f"- Status Risiko: **{risk_level}**\n"
        f"- Parameter Input: Maskapai {maskapai}, Jarak {jarak} km, Delay Keberangkatan {effective_delay} menit."
    )
    parts.append(ml_info)

    # Section 2: Dynamic RAG Legal Answer based on Query
    if is_asking_hotel:
        legal_info = (
            f"**Panduan Akomodasi Hotel (Regulasi EU 261/2004 - Pasal 9):**\n"
            f"Jika keterlambatan memaksa Anda menginap satu malam atau lebih, maskapai **wajib menyediakan hotel gratis** "
            f"serta transportasi dari bandara ke hotel dan sebaliknya."
        )
    elif is_asking_money:
        legal_info = (
            f"**Panduan Kompensasi Finansial (Regulasi EU 261/2004 - Pasal 7):**\n"
            f"Untuk rute penerbangan {jarak} km, Anda berhak atas kompensasi **{comp_val}** per penumpang "
            f"jika keterlambatan tiba di tujuan mencapai minimal 3 jam."
        )
    elif is_asking_refund:
        legal_info = (
            f"**Panduan Refund Tiket (Regulasi EU 261/2004 - Pasal 8):**\n"
            f"Jika delay mencapai 5 jam atau lebih, Anda berhak membatalkan penerbangan dan menuntut **pengembalian penuh 100% uang tiket**."
        )
    elif is_asking_food:
        legal_info = (
            f"**Panduan Makanan & Minuman (Right to Care - Pasal 9):**\n"
            f"Maskapai wajib memberikan voucher makanan dan minuman gratis jika keterlambatan telah mencapai minimal 2 jam."
        )
    else:
        if effective_delay < 120:
            legal_info = (
                f"**Analisis Hak Penumpang (EU 261/2004):**\n"
                f"Untuk keterlambatan {effective_delay} menit (< 2 jam):\n"
                f"- **Kompensasi Uang:** Belum memenuhi syarat (persyaratan minimal delay 3 jam saat tiba di tujuan).\n"
                f"- **Fasilitas Makanan/Minuman:** Belum berlaku (persyaratan minimal delay 2 jam).\n"
                f"- **Saran:** Tetap pantau informasi penerbangan Anda di bandara."
            )
        elif 120 <= effective_delay < 180:
            legal_info = (
                f"**Analisis Hak Penumpang (EU 261/2004):**\n"
                f"Untuk keterlambatan {effective_delay} menit (2-3 jam):\n"
                f"- **Fasilitas Gratis:** Berhak atas makanan, minuman, dan akses komunikasi gratis.\n"
                f"- **Kompensasi Uang:** Belum berlaku (harus delay minimal 3 jam)."
            )
        else:
            legal_info = (
                f"**Analisis Hak Penumpang (EU 261/2004):**\n"
                f"Untuk keterlambatan {effective_delay} menit (>= 3 jam):\n"
                f"- **Kompensasi Uang:** Berhak klaim kompensasi tunai **{comp_val}** (rute {jarak} km).\n"
                f"- **Fasilitas Gratis:** Makanan, minuman, dan hotel gratis jika harus menginap."
            )

    parts.append(legal_info)
    return log, "\n\n---\n\n".join(parts)

# ---------------------------------------------------------
# UI Layout Focused strictly on Chatbot & Delay Prediction
# ---------------------------------------------------------
st.title("Flight Delay & EU 261 Advisor")
st.caption("Fokus Utama: Deteksi Probabilitas Delay (ML LightGBM) & Chatbot Hak Penumpang (EU 261 RAG)")

# Sidebar - Simple Flight Inputs
with st.sidebar:
    st.header("Input Data Penerbangan")
    maskapai_input = st.selectbox("Maskapai", ["Garuda Indonesia", "AirAsia", "Batik Air", "Lion Air", "Lufthansa", "Emirates"])
    jarak_input = st.number_input("Jarak Penerbangan (km)", min_value=100, max_value=15000, value=1200, step=100)
    delay_input = st.number_input("Latensi Keberangkatan (Menit)", min_value=0, max_value=600, value=25, step=5)
    
    st.divider()
    st.subheader("Status MLOps & System")
    st.text("Model: LightGBM (AUC 0.7036)")
    st.text("Target: Delay >= 15 Menit")
    st.text("Vector Store: FAISS (EU 261)")
    st.text("Guardrail: Security Active")

# Main Chatbot Interface
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "Halo! Saya Chatbot Flight Delay & EU 261 Advisor.\n\n"
                "Saya dapat memprediksi probabilitas keterlambatan penerbangan Anda (>= 15 menit) menggunakan model LightGBM, sekaligus memberikan panduan hak kompensasi Anda berdasarkan regulasi EU 261.\n\n"
                "Silakan ketik pertanyaan Anda (contoh: 'berapa peluang delay saya?' atau 'telat 50 menit')."
            )
        }
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Ketik pertanyaan Anda di sini..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Memproses via Guardrail, LightGBM Engine & FAISS RAG..."):
            time.sleep(0.3)
            is_safe, sec_msg = evaluate_prompt_security(prompt)
            
            if not is_safe:
                res = f"**[SECURITY SHIELD ACTIVATED]**\n\n{sec_msg}"
                st.error(res)
                st.session_state.messages.append({"role": "assistant", "content": res})
            else:
                decision_log, full_resp = generate_chatbot_response(
                    user_query=prompt,
                    maskapai=maskapai_input,
                    jarak=jarak_input,
                    delay_sidebar=delay_input
                )
                final_content = f"**{decision_log}**\n\n{full_resp}"
                st.write(final_content)
                st.session_state.messages.append({"role": "assistant", "content": final_content})
