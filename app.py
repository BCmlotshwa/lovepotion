from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>LovePotion - Bongani & VT Ndou</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@300;500&display=swap" rel="stylesheet">
        <style>
            body { margin:0; font-family:'Poppins', sans-serif; background:#fffafb; color:#444; }
            .hero { background: linear-gradient(rgba(255,107,157,0.6), rgba(196,69,105,0.6)), url('https://images.unsplash.com/photo-1518895949257-7621c3c786d7?w=900'); background-size:cover; background-position:center; height:85vh; display:flex; align-items:center; justify-content:center; text-align:center; color:white; padding:20px; }
            .hero h1 { font-family:'Dancing Script', cursive; font-size:3.5em; margin:0; text-shadow:0 2px 10px rgba(0,0,0,0.3); }
            .quote-bar { background: linear-gradient(135deg,#ff6b9d,#ffd166,#06d6a0,#118ab2); padding:18px; text-align:center; color:white; font-family:'Dancing Script', cursive; font-size:1.6em; }
            .container { max-width:850px; margin:-60px auto 0; background:white; padding:40px; border-radius:30px; box-shadow:0 15px 40px rgba(255,107,157,0.2); position:relative; border:3px solid #ffe5ec; }
            .couple-pic { width:170px; height:170px; border-radius:50%; border:6px solid white; box-shadow:0 8px 20px rgba(255,107,157,0.4); margin:-110px auto 20px; display:flex; align-items:center; justify-content:center; font-size:1.3em; font-weight:bold; background:linear-gradient(135deg,#ffafcc,#ff6b9d,#c44569); color:white; }
            .flower-divider { text-align:center; font-size:2em; margin:20px 0; letter-spacing:10px; }
            h2 { color:#c44569; text-align:center; font-family:'Dancing Script', cursive; font-size:2.2em; }
            .buttons { display:flex; gap:15px; justify-content:center; margin:30px 0; flex-wrap:wrap; }
            .btn { padding:16px 28px; border-radius:50px; text-decoration:none; font-weight:600; display:inline-block; cursor:pointer; border:none; font-size:1em; box-shadow:0 4px 15px rgba(0,0,0,0.1); transition:0.3s; }
            .btn:hover{ transform:translateY(-3px); }
            .btn-pink { background:linear-gradient(135deg,#ff6b9d,#ff8fab); color:white; }
            .btn-purple { background:linear-gradient(135deg,#a78bfa,#c44569); color:white; }
            .btn-green { background:linear-gradient(135deg,#06d6a0,#118ab2); color:white; }
            .hidden-section { display:none; margin-top:25px; padding:30px; border-radius:20px; animation: fadeIn 0.6s; }
            @keyframes fadeIn { from{opacity:0; transform:translateY(15px);} to{opacity:1; transform:translateY(0);} }
            .dos-donts { background:linear-gradient(180deg,#fff0f3,#ffe5ec); border:2px dashed #ff8fab; }
            .dos-donts-grid { display:grid; grid-template-columns:1fr 1fr; gap:20px; text-align:left; }
            .do-box { background:#e8f5e9; padding:18px; border-radius:15px; border-left:6px solid #4caf50; }
            .dont-box { background:#ffebee; padding:18px; border-radius:15px; border-left:6px solid #f44336; }
            .build-section { background:linear-gradient(180deg,#f3e5f5,#e1bee7); border:2px dashed #ce93d8; }
            .build-grid { display:grid; grid-template-columns:1fr 1fr; gap:20px; }
            .view-card { background:white; padding:22px; border-radius:18px; box-shadow:0 5px 15px rgba(0,0,0,0.07); border-top:5px solid #ff6b9d; }
            .love-quote { background:linear-gradient(135deg,#ffafcc20,#a78bfa20); border-left:5px solid #ff6b9d; padding:15px 20px; border-radius:10px; margin:20px 0; font-style:italic; font-family:'Dancing Script', cursive; font-size:1.4em; color:#c44569; }
            @media(max-width:600px){ .dos-donts-grid, .build-grid{grid-template-columns:1fr;} .hero h1{font-size:2.5em;} }
        </style>
    </head>
    <body>
        <div class="hero">
            <div>
                <h1>❤️ Bongani & VT Ndou</h1>
                <p style="font-size:1.4em; font-weight:300;">From Tinder Match to Life Partners</p>
                <p style="font-size:1.1em;">🌸 Middelburg Love Story 🌸</p>
            </div>
        </div>

        <div class="quote-bar">🌹 "We didn't find love, we built it - petal by petal, day by day" 🌹</div>
        
        <div class="container">
            <div class="couple-pic">B & VT 🌷</div>
            
            <div class="flower-divider">🌸 🌺 🌷 🌼 💐</div>
            
            <h2>How We Met</h2>
            <div class="love-quote">"Every love story is beautiful, but ours is my favorite. - Bongani"</div>
            <p style="line-height:1.9; font-size:1.1em; text-align:center;">
                We swiped right on Tinder. Everyone said Tinder is not serious, but we proved them wrong. 🌹<br>
                That first chat turned into a first meetup in <b>Middelburg</b>, and that meetup turned into us choosing each other every single day. Like flowers need sun, we grew with honesty and loyalty.
            </p>

            <div class="love-quote" style="border-left-color:#06d6a0; color:#118ab2;">"True love doesn't happen by accident, it's built with intention. - VT Ndou" 🌷</div>

            <div class="buttons">
                <button class="btn btn-pink" onclick="toggle('dos')">🌸 Do's & Don'ts 🌸</button>
                <button class="btn btn-purple" onclick="toggle('build')">💐 How We Build 💐</button>
            </div>

            <div id="dos" class="hidden-section dos-donts">
                <h2>🌹 Do's & Don'ts To Be True 🌹</h2>
                <div class="dos-donts-grid">
                    <div class="do-box">
                        <h3>🌷 DO'S - Water Your Love</h3>
                        <ul>
                            <li>💚 DO delete dating apps after you find the one</li>
                            <li>💚 DO tell the truth even when hard - honesty is fertilizer</li>
                            <li>💚 DO listen to build, not to reply</li>
                            <li>💚 DO pray, plan & grow together daily</li>
                            <li>💚 DO compliment like you water flowers - everyday</li>
                        </ul>
                    </div>
                    <div class="dont-box">
                        <h3>🥀 DON'TS - Don't Kill The Garden</h3>
                        <ul>
                            <li>💔 DON'T entertain exes or secret DMs</li>
                            <li>💔 DON'T go to sleep angry - weeds grow overnight</li>
                            <li>💔 DON'T compare your love to Instagram</li>
                            <li>💔 DON'T lie - small lies kill big gardens</li>
                            <li>💔 DON'T stop dating after commitment</li>
                        </ul>
                    </div>
                </div>
                <div class="love-quote">"Love is like a flower, you have to water it daily or it dies."</div>
            </div>

            <div id="build" class="hidden-section build-section">
                <h2>🌼 How We Build Each Other 🌼</h2>
                <div class="build-grid">
                    <div class="view-card" style="border-top-color:#2c3e50;">
                        <h3>👨🏾 Bongani's View 🌻</h3>
                        <p>Building VT means I build MYSELF first. I can't give what I don't have. So I code, I hustle, I grow. I protect her peace like a gardener protects his roses. I push her by pushing myself. Love is not just saying "I love you", it's becoming a better man every sunrise. 🌞</p>
                        <div class="love-quote" style="font-size:1.1em;">"A real man builds, he doesn't just love."</div>
                    </div>
                    <div class="view-card" style="border-top-color:#ff6b9d;">
                        <h3>👩🏾 VT Ndou's View 🌸</h3>
                        <p>Building Bongani is being his peace and his push. When he doubts, I remind him he is a king. When he wins, I celebrate like it's my win. I hold him with love, correct with kindness. We are two flowers from different gardens that decided to bloom together. 🌷💐</p>
                        <div class="love-quote" style="font-size:1.1em;">"Behind every strong man is a woman who chose to build with him."</div>
                    </div>
                </div>
            </div>

            <div class="flower-divider">🌺 🌸 🌷 🌹 💐 🌼</div>

            <div class="buttons">
                <a class="btn btn-green" href="/bongani">👨🏾 Bongani's Story</a>
                <a class="btn btn-green" href="/vt-ndou">👩🏾 VT Ndou's Story</a>
            </div>

            <p style="text-align:center; margin-top:40px; color:#ff6b9d; font-family:'Dancing Script', cursive; font-size:1.5em;">Made with ❤️ & 🌸 by Bongani & VT • Middelburg • LovePotion 2026</p>
        </div>

        <script>
            function toggle(id) {
                var el = document.getElementById(id);
                var other = id === 'dos' ? document.getElementById('build') : document.getElementById('dos');
                other.style.display = 'none';
                if (el.style.display === 'block') {
                    el.style.display = 'none';
                } else {
                    el.style.display = 'block';
                    el.scrollIntoView({behavior:'smooth'});
                }
            }
        </script>
    </body>
    </html>
    """

@app.route("/bongani")
def bongani():
    return """<html><head><meta name="viewport" content="width=device-width, initial-scale=1"><link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&display=swap" rel="stylesheet"><style>body{font-family:Poppins,sans-serif; max-width:700px; margin:0 auto; padding:30px; background:linear-gradient(135deg,#fff0f3,#ffe5ec);} .card{background:white; padding:30px; border-radius:25px; line-height:1.8; border:3px solid #ffafcc;} a{color:#c44569; text-decoration:none;}</style></head><body><div class="card"><a href="/">← Back 🌸</a><h1 style="font-family:'Dancing Script',cursive;">👨🏾 Bongani 🌻</h1><p>Developer, dreamer, and a man who learned real love is built, not found. Met VT on Tinder in Middelburg and knew she was different like a rare flower.</p><p style="font-family:'Dancing Script',cursive; color:#c44569; font-size:1.3em;">"I build for us."</p></div></body></html>"""

@app.route("/vt-ndou")
def vt():
    return """<html><head><meta name="viewport" content="width=device-width, initial-scale=1"><link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&display=swap" rel="stylesheet"><style>body{font-family:Poppins,sans-serif; max-width:700px; margin:0 auto; padding:30px; background:linear-gradient(135deg,#f3e5f5,#ffe5ec);} .card{background:white; padding:30px; border-radius:25px; line-height:1.8; border:3px solid #ce93d8;} a{color:#ff6b9d; text-decoration:none;}</style></head><body><div class="card"><a href="/">← Back 🌸</a><h1 style="font-family:'Dancing Script',cursive;">👩🏾 Miss VT Ndou 🌷</h1><p>The queen behind LovePotion. Smart, kind, strong, like a sunflower - always turning to light. She keeps me honest and focused.</p><p style="font-family:'Dancing Script',cursive; color:#c44569; font-size:1.3em;">"We bloom together."</p></div></body></html>"""

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
