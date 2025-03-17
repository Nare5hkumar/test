from flask import Flask, request, jsonify
import instaloader

app = Flask(__name__)

def download_reel(url):
    try:
        parts = url.split("/")
        if len(parts) < 3:
            return "Invalid URL format"

        shortcode = parts[-2]  # Extract Instagram reel shortcode
        L = instaloader.Instaloader()
        post = instaloader.Post.from_shortcode(L.context, shortcode)
        return post.video_url
    except Exception as e:
        return str(e)

@app.route('/download', methods=['GET'])
def download():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "URL parameter is required"}), 400

    video_url = download_reel(url)
    return jsonify({"download_link": video_url})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)