#from flaskwebgui import FlaskUI
from youtube_video_downloader import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
    #FlaskUI(app, width=1200, height=800).run()