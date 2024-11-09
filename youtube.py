import tkinter
import customtkinter
import yt_dlp

def startDownload():
    # Create a YoutubeDL object with progress hook
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.mp3',
        'progress_hooks': [on_progress]
    }
    
    try:
        url = link.get()
        with yt_dlp.YoutubeDL({'quiet': True}) as ydl_info:
            info_dict = ydl_info.extract_info(url, download=False)
            video_title = info_dict.get('title', 'Video')
            titleLabel.configure(text=f"Descargando: {video_title}")
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        finishLabel.configure(text="Descarga completada", text_color="green")
    
    except Exception as e:
        finishLabel.configure(text="Hubo un problema al descargar el video: " + str(e), text_color="red")
        
def on_progress(d):
    if d['status'] == 'downloading':
        total_bytes = d.get('total_bytes', 0)
        downloaded_bytes = d.get('downloaded_bytes', 0)
        if total_bytes > 0:
            percentage = (downloaded_bytes / total_bytes) * 100
            pPercentage.configure(text=f"{percentage:.2f}%")
            pPercentage.update()
            progressBar.set(percentage / 100)
    elif d['status'] == 'finished':
        progressBar.set(1.0)

# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Descargador de audio de YouTube")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Descargador de audio de YouTube")
title.pack(padx=10, pady=10)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=340, height=40, textvariable=url_var)
link.pack()

# Video title label
titleLabel = customtkinter.CTkLabel(app, text="")
titleLabel.pack(pady=5)

# Progress percentage
pPercentage = customtkinter.CTkLabel(app, text="0 %")
pPercentage.pack()

# Progress bar
progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Download button
download = customtkinter.CTkButton(app, text="Descargar", command=startDownload)
download.pack(padx=10, pady=10)

# Finished Downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Run app
app.mainloop()
