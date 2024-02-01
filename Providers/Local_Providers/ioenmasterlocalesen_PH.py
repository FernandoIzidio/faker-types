import datetime, decimal, typing_extensions, json
from typing import (
    Union,
    Optional,
    TYPE_CHECKING,
    Collection,
    Sequence,
    TypeVar,
    OrderedDict,
    List,
    Dict,
    Tuple,
    Type,
    Any,
    Iterator,
    Callable,
    Iterable,
    Set,
)
import uuid

HueType = TypeVar("HueType")
T = TypeVar("T")
M = TypeVar("M")
F = TypeVar("F")
CT_co = Type("CT_co")
T_co = Type("T_co")
TEnum = Type("TeNum")
KT = TypeVar("KT")
VT = TypeVar("VT")


if TYPE_CHECKING:
    from faker.providers.credit_card import CardType
from faker.providers.address.en_PH import Provider


class Provider:
    def address(
        self,
    ) -> str:
        ...

    def administrative_unit(
        self,
    ) -> str:
        ...

    def building_name(
        self,
    ) -> str:
        ...

    def building_name_suffix(
        self,
    ) -> str:
        ...

    def building_number(
        self,
    ) -> str:
        ...

    def building_unit_number(
        self,
    ) -> str:
        ...

    def city(
        self,
    ) -> str:
        ...

    def city_suffix(
        self,
    ) -> str:
        ...

    def country(
        self,
    ) -> str:
        ...

    def country_code(self, representation: str = "alpha-2") -> str:
        ...

    def current_country(
        self,
    ) -> str:
        ...

    def current_country_code(
        self,
    ) -> str:
        ...

    def floor_number(
        self,
    ) -> str:
        ...

    def floor_unit_number(
        self,
    ) -> str:
        ...

    def luzon_province(
        self,
    ) -> str:
        ...

    def luzon_province_address(
        self,
    ) -> str:
        ...

    def luzon_province_postcode(
        self,
    ) -> str:
        ...

    def metro_manila_address(
        self,
    ) -> str:
        ...

    def metro_manila_lgu(
        self,
    ) -> str:
        ...

    def metro_manila_postcode(
        self,
    ) -> str:
        ...

    def mindanao_province(
        self,
    ) -> str:
        ...

    def mindanao_province_address(
        self,
    ) -> str:
        ...

    def mindanao_province_postcode(
        self,
    ) -> str:
        ...

    def ordinal_floor_number(
        self,
    ) -> str:
        ...

    def ordinal_street_number(
        self,
    ) -> str:
        ...

    def partitioned_building_number(
        self,
    ) -> str:
        ...

    def postcode(
        self,
    ) -> str:
        ...

    def province(
        self,
    ) -> str:
        ...

    def province_lgu(
        self,
    ) -> str:
        ...

    def standalone_building_number(
        self,
    ) -> str:
        ...

    def street_address(
        self,
    ) -> str:
        ...

    def street_name(
        self,
    ) -> str:
        ...

    def street_suffix(
        self,
    ) -> str:
        ...

    def subdivision_block_number(
        self,
    ) -> str:
        ...

    def subdivision_lot_number(
        self,
    ) -> str:
        ...

    def subdivision_name(
        self,
    ) -> str:
        ...

    def subdivision_name_suffix(
        self,
    ) -> str:
        ...

    def subdivision_unit_number(
        self,
    ) -> str:
        ...

    def visayas_province(
        self,
    ) -> str:
        ...

    def visayas_province_address(
        self,
    ) -> str:
        ...

    def visayas_province_postcode(
        self,
    ) -> str:
        ...


from faker.providers.automotive.en_PH import Provider


class Provider:
    def automobile_license_plate(
        self,
    ) -> str:
        ...

    def license_plate(
        self,
    ) -> str:
        ...

    def motorcycle_license_plate(
        self,
    ) -> str:
        ...

    def protocol_license_plate(
        self,
    ) -> str:
        ...

    def vin(
        self,
    ) -> str:
        ...


from faker.providers.bank.en_PH import Provider


