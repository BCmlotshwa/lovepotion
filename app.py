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
        <style>
            body { margin:0; font-family: Georgia, serif; background:#fff8f9; color:#333; }
            .hero { background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('https://images.unsplash.com/photo-1516589178581-6cd7833ae3b2?w=800'); background-size:cover; background-position:center; height:80vh; display:flex; align-items:center; justify-content:center; text-align:center; color:white; padding:20px; }
            .hero h1 { font-size:2.8em; margin:0; }
            .container { max-width:800px; margin:-50px auto 0; background:white; padding:40px; border-radius:20px; box-shadow:0 10px 30px rgba(0,0,0,0.1); position:relative; }
            .couple-pic { width:160px; height:160px; border-radius:50%; object-fit:cover; border:5px solid white; box-shadow:0 5px 15px rgba(0,0,0,0.2); margin:-100px auto 20px; display:block; background:linear-gradient(135deg,#ff6b9d,#c44569); color:white; display:flex; align-items:center; justify-content:center; font-size:1.2em; font-weight:bold; text-align:center; }
            h2 { color:#c44569; }
            .tips { background:#fff0f3; padding:20px; border-radius:15px; border-left:5px solid #ff6b9d; margin:20px 0; }
            .buttons { display:flex; gap:15px; justify-content:center; margin:30px 0; flex-wrap:wrap; }
            .btn { padding:15px 25px; border-radius:50px; text-decoration:none; font-weight:bold; display:inline-block; }
            .btn-bongani { background:#2c3e50; color:white; }
            .btn-her { background:#ff6b9d; color:white; }
            .advice { display:grid; grid-template-columns:1fr 1fr; gap:20px; margin-top:30px; }
            @media(max-width:600px){ .advice{grid-template-columns:1fr;} .hero h1{font-size:2em;} }
            .advice-card { background:#f8f9fa; padding:20px; border-radius:15px; text-align:center; }
        </style>
    </head>
    <body>
        <div class="hero">
            <div>
                <h1>💘 Bongani & VT Ndou</h1>
                <p style="font-size:1.3em;">From Tinder Match to Life Partners</p>
            </div>
        </div>
        
        <div class="container">
            <div class="couple-pic">B & VT</div>
            <h2 style="text-align:center;">How We Met - Tinder to True Love</h2>
            <p style="line-height:1.8; font-size:1.1em;">
                We swiped right on Tinder. Everyone said Tinder is not serious, but we proved them wrong.
                What started as a simple "Hi" turned into a 3-hour first chat, that chat turned into a first meetup in Rustenburg,
                and that meetup turned into us choosing each other every single day.<br><br>
                We didn't just find love, we decided to BUILD it. Tinder brought us together, but honesty, loyalty, and pushing each other to grow kept us together.
            </p>

            <div class="buttons">
                <a class="btn btn-bongani" href="/bongani">👨🏾 Bongani's Story</a>
                <a class="btn btn-her" href="/vt-ndou">👩🏾 VT Ndou's Story</a>
            </div>

            <h2>💡 How To Be True To Your Partner</h2>
            <div class="tips">
                <p><strong>1. Delete the Apps After You Find The One:</strong> We met on Tinder, then we deleted Tinder. Loyalty is sexy.</p>
                <p><strong>2. Honesty is the Potion:</strong> Tell the truth even when it's uncomfortable. No DMs, no secrets.</p>
                <p><strong>3. Listen to Build, Not to Reply:</strong> VT taught me to hear her dreams, not just her complaints.</p>
                <p><strong>4. Choose Each Other Daily:</strong> Love is not a feeling, it's a decision before God and each other.</p>
            </div>

            <h2>🏗️ How To Build Each Other</h2>
            <div class="advice">
                <div class="advice-card">
                    <h3>🚀 Support Dreams</h3>
                    <p>VT supports my coding dream, I support hers. We are each other's biggest fans.</p>
                </div>
                <div class="advice-card">
                    <h3>🤝 Communicate</h3>
                    <p>From Tinder chat to real talk - we talk about money, future, fears. No silent treatment.</p>
                </div>
            </div>

            <p style="text-align:center; margin-top:40px; color:#888;">Made with ❤️ by Bongani & VT • Rustenburg • LovePotion 2026</p>
        </div>
    </body>
    </html>
    """

@app.route("/bongani")
def bongani():
    return """
    <html><head><meta name="viewport" content="width=device-width, initial-scale=1">
    <style>body{font-family:sans-serif; max-width:700px; margin:0 auto; padding:30px; background:#f8f9fa;} .card{background:white; padding:30px; border-radius:20px; line-height:1.7;} a{color:#c44569; text-decoration:none;}</style>
    </head><body><div class="card">
    <a href="/">← Back</a>
    <h1>👨🏾 Bongani</h1>
    <p>I'm Bongani from Rustenburg. Developer, dreamer, and a man who learned that real love is built, not found.</p>
    <p>I met VT on Tinder and I knew quickly she was different. My mission is to build a life where we both win, and build LovePotion to show other young South Africans that you CAN find real love online if you are true.</p>
    <p><strong>What I'm building:</strong> My skills, our future, and this website.</p>
    </div></body></html>
    """

@app.route("/vt-ndou")
def vt():
    return """
    <html><head><meta name="viewport" content="width=device-width, initial-scale=1">
    <style>body{font-family:sans-serif; max-width:700px; margin:0 auto; padding:30px; background:#fff0f3;} .card{background:white; padding:30px; border-radius:20px; line-height:1.7;} a{color:#ff6b9d; text-decoration:none;}</style>
    </head><body><div class="card">
    <a href="/">← Back</a>
    <h1>👩🏾 Miss VT Ndou</h1>
    <p>The queen behind LovePotion. Smart, kind, strong, and the reason I believe in true love.</p>
    <p>She showed me that a woman who builds with you is worth more than a thousand matches. She keeps me honest, keeps me focused, and keeps me true.</p>
    <p><em>(Bongani, ask VT to write her own bio here - in her own words!)</em></p>
    </div></body></html>
    """

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
