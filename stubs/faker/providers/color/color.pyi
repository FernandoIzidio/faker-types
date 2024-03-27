from ...factory import Generator as Generator
from ...typing import HueType as HueType
from _typeshed import Incomplete
from typing import Dict, Hashable, Optional, Sequence, Tuple

ColorFormat: Incomplete
COLOR_MAP: Dict[str, Dict[str, Sequence[Tuple[int, int]]]]

class RandomColor:
    colormap: Incomplete
    random: Incomplete
    seed: Incomplete
    def __init__(self, generator: Optional['Generator'] = None, seed: Optional[Hashable] = None) -> None: ...
    def generate(self, hue: Optional[HueType] = None, luminosity: Optional[str] = None, color_format: ColorFormat = 'hex') -> str: ...
    def generate_hsv(self, hue: Optional[HueType] = None, luminosity: Optional[str] = None) -> Tuple[int, int, int]: ...
    def generate_rgb(self, hue: Optional[HueType] = None, luminosity: Optional[str] = None) -> Tuple[int, int, int]: ...
    def generate_rgb_float(self, hue: Optional[HueType] = None, luminosity: Optional[str] = None) -> Tuple[float, float, float]: ...
    def generate_hsl(self, hue: Optional[HueType] = None, luminosity: Optional[str] = None) -> Tuple[int, int, int]: ...
    def pick_hue(self, hue: Optional[HueType]) -> int: ...
    def pick_saturation(self, hue: int, hue_name: Optional[HueType], luminosity: Optional[str]) -> int: ...
    def pick_brightness(self, h: int, s: int, luminosity: Optional[str]) -> int: ...
    def set_format(self, hsv: Tuple[int, int, int], color_format: ColorFormat) -> str: ...
    def get_minimum_brightness(self, h: int, s: int) -> int: ...
    def get_hue_range(self, color_input: Optional[HueType]) -> Tuple[int, int]: ...
    def get_saturation_range(self, hue: int) -> Tuple[int, int]: ...
    def get_color_info(self, hue: int) -> Dict[str, Sequence[Tuple[int, int]]]: ...
    def random_within(self, r: Sequence[int]) -> int: ...
    @classmethod
    def hsv_to_rgb_float(cls, hsv: Tuple[int, int, int]) -> Tuple[float, float, float]: ...
    @classmethod
    def hsv_to_rgb(cls, hsv: Tuple[int, int, int]) -> Tuple[int, int, int]: ...
    @classmethod
    def hsv_to_hsl(cls, hsv: Tuple[int, int, int]) -> Tuple[int, int, int]: ...