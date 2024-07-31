import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import difflib
import logging


class BulkRenameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bulk Rename Subtitles")
        self.root.geometry("500x400")

        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.progress_bar = None
        self.status_label = None
        self.log_text = None

        self.setup_logging()
        self.create_widgets()

    @staticmethod
    def setup_logging():
        logging.basicConfig(
            filename="subtitle_renamer.log",
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
        )

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        label = ttk.Label(
            main_frame,
            text="Select the directory containing your movie and subtitle files:",
            wraplength=400,
        )
        label.pack(pady=10)

        select_button = ttk.Button(
            main_frame, text="Select Directory", command=self.select_directory
        )
        select_button.pack(pady=10)

        self.progress_bar = ttk.Progressbar(
            main_frame, orient=tk.HORIZONTAL, length=300, mode="determinate"
        )
        self.progress_bar.pack(pady=10)

        self.status_label = ttk.Label(main_frame, text="")
        self.status_label.pack(pady=10)

        self.log_text = tk.Text(main_frame, height=10, width=60, state=tk.DISABLED)
        self.log_text.pack(pady=10)

    def select_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.rename_subtitles(directory)

    def rename_subtitles(self, directory):
        movie_extensions = [".mp4", ".mkv", ".avi", ".mov"]
        subtitle_extensions = [".srt", ".sub"]

        try:
            movies = []
            subtitles = []

            # Scan directory for movie and subtitle files
            for filename in os.listdir(directory):
                file_path = os.path.join(directory, filename)
                if os.path.isfile(file_path):
                    name, ext = os.path.splitext(filename)
                    if ext.lower() in movie_extensions:
                        movies.append((name, file_path))
                    elif ext.lower() in subtitle_extensions:
                        subtitles.append((name, file_path))

            total_files = len(movies)
            self.progress_bar["maximum"] = total_files

            # Rename subtitles to match movies
            for index, (movie_name, movie_path) in enumerate(movies):
                best_match = None
                best_ratio = 0.0
                for subtitle_name, subtitle_path in subtitles:
                    ratio = difflib.SequenceMatcher(
                        None, movie_name, subtitle_name
                    ).ratio()
                    if ratio > best_ratio:
                        best_ratio = ratio
                        best_match = subtitle_path

                if best_match:
                    new_subtitle_path = os.path.join(
                        directory, movie_name + os.path.splitext(best_match)[1]
                    )
                    try:
                        os.rename(best_match, new_subtitle_path)
                        log_message = f"Renamed {best_match} to {new_subtitle_path}"
                        logging.info(log_message)
                        self.update_log(log_message)
                    except FileNotFoundError:
                        error_message = f"Error: File not found - {best_match}"
                        logging.error(error_message)
                        self.update_log(error_message)
                    except PermissionError:
                        error_message = f"Error: Permission denied - {best_match}"
                        logging.error(error_message)
                        self.update_log(error_message)

                self.progress_bar["value"] = index + 1
                self.root.update_idletasks()

            self.status_label.config(text="Subtitles renamed successfully!")
            messagebox.showinfo("Success", "Subtitles renamed successfully!")

        except Exception as e:
            error_message = f"An unexpected error occurred: {str(e)}"
            logging.error(error_message)
            self.update_log(error_message)
            messagebox.showerror("Error", error_message)

    def update_log(self, message):
        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.log_text.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    app = BulkRenameApp(root)
    root.mainloop()
