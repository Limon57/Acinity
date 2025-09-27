import streamlit as st
import base64

st.set_page_config(page_title="Acinity", layout="wide")

# convert image to base64
def to_base64(path: str) -> str:
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# logo path
logo_b64 = to_base64("hub/templates/images/Clipfinderlogo.png")

# styles
st.markdown("""
<style>
.stApp { background:#000; color:#fff; }

/* main title */
.big-font{
  font-size:70px !important;
  font-family:Giaza, serif;
  font-weight:bold;
  color:#fff;
  text-align:left;
  margin-top:-10px;
  margin-bottom:20px;
}

/* outer container */
.big-container{
  background:#d3d3d3;
  border-radius:10px;
  padding:30px;
  margin-top:20px;
  min-height:80vh;
  display:flex;
  flex-direction:column;
  align-items:flex-start;
}

/* apps title */
.container-title{
  font-size:50px !important;
  font-family:Giaza, serif;
  font-weight:bold;
  color:#000;
  text-align:center;
  width:100%;
  margin:0 0 30px 0;
}

/* tool card (darker) */
.inner-container{
  background:#2b2f36;       /* darker card */
  border-radius:15px;
  width:55%;
  max-width:600px;
  height:200px;
  display:flex;
  align-items:center;
  justify-content:flex-start;
  padding:20px 25px;
  gap:25px;
  margin-bottom:25px;
}
/* force white text inside the card */
.inner-container, .inner-container *{
  color:#fff !important;
}

/* logo button (no white box/lines) */
.logo-button{
  display:inline-flex;
  justify-content:center;
  align-items:center;
  width:150px; height:150px;
  background:transparent;     /* was white */
  border:none;
  outline:none;
  border-radius:10px;
  overflow:hidden;
  text-decoration:none;
  transition:transform .2s ease-in-out;
  line-height:0;              /* kill inline gap */
  box-shadow:none;
}
.logo-button:focus{ outline:none; }
.logo-button:hover{ transform:scale(1.05); }
.logo-button img{
  width:100%; height:100%;
  object-fit:contain;
  display:block;              /* no stray whitespace */
  border-radius:10px;
}

/* tool info */
.tool-info{
  display:flex;
  flex-direction:column;
  justify-content:center;
}
.tool-title{
  font-size:30px;
  font-weight:bold;
  font-family:Giaza, serif;
  margin-bottom:10px;
}
.tool-desc{
  font-size:15px;
  line-height:1.3;
  max-width:400px;
}
</style>
""", unsafe_allow_html=True)

# main title
st.markdown('<p class="big-font">Acinity</p>', unsafe_allow_html=True)

# container and tool card
st.markdown(f"""
<div class="big-container">
  <p class="container-title">Apps</p>

  <div class="inner-container">
    <a href="http://localhost:8501/tool-gui" target="_blank" class="logo-button">
      <img src="data:image/png;base64,{logo_b64}" alt="Tool Logo">
    </a>
    <div class="tool-info">
      <div class="tool-title">ClipFinder</div>
      <div class="tool-desc">
        ClipFinder is a tool that lets you upload a video and use text to find specific moments. 
        It automatically shows you the exact part of the video that matches your text. 
        From there, you can clip and save just the segment you need, making clips fast and simple.
      </div>
    </div>
  </div>

</div>
""", unsafe_allow_html=True)
