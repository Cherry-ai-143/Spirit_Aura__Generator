import cv2
import numpy as np
import streamlit as st
import streamlit.components.v1 as components
import time
import base64

# ================= CONFIG =================
IMAGE_PATH = "FIRST_LOOK.webp"
AUDIO_PATH = "aura_music2.mp3"

LINE_THICKNESS = 2
POINT_SKIP = 5               # speed vs quality
FRAME_UPDATE_SKIP = 12       # batch UI updates
DRAW_SLEEP = 0.02            # ⏱ sketch timing (~50–55 sec)

CANNY_LOW = 80
CANNY_HIGH = 180
COLOR_CLUSTERS = 8

REVEAL_STEPS = 30            # ~10–12 sec reveal
FADE_ZONE = 40
# =========================================

st.set_page_config(page_title="Spirit Aura Generator", layout="wide")
st.title("✨ Spirit Aura Generator")

# ---------- SESSION STATE ----------
if "music_started" not in st.session_state:
    st.session_state.music_started = False

start = st.button("Generate Aura ✨")
if not start:
    st.stop()

# ---------- AUTO-PLAY + LOOP AUDIO ----------
if not st.session_state.music_started:
    with open(AUDIO_PATH, "rb") as f:
        audio_bytes = f.read()

    audio_base64 = base64.b64encode(audio_bytes).decode()
    audio_html = f"""
    <audio id="bgm" autoplay loop>
      <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
    </audio>
    <script>
      var audio = document.getElementById("bgm");
      if (audio) {{
          audio.volume = 0.6;
          audio.play();
      }}
    </script>
    """
    components.html(audio_html, height=0)
    st.session_state.music_started = True
# ------------------------------------------

# ---------- LOAD IMAGE ----------
img = cv2.imread(IMAGE_PATH)
if img is None:
    st.error("Image not found")
    st.stop()

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
h, w = img.shape[:2]

# ---------- COLOR CLUSTERING ----------
data = img.reshape((-1, 3)).astype(np.float32)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 15, 1.0)

_, labels, centers = cv2.kmeans(
    data, COLOR_CLUSTERS, None, criteria, 5, cv2.KMEANS_RANDOM_CENTERS
)

centers = np.uint8(centers)
color_img = centers[labels.flatten()].reshape(img.shape)

# ---------- EDGE DETECTION ----------
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(gray, CANNY_LOW, CANNY_HIGH)

contours, _ = cv2.findContours(
    edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)

# ---------- CANVASES ----------
sketch_canvas = np.ones((h, w, 3), dtype=np.uint8) * 255
reveal_mask = np.zeros((h, w), dtype=np.uint8)
frame_holder = st.empty()

# ================= DRAWING PHASE =================
draw_count = 0
final_frame = sketch_canvas.copy()

for contour in contours:
    if len(contour) < 2:
        continue
    for i in range(POINT_SKIP, len(contour), POINT_SKIP):
        p1 = contour[i - POINT_SKIP][0]
        p2 = contour[i][0]

        cv2.line(sketch_canvas, tuple(p1), tuple(p2), (0, 0, 0), LINE_THICKNESS)
        cv2.line(reveal_mask, tuple(p1), tuple(p2), 255, LINE_THICKNESS + 2)

        draw_count += 1

        if draw_count % FRAME_UPDATE_SKIP == 0:
            mask_3ch = cv2.cvtColor(reveal_mask, cv2.COLOR_GRAY2RGB)
            revealed_color = cv2.bitwise_and(color_img, mask_3ch)

            final_frame = cv2.addWeighted(
                sketch_canvas, 1.0,
                revealed_color, 1.0,
                0
            )
            frame_holder.image(final_frame)
            time.sleep(DRAW_SLEEP)

# ================= FINAL REVEAL =================
for step in range(REVEAL_STEPS + 1):
    mask = np.zeros((h, w), dtype=np.float32)
    reveal_height = int((step / REVEAL_STEPS) * h)

    if reveal_height > 0:
        mask[h - reveal_height : h, :] = 1.0
        y_start = max(h - reveal_height - FADE_ZONE, 0)
        for y in range(y_start, h - reveal_height):
            mask[y, :] = (y - y_start) / FADE_ZONE

    mask_3ch = np.dstack([mask] * 3)
    blended = (final_frame * (1 - mask_3ch) + img * mask_3ch).astype(np.uint8)
    frame_holder.image(blended)
    time.sleep(0.02)

# ---------- STOP MUSIC ----------
stop_audio_html = """
<script>
  var audio = document.getElementById("bgm");
  if (audio) {
      audio.pause();
      audio.currentTime = 0;
  }
</script>
"""
components.html(stop_audio_html, height=0)

st.success("✨ Aura Generated Successfully ✨")