class Provider:
    def aba(
        self,
    ) -> str:
        ...

    def bank_country(
        self,
    ) -> str:
        ...

    def bban(
        self,
    ) -> str:
        ...

    def iban(
        self,
    ) -> str:
        ...

    def swift(
        self,
        length: Optional[int] = None,
        primary: bool = False,
        use_dataset: bool = False,
    ) -> str:
        ...

    def swift11(self, primary: bool = False, use_dataset: bool = False) -> str:
        ...

    def swift8(self, use_dataset: bool = False) -> str:
        ...


from faker.providers.company.en_PH import Provider


class Provider:
    def bs(
        self,
    ) -> str:
        ...

    def catch_phrase(
        self,
    ) -> str:
        ...

    def company(
        self,
    ) -> str:
        ...

    def company_suffix(
        self,
    ) -> str:
        ...

    def company_type(
        self,
    ) -> str:
        ...

    def random_company_acronym(
        self,
    ) -> str:
        ...

    def random_company_adjective(
        self,
    ) -> str:
        ...

    def random_company_noun_chain(
        self,
    ) -> str:
        ...

    def random_company_product(
        self,
    ) -> str:
        ...


from faker.providers.date_time.en_PH import Provider


class Provider:
    def am_pm(
        self,
    ) -> str:
        ...

    def century(
        self,
    ) -> str:
        ...

    def date(
        self,
        pattern: str = "%Y-%m-%d",
        end_datetime: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int, None
        ] = None,
    ) -> str:
        ...

    def date_between(
        self,
        start_date: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int
        ] = "-30y",
        end_date: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int
        ] = "today",
    ) -> datetime.date:
        ...

    def date_between_dates(
        self,
        date_start: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int, None
        ] = None,
        date_end: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int, None
        ] = None,
    ) -> datetime.date:
        ...

    def date_object(
        self, end_datetime: Optional[datetime.datetime] = None
    ) -> datetime.date:
        ...

    def date_of_birth(
        self,
        tzinfo: Optional[datetime.tzinfo] = None,
        minimum_age: int = 0,
        maximum_age: int = 115,
    ) -> datetime.date:
        ...

    def date_this_century(
        self, before_today: bool = True, after_today: bool = False
    ) -> datetime.date:
        ...

    def date_this_decade(
        self, before_today: bool = True, after_today: bool = False
    ) -> datetime.date:
        ...

    def date_this_month(
        self, before_today: bool = True, after_today: bool = False
    ) -> datetime.date:
        ...

    def date_this_year(
        self, before_today: bool = True, after_today: bool = False
    ) -> datetime.date:
        ...

    def date_time(
        self,
        tzinfo: Optional[datetime.tzinfo] = None,
        end_datetime: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int, None
        ] = None,
    ) -> datetime.datetime:
        ...

    def date_time_ad(
        self,
        tzinfo: Optional[datetime.tzinfo] = None,
        end_datetime: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int, None
        ] = None,
        start_datetime: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int, None
        ] = None,
    ) -> datetime.datetime:
        ...

    def date_time_between(
        self,
        start_date: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int
        ] = "-30y",
        end_date: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int
        ] = "now",
        tzinfo: Optional[datetime.tzinfo] = None,
    ) -> datetime.datetime:
        ...

    def date_time_between_dates(
        self,
        datetime_start: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int, None
        ] = None,
        datetime_end: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int, None
        ] = None,
        tzinfo: Optional[datetime.tzinfo] = None,
    ) -> datetime.datetime:
        ...

    def date_time_this_century(
        self,
        before_now: bool = True,
        after_now: bool = False,
        tzinfo: Optional[datetime.tzinfo] = None,
    ) -> datetime.datetime:
        ...

    def date_time_this_decade(
        self,
        before_now: bool = True,
        after_now: bool = False,
        tzinfo: Optional[datetime.tzinfo] = None,
    ) -> datetime.datetime:
        ...

    def date_time_this_month(
        self,
        before_now: bool = True,
        after_now: bool = False,
        tzinfo: Optional[datetime.tzinfo] = None,
    ) -> datetime.datetime:
        ...

    def date_time_this_year(
        self,
        before_now: bool = True,
        after_now: bool = False,
        tzinfo: Optional[datetime.tzinfo] = None,
    ) -> datetime.datetime:
        ...

    def day_of_month(
        self,
    ) -> str:
        ...

    def day_of_week(
        self,
    ) -> str:
        ...

    def future_date(
        self,
        end_date: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int
        ] = "+30d",
        tzinfo: Optional[datetime.tzinfo] = None,
    ) -> datetime.date:
        ...

    def future_datetime(
        self,
        end_date: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int
        ] = "+30d",
        tzinfo: Optional[datetime.tzinfo] = None,
    ) -> datetime.datetime:
        ...

    def iso8601(
        self,
        tzinfo: Optional[datetime.tzinfo] = None,
        end_datetime: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int, None
        ] = None,
        sep: str = "T",
        timespec: str = "auto",
    ) -> str:
        ...

    def month(
        self,
    ) -> str:
        ...

    def month_name(
        self,
    ) -> str:
        ...

    def past_date(
        self,
        start_date: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int
        ] = "-30d",
        tzinfo: Optional[datetime.tzinfo] = None,
    ) -> datetime.date:
        ...

    def past_datetime(
        self,
        start_date: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int
        ] = "-30d",
        tzinfo: Optional[datetime.tzinfo] = None,
    ) -> datetime.datetime:
        ...

    def pytimezone(self, *args, **kwargs) -> Optional[datetime.tzinfo]:
        ...

    def time(
        self,
        pattern: str = "%H:%M:%S",
        end_datetime: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int, None
        ] = None,
    ) -> str:
        ...

    def time_delta(
        self,
        end_datetime: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int, None
        ] = None,
    ) -> datetime.timedelta:
        ...

    def time_object(
        self,
        end_datetime: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int, None
        ] = None,
    ) -> datetime.time:
        ...

    def time_series(
        self,
        start_date: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int
        ] = "-30d",
        end_date: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int
        ] = "now",
        precision: Optional[float] = None,
        distrib: Optional[Callable[[datetime.datetime], float]] = None,
        tzinfo: Optional[datetime.tzinfo] = None,
    ) -> Iterator[Tuple[datetime.datetime, Any]]:
        ...

    def timezone(
        self,
    ) -> str:
        ...

    def unix_time(
        self,
        end_datetime: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int, None
        ] = None,
        start_datetime: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int, None
        ] = None,
    ) -> int:
        ...

    def year(
        self,
    ) -> str:
        ...


