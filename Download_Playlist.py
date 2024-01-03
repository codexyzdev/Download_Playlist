import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pytube import YouTube, Playlist
from moviepy.editor import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio
import os
import threading

class VideoDownloader:
    def __init__(self, window):
        self.window = window
        self.setup_ui()

    def setup_ui(self):
        self.window.title("Descargar MP3")
        self.window.geometry("640x320")

        self.frame = tk.Frame(self.window, padx=20, pady=20)
        self.frame.pack()

        self.create_widgets()

    def create_widgets(self):
        self.create_url_input()
        self.create_download_button()
        self.create_status_label()
        self.create_progressbar()

    def create_url_input(self):
        url_label = tk.Label(self.frame, text="URL del Playlist:")
        url_label.grid(row=0, column=0, padx=(0, 10), pady=(0, 10))

        self.url_entry = tk.Entry(self.frame, width=40)
        self.url_entry.grid(row=0, column=1, pady=(0, 10))

    def create_download_button(self):
        download_button = tk.Button(
            self.frame, text="Descargar MP3", command=self.download_list)
        download_button.grid(row=1, column=0, columnspan=2, pady=(10, 20))

    def create_status_label(self):
        self.status_label = tk.Label(self.frame, text="", wraplength=600)
        self.status_label.grid(row=2, column=0, columnspan=2)

    def create_progressbar(self):
        self.progress_var = tk.DoubleVar()
        self.progressbar = ttk.Progressbar(
            self.frame, variable=self.progress_var, mode="determinate", maximum=100)
        self.progressbar.grid(row=3, column=0, columnspan=2, pady=(10, 20))
        self.progress_label = tk.Label(self.frame, text="")
        self.progress_label.grid(row=4, column=0, columnspan=2)

    def update_progress(self, current, total, filename):
        progress_percentage = (current / total) * 100
        self.progress_var.set(progress_percentage)
        self.progress_label.config(
            text=f"Descargando: {filename} ({current}/{total})")

    def download_video(self, url, output_folder, current_index, total_count):
        try:
            yt = YouTube(url)
            video = yt.streams.get_highest_resolution()

            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            video_file = os.path.join(output_folder, video.default_filename)
            video.download(output_folder)
            self.convert_to_mp3(video_file, output_folder)
            self.status_label.config(
                text=f"¡Descarga y conversión completadas para {video.title}")
            self.update_progress(current_index + 1, total_count, video.title)
        except Exception as e:
            error_message = str(e)
            print(
                f"Error durante la descarga y conversión de {url}: {error_message}")
            self.status_label.config(
                text=f"Error durante la descarga de {url}: {error_message}")

    def convert_to_mp3(self, video_file, output_folder):
        audio_file = os.path.join(
            output_folder, f"{os.path.splitext(os.path.basename(video_file))[0]}.mp3")

        try:
            ffmpeg_extract_audio(video_file, audio_file)
            print("¡Conversión a MP3 completada!")
            print('Eliminando .mp4')
            os.remove(video_file)
            print('.mp4 eliminado')
        except Exception as e:
            print("Ocurrió un error durante la conversión:", str(e))

    def download_list(self):
        video_url = self.url_entry.get()

        if not video_url:
            self.status_label.config(text="Por favor, ingrese una URL.")
            return

        output_folder = filedialog.askdirectory(
            title="Seleccione la carpeta de salida")

        if not output_folder:
            self.status_label.config(
                text="Operación cancelada por el usuario.")
            return

        try:
            links = Playlist(video_url)
            total_count = len(links)

            if total_count > 0:
                # Crear un hilo para la descarga y conversión
                download_thread = threading.Thread(
                    target=self.download_list_threaded, args=(links, output_folder, total_count))
                download_thread.start()
            else:
                print('Error al descargar')
        except Exception as e:
            print("Ocurrió un error durante la conversión:", str(e))

    def download_list_threaded(self, links, output_folder, total_count):
        for index, link in enumerate(links):
            self.download_video(link, output_folder, index, total_count)
        self.window.after(1000, self.reset_interface)

    def reset_interface(self):
        self.url_entry.delete(0, tk.END)
        self.status_label.config(text="")
        self.progress_var.set(0)
        self.progress_label.config(text="")
        messagebox.showinfo("Descarga Completa", "La descarga de la lista de reproducción ha finalizado.")

if __name__ == "__main__":
    window = tk.Tk()
    app = VideoDownloader(window)
    window.mainloop()
