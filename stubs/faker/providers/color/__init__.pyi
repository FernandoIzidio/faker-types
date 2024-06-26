from .. import BaseProvider as BaseProvider, ElementsType as ElementsType
from ...typing import HueType as HueType
from .color import RandomColor as RandomColor
from functools import cached_property as cached_property
from typing import Dict, Optional, Tuple

localized: bool

class Provider(BaseProvider):
    all_colors: Dict[str, str]
    safe_colors: ElementsType[str]
    def color_name(self) -> str: ...
    def safe_color_name(self) -> str: ...
    def hex_color(self) -> str: ...
    def safe_hex_color(self) -> str: ...
    def rgb_color(self) -> str: ...
    def rgb_css_color(self) -> str: ...
    def color(self, hue: Optional[HueType] = None, luminosity: Optional[str] = None, color_format: str = 'hex') -> str: ...
    def color_rgb(self, hue: Optional[HueType] = None, luminosity: Optional[str] = None) -> Tuple[int, int, int]: ...
    def color_rgb_float(self, hue: Optional[HueType] = None, luminosity: Optional[str] = None) -> Tuple[float, float, float]: ...
    def color_hsl(self, hue: Optional[HueType] = None, luminosity: Optional[str] = None) -> Tuple[int, int, int]: ...
    def color_hsv(self, hue: Optional[HueType] = None, luminosity: Optional[str] = None) -> Tuple[int, int, int]: ...
