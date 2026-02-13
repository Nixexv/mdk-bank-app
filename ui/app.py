from __future__ import annotations

from pathlib import Path
import tkinter as tk
import webbrowser
from tkinter import font as tkfont
from tkinter import messagebox

from .assets import AssetLoader
from .layout import Colors, Fonts, Layout


class BankApp(tk.Tk):
    """Static bank window mockup based on fixed coordinates."""

    def __init__(self) -> None:
        super().__init__()
        self.title("Уралсиб — макет")
        self.geometry("1200x740")
        self.minsize(1200, 740)
        self.maxsize(1200, 740)
        self.resizable(False, False)

        self.colors = Colors(
            header="#250F56",
            left="#5F5180",
            content="#E3E2ED",
            accent="#250F56",
            text_light="#F2E6E8",
            text_dark="#250F56",
            white="#FFFFFF",
            input="#E3E2ED",
        )
        self.fonts = Fonts(
            family="Poppins",
            title=20,
            subtitle=16,
            label=24,
            medium=20,
            small=15,
            icon=34,
            card_title=18,
            card_subtitle=14,
        )

        self._init_fonts()
        self._entries: list[tk.Entry] = []
        self._entry_specs = [
            (42, 124, 315, 42),
            (42, 194, 315, 42),
            (444, 271, 312, 42),
            (444, 341, 132, 42),
            (624, 341, 132, 42),
            (425, 490, 350, 42),
            (425, 587, 350, 42),
        ]

        asset_dir = Path(__file__).resolve().parent.parent / "asset"
        self.assets = AssetLoader(asset_dir)
        if not self.assets.can_load():
            messagebox.showerror(
                "Pillow не установлен",
                "Для отображения изображений нужен пакет Pillow.\n"
                "Установите: pip install pillow",
            )

        self.canvas = tk.Canvas(
            self,
            bg=self.colors.content,
            highlightthickness=0,
        )
        self.canvas.pack(fill="both", expand=True)

        self.layout = Layout(self.canvas, self.colors, self.fonts, self.assets, self._open_adv_link)
        self.layout.draw(1200, 740)
        self._place_entries()

    def _init_fonts(self) -> None:
        try:
            tkfont.Font(family=self.fonts.family, size=12)
        except tk.TclError:
            # Fallback to default fonts if Poppins is not installed.
            self.fonts = Fonts(
                family="Helvetica",
                title=20,
                subtitle=16,
                label=24,
                medium=20,
                small=15,
                icon=34,
                card_title=18,
                card_subtitle=14,
            )

    def _place_entries(self) -> None:
        self._entries.clear()
        for i, spec in enumerate(self._entry_specs):
            x, y, w, h = spec
            show = "•" if i == 1 else ""
            entry = self._make_entry(show=show)
            entry.place(x=x, y=y, width=w, height=h)
            entry.configure(font=(self.fonts.family, self.fonts.small, "bold"))
            self._entries.append(entry)

    def _make_entry(self, show: str | None = None) -> tk.Entry:
        entry = tk.Entry(
            self,
            bg=self.colors.input,
            fg=self.colors.text_dark,
            relief="flat",
            highlightthickness=0,
            show=show or "",
        )
        return entry

    @staticmethod
    def _open_adv_link(_event: tk.Event) -> None:
        webbrowser.open("https://www.roblox.com/")
