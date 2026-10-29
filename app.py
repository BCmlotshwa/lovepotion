from flask import Flask
import os

app = Flask(__name__)

# HOME PAGE - Your Love Story
@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>LovePotion - Our Story</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body { margin:0; font-family: Georgia, serif; background:#fff8f9; color:#333; }
            .hero { background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('https://images.unsplash.com/photo-1516589178581-6cd7833ae3b2?w=800'); background-size:cover; background-position:center; height:80vh; display:flex; align-items:center; justify-content:center; text-align:center; color:white; padding:20px; }
            .hero h1 { font-size:3em; margin:0; }
            .container { max-width:800px; margin:-50px auto 0; background:white; padding:40px; border-radius:20px; box-shadow:0 10px 30px rgba(0,0,0,0.1); position:relative; }
            .couple-pic { width:150px; height:150px; border-radius:50%; object-fit:cover; border:5px solid white; box-shadow:0 5px 15px rgba(0,0,0,0.2); margin:-100px auto 20px; display:block; background:#ff6b9d; display:flex; align-items:center; justify-content:center; font-size:4em; }
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
                <h1>💘 LovePotion</h1>
                <p style="font-size:1.3em;">The story of Bongani & His Queen</p>
            </div>
        </div>
        
        <div class="container">
            <div class="couple-pic">💑</div>
            <h2 style="text-align:center;">How We Met</h2>
            <p style="line-height:1.8; font-size:1.1em;">
                Every great love story has a beginning. Ours started not with fireworks, but with a simple conversation that turned into hours, 
                hours into days, and days into a promise to build each other. We met unexpectedly, but we chose each other intentionally every day since.
                <br><br>
                <em>(Edit this story here in app.py - write your real how you met story!)</em>
            </p>

            <div class="buttons">
                <a class="btn btn-bongani" href="/bongani">👨🏾 Read Bongani's Bio</a>
                <a class="btn btn-her" href="/girlfriend">👩🏾 Read Her Bio</a>
            </div>

            <h2>💡 How To Be True To Your Partner</h2>
            <div class="tips">
                <p><strong>1. Honesty is the Potion:</strong> No secrets. Even small lies break trust.</p>
                <p><strong>2. Listen to Build, Not to Reply:</strong> Hear her dreams, not just her words.</p>
                <p><strong>3. Choose Her Daily:</strong> Love is not a feeling, it's a decision you make every morning.</p>
                <p><strong>4. Pray / Grow Together:</strong> Build spiritually, not just romantically.</p>
            </div>

            <h2>🏗️ How To Build Each Other</h2>
            <div class="advice">
                <div class="advice-card">
                    <h3>🚀 Support Dreams</h3>
                    <p>Celebrate her wins like they are yours. Push each other to be better.</p>
                </div>
                <div class="advice-card">
                    <h3>🤝 Communicate</h3>
                    <p>No silent treatment. Talk even when it's hard. That's growth.</p>
                </div>
            </div>

            <p style="text-align:center; margin-top:40px; color:#888;">Made with ❤️ in Rustenburg • LovePotion 2026</p>
        </div>
    </body>
    </html>
    """

@app.route("/bongani")
def bongani():
    return """
    <html><head><meta name="viewport" content="width=device-width, initial-scale=1">
    <style>body{font-family:sans-serif; max-width:700px; margin:0 auto; padding:30px; background:#f8f9fa;} .card{background:white; padding:30px; border-radius:20px;} a{color:#c44569;}</style>
    </head><body><div class="card">
    <a href="/">← Back to Our Story</a>
    <h1>👨🏾 Bongani</h1>
    <p><em>(Edit this!)</em> I am Bongani from Rustenburg. A dreamer, a builder, a man learning to love right. 
    I believe a real man builds his woman, protects her peace, and stays true when no one is watching.</p>
    <p>My mission is to build LovePotion to inspire other young couples in SA.</p>
    </div></body></html>
    """

@app.route("/girlfriend")
def girlfriend():
    return """
    <html><head><meta name="viewport" content="width=device-width, initial-scale=1">
    <style>body{font-family:sans-serif; max-width:700px; margin:0 auto; padding:30px; background:#fff0f3;} .card{background:white; padding:30px; border-radius:20px;} a{color:#ff6b9d;}</style>
    </head><body><div class="card">
    <a href="/">← Back to Our Story</a>
    <h1>👩🏾 My Queen</h1>
    <p><em>(Edit this! Put her real name and bio!)</em> She is the reason LovePotion exists. 
    Smart, kind, strong. She taught me that love is patient and building each other is the real potion.</p>
    <p>Her dream is... (write her dream here)</p>
    </div></body></html>
    """

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
