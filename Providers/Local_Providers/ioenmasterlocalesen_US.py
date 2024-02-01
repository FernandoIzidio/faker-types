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
from faker.providers.address.en_US import Provider


class Provider:
    def address(
        self,
    ) -> str:
        ...

    def administrative_unit(
        self,
    ) -> str:
        ...

    def building_number(
        self,
    ) -> str:
        ...

    def city(
        self,
    ) -> str:
        ...

    def city_prefix(
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

    def military_apo(
        self,
    ) -> str:
        ...

    def military_dpo(
        self,
    ) -> str:
        ...

    def military_ship(
        self,
    ) -> str:
        ...

    def military_state(
        self,
    ) -> str:
        ...

    def postalcode(
        self,
    ) -> str:
        ...

    def postalcode_in_state(self, state_abbr: Optional[str] = None) -> str:
        ...

    def postalcode_plus4(
        self,
    ) -> str:
        ...

    def postcode(
        self,
    ) -> str:
        ...

    def postcode_in_state(self, state_abbr: Optional[str] = None) -> str:
        ...

    def secondary_address(
        self,
    ) -> str:
        ...

    def state(
        self,
    ) -> str:
        ...

    def state_abbr(
        self,
        include_territories: bool = True,
        include_freely_associated_states: bool = True,
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

    def zipcode(
        self,
    ) -> str:
        ...

    def zipcode_in_state(self, state_abbr: Optional[str] = None) -> str:
        ...

    def zipcode_plus4(
        self,
    ) -> str:
        ...


from faker.providers.automotive.en_US import Provider


class Provider:
    def license_plate(
        self,
    ) -> str:
        ...

    def vin(
        self,
    ) -> str:
        ...


from faker.providers.barcode.en_US import Provider


class Provider:
    def ean(
        self,
        length: int = 13,
        prefixes: Tuple[Union[int, str, Tuple[Union[int, str], ...]], ...] = (),
    ) -> str:
        ...

    def ean13(
        self,
        prefixes: Tuple[Union[int, str, Tuple[Union[int, str], ...]], ...] = (),
        leading_zero: Optional[bool] = None,
    ) -> str:
        ...

    def ean8(self, prefixes: Tuple[()] = ()) -> str:
        ...

    def localized_ean(self, length: int = 13) -> str:
        ...

    def localized_ean13(
        self,
    ) -> str:
        ...

    def localized_ean8(
        self,
    ) -> str:
        ...

    def upc_a(
        self,
        upc_ae_mode: bool = False,
        base: Optional[str] = None,
        number_system_digit: Optional[int] = None,
    ) -> str:
        ...

    def upc_e(
        self,
        base: Optional[str] = None,
        number_system_digit: Optional[int] = None,
        safe_mode: bool = True,
    ) -> str:
        ...


from faker.providers.color.en_US import Provider


class Provider:
    def color(
        self,
        hue: Optional[HueType] = None,
        luminosity: Optional[str] = None,
        color_format: str = "hex",
    ) -> str:
        ...

    def color_name(
        self,
    ) -> str:
        ...

    def hex_color(
        self,
    ) -> str:
        ...

    def rgb_color(
        self,
    ) -> str:
        ...

    def rgb_css_color(
        self,
    ) -> str:
        ...

    def safe_color_name(
        self,
    ) -> str:
        ...

    def safe_hex_color(
        self,
    ) -> str:
        ...


from faker.providers.company.en_US import Provider


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


from faker.providers.credit_card.en_US import Provider


class Provider:
    def credit_card_expire(
        self,
        start: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int
        ] = "now",
        end: Union[
            datetime.date, datetime.datetime, datetime.timedelta, str, int
        ] = "+10y",
        date_format: str = "%m/%y",
    ) -> str:
        ...

    def credit_card_full(self, card_type: Optional[CardType] = None) -> str:
        ...

    def credit_card_number(self, card_type: Optional[CardType] = None) -> str:
        ...

    def credit_card_provider(self, card_type: Optional[CardType] = None) -> str:
        ...

    def credit_card_security_code(self, card_type: Optional[CardType] = None) -> str:
        ...


from faker.providers.currency.en_US import Provider


class Provider:
    def cryptocurrency(
        self,
    ) -> Tuple[str, str]:
        ...

    def cryptocurrency_code(
        self,
    ) -> str:
        ...

    def cryptocurrency_name(
        self,
    ) -> str:
        ...

    def currency(
        self,
    ) -> Tuple[str, str]:
        ...

    def currency_code(
        self,
    ) -> str:
        ...

    def currency_name(
        self,
    ) -> str:
        ...

    def currency_symbol(self, code: Optional[str] = None) -> str:
        ...

    def pricetag(
        self,
    ) -> str:
        ...


from faker.providers.date_time.en_US import Provider


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


from faker.providers.emoji.en_US import Provider


class Provider:
    def emoji(
        self,
    ) -> str:
        ...


from faker.providers.file.en_US import Provider


class Provider:
    def file_extension(self, category: Optional[str] = None) -> str:
        ...

    def file_name(
        self, category: Optional[str] = None, extension: Optional[str] = None
    ) -> str:
        ...

    def file_path(
        self,
        depth: int = 1,
        category: Optional[str] = None,
        extension: Optional[str] = None,
        absolute: Optional[bool] = True,
    ) -> str:
        ...

    def mime_type(self, category: Optional[str] = None) -> str:
        ...

    def unix_device(self, prefix: Optional[str] = None) -> str:
        ...

    def unix_partition(self, prefix: Optional[str] = None) -> str:
        ...


from faker.providers.geo.en_US import Provider


class Provider:
    def coordinate(
        self, center: Optional[float] = None, radius: Union[float, int] = 0.001
    ) -> decimal.Decimal:
        ...

    def latitude(
        self,
    ) -> decimal.Decimal:
        ...

    def latlng(
        self,
    ) -> Tuple[decimal.Decimal, decimal.Decimal]:
        ...

    def local_latlng(
        self, country_code: str = "US", coords_only: bool = False
    ) -> Optional[Tuple[str, ...]]:
        ...

    def location_on_land(self, coords_only: bool = False) -> Tuple[str, ...]:
        ...

    def longitude(
        self,
    ) -> decimal.Decimal:
        ...


from faker.providers.internet.en_US import Provider


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


from faker.providers.isbn.en_US import Provider


class Provider:
    def isbn10(self, separator: str = "-") -> str:
        ...

    def isbn13(self, separator: str = "-") -> str:
        ...


from faker.providers.job.en_US import Provider


class Provider:
    def job(
        self,
    ) -> str:
        ...


from faker.providers.lorem.en_US import Provider


class Provider:
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


from faker.providers.misc.en_US import Provider


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

    def psv(
        self,
        header: Optional[Sequence[str]] = None,
        data_columns: Tuple[str, str] = ("{{name}}", "{{address}}"),
        num_rows: int = 10,
        include_row_ids: bool = False,
    ) -> str:
        ...

    def sha1(self, raw_output: bool = False) -> Union[bytes, str]:
        ...

    def sha256(self, raw_output: bool = False) -> Union[bytes, str]:
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


from faker.providers.passport.en_US import Provider


class Provider:
    def passport_dates(
        self, birthday: datetime.date = datetime.date(2023, 7, 11)
    ) -> Tuple[str, str, str]:
        ...

    def passport_dob(
        self,
    ) -> datetime.date:
        ...

    def passport_full(
        self,
    ) -> str:
        ...

    def passport_gender(self, seed: int = 0) -> str:
        ...

    def passport_number(
        self,
    ) -> str:
        ...

    def passport_owner(self, gender: str = "X") -> Tuple[str, str]:
        ...


from faker.providers.person.en_US import Provider


class Provider:
    def first_name(
        self,
    ) -> str:
        ...

    def first_name_female(
        self,
    ) -> str:
        ...

    def first_name_male(
        self,
    ) -> str:
        ...

    def first_name_nonbinary(
        self,
    ) -> str:
        ...

    def language_name(
        self,
    ) -> str:
        ...

    def last_name(
        self,
    ) -> str:
        ...

    def last_name_female(
        self,
    ) -> str:
        ...

    def last_name_male(
        self,
    ) -> str:
        ...

    def last_name_nonbinary(
        self,
    ) -> str:
        ...

    def name(
        self,
    ) -> str:
        ...

    def name_female(
        self,
    ) -> str:
        ...

    def name_male(
        self,
    ) -> str:
        ...

    def name_nonbinary(
        self,
    ) -> str:
        ...

    def prefix(
        self,
    ) -> str:
        ...

    def prefix_female(
        self,
    ) -> str:
        ...

    def prefix_male(
        self,
    ) -> str:
        ...

    def prefix_nonbinary(
        self,
    ) -> str:
        ...

    def suffix(
        self,
    ) -> str:
        ...

    def suffix_female(
        self,
    ) -> str:
        ...

    def suffix_male(
        self,
    ) -> str:
        ...

    def suffix_nonbinary(
        self,
    ) -> str:
        ...


from faker.providers.phone_number.en_US import Provider


class Provider:
    def basic_phone_number(
        self,
    ) -> str:
        ...

    def country_calling_code(
        self,
    ) -> str:
        ...

    def msisdn(
        self,
    ) -> str:
        ...

    def phone_number(
        self,
    ) -> str:
        ...


from faker.providers.profile.en_US import Provider


class Provider:
    def profile(
        self,
        fields: Optional[List[str]] = None,
        sex: Optional[typing_extensions.Literal["M", "F"][M, F]] = None,
    ) -> Dict[
        str,
        Union[str, Tuple[decimal.Decimal, decimal.Decimal], List[str], datetime.date],
    ]:
        ...

    def simple_profile(
        self, sex: Optional[typing_extensions.Literal["M", "F"][M, F]] = None
    ) -> Dict[
        str, Union[str, datetime.date, typing_extensions.Literal["M", "F"][M, F]]
    ]:
        ...


from faker.providers.python.en_US import Provider


class Provider:
    def enum(self, enum_cls: Type[TEnum]) -> TEnum:
        ...

    def pybool(self, truth_probability: int = 50) -> bool:
        ...

    def pydecimal(
        self,
        left_digits=None,
        right_digits=None,
        positive=False,
        min_value=None,
        max_value=None,
    ):
        ...

    def pydict(
        self,
        nb_elements: int = 10,
        variable_nb_elements: bool = True,
        value_types: Union[List[Type[CT_co]], Tuple[Type[CT_co], ...], None] = None,
        allowed_types: Union[List[Type[CT_co]], Tuple[Type[CT_co], ...], None] = None,
    ) -> Dict[Any, Any]:
        ...

    def pyfloat(
        self,
        left_digits=None,
        right_digits=None,
        positive=False,
        min_value=None,
        max_value=None,
    ):
        ...

    def pyint(self, min_value: int = 0, max_value: int = 9999, step: int = 1) -> int:
        ...

    def pyiterable(
        self,
        nb_elements: int = 10,
        variable_nb_elements: bool = True,
        value_types: Union[List[Type[CT_co]], Tuple[Type[CT_co], ...], None] = None,
        allowed_types: Union[List[Type[CT_co]], Tuple[Type[CT_co], ...], None] = None,
    ) -> Iterable[Any]:
        ...

    def pylist(
        self,
        nb_elements: int = 10,
        variable_nb_elements: bool = True,
        value_types: Union[List[Type[CT_co]], Tuple[Type[CT_co], ...], None] = None,
        allowed_types: Union[List[Type[CT_co]], Tuple[Type[CT_co], ...], None] = None,
    ) -> List[Any]:
        ...

    def pyobject(
        self,
        object_type: Optional[
            Type[Union[bool, str, float, int, tuple, set, list, Iterable[T_co], dict]]
        ] = None,
    ) -> Union[bool, str, float, int, tuple, set, list, Iterable[T_co], dict, None]:
        ...

    def pyset(
        self,
        nb_elements: int = 10,
        variable_nb_elements: bool = True,
        value_types: Union[List[Type[CT_co]], Tuple[Type[CT_co], ...], None] = None,
        allowed_types: Union[List[Type[CT_co]], Tuple[Type[CT_co], ...], None] = None,
    ) -> Set[Any]:
        ...

    def pystr(
        self,
        min_chars: Optional[int] = None,
        max_chars: int = 20,
        prefix: str = "",
        suffix: str = "",
    ) -> str:
        ...

    def pystr_format(
        self,
        string_format: str = "?#-###{{random_int}}{{random_letter}}",
        letters: str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
    ) -> str:
        ...

    def pystruct(
        self,
        count: int = 10,
        value_types: Union[List[Type[CT_co]], Tuple[Type[CT_co], ...], None] = None,
        allowed_types: Union[List[Type[CT_co]], Tuple[Type[CT_co], ...], None] = None,
    ) -> Tuple[List[T], Dict[KT, VT], Dict[KT, VT]]:
        ...

    def pytuple(
        self,
        nb_elements: int = 10,
        variable_nb_elements: bool = True,
        value_types: Union[List[Type[CT_co]], Tuple[Type[CT_co], ...], None] = None,
        allowed_types: Union[List[Type[CT_co]], Tuple[Type[CT_co], ...], None] = None,
    ) -> Tuple[Any, ...]:
        ...


from faker.providers.sbn.en_US import Provider


class Provider:
    def sbn9(self, separator: str = "-") -> str:
        ...


from faker.providers.ssn.en_US import Provider


class Provider:
    def ein(
        self,
    ) -> str:
        ...

    def invalid_ssn(
        self,
    ) -> str:
        ...

    def itin(
        self,
    ) -> str:
        ...

    def ssn(self, taxpayer_identification_number_type: str = "SSN") -> str:
        ...


from faker.providers.user_agent.en_US import Provider


class Provider:
    def android_platform_token(
        self,
    ) -> str:
        ...

    def chrome(
        self,
        version_from: int = 13,
        version_to: int = 63,
        build_from: int = 800,
        build_to: int = 899,
    ) -> str:
        ...

    def firefox(
        self,
    ) -> str:
        ...

    def internet_explorer(
        self,
    ) -> str:
        ...

    def ios_platform_token(
        self,
    ) -> str:
        ...

    def linux_platform_token(
        self,
    ) -> str:
        ...

    def linux_processor(
        self,
    ) -> str:
        ...

    def mac_platform_token(
        self,
    ) -> str:
        ...

    def mac_processor(
        self,
    ) -> str:
        ...

    def opera(
        self,
    ) -> str:
        ...

    def safari(
        self,
    ) -> str:
        ...

    def user_agent(
        self,
    ) -> str:
        ...

    def windows_platform_token(
        self,
    ) -> str:
        ...