from faker.providers.internet.en_PH import Provider


class Provider:
    def ascii_company_email(
        self,
    ) -> str:
        ...

    def ascii_email(
        self,
    ) -> str:
        ...

    def ascii_free_email(
        self,
    ) -> str:
        ...

    def ascii_safe_email(
        self,
    ) -> str:
        ...

    def company_email(
        self,
    ) -> str:
        ...

    def dga(
        self,
        year: Optional[int] = None,
        month: Optional[int] = None,
        day: Optional[int] = None,
        tld: Optional[str] = None,
        length: Optional[int] = None,
    ) -> str:
        ...

    def domain_name(self, levels: int = 1) -> str:
        ...

    def domain_word(
        self,
    ) -> str:
        ...

    def email(self, safe: bool = True, domain: Optional[str] = None) -> str:
        ...

    def free_email(
        self,
    ) -> str:
        ...

    def free_email_domain(
        self,
    ) -> str:
        ...

    def hostname(self, levels: int = 1) -> str:
        ...

    def http_method(
        self,
    ) -> str:
        ...

    def iana_id(
        self,
    ) -> str:
        ...

    def image_url(
        self,
        width: Optional[int] = None,
        height: Optional[int] = None,
        placeholder_url: Optional[str] = None,
    ) -> str:
        ...

    def ipv4(
        self,
        network: bool = False,
        address_class: Optional[str] = None,
        private: Optional[str] = None,
    ) -> str:
        ...

    def ipv4_network_class(
        self,
    ) -> str:
        ...

    def ipv4_private(
        self, network: bool = False, address_class: Optional[str] = None
    ) -> str:
        ...

    def ipv4_public(
        self, network: bool = False, address_class: Optional[str] = None
    ) -> str:
        ...

    def ipv6(self, network: bool = False) -> str:
        ...

    def mac_address(
        self,
    ) -> str:
        ...

    def nic_handle(self, suffix: str = "FAKE") -> str:
        ...

    def nic_handles(self, count: int = 1, suffix: str = "????") -> List[str]:
        ...

    def port_number(
        self, is_system: bool = False, is_user: bool = False, is_dynamic: bool = False
    ) -> int:
        ...

    def ripe_id(
        self,
    ) -> str:
        ...

    def safe_domain_name(
        self,
    ) -> str:
        ...

    def safe_email(
        self,
    ) -> str:
        ...

    def slug(self, value: Optional[str] = None) -> str:
        ...

    def tld(
        self,
    ) -> str:
        ...

    def uri(
        self,
    ) -> str:
        ...

    def uri_extension(
        self,
    ) -> str:
        ...

    def uri_page(
        self,
    ) -> str:
        ...

    def uri_path(self, deep: Optional[int] = None) -> str:
        ...

    def url(self, schemes: Optional[List[str]] = None) -> str:
        ...

    def user_name(
        self,
    ) -> str:
        ...


