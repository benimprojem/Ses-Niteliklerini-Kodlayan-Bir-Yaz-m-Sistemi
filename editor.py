import tkinter as tk
from tkinter import ttk
from typing import Optional

from notation_system import Segment, encode_segment, build_annotation_line


class SimpleNotationEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Ses Notasyonu Editörü")
        self.root.geometry("980x620")

        self.volume = 4
        self.pitch_index = 14  # C4
        self.duration_ms = 500
        self.mode = "normal"
        self.extension = 0
        self.silent_lip = False

        self.selection_var = tk.StringVar(value="Seçili metin yok")

        top = ttk.Frame(root, padding=12)
        top.pack(fill="x")

        ttk.Label(top, text="Seçili metin:").grid(row=0, column=0, sticky="w")
        ttk.Label(top, textvariable=self.selection_var, foreground="darkblue", font=("Segoe UI", 10, "bold")).grid(row=0, column=1, sticky="w", padx=(10, 0))

        # Editing area
        editor_frame = ttk.Frame(root)
        editor_frame.pack(fill="both", expand=True, padx=12, pady=(0, 12))

        left = ttk.Frame(editor_frame)
        left.pack(side="left", fill="both", expand=True)

        self.text_widget = tk.Text(left, wrap="word", font=("Segoe UI", 12), height=18)
        self.text_widget.pack(fill="both", expand=True)
        self.text_widget.insert("1.0", "Ahmet, neredesin?\n\nBurası örnek bir metin.")

        right = ttk.Frame(editor_frame, width=320)
        right.pack(side="right", fill="y", padx=(12, 0))

        ttk.Label(right, text="Ayarlar", font=("Segoe UI", 11, "bold")).pack(anchor="w", pady=(0, 8))

        ttk.Label(right, text="Ses şiddeti: 1-7").pack(anchor="w")
        self.vol_var = tk.StringVar(value="4")
        ttk.Entry(right, textvariable=self.vol_var, width=10).pack(anchor="w", pady=(0, 8))

        ttk.Label(right, text="Perde: C2 ... C5").pack(anchor="w")
        self.pitch_var = tk.StringVar(value="C4")
        ttk.Entry(right, textvariable=self.pitch_var, width=10).pack(anchor="w", pady=(0, 8))

        ttk.Label(right, text="Süre (ms):").pack(anchor="w")
        self.dur_var = tk.StringVar(value="500")
        ttk.Entry(right, textvariable=self.dur_var, width=10).pack(anchor="w", pady=(0, 8))

        ttk.Label(right, text="Mod:").pack(anchor="w")
        self.mode_var = tk.StringVar(value="normal")
        ttk.Combobox(right, textvariable=self.mode_var, values=["normal", "whisper", "shout", "lip"], state="readonly", width=12).pack(anchor="w", pady=(0, 8))

        ttk.Button(right, text="Seçilene uygula", command=self.apply_to_selection).pack(anchor="w", pady=(6, 0))
        ttk.Button(right, text="Geçerli notasyonu göster", command=self.show_current_annotation).pack(anchor="w", pady=(6, 0))

        self.output = tk.Text(root, height=8, font=("Consolas", 10), bg="#f7f7f7")
        self.output.pack(fill="x", padx=12, pady=(0, 12))

        self.text_widget.bind("<ButtonRelease-1>", self.update_selection)
        self.text_widget.bind("<Control-Up>", self.increase_volume)
        self.text_widget.bind("<Control-Down>", self.decrease_volume)
        self.text_widget.bind("<Alt-Up>", self.increase_pitch)
        self.text_widget.bind("<Alt-Down>", self.decrease_pitch)
        self.text_widget.bind("<Control-Right>", self.increase_duration)
        self.text_widget.bind("<Control-Left>", self.decrease_duration)

    def update_selection(self, event=None):
        sel = self.text_widget.get("sel.first", "sel.last")
        if sel:
            self.selection_var.set(sel)
        else:
            self.selection_var.set("Seçili metin yok")

    def current_segment(self, text: str) -> Segment:
        return Segment(
            text=text,
            volume=int(self.vol_var.get() or 4),
            pitch=self.pitch_var.get() or "C4",
            duration_ms=int(self.dur_var.get() or 500),
            mode=self.mode_var.get() or "normal",
            extension=self.extension,
            silent_lip=self.silent_lip,
        )

    def apply_to_selection(self):
        sel = self.text_widget.selection_get()
        if not sel:
            return
        seg = self.current_segment(sel)
        rendered = build_annotation_line(sel, seg.volume, seg.pitch, seg.duration_ms, seg.mode, seg.silent_lip, seg.extension)
        self.output.insert(tk.END, rendered + "\n")
        self.output.see(tk.END)

    def show_current_annotation(self):
        sel = self.text_widget.selection_get() if self.text_widget.selection_get() else "örnek"
        seg = self.current_segment(sel)
        self.output.insert(tk.END, seg.render_visual() + "\n")
        self.output.see(tk.END)

    def increase_volume(self, event=None):
        current = max(1, min(7, int(self.vol_var.get())))
        self.vol_var.set(str(min(7, current + 1)))
        return "break"

    def decrease_volume(self, event=None):
        current = max(1, min(7, int(self.vol_var.get())))
        self.vol_var.set(str(max(1, current - 1)))
        return "break"

    def increase_pitch(self, event=None):
        options = ["C2", "D2", "E2", "F2", "G2", "A2", "B2", "C3", "D3", "E3", "F3", "G3", "A3", "B3", "C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5", "D5", "E5", "F5", "G5", "A5", "B5"]
        current = self.pitch_var.get() or "C4"
        idx = options.index(current) if current in options else 14
        self.pitch_var.set(options[min(len(options) - 1, idx + 1)])
        return "break"

    def decrease_pitch(self, event=None):
        options = ["C2", "D2", "E2", "F2", "G2", "A2", "B2", "C3", "D3", "E3", "F3", "G3", "A3", "B3", "C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5", "D5", "E5", "F5", "G5", "A5", "B5"]
        current = self.pitch_var.get() or "C4"
        idx = options.index(current) if current in options else 14
        self.pitch_var.set(options[max(0, idx - 1)])
        return "break"

    def increase_duration(self, event=None):
        current = max(100, int(self.dur_var.get()))
        self.dur_var.set(str(current + 100))
        return "break"

    def decrease_duration(self, event=None):
        current = max(100, int(self.dur_var.get()))
        self.dur_var.set(str(max(100, current - 100)))
        return "break"


def main():
    root = tk.Tk()
    SimpleNotationEditor(root)
    root.mainloop()


if __name__ == "__main__":
    main()
