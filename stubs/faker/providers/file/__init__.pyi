from .. import BaseProvider as BaseProvider, ElementsType as ElementsType
from typing import Dict, Literal, Optional, Sequence, Union

class Provider(BaseProvider):
    application_mime_types: ElementsType[str]
    audio_mime_types: ElementsType[str]
    image_mime_types: ElementsType[str]
    message_mime_types: ElementsType[str]
    model_mime_types: ElementsType[str]
    multipart_mime_types: ElementsType[str]
    text_mime_types: ElementsType[str]
    video_mime_types: ElementsType[str]
    mime_types: Dict[str, ElementsType[str]]
    audio_file_extensions: ElementsType[str]
    image_file_extensions: ElementsType[str]
    text_file_extensions: ElementsType[str]
    video_file_extensions: ElementsType[str]
    office_file_extensions: ElementsType[str]
    file_extensions: Dict[str, ElementsType[str]]
    file_systems_path_rules: Dict[str, Dict]
    unix_device_prefixes: ElementsType[str]
    def mime_type(self, category: Optional[str] = None) -> str: ...
    def file_name(self, category: Optional[str] = None, extension: Optional[str] = None) -> str: ...
    def file_extension(self, category: Optional[str] = None) -> str: ...
    def file_path(self, depth: int = 1, category: Optional[str] = None, extension: Optional[Union[str, Sequence[str]]] = None, absolute: Optional[bool] = True, file_system_rule: Literal['linux', 'windows'] = 'linux') -> str: ...
    def unix_device(self, prefix: Optional[str] = None) -> str: ...
    def unix_partition(self, prefix: Optional[str] = None) -> str: ...