from faker.providers.lorem.en_PH import Provider


class Provider:
    def english_paragraph(
        self, nb_sentences: int = 3, variable_nb_sentences: bool = True
    ) -> str:
        ...

    def english_paragraphs(self, nb: int = 3) -> List[str]:
        ...

    def english_sentence(
        self, nb_words: int = 6, variable_nb_words: bool = True
    ) -> str:
        ...

    def english_sentences(self, nb: int = 3) -> List[str]:
        ...

    def english_text(self, max_nb_chars: int = 200) -> str:
        ...

    def english_texts(self, nb_texts: int = 3, max_nb_chars: int = 200) -> List[str]:
        ...

    def english_word(
        self,
    ) -> str:
        ...

    def english_words(self, nb: int = 3, unique: bool = False) -> List[str]:
        ...

    def paragraph(
        self,
        nb_sentences: int = 3,
        variable_nb_sentences: bool = True,
        ext_word_list: Optional[Sequence[str]] = None,
    ) -> str:
        ...

    def paragraphs(
        self, nb: int = 3, ext_word_list: Optional[Sequence[str]] = None
    ) -> List[str]:
        ...

    def sentence(
        self,
        nb_words: int = 6,
        variable_nb_words: bool = True,
        ext_word_list: Optional[Sequence[str]] = None,
    ) -> str:
        ...

    def sentences(
        self, nb: int = 3, ext_word_list: Optional[Sequence[str]] = None
    ) -> List[str]:
        ...

    def text(
        self, max_nb_chars: int = 200, ext_word_list: Optional[Sequence[str]] = None
    ) -> str:
        ...

    def texts(
        self,
        nb_texts: int = 3,
        max_nb_chars: int = 200,
        ext_word_list: Optional[Sequence[str]] = None,
    ) -> List[str]:
        ...

    def word(
        self,
        part_of_speech: Optional[str] = None,
        ext_word_list: Optional[Sequence[str]] = None,
    ) -> str:
        ...

    def words(
        self,
        nb: int = 3,
        part_of_speech: Optional[str] = None,
        ext_word_list: Optional[Sequence[str]] = None,
        unique: bool = False,
    ) -> List[str]:
        ...


from faker.providers.misc.en_PH import Provider


