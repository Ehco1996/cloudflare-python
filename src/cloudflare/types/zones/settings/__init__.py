# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .zones_nel import ZonesNEL as ZonesNEL
from .zones_ssl import ZonesSSL as ZonesSSL
from .zones_waf import ZonesWAF as ZonesWAF
from .zones_0rtt import Zones0rtt as Zones0rtt
from .zones_ipv6 import ZonesIPV6 as ZonesIPV6
from .zones_webp import ZonesWebp as ZonesWebp
from .zones_http2 import ZonesHTTP2 as ZonesHTTP2
from .zones_http3 import ZonesHTTP3 as ZonesHTTP3
from .zones_brotli import ZonesBrotli as ZonesBrotli
from .zones_minify import ZonesMinify as ZonesMinify
from .zones_mirage import ZonesMirage as ZonesMirage
from .zones_polish import ZonesPolish as ZonesPolish
from .zones_ciphers import ZonesCiphers as ZonesCiphers
from .zones_tls_1_3 import ZonesTLS1_3 as ZonesTLS1_3
from .nel_edit_params import NELEditParams as NELEditParams
from .ssl_edit_params import SSLEditParams as SSLEditParams
from .waf_edit_params import WAFEditParams as WAFEditParams
from .zones_buffering import ZonesBuffering as ZonesBuffering
from .zones_nel_param import ZonesNELParam as ZonesNELParam
from .zones_ssl_param import ZonesSSLParam as ZonesSSLParam
from .zones_waf_param import ZonesWAFParam as ZonesWAFParam
from .ipv6_edit_params import IPV6EditParams as IPV6EditParams
from .webp_edit_params import WebpEditParams as WebpEditParams
from .zones_0rtt_param import Zones0rttParam as Zones0rttParam
from .zones_ipv6_param import ZonesIPV6Param as ZonesIPV6Param
from .zones_webp_param import ZonesWebpParam as ZonesWebpParam
from .zones_websockets import ZonesWebsockets as ZonesWebsockets
from .http2_edit_params import HTTP2EditParams as HTTP2EditParams
from .http3_edit_params import HTTP3EditParams as HTTP3EditParams
from .zones_cache_level import ZonesCacheLevel as ZonesCacheLevel
from .zones_early_hints import ZonesEarlyHints as ZonesEarlyHints
from .zones_http2_param import ZonesHTTP2Param as ZonesHTTP2Param
from .zones_http3_param import ZonesHTTP3Param as ZonesHTTP3Param
from .zones_pseudo_ipv4 import ZonesPseudoIPV4 as ZonesPseudoIPV4
from .brotli_edit_params import BrotliEditParams as BrotliEditParams
from .cipher_edit_params import CipherEditParams as CipherEditParams
from .minify_edit_params import MinifyEditParams as MinifyEditParams
from .mirage_edit_params import MirageEditParams as MirageEditParams
from .polish_edit_params import PolishEditParams as PolishEditParams
from .zones_brotli_param import ZonesBrotliParam as ZonesBrotliParam
from .zones_minify_param import ZonesMinifyParam as ZonesMinifyParam
from .zones_mirage_param import ZonesMirageParam as ZonesMirageParam
from .zones_polish_param import ZonesPolishParam as ZonesPolishParam
from .tls_1_3_edit_params import TLS1_3EditParams as TLS1_3EditParams
from .zones_advanced_ddos import ZonesAdvancedDDOS as ZonesAdvancedDDOS
from .zones_always_online import ZonesAlwaysOnline as ZonesAlwaysOnline
from .zones_browser_check import ZonesBrowserCheck as ZonesBrowserCheck
from .zones_challenge_ttl import ZonesChallengeTTL as ZonesChallengeTTL
from .zones_ciphers_param import ZonesCiphersParam as ZonesCiphersParam
from .zones_rocket_loader import ZonesRocketLoader as ZonesRocketLoader
from .zones_tls_1_3_param import ZonesTLS1_3Param as ZonesTLS1_3Param
from .zero_rtt_edit_params import ZeroRTTEditParams as ZeroRTTEditParams
from .zones_image_resizing import ZonesImageResizing as ZonesImageResizing
from .zones_ip_geolocation import ZonesIPGeolocation as ZonesIPGeolocation
from .zones_security_level import ZonesSecurityLevel as ZonesSecurityLevel
from .websocket_edit_params import WebsocketEditParams as WebsocketEditParams
from .zones_buffering_param import ZonesBufferingParam as ZonesBufferingParam
from .zones_min_tls_version import ZonesMinTLSVersion as ZonesMinTLSVersion
from .zones_mobile_redirect import ZonesMobileRedirect as ZonesMobileRedirect
from .zones_security_header import ZonesSecurityHeader as ZonesSecurityHeader
from .zones_ssl_recommender import ZonesSSLRecommender as ZonesSSLRecommender
from .zones_tls_client_auth import ZonesTLSClientAuth as ZonesTLSClientAuth
from .early_hint_edit_params import EarlyHintEditParams as EarlyHintEditParams
from .speed_cloudflare_fonts import SpeedCloudflareFonts as SpeedCloudflareFonts
from .zones_always_use_https import ZonesAlwaysUseHTTPS as ZonesAlwaysUseHTTPS
from .zones_development_mode import ZonesDevelopmentMode as ZonesDevelopmentMode
from .zones_orange_to_orange import ZonesOrangeToOrange as ZonesOrangeToOrange
from .zones_prefetch_preload import ZonesPrefetchPreload as ZonesPrefetchPreload
from .zones_websockets_param import ZonesWebsocketsParam as ZonesWebsocketsParam
from .cache_level_edit_params import CacheLevelEditParams as CacheLevelEditParams
from .pseudo_ipv4_edit_params import PseudoIPV4EditParams as PseudoIPV4EditParams
from .zones_browser_cache_ttl import ZonesBrowserCacheTTL as ZonesBrowserCacheTTL
from .zones_cache_level_param import ZonesCacheLevelParam as ZonesCacheLevelParam
from .zones_early_hints_param import ZonesEarlyHintsParam as ZonesEarlyHintsParam
from .zones_email_obfuscation import ZonesEmailObfuscation as ZonesEmailObfuscation
from .zones_h2_prioritization import ZonesH2Prioritization as ZonesH2Prioritization
from .zones_pseudo_ipv4_param import ZonesPseudoIPV4Param as ZonesPseudoIPV4Param
from .font_setting_edit_params import FontSettingEditParams as FontSettingEditParams
from .zones_hotlink_protection import ZonesHotlinkProtection as ZonesHotlinkProtection
from .zones_proxy_read_timeout import ZonesProxyReadTimeout as ZonesProxyReadTimeout
from .always_online_edit_params import AlwaysOnlineEditParams as AlwaysOnlineEditParams
from .browser_check_edit_params import BrowserCheckEditParams as BrowserCheckEditParams
from .challenge_ttl_edit_params import ChallengeTTLEditParams as ChallengeTTLEditParams
from .rocket_loader_edit_params import RocketLoaderEditParams as RocketLoaderEditParams
from .zones_advanced_ddos_param import ZonesAdvancedDDOSParam as ZonesAdvancedDDOSParam
from .zones_always_online_param import ZonesAlwaysOnlineParam as ZonesAlwaysOnlineParam
from .zones_browser_check_param import ZonesBrowserCheckParam as ZonesBrowserCheckParam
from .zones_challenge_ttl_param import ZonesChallengeTTLParam as ZonesChallengeTTLParam
from .zones_opportunistic_onion import ZonesOpportunisticOnion as ZonesOpportunisticOnion
from .zones_rocket_loader_param import ZonesRocketLoaderParam as ZonesRocketLoaderParam
from .zones_server_side_exclude import ZonesServerSideExclude as ZonesServerSideExclude
from .image_resizing_edit_params import ImageResizingEditParams as ImageResizingEditParams
from .ip_geolocation_edit_params import IPGeolocationEditParams as IPGeolocationEditParams
from .security_level_edit_params import SecurityLevelEditParams as SecurityLevelEditParams
from .zones_image_resizing_param import ZonesImageResizingParam as ZonesImageResizingParam
from .zones_ip_geolocation_param import ZonesIPGeolocationParam as ZonesIPGeolocationParam
from .zones_security_level_param import ZonesSecurityLevelParam as ZonesSecurityLevelParam
from .min_tls_version_edit_params import MinTLSVersionEditParams as MinTLSVersionEditParams
from .mobile_redirect_edit_params import MobileRedirectEditParams as MobileRedirectEditParams
from .security_header_edit_params import SecurityHeaderEditParams as SecurityHeaderEditParams
from .ssl_recommender_edit_params import SSLRecommenderEditParams as SSLRecommenderEditParams
from .tls_client_auth_edit_params import TLSClientAuthEditParams as TLSClientAuthEditParams
from .zones_min_tls_version_param import ZonesMinTLSVersionParam as ZonesMinTLSVersionParam
from .zones_mobile_redirect_param import ZonesMobileRedirectParam as ZonesMobileRedirectParam
from .zones_security_header_param import ZonesSecurityHeaderParam as ZonesSecurityHeaderParam
from .zones_ssl_recommender_param import ZonesSSLRecommenderParam as ZonesSSLRecommenderParam
from .zones_tls_client_auth_param import ZonesTLSClientAuthParam as ZonesTLSClientAuthParam
from .zones_true_client_ip_header import ZonesTrueClientIPHeader as ZonesTrueClientIPHeader
from .always_use_https_edit_params import AlwaysUseHTTPSEditParams as AlwaysUseHTTPSEditParams
from .development_mode_edit_params import DevelopmentModeEditParams as DevelopmentModeEditParams
from .orange_to_orange_edit_params import OrangeToOrangeEditParams as OrangeToOrangeEditParams
from .prefetch_preload_edit_params import PrefetchPreloadEditParams as PrefetchPreloadEditParams
from .zones_always_use_https_param import ZonesAlwaysUseHTTPSParam as ZonesAlwaysUseHTTPSParam
from .zones_development_mode_param import ZonesDevelopmentModeParam as ZonesDevelopmentModeParam
from .zones_orange_to_orange_param import ZonesOrangeToOrangeParam as ZonesOrangeToOrangeParam
from .zones_prefetch_preload_param import ZonesPrefetchPreloadParam as ZonesPrefetchPreloadParam
from .browser_cache_ttl_edit_params import BrowserCacheTTLEditParams as BrowserCacheTTLEditParams
from .email_obfuscation_edit_params import EmailObfuscationEditParams as EmailObfuscationEditParams
from .h2_prioritization_edit_params import H2PrioritizationEditParams as H2PrioritizationEditParams
from .zones_browser_cache_ttl_param import ZonesBrowserCacheTTLParam as ZonesBrowserCacheTTLParam
from .zones_email_obfuscation_param import ZonesEmailObfuscationParam as ZonesEmailObfuscationParam
from .zones_h2_prioritization_param import ZonesH2PrioritizationParam as ZonesH2PrioritizationParam
from .hotlink_protection_edit_params import HotlinkProtectionEditParams as HotlinkProtectionEditParams
from .proxy_read_timeout_edit_params import ProxyReadTimeoutEditParams as ProxyReadTimeoutEditParams
from .response_buffering_edit_params import ResponseBufferingEditParams as ResponseBufferingEditParams
from .zones_automatic_https_rewrites import ZonesAutomaticHTTPSRewrites as ZonesAutomaticHTTPSRewrites
from .zones_hotlink_protection_param import ZonesHotlinkProtectionParam as ZonesHotlinkProtectionParam
from .zones_opportunistic_encryption import ZonesOpportunisticEncryption as ZonesOpportunisticEncryption
from .zones_proxy_read_timeout_param import ZonesProxyReadTimeoutParam as ZonesProxyReadTimeoutParam
from .opportunistic_onion_edit_params import OpportunisticOnionEditParams as OpportunisticOnionEditParams
from .server_side_exclude_edit_params import ServerSideExcludeEditParams as ServerSideExcludeEditParams
from .zones_opportunistic_onion_param import ZonesOpportunisticOnionParam as ZonesOpportunisticOnionParam
from .zones_server_side_exclude_param import ZonesServerSideExcludeParam as ZonesServerSideExcludeParam
from .true_client_ip_header_edit_params import TrueClientIPHeaderEditParams as TrueClientIPHeaderEditParams
from .zones_origin_error_page_pass_thru import ZonesOriginErrorPagePassThru as ZonesOriginErrorPagePassThru
from .zones_sort_query_string_for_cache import ZonesSortQueryStringForCache as ZonesSortQueryStringForCache
from .zones_true_client_ip_header_param import ZonesTrueClientIPHeaderParam as ZonesTrueClientIPHeaderParam
from .automatic_https_rewrite_edit_params import AutomaticHTTPSRewriteEditParams as AutomaticHTTPSRewriteEditParams
from .origin_max_http_version_edit_params import OriginMaxHTTPVersionEditParams as OriginMaxHTTPVersionEditParams
from .opportunistic_encryption_edit_params import OpportunisticEncryptionEditParams as OpportunisticEncryptionEditParams
from .origin_max_http_version_get_response import OriginMaxHTTPVersionGetResponse as OriginMaxHTTPVersionGetResponse
from .zones_automatic_https_rewrites_param import ZonesAutomaticHTTPSRewritesParam as ZonesAutomaticHTTPSRewritesParam
from .zones_opportunistic_encryption_param import ZonesOpportunisticEncryptionParam as ZonesOpportunisticEncryptionParam
from .origin_max_http_version_edit_response import OriginMaxHTTPVersionEditResponse as OriginMaxHTTPVersionEditResponse
from .zones_automatic_platform_optimization import (
    ZonesAutomaticPlatformOptimization as ZonesAutomaticPlatformOptimization,
)
from .origin_error_page_pass_thru_edit_params import (
    OriginErrorPagePassThruEditParams as OriginErrorPagePassThruEditParams,
)
from .sort_query_string_for_cache_edit_params import (
    SortQueryStringForCacheEditParams as SortQueryStringForCacheEditParams,
)
from .zones_origin_error_page_pass_thru_param import (
    ZonesOriginErrorPagePassThruParam as ZonesOriginErrorPagePassThruParam,
)
from .zones_sort_query_string_for_cache_param import (
    ZonesSortQueryStringForCacheParam as ZonesSortQueryStringForCacheParam,
)
from .automatic_platform_optimization_edit_params import (
    AutomaticPlatformOptimizationEditParams as AutomaticPlatformOptimizationEditParams,
)
from .zones_automatic_platform_optimization_param import (
    ZonesAutomaticPlatformOptimizationParam as ZonesAutomaticPlatformOptimizationParam,
)
