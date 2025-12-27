<!-- ===================================================== -->
<!-- =================== EVID X X MUSIC ================== -->
<!-- ===================================================== -->

<!-- ===================== STYLE 1: GIF BANNER ===================== -->
<!-- ACTIVE -->
<h1 align="center">
── 「 ✦ 👾 𝐄𝐕𝐈𝐃 ✘ ✘ 𝐌𝐔𝐒𝐈𝐂 👾 ✦ 」 ──
</h1>

<p align="center">
 <img
  src="https://files.catbox.moe/qq6yk6.gif"
  alt="Dark Hacker Console"
  width="100%"
/>
</p>

<!-- ===================== STYLE 2: NEON / CYBERPUNK ===================== -->
<!--
<h1 align="center">
── 「 ✦ ⚡ 𝐄𝐕𝐈𝐃 ✘ ✘ 𝐌𝐔𝐒𝐈𝐂 ⚡ ✦ 」 ──
</h1>

<p align="center">
  <img
    src="https://images.unsplash.com/photo-1519681393784-d120267933ba?q=80&w=1600&auto=format&fit=crop"
    width="100%"
  />
</p>
-->

<!-- ===================== STYLE 3: ULTRA-MINIMAL DARK ===================== -->
<!--
<h1 align="center">𝐄𝐕𝐈𝐃 ✘ ✘ 𝐌𝐔𝐒𝐈𝐂</h1>
<p align="center"><b>Minimal • Dark • Powerful</b></p>
-->

<!-- ===================== STYLE 4: WAVEFORM STYLE ===================== -->
<!--
<h1 align="center">
── 「 🎼 𝐄𝐕𝐈𝐃 ✘ ✘ 𝐌𝐔𝐒𝐈𝐂 🎼 」 ──
</h1>

<p align="center">
  <img
    src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png"
    width="100%"
  />
</p>
-->

<p align="center">
  <img src="https://img.shields.io/github/stars/Evid3008/EvidXMusic?style=for-the-badge&logo=github&color=00e5ff" />
  <img src="https://img.shields.io/github/forks/Evid3008/EvidXMusic?style=for-the-badge&logo=github&color=7c4dff" />
  <img src="https://img.shields.io/badge/License-GPL--3.0-purple?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Built%20With-Python-yellow?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/github/last-commit/Evid3008/EvidXMusic?style=for-the-badge&logo=github&color=00c853" />
</p>

<p align="center">
  <img
    src="https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&size=22&duration=2800&pause=1200&color=00E5FF&center=true&vCenter=true&width=900&lines=🎧+Next-Gen+Telegram+Music+Bot;⚡+Fast+•+Stable+•+Modern;🔁+Smart+Auto+Play+Enabled;🎶+Voice+Chat+Music+Streaming+Reimagined"
  />
</p>

---

## 🎵 About EvidXMusic

**EvidXMusic** is a next-generation **Telegram Music Bot** built using **Python & Pyrogram v2**.  
It delivers smooth, high-quality music streaming in Telegram voice chats with a modern interface and smart automation.

---

## 🚀 Features

- 🎶 High-quality voice chat music streaming  
- 🔍 YouTube search & instant play  
- 📃 Queue & playlist management  
- ⏯️ Play / Pause / Resume / Skip  
- 🔁 **Auto Play** – automatically plays related tracks  
- 🗳️ Vote-based admin controls  
- 🌐 Multi-language support  
- ⚡ Optimized for VPS & local hosting  

---

## 🧑‍💻 Developer & Project

- **Developer:** EVID  
- **Telegram:** [@iq4u8](https://t.me/iq4u8)  
- **GitHub:** https://github.com/Evid3008  
- **Repository:** https://github.com/Evid3008/EvidXMusic  

---

## 🛠 Deployment (VPS / Localhost)

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip ffmpeg -y
pip3 install -U pip
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install -y nodejs

git clone https://github.com/Evid3008/EvidXMusic
cd EvidXMusic
pip install -U -r requirements.txt
cp sample.env .env
nano .env
bash start
