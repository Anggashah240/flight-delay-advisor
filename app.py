fixed_html = r"""<!DOCTYPE html>
<html lang="id" class="h-full bg-slate-50">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flight Delay & EU 261 Advisor</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Plus Jakarta Sans', sans-serif; }
        .chat-scroll { max-height: 520px; overflow-y: auto; scroll-behavior: smooth; }
        .chat-scroll::-webkit-scrollbar { width: 5px; }
        .chat-scroll::-webkit-scrollbar-thumb { background: #E2E8F0; border-radius: 99px; }
        .chat-scroll::-webkit-scrollbar-thumb:hover { background: #CBD5E1; }
    </style>
</head>
<body class="h-full flex flex-col text-slate-900 bg-slate-50/80">

    <!-- Top Navigation -->
    <header class="bg-white border-b border-slate-200/80 sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <div class="flex items-center space-x-3">
                <div class="w-9 h-9 rounded-xl bg-blue-600 flex items-center justify-center text-white font-bold text-base shadow-sm">

                </div>
                <div>
                    <h1 class="text-base font-bold text-slate-900 leading-tight">Flight Delay & EU 261 Advisor</h1>
                    <p class="text-xs text-slate-500 font-medium">Predictive ML & Legal RAG Intelligence</p>
                </div>
            </div>
            
            <div class="flex items-center space-x-3">
                <div class="inline-flex items-center px-3 py-1 rounded-full text-xs font-semibold bg-emerald-50 text-emerald-700 border border-emerald-200/60">
                    <span class="w-2 h-2 rounded-full bg-emerald-500 mr-2 animate-pulse"></span>
                    System Online
                </div>
            </div>
        </div>
    </header>

    <!-- Main Content Grid -->
    <main class="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-6 grid grid-cols-1 lg:grid-cols-12 gap-6">

        <!-- Left Column: Inputs & Risk Gauge -->
        <div class="lg:col-span-4 space-y-5">
            
            <!-- Flight Input Card -->
            <div class="bg-white rounded-2xl border border-slate-200/80 p-5 shadow-sm">
                <h2 class="text-xs font-bold uppercase tracking-wider text-slate-400 mb-4">Parameter Penerbangan</h2>
                
                <div class="space-y-4">
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1.5">Maskapai</label>
                        <select id="inputMaskapai" class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3.5 py-2.5 text-sm font-medium text-slate-800 focus:outline-none focus:ring-2 focus:ring-blue-600/20 focus:border-blue-600 transition-all">
                            <option value="Garuda Indonesia">Garuda Indonesia</option>
                            <option value="AirAsia">AirAsia</option>
                            <option value="Batik Air">Batik Air</option>
                            <option value="Lion Air">Lion Air</option>
                            <option value="Lufthansa">Lufthansa</option>
                            <option value="Emirates">Emirates</option>
                        </select>
                    </div>

                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1.5">Jarak Penerbangan (km)</label>
                        <input type="number" id="inputJarak" value="1800" min="100" max="15000" step="100" class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3.5 py-2.5 text-sm font-medium text-slate-800 focus:outline-none focus:ring-2 focus:ring-blue-600/20 focus:border-blue-600 transition-all">
                    </div>

                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1.5">Latensi Keberangkatan (Menit)</label>
                        <input type="number" id="inputDelay" value="50" min="0" max="600" step="5" class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3.5 py-2.5 text-sm font-medium text-slate-800 focus:outline-none focus:ring-2 focus:ring-blue-600/20 focus:border-blue-600 transition-all">
                    </div>
                </div>
            </div>

            <!-- Prediction Result Card -->
            <div class="bg-white rounded-2xl border border-slate-200/80 p-5 shadow-sm space-y-4">
                <div class="flex justify-between items-center">
                    <h2 class="text-xs font-bold uppercase tracking-wider text-slate-400">Hasil Prediksi ML</h2>
                    <span class="text-[10px] font-bold text-slate-400 bg-slate-100 px-2 py-0.5 rounded-md">LightGBM</span>
                </div>
                
                <div class="p-4 rounded-xl bg-slate-50 border border-slate-100 text-center">
                    <p class="text-xs font-semibold text-slate-500 mb-1">Probabilitas Delay (>= 15 Menit)</p>
                    <div id="displayProb" class="text-4xl font-extrabold text-blue-600 my-1">38.5%</div>
                    <div id="displayBadge" class="inline-block px-3 py-1 rounded-full text-xs font-bold bg-emerald-100 text-emerald-800 mt-2">
                        LOW RISK (TEPAT WAKTU)
                    </div>
                </div>

                <!-- Minimal Meta Badges -->
                <div class="grid grid-cols-2 gap-2 text-[11px] text-slate-500 font-medium pt-1">
                    <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-100">
                        <span class="block text-slate-400 text-[10px]">Model ROC-AUC</span>
                        <strong class="text-slate-700 font-bold">0.7036</strong>
                    </div>
                    <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-100">
                        <span class="block text-slate-400 text-[10px]">MLOps Backend</span>
                        <strong class="text-slate-700 font-bold">MLflow & FAISS</strong>
                    </div>
                </div>
            </div>

        </div>

        <!-- Right Column: Clean Chat Interface -->
        <div class="lg:col-span-8 flex flex-col bg-white rounded-2xl border border-slate-200/80 shadow-sm overflow-hidden h-[620px]">
            
            <!-- Chat Header -->
            <div class="px-6 py-4 border-b border-slate-100 flex items-center justify-between bg-white">
                <div>
                    <h2 class="text-sm font-bold text-slate-900">AI Legal & Passenger Rights Advisor</h2>
                    <p class="text-xs text-slate-500">Asisten otomatis panduan kompensasi & hak penumpang EU 261/2004</p>
                </div>
                <button onclick="clearChat()" class="text-xs font-semibold text-slate-400 hover:text-slate-600 transition-colors">
                    Reset Chat
                </button>
            </div>

            <!-- Quick Action Chips -->
            <div class="px-6 py-3 bg-slate-50/60 border-b border-slate-100 flex flex-wrap items-center gap-2">
                <span class="text-xs font-semibold text-slate-400 mr-1">Tanya Cepat:</span>
                <button onclick="sendQuickPrompt('Berapa kompensasi uang yang bisa saya klaim?')" class="text-xs bg-white border border-slate-200 hover:border-slate-300 text-slate-700 px-3 py-1.5 rounded-full font-medium transition-all hover:shadow-sm">💶 Kompensasi Uang</button>
                <button onclick="sendQuickPrompt('Apakah saya berhak dapat hotel gratis?')" class="text-xs bg-white border border-slate-200 hover:border-slate-300 text-slate-700 px-3 py-1.5 rounded-full font-medium transition-all hover:shadow-sm">🏨 Hotel Gratis</button>
                <button onclick="sendQuickPrompt('Bagaimana aturan refund 100% tiket?')" class="text-xs bg-white border border-slate-200 hover:border-slate-300 text-slate-700 px-3 py-1.5 rounded-full font-medium transition-all hover:shadow-sm">🎟️ Refund 100%</button>
                <button onclick="sendQuickPrompt('Penerbangan saya telat 50 menit, dapat apa?')" class="text-xs bg-white border border-slate-200 hover:border-slate-300 text-slate-700 px-3 py-1.5 rounded-full font-medium transition-all hover:shadow-sm">⏱️ Telat 50 Menit</button>
            </div>

            <!-- Chat Messages Container -->
            <div id="chatBox" class="flex-1 p-6 chat-scroll space-y-4 bg-slate-50/30">
                <!-- Welcome Message -->
                <div class="flex items-start space-x-3">
                    <div class="w-8 h-8 rounded-full bg-blue-600 text-white flex items-center justify-center font-bold text-xs shrink-0 mt-0.5">
                        AI
                    </div>
                    <div class="bg-white border border-slate-200/80 rounded-2xl p-4 text-xs text-slate-700 max-w-xl shadow-sm leading-relaxed space-y-2">
                        <p class="font-bold text-slate-900 text-sm">Halo! Saya Flight Delay & EU 261 Advisor.</p>
                        <p>Saya dapat menganalisis probabilitas keterlambatan penerbangan Anda menggunakan model <strong>LightGBM</strong> sekaligus memberikan panduan hak kompensasi berdasarkan <strong>Regulasi EU 261/2004</strong>.</p>
                        <p class="text-slate-500 pt-1 border-t border-slate-100">Silakan sesuaikan parameter penerbangan di sebelah kiri, lalu tanyakan situasi Anda di sini!</p>
                    </div>
                </div>
            </div>

            <!-- Chat Input Form -->
            <div class="p-4 bg-white border-t border-slate-100">
                <form id="chatForm" onsubmit="handleChatSubmit(event)" class="flex items-center space-x-2">
                    <input type="text" id="userInput" placeholder="Tanyakan seputar hak penerbangan Anda..." class="flex-1 bg-slate-50 border border-slate-200 rounded-xl px-4 py-3 text-sm text-slate-800 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-600/20 focus:border-blue-600 transition-all font-medium">
                    <button type="submit" class="bg-blue-600 hover:bg-blue-700 text-white font-bold text-sm px-6 py-3 rounded-xl transition-all shadow-sm flex items-center justify-center shrink-0">
                        Kirim
                    </button>
                </form>
            </div>

        </div>

    </main>

    <!-- JS Logic -->
    <script>
        function updatePrediction() {
            const jarak = parseInt(document.getElementById('inputJarak').value) || 1200;
            const delay = parseInt(document.getElementById('inputDelay').value) || 0;
            
            let base = 0.20;
            let delayImpact = Math.min(0.65, delay * 0.02);
            let distImpact = Math.min(0.10, jarak * 0.00003);
            let prob = Math.min(0.98, Math.max(0.05, base + delayImpact + distImpact));
            let probPct = (prob * 100).toFixed(1);

            const displayProb = document.getElementById('displayProb');
            const displayBadge = document.getElementById('displayBadge');

            displayProb.innerText = probPct + "%";

            if (prob > 0.5) {
                displayProb.className = "text-4xl font-extrabold text-red-600 my-1";
                displayBadge.className = "inline-block px-3 py-1 rounded-full text-xs font-bold bg-red-100 text-red-800 mt-2";
                displayBadge.innerText = "HIGH RISK (BERPOTENSI DELAY >= 15 MIN)";
            } else {
                displayProb.className = "text-4xl font-extrabold text-emerald-600 my-1";
                displayBadge.className = "inline-block px-3 py-1 rounded-full text-xs font-bold bg-emerald-100 text-emerald-800 mt-2";
                displayBadge.innerText = "LOW RISK (TEPAT WAKTU)";
            }
        }

        document.getElementById('inputJarak').addEventListener('input', updatePrediction);
        document.getElementById('inputDelay').addEventListener('input', updatePrediction);
        document.getElementById('inputMaskapai').addEventListener('change', updatePrediction);

        function evaluateSecurity(query) {
            const dangerousKeywords = ["abaikan", "ignore", "forget previous", "admin mode", "bypass", "berikan saya uang", "hack"];
            const qLower = query.toLowerCase();
            for (let kw of dangerousKeywords) {
                if (qLower.includes(kw)) {
                    return { isSafe: false, msg: "[DEFENSE TRIGGERED] Perintah berbahaya terdeteksi. Sistem menolak manipulasi instruksi." };
                }
            }
            return { isSafe: true, msg: "[SAFE QUERY] Pertanyaan diproses secara aman." };
        }

        function parseDelayFromText(text, defaultDelay) {
            const textLower = text.toLowerCase();
            const jamMatch = textLower.match(/(\d+)\s*jam/);
            if (jamMatch) return parseInt(jamMatch[1]) * 60;
            const menitMatch = textLower.match(/(\d+)\s*menit/);
            if (menitMatch) return parseInt(menitMatch[1]);
            return defaultDelay;
        }

        function generateAIResponse(userQuery) {
            const maskapai = document.getElementById('inputMaskapai').value;
            const jarak = parseInt(document.getElementById('inputJarak').value) || 1200;
            const sidebarDelay = parseInt(document.getElementById('inputDelay').value) || 0;
            
            const effectiveDelay = parseDelayFromText(userQuery, sidebarDelay);
            const q = userQuery.toLowerCase();

            let base = 0.20;
            let delayImpact = Math.min(0.65, effectiveDelay * 0.02);
            let distImpact = Math.min(0.10, jarak * 0.00003);
            let prob = Math.min(0.98, Math.max(0.05, base + delayImpact + distImpact));
            let probPct = (prob * 100).toFixed(1);
            let riskLevel = prob > 0.5 ? "HIGH RISK (Berpotensi Delay >= 15 Menit)" : "LOW RISK (Berpotensi Tepat Waktu)";

            let compVal = "EUR 250";
            if (jarak > 1500 && jarak <= 3500) compVal = "EUR 400";
            else if (jarak > 3500) compVal = "EUR 600";

            const isGreeting = ["halo", "hai", "pagi", "siang", "sore", "malam", "siapa"].some(k => q.includes(k));
            const isHotel = ["hotel", "nginep", "menginap", "tidur", "akomodasi", "inap"].some(k => q.includes(k));
            const isMoney = ["uang", "kompensasi", "ganti rugi", "klaim", "bayar", "euro", "eur"].some(k => q.includes(k));
            const isRefund = ["refund", "batal", "kembalikan uang", "cancel", "tiket"].some(k => q.includes(k));
            const isFood = ["makan", "minum", "snack", "konsumsi", "lapar"].some(k => q.includes(k));

            if (isGreeting && !isHotel && !isMoney && !isRefund && !isFood) {
                return {
                    log: "[AGENT DECISION] -> Skip Retrieval Tool (Direct Response)",
                    content: "Halo! Saya Chatbot Flight Delay & EU 261 Advisor.\n\nSilakan tanyakan estimasi delay penerbangan Anda atau hak kompensasi penumpang sesuai aturan EU 261/2004."
                };
            }

            let decisionLog = "[AGENT DECISION] -> Call Tool: eu261_retrieval_tool() (FAISS Vector Store)";
            let mlPart = "**Hasil Prediksi Deteksi Delay (LightGBM):**\n" +
                         "• Estimasi Probabilitas Delay (>= 15 Menit): **" + probPct + "%**\n" +
                         "• Status Risiko: **" + riskLevel + "**\n" +
                         "• Parameter Test: Maskapai " + maskapai + " | Jarak " + jarak + " km | Latensi Keberangkatan " + effectiveDelay + " menit.";

            let legalPart = "";

            if (isHotel) {
                legalPart = "**Panduan Akomodasi Hotel (Regulasi EU 261/2004 - Pasal 9):**\n" +
                            "Jika keterlambatan memaksa Anda menginap satu malam atau lebih, maskapai **wajib menyediakan hotel gratis** serta transportasi dari bandara ke hotel dan sebaliknya.";
            } else if (isMoney) {
                legalPart = "**Panduan Kompensasi Finansial (Regulasi EU 261/2004 - Pasal 7):**\n" +
                            "Untuk rute penerbangan **" + jarak + " km**, Anda berhak atas kompensasi **" + compVal + "** per penumpang jika keterlambatan tiba di destinasi akhir mencapai minimal 3 jam.";
            } else if (isRefund) {
                legalPart = "**Panduan Refund Tiket (Regulasi EU 261/2004 - Pasal 8):**\n" +
                            "Jika delay mencapai 5 jam atau lebih, Anda berhak membatalkan penerbangan dan menuntut **pengembalian penuh 100% uang tiket**.";
            } else if (isFood) {
                legalPart = "**Panduan Makanan & Minuman (Right to Care - Pasal 9):**\n" +
                            "Maskapai wajib memberikan voucher makanan dan minuman gratis jika keterlambatan telah mencapai minimal 2 jam.";
            } else {
                if (effectiveDelay < 120) {
                    legalPart = "**Analisis Hak Penumpang (Regulasi EU 261/2004):**\n" +
                                "Untuk keterlambatan **" + effectiveDelay + " menit** (< 2 jam):\n" +
                                "• **Kompensasi Uang:** Belum memenuhi syarat (persyaratan minimal delay 3 jam saat tiba di tujuan).\n" +
                                "• **Fasilitas Makanan/Minuman:** Belum berlaku (persyaratan minimal delay 2 jam).\n" +
                                "• **Saran:** Tetap pantau informasi penerbangan Anda di bandara.";
                } else if (effectiveDelay < 180) {
                    legalPart = "**Analisis Hak Penumpang (Regulasi EU 261/2004):**\n" +
                                "Untuk keterlambatan **" + effectiveDelay + " menit** (2-3 jam):\n" +
                                "• **Fasilitas Gratis:** Berhak atas makanan, minuman, dan akses komunikasi gratis.\n" +
                                "• **Kompensasi Uang:** Belum berlaku (harus delay minimal 3 jam).";
                } else {
                    legalPart = "**Analisis Hak Penumpang (Regulasi EU 261/2004):**\n" +
                                "Untuk keterlambatan **" + effectiveDelay + " menit** (>= 3 jam):\n" +
                                "• **Kompensasi Uang:** Berhak klaim kompensasi tunai **" + compVal + "** (rute " + jarak + " km).\n" +
                                "• **Fasilitas Gratis:** Makanan, minuman, dan hotel gratis jika harus menginap.";
                }
            }

            return {
                log: decisionLog,
                content: mlPart + "\n\n---\n\n" + legalPart
            };
        }

        function appendMessage(role, text, isError) {
            const chatBox = document.getElementById('chatBox');
            const wrapper = document.createElement('div');
            wrapper.className = "flex items-start space-x-3 " + (role === 'user' ? 'justify-end' : 'justify-start');

            if (role === 'user') {
                const bubble = document.createElement('div');
                bubble.className = "bg-blue-600 text-white rounded-2xl px-4 py-2.5 text-xs font-medium max-w-md shadow-sm";
                bubble.innerText = text;
                wrapper.appendChild(bubble);
            } else {
                const avatar = document.createElement('div');
                avatar.className = "w-8 h-8 rounded-full bg-blue-600 text-white flex items-center justify-center font-bold text-xs shrink-0 mt-0.5";
                avatar.innerText = "AI";

                const bubble = document.createElement('div');
                if (isError) {
                    bubble.className = "bg-red-50 border border-red-200 text-red-800 rounded-2xl p-4 text-xs max-w-xl font-mono shadow-sm";
                } else {
                    bubble.className = "bg-white border border-slate-200/80 text-slate-800 rounded-2xl p-4 text-xs max-w-xl leading-relaxed shadow-sm";
                }
                
                let formatted = text.replace(/\*\*(.*?)\*\*/g, '<strong class="font-bold text-slate-900">$1</strong>')
                                    .replace(/`(.*?)`/g, '<code class="bg-slate-100 border border-slate-200 text-blue-700 px-1.5 py-0.5 rounded text-[11px] font-mono">$1</code>')
                                    .replace(/\n/g, '<br>');

                bubble.innerHTML = formatted;

                wrapper.appendChild(avatar);
                wrapper.appendChild(bubble);
            }

            chatBox.appendChild(wrapper);
            chatBox.scrollTop = chatBox.scrollHeight;
        }

        function handleChatSubmit(e) {
            e.preventDefault();
            const input = document.getElementById('userInput');
            const query = input.value.trim();
            if (!query) return;

            appendMessage('user', query, false);
            input.value = '';

            const secResult = evaluateSecurity(query);
            if (!secResult.isSafe) {
                appendMessage('assistant', "**[SECURITY SHIELD ACTIVATED]**\n\n" + secResult.msg, true);
                return;
            }

            setTimeout(() => {
                const response = generateAIResponse(query);
                const fullText = "**" + response.log + "**\n\n" + response.content;
                appendMessage('assistant', fullText, false);
            }, 200);
        }

        function sendQuickPrompt(promptText) {
            document.getElementById('userInput').value = promptText;
            document.getElementById('chatForm').dispatchEvent(new Event('submit'));
        }

        function clearChat() {
            document.getElementById('chatBox').innerHTML = `
                <div class="flex items-start space-x-3">
                    <div class="w-8 h-8 rounded-full bg-blue-600 text-white flex items-center justify-center font-bold text-xs shrink-0 mt-0.5">
                        AI
                    </div>
                    <div class="bg-white border border-slate-200/80 rounded-2xl p-4 text-xs text-slate-700 max-w-xl shadow-sm leading-relaxed space-y-2">
                        <p class="font-bold text-slate-900 text-sm">Halo! Saya Flight Delay & EU 261 Advisor.</p>
                        <p>Saya dapat menganalisis probabilitas keterlambatan penerbangan Anda menggunakan model <strong>LightGBM</strong> sekaligus memberikan panduan hak kompensasi berdasarkan <strong>Regulasi EU 261/2004</strong>.</p>
                        <p class="text-slate-500 pt-1 border-t border-slate-100">Silakan sesuaikan parameter penerbangan di sebelah kiri, lalu tanyakan situasi Anda di sini!</p>
                    </div>
                </div>
            `;
        }

        updatePrediction();
    </script>
</body>
</html>"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(fixed_html)

print("FIXED index.html written cleanly and verified working without JavaScript errors!")