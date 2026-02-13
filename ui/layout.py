from __future__ import annotations

import tkinter as tk
from dataclasses import dataclass
from typing import Callable

from .assets import AssetLoader
from .draw import place_image, rounded_rect


@dataclass(frozen=True)
class Colors:
    header: str
    left: str
    content: str
    accent: str
    text_light: str
    text_dark: str
    white: str
    input: str


@dataclass(frozen=True)
class Fonts:
    family: str
    title: int
    subtitle: int
    label: int
    medium: int
    small: int
    icon: int
    card_title: int
    card_subtitle: int


class Layout:
    BASE_WIDTH = 1200
    BASE_HEIGHT = 740

    def __init__(
        self,
        canvas: tk.Canvas,
        colors: Colors,
        fonts: Fonts,
        assets: AssetLoader,
        on_adv_click: Callable[[tk.Event], None],
    ) -> None:
        self.canvas = canvas
        self.colors = colors
        self.fonts = fonts
        self.assets = assets
        self.on_adv_click = on_adv_click
        self._scale = 1.0
        self._offset_x = 0.0
        self._offset_y = 0.0

    @staticmethod
    def compute_metrics(width: int, height: int) -> tuple[float, float, float]:
        scale = min(width / Layout.BASE_WIDTH, height / Layout.BASE_HEIGHT)
        offset_x = (width - Layout.BASE_WIDTH * scale) / 2
        offset_y = (height - Layout.BASE_HEIGHT * scale) / 2
        return scale, offset_x, offset_y

    def _sx(self, x: float) -> int:
        return int(round(x * self._scale + self._offset_x))

    def _sy(self, y: float) -> int:
        return int(round(y * self._scale + self._offset_y))

    def _s(self, value: float, minimum: int = 1) -> int:
        return max(minimum, int(round(value * self._scale)))

    def _font(self, size: int, weight: str = "bold") -> tuple:
        return (self.fonts.family, self._s(size, minimum=8), weight)

    def draw(self, width: int, height: int) -> None:
        self.canvas.delete("all")
        self._scale, self._offset_x, self._offset_y = self.compute_metrics(width, height)
        self._draw_background()
        self._draw_header()
        self._draw_left_panel()
        self._draw_main_content()

    def _draw_background(self) -> None:
        self.canvas.create_rectangle(
            0, 0, self.canvas.winfo_width(), self.canvas.winfo_height(),
            fill=self.colors.content, outline=self.colors.content
        )
        self.canvas.create_rectangle(
            self._sx(0), self._sy(0), self._sx(400), self._sy(740),
            fill=self.colors.left, outline=self.colors.left
        )

    def _draw_header(self) -> None:
        self.canvas.create_rectangle(
            self._sx(0), self._sy(0), self._sx(1200), self._sy(80),
            fill=self.colors.header, outline=self.colors.header
        )

        logo = self.assets.load_image("logo", "logo.jpg", self._s(355), self._s(80))
        place_image(self.canvas, logo, self._sx(0), self._sy(0))

        self.canvas.create_rectangle(
            self._sx(1040), self._sy(14), self._sx(1090), self._sy(64),
            outline=self.colors.text_light, width=self._s(1)
        )
        self.canvas.create_text(
            self._sx(1065),
            self._sy(39),
            text="?",
            fill=self.colors.text_light,
            font=self._font(self.fonts.icon),
        )

        self.canvas.create_line(
            self._sx(1130), self._sy(24), self._sx(1180), self._sy(24),
            fill=self.colors.text_light, width=self._s(5)
        )
        self.canvas.create_line(
            self._sx(1130), self._sy(39), self._sx(1180), self._sy(39),
            fill=self.colors.text_light, width=self._s(5)
        )
        self.canvas.create_line(
            self._sx(1130), self._sy(54), self._sx(1180), self._sy(54),
            fill=self.colors.text_light, width=self._s(5)
        )

    def _draw_left_panel(self) -> None:
        rounded_rect(
            self.canvas,
            self._sx(38), self._sy(120), self._sx(361), self._sy(170),
            self._s(10), self.colors.input, ""
        )
        rounded_rect(
            self.canvas,
            self._sx(38), self._sy(190), self._sx(361), self._sy(240),
            self._s(10), self.colors.input, ""
        )

        self.canvas.create_text(
            self._sx(54),
            self._sy(145),
            text="ЛОГИН",
            anchor="w",
            fill=self.colors.white,
            font=self._font(self.fonts.label),
        )
        self.canvas.create_text(
            self._sx(54),
            self._sy(215),
            text="ПАРОЛЬ",
            anchor="w",
            fill=self.colors.white,
            font=self._font(self.fonts.label),
        )

        self.canvas.create_text(
            self._sx(38),
            self._sy(278),
            text="Запомнить логин",
            anchor="w",
            fill=self.colors.text_light,
            font=self._font(self.fonts.label),
        )

        self.canvas.create_rectangle(
            self._sx(331), self._sy(263), self._sx(361), self._sy(293),
            outline="#EEE0E5", width=self._s(1)
        )
        self.canvas.create_text(
            self._sx(346),
            self._sy(278),
            text="✓",
            fill=self.colors.text_light,
            font=self._font(self.fonts.label),
        )

        rounded_rect(
            self.canvas,
            self._sx(38), self._sy(336), self._sx(361), self._sy(396),
            self._s(10), self.colors.accent, ""
        )
        self.canvas.create_text(
            self._sx(200),
            self._sy(366),
            text="АВТОРИЗОВАТЬСЯ",
            fill=self.colors.text_light,
            font=self._font(self.fonts.label),
        )

        self.canvas.create_text(
            self._sx(38),
            self._sy(451),
            text="Это длинный текст перед..",
            anchor="w",
            fill=self.colors.text_light,
            font=self._font(self.fonts.medium),
        )
        man = self.assets.load_image("man", "man.png", self._s(30), self._s(30))
        place_image(self.canvas, man, self._sx(331), self._sy(436))

        rounded_rect(
            self.canvas,
            self._sx(38), self._sy(486), self._sx(361), self._sy(536),
            self._s(10), self.colors.white, ""
        )
        self.canvas.create_text(
            self._sx(200),
            self._sy(511),
            text="ЗАРЕГИСТРИРОВАТЬСЯ",
            fill=self.colors.text_dark,
            font=self._font(self.fonts.label),
        )

    def _draw_main_content(self) -> None:
        self.canvas.create_text(
            self._sx(442),
            self._sy(132),
            text="УМНАЯ СИСТЕМА ПЕРЕВОДОВ",
            anchor="w",
            fill=self.colors.text_dark,
            font=self._font(self.fonts.title),
        )
        self.canvas.create_text(
            self._sx(464),
            self._sy(155),
            text="С ВНЕДРЕНИЕМ СОВРЕМЕННЫХ ИИ",
            anchor="w",
            fill=self.colors.text_dark,
            font=self._font(self.fonts.subtitle),
        )
        self.canvas.create_text(
            self._sx(1014),
            self._sy(112),
            text="НАМ ДОВЕРЯЮТ",
            anchor="w",
            fill=self.colors.text_dark,
            font=self._font(self.fonts.title),
        )

        rounded_rect(
            self.canvas,
            self._sx(420), self._sy(190), self._sx(780), self._sy(419),
            self._s(16), self.colors.accent, ""
        )
        self.canvas.create_text(
            self._sx(450),
            self._sy(236),
            text="Уралсиб",
            anchor="w",
            fill=self.colors.white,
            font=self._font(self.fonts.card_title),
        )
        self.canvas.create_text(
            self._sx(740),
            self._sy(236),
            text="Business",
            anchor="e",
            fill=self.colors.white,
            font=self._font(self.fonts.card_subtitle),
        )

        rounded_rect(
            self.canvas,
            self._sx(440), self._sy(267), self._sx(760), self._sy(317),
            self._s(10), self.colors.input, ""
        )
        rounded_rect(
            self.canvas,
            self._sx(440), self._sy(337), self._sx(580), self._sy(387),
            self._s(10), self.colors.input, ""
        )
        rounded_rect(
            self.canvas,
            self._sx(620), self._sy(337), self._sx(760), self._sy(387),
            self._s(10), self.colors.input, ""
        )

        self.canvas.create_text(
            self._sx(451),
            self._sy(292),
            text="НОМЕР КАРТЫ",
            anchor="w",
            fill=self.colors.white,
            font=self._font(self.fonts.label),
        )
        self.canvas.create_text(
            self._sx(451),
            self._sy(362),
            text="MM/ГГ",
            anchor="w",
            fill=self.colors.white,
            font=self._font(self.fonts.label),
        )
        self.canvas.create_text(
            self._sx(631),
            self._sy(362),
            text="CVC/CVV",
            anchor="w",
            fill=self.colors.white,
            font=self._font(self.fonts.label),
        )

        self.canvas.create_text(
            self._sx(426),
            self._sy(470),
            text="Сумма перевода",
            anchor="w",
            fill=self.colors.text_dark,
            font=self._font(self.fonts.small),
        )
        rounded_rect(
            self.canvas,
            self._sx(421), self._sy(486), self._sx(779), self._sy(536),
            self._s(10), self.colors.input, self.colors.accent, self._s(1)
        )

        self.canvas.create_text(
            self._sx(426),
            self._sy(567),
            text="Сообщение получателю",
            anchor="w",
            fill=self.colors.text_dark,
            font=self._font(self.fonts.small),
        )
        rounded_rect(
            self.canvas,
            self._sx(421), self._sy(583), self._sx(779), self._sy(633),
            self._s(10), self.colors.input, self.colors.accent, self._s(1)
        )

        rounded_rect(
            self.canvas,
            self._sx(421), self._sy(653), self._sx(779), self._sy(713),
            self._s(10), self.colors.accent, ""
        )
        self.canvas.create_text(
            self._sx(600),
            self._sy(683),
            text="ПЕРЕВЕСТИ",
            fill=self.colors.text_light,
            font=self._font(self.fonts.label),
        )

        self.canvas.create_rectangle(
            self._sx(804), self._sy(138), self._sx(1182), self._sy(735),
            outline=self.colors.accent, width=self._s(3)
        )
        adv = self.assets.load_image(
            "adv", "adv.jpg", self._s(372), self._s(591), fill=True
        )
        adv_id = place_image(self.canvas, adv, self._sx(807), self._sy(141))
        if adv_id is not None:
            self.canvas.tag_bind(adv_id, "<Button-1>", self.on_adv_click)
            self.canvas.tag_bind(adv_id, "<Enter>", lambda _e: self.canvas.configure(cursor="hand2"))
            self.canvas.tag_bind(adv_id, "<Leave>", lambda _e: self.canvas.configure(cursor=""))