class Provider:
    def binary(self, length: int = 1048576) -> bytes:
        ...

    def boolean(self, chance_of_getting_true: int = 50) -> bool:
        ...

    def csv(
        self,
        header: Optional[Sequence[str]] = None,
        data_columns: Tuple[str, str] = ("{{name}}", "{{address}}"),
        num_rows: int = 10,
        include_row_ids: bool = False,
    ) -> str:
        ...

    def dsv(
        self,
        dialect: str = "faker-csv",
        header: Optional[Sequence[str]] = None,
        data_columns: Tuple[str, str] = ("{{name}}", "{{address}}"),
        num_rows: int = 10,
        include_row_ids: bool = False,
        **fmtparams
    ) -> str:
        ...

    def fixed_width(
        self,
        data_columns: Optional[list] = None,
        num_rows: int = 10,
        align: str = "left",
    ) -> str:
        ...

    def gemstone_name(
        self,
    ) -> str:
        ...

    def image(
        self,
        size: Tuple[int, int] = (256, 256),
        image_format: str = "png",
        hue: Union[int, Sequence[int], str, None] = None,
        luminosity: Optional[str] = None,
    ) -> bytes:
        ...

    def json(
        self,
        data_columns: Optional[List[T]] = None,
        num_rows: int = 10,
        indent: Optional[int] = None,
        cls: Optional[Type[json.encoder.JSONEncoder]] = None,
    ) -> str:
        ...

    def json_bytes(
        self,
        data_columns: Optional[List[T]] = None,
        num_rows: int = 10,
        indent: Optional[int] = None,
        cls: Optional[Type[json.encoder.JSONEncoder]] = None,
    ) -> bytes:
        ...

    def md5(self, raw_output: bool = False) -> Union[bytes, str]:
        ...

    def mountain_name(
        self,
    ) -> str:
        ...

    def null_boolean(
        self,
    ) -> Optional[bool]:
        ...

    def password(
        self,
        length: int = 10,
        special_chars: bool = True,
        digits: bool = True,
        upper_case: bool = True,
        lower_case: bool = True,
    ) -> str:
        ...

    def plant_name(
        self,
    ) -> str:
        ...

    def psv(
        self,
        header: Optional[Sequence[str]] = None,
        data_columns: Tuple[str, str] = ("{{name}}", "{{address}}"),
        num_rows: int = 10,
        include_row_ids: bool = False,
    ) -> str:
        ...

    def random_object_name(
        self,
    ) -> str:
        ...

    def sha1(self, raw_output: bool = False) -> Union[bytes, str]:
        ...

    def sha256(self, raw_output: bool = False) -> Union[bytes, str]:
        ...

    def space_object_name(
        self,
    ) -> str:
        ...

    def tar(
        self,
        uncompressed_size: int = 65536,
        num_files: int = 1,
        min_file_size: int = 4096,
        compression: Optional[str] = None,
    ) -> bytes:
        ...

    def tsv(
        self,
        header: Optional[Sequence[str]] = None,
        data_columns: Tuple[str, str] = ("{{name}}", "{{address}}"),
        num_rows: int = 10,
        include_row_ids: bool = False,
    ) -> str:
        ...

    def uuid4(
        self,
        cast_to: Union[
            Callable[[uuid.UUID], str], Callable[[uuid.UUID], bytes], None
        ] = "str",
    ) -> Union[bytes, str, uuid.UUID]:
        ...

    def xml(
        self,
        nb_elements: int = 10,
        variable_nb_elements: bool = True,
        value_types: Union[List[Type[CT_co]], Tuple[Type[CT_co], ...], None] = None,
        allowed_types: Union[List[Type[CT_co]], Tuple[Type[CT_co], ...], None] = None,
    ) -> str:
        ...

    def zip(
        self,
        uncompressed_size: int = 65536,
        num_files: int = 1,
        min_file_size: int = 4096,
        compression: Optional[str] = None,
    ) -> bytes:
        ...


from faker.providers.phone_number.en_PH import Provider


class Provider:
    def area2_landline_number(
        self,
    ) -> str:
        ...

    def bayantel_area2_landline_number(
        self,
    ) -> str:
        ...

    def bayantel_landline_identifier(
        self,
    ) -> str:
        ...

    def globe_area2_landline_number(
        self,
    ) -> str:
        ...

    def globe_mobile_number(
        self,
    ) -> str:
        ...

    def globe_mobile_number_prefix(
        self,
    ) -> str:
        ...

    def landline_number(
        self,
    ) -> str:
        ...

    def misc_area2_landline_number(
        self,
    ) -> str:
        ...

    def misc_landline_identifier(
        self,
    ) -> str:
        ...

    def mobile_number(
        self,
    ) -> str:
        ...

    def non_area2_landline_area_code(
        self,
    ) -> str:
        ...

    def non_area2_landline_number(
        self,
    ) -> str:
        ...

    def pldt_area2_landline_number(
        self,
    ) -> str:
        ...

    def smart_mobile_number(
        self,
    ) -> str:
        ...

    def smart_mobile_number_prefix(
        self,
    ) -> str:
        ...

    def sun_mobile_number(
        self,
    ) -> str:
        ...

    def sun_mobile_number_prefix(
        self,
    ) -> str:
        ...


from faker.providers.ssn.en_PH import Provider


class Provider:
    def gsis(
        self,
    ) -> str:
        ...

    def pagibig(
        self,
    ) -> str:
        ...

    def philhealth(
        self,
    ) -> str:
        ...

    def ssn(
        self,
    ) -> str:
        ...

    def sss(
        self,
    ) -> str:
        ...

    def umid(
        self,
    ) -> str:
        ...
