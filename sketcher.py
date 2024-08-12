import streamlit as st
import streamlit.components.v1 as components

# HTML + JavaScript code for the drawing canvas
html_code = """
<!DOCTYPE html>
<html>
<head>
<style>
  canvas {
    border: 1px solid black;
  }
</style>
</head>
<body>
<canvas id="canvas" width="500" height="500"></canvas>
<script>
  const canvas = document.getElementById('canvas');
  const ctx = canvas.getContext('2d');
  let drawing = false;

  canvas.addEventListener('mousedown', () => {
    drawing = true;
  });

  canvas.addEventListener('mouseup', () => {
    drawing = false;
    ctx.beginPath();
  });

  canvas.addEventListener('mousemove', (event) => {
    if (!drawing) return;

    ctx.lineWidth = 5;
    ctx.lineCap = 'round';
    ctx.strokeStyle = 'black';

    ctx.lineTo(event.clientX - canvas.offsetLeft, event.clientY - canvas.offsetTop);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(event.clientX - canvas.offsetLeft, event.clientY - canvas.offsetTop);
  });

  function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
  }

  window.clearCanvas = clearCanvas;
</script>
<button onclick="clearCanvas()">Clear Canvas</button>
</body>
</html>
"""

# Streamlit app layout
st.title("Sketcher App")

# Render the HTML and JavaScript code
components.html(html_code, height=600)
