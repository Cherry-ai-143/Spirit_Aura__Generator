# ✨ Spirit Aura Generator

**Spirit Aura Generator** is a cinematic, interactive **Streamlit-based web application** that transforms an image into a **spiritual sketch-style aura animation** with synchronized background music.

The application gradually draws the image like an artist’s sketch, reveals colors organically, and completes with a smooth final reveal — all while background music auto-plays and loops until the process finishes.

---

## 🔮 Project Highlights

* 🎨 **Sketch-style aura generation** using OpenCV
* 🌈 **Color clustering** for artistic color reveal
* ✍️ **Progressive contour drawing animation**
* 🎵 **Auto-playing & looping background music** (no manual click)
* ⏱️ Controlled animation duration (~1–1.1 minutes)
* 🌐 Fully web-based using **Streamlit**
* 🧠 Efficient frame batching for smooth performance

---

## 🧰 Tech Stack

| Component        | Technology                                   |
| ---------------- | -------------------------------------------- |
| Language         | Python                                       |
| UI Framework     | Streamlit                                    |
| Image Processing | OpenCV (cv2)                                 |
| Numerical Ops    | NumPy                                        |
| Audio Handling   | HTML + JavaScript (via Streamlit components) |
| Image Format     | WebP                                         |

---

## 📁 Project Structure

```
SPIRIT-AURA-GENERATOR/
│
├── app.py               # Main Streamlit application
├── FIRST_LOOK.webp      # Input image (WebP format)
├── aura_music.mp3       # Background music
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## ⚙️ How It Works (Logic Overview)

### 1️⃣ Image Preprocessing

* Input image is loaded and converted to RGB
* Gaussian blur + Canny edge detection used to extract contours

### 2️⃣ Color Clustering

* KMeans clustering reduces image colors into artistic palettes
* Clustered colors are revealed progressively

### 3️⃣ Sketch Drawing Phase

* Contours are drawn point-by-point on a white canvas
* Frame updates are batched for performance
* Reveal mask uncovers color beneath the sketch

### 4️⃣ Final Aura Reveal

* Smooth vertical fade reveals the full original image
* Creates a spiritual, cinematic ending

### 5️⃣ Music Synchronization

* Music auto-plays when generation starts
* Audio loops continuously during animation
* Music stops cleanly when aura generation completes

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/spirit-aura-generator.git
cd spirit-aura-generator
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the App

```bash
streamlit run app.py
```

---

## 🖼️ Input Image Guidelines

* Supported formats: **PNG / JPG / JPEG / BMP / GIF** (convert to WebP)
* Recommended resolution: **≤ 1920×1080**
* Use WebP for faster loading and smoother animation

### Convert Image to WebP (OpenCV)

```python
cv2.imwrite("FIRST_LOOK.webp", img, [cv2.IMWRITE_WEBP_QUALITY, 90])
```

---

## 🎵 Audio Guidelines

* Format: **MP3**
* Duration: Any (audio loops automatically)
* Place file as: `aura_music.mp3`

---

## ⏱️ Animation Timing Control

Key parameters in `app.py`:

* `POINT_SKIP` → drawing detail vs speed
* `DRAW_SLEEP` → sketch duration
* `REVEAL_STEPS` → final reveal smoothness

These allow precise control over total animation time.

---

## 🌟 Use Cases

* Creative coding projects
* Digital art & generative visuals
* Spiritual / aura visualization
* Portfolio demonstration
* Streamlit + OpenCV showcase

---

## 📌 Future Enhancements

* Multiple aura styles
* Beat-synced color reveal
* User-uploaded images
* Download generated video
* Mobile-friendly UI

---

## 👨‍💻 Author

**Mohan C C**
Final Year Engineering Student (AIML)
Passionate about AI, computer vision, and creative web apps

---

## 📜 License

This project is licensed under the **MIT License**.

Feel free to use, modify, and share 🚀

---

✨ *If you like this project, don’t forget to ⭐ the repository!* ✨
