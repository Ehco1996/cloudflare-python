# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "AppCreateParams",
    "Variant0",
    "Variant0CorsHeaders",
    "Variant1",
    "Variant1SaasApp",
    "Variant1SaasAppAccessSamlSaasApp",
    "Variant1SaasAppAccessSamlSaasAppCustomAttributes",
    "Variant1SaasAppAccessSamlSaasAppCustomAttributesSource",
    "Variant1SaasAppAccessOidcSaasApp",
    "Variant2",
    "Variant2CorsHeaders",
    "Variant3",
    "Variant3CorsHeaders",
    "Variant4",
    "Variant5",
    "Variant6",
    "Variant7",
]


class Variant0(TypedDict, total=False):
    account_or_zone: Required[str]

    domain: Required[str]
    """The primary hostname and path that Access will secure.

    If the app is visible in the App Launcher dashboard, this is the domain that
    will be displayed.
    """

    type: Required[str]
    """The application type."""

    allow_authenticate_via_warp: bool
    """
    When set to true, users can authenticate to this application using their WARP
    session. When set to false this application will always require direct IdP
    authentication. This setting always overrides the organization setting for WARP
    authentication.
    """

    allowed_idps: List[str]
    """The identity providers your users can select when connecting to this
    application.

    Defaults to all IdPs configured in your account.
    """

    app_launcher_visible: bool
    """Displays the application in the App Launcher."""

    auto_redirect_to_identity: bool
    """When set to `true`, users skip the identity provider selection step during
    login.

    You must specify only one identity provider in allowed_idps.
    """

    cors_headers: Variant0CorsHeaders

    custom_deny_message: str
    """
    The custom error message shown to a user when they are denied access to the
    application.
    """

    custom_deny_url: str
    """
    The custom URL a user is redirected to when they are denied access to the
    application when failing identity-based rules.
    """

    custom_non_identity_deny_url: str
    """
    The custom URL a user is redirected to when they are denied access to the
    application when failing non-identity rules.
    """

    custom_pages: List[str]
    """The custom pages that will be displayed when applicable for this application"""

    enable_binding_cookie: bool
    """
    Enables the binding cookie, which increases security against compromised
    authorization tokens and CSRF attacks.
    """

    http_only_cookie_attribute: bool
    """
    Enables the HttpOnly cookie attribute, which increases security against XSS
    attacks.
    """

    logo_url: str
    """The image URL for the logo shown in the App Launcher dashboard."""

    name: str
    """The name of the application."""

    path_cookie_attribute: bool
    """Enables cookie paths to scope an application's JWT to the application path.

    If disabled, the JWT will scope to the hostname by default
    """

    same_site_cookie_attribute: str
    """
    Sets the SameSite cookie setting, which provides increased security against CSRF
    attacks.
    """

    self_hosted_domains: List[str]
    """List of domains that Access will secure."""

    service_auth_401_redirect: bool
    """Returns a 401 status code when the request is blocked by a Service Auth policy."""

    session_duration: str
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """

    skip_interstitial: bool
    """Enables automatic authentication through cloudflared."""

    tags: List[str]
    """The tags you want assigned to an application.

    Tags are used to filter applications in the App Launcher dashboard.
    """


class Variant0CorsHeaders(TypedDict, total=False):
    allow_all_headers: bool
    """Allows all HTTP request headers."""

    allow_all_methods: bool
    """Allows all HTTP request methods."""

    allow_all_origins: bool
    """Allows all origins."""

    allow_credentials: bool
    """
    When set to `true`, includes credentials (cookies, authorization headers, or TLS
    client certificates) with requests.
    """

    allowed_headers: Iterable[object]
    """Allowed HTTP request headers."""

    allowed_methods: List[Literal["GET", "POST", "HEAD", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE", "PATCH"]]
    """Allowed HTTP request methods."""

    allowed_origins: Iterable[object]
    """Allowed origins."""

    max_age: float
    """The maximum number of seconds the results of a preflight request can be cached."""


class Variant1(TypedDict, total=False):
    account_or_zone: Required[str]

    allowed_idps: List[str]
    """The identity providers your users can select when connecting to this
    application.

    Defaults to all IdPs configured in your account.
    """

    app_launcher_visible: bool
    """Displays the application in the App Launcher."""

    auto_redirect_to_identity: bool
    """When set to `true`, users skip the identity provider selection step during
    login.

    You must specify only one identity provider in allowed_idps.
    """

    custom_pages: List[str]
    """The custom pages that will be displayed when applicable for this application"""

    logo_url: str
    """The image URL for the logo shown in the App Launcher dashboard."""

    name: str
    """The name of the application."""

    saas_app: Variant1SaasApp

    tags: List[str]
    """The tags you want assigned to an application.

    Tags are used to filter applications in the App Launcher dashboard.
    """

    type: str
    """The application type."""


class Variant1SaasAppAccessSamlSaasAppCustomAttributesSource(TypedDict, total=False):
    name: str
    """The name of the IdP attribute."""


class Variant1SaasAppAccessSamlSaasAppCustomAttributes(TypedDict, total=False):
    name: str
    """The name of the attribute."""

    name_format: Literal[
        "urn:oasis:names:tc:SAML:2.0:attrname-format:unspecified",
        "urn:oasis:names:tc:SAML:2.0:attrname-format:basic",
        "urn:oasis:names:tc:SAML:2.0:attrname-format:uri",
    ]
    """A globally unique name for an identity or service provider."""

    source: Variant1SaasAppAccessSamlSaasAppCustomAttributesSource


class Variant1SaasAppAccessSamlSaasApp(TypedDict, total=False):
    auth_type: Literal["saml", "oidc"]
    """Optional identifier indicating the authentication protocol used for the saas
    app.

    Required for OIDC. Default if unset is "saml"
    """

    consumer_service_url: str
    """
    The service provider's endpoint that is responsible for receiving and parsing a
    SAML assertion.
    """

    custom_attributes: Variant1SaasAppAccessSamlSaasAppCustomAttributes

    default_relay_state: str
    """
    The URL that the user will be redirected to after a successful login for IDP
    initiated logins.
    """

    idp_entity_id: str
    """The unique identifier for your SaaS application."""

    name_id_format: Literal["id", "email"]
    """The format of the name identifier sent to the SaaS application."""

    name_id_transform_jsonata: str
    """
    A [JSONata](https://jsonata.org/) expression that transforms an application's
    user identities into a NameID value for its SAML assertion. This expression
    should evaluate to a singular string. The output of this expression can override
    the `name_id_format` setting.
    """

    public_key: str
    """The Access public certificate that will be used to verify your identity."""

    sp_entity_id: str
    """A globally unique name for an identity or service provider."""

    sso_endpoint: str
    """The endpoint where your SaaS application will send login requests."""


class Variant1SaasAppAccessOidcSaasApp(TypedDict, total=False):
    app_launcher_url: str
    """The URL where this applications tile redirects users"""

    auth_type: Literal["saml", "oidc"]
    """Identifier of the authentication protocol used for the saas app.

    Required for OIDC.
    """

    client_id: str
    """The application client id"""

    client_secret: str
    """The application client secret, only returned on POST request."""

    grant_types: List[Literal["authorization_code", "authorization_code_with_pkce"]]
    """The OIDC flows supported by this application"""

    group_filter_regex: str
    """A regex to filter Cloudflare groups returned in ID token and userinfo endpoint"""

    public_key: str
    """The Access public certificate that will be used to verify your identity."""

    redirect_uris: List[str]
    """
    The permitted URL's for Cloudflare to return Authorization codes and Access/ID
    tokens
    """

    scopes: List[Literal["openid", "groups", "email", "profile"]]
    """Define the user information shared with access"""


Variant1SaasApp = Union[Variant1SaasAppAccessSamlSaasApp, Variant1SaasAppAccessOidcSaasApp]


class Variant2(TypedDict, total=False):
    account_or_zone: Required[str]

    domain: Required[str]
    """The primary hostname and path that Access will secure.

    If the app is visible in the App Launcher dashboard, this is the domain that
    will be displayed.
    """

    type: Required[str]
    """The application type."""

    allow_authenticate_via_warp: bool
    """
    When set to true, users can authenticate to this application using their WARP
    session. When set to false this application will always require direct IdP
    authentication. This setting always overrides the organization setting for WARP
    authentication.
    """

    allowed_idps: List[str]
    """The identity providers your users can select when connecting to this
    application.

    Defaults to all IdPs configured in your account.
    """

    app_launcher_visible: bool
    """Displays the application in the App Launcher."""

    auto_redirect_to_identity: bool
    """When set to `true`, users skip the identity provider selection step during
    login.

    You must specify only one identity provider in allowed_idps.
    """

    cors_headers: Variant2CorsHeaders

    custom_deny_message: str
    """
    The custom error message shown to a user when they are denied access to the
    application.
    """

    custom_deny_url: str
    """
    The custom URL a user is redirected to when they are denied access to the
    application when failing identity-based rules.
    """

    custom_non_identity_deny_url: str
    """
    The custom URL a user is redirected to when they are denied access to the
    application when failing non-identity rules.
    """

    custom_pages: List[str]
    """The custom pages that will be displayed when applicable for this application"""

    enable_binding_cookie: bool
    """
    Enables the binding cookie, which increases security against compromised
    authorization tokens and CSRF attacks.
    """

    http_only_cookie_attribute: bool
    """
    Enables the HttpOnly cookie attribute, which increases security against XSS
    attacks.
    """

    logo_url: str
    """The image URL for the logo shown in the App Launcher dashboard."""

    name: str
    """The name of the application."""

    path_cookie_attribute: bool
    """Enables cookie paths to scope an application's JWT to the application path.

    If disabled, the JWT will scope to the hostname by default
    """

    same_site_cookie_attribute: str
    """
    Sets the SameSite cookie setting, which provides increased security against CSRF
    attacks.
    """

    self_hosted_domains: List[str]
    """List of domains that Access will secure."""

    service_auth_401_redirect: bool
    """Returns a 401 status code when the request is blocked by a Service Auth policy."""

    session_duration: str
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """

    skip_interstitial: bool
    """Enables automatic authentication through cloudflared."""

    tags: List[str]
    """The tags you want assigned to an application.

    Tags are used to filter applications in the App Launcher dashboard.
    """


class Variant2CorsHeaders(TypedDict, total=False):
    allow_all_headers: bool
    """Allows all HTTP request headers."""

    allow_all_methods: bool
    """Allows all HTTP request methods."""

    allow_all_origins: bool
    """Allows all origins."""

    allow_credentials: bool
    """
    When set to `true`, includes credentials (cookies, authorization headers, or TLS
    client certificates) with requests.
    """

    allowed_headers: Iterable[object]
    """Allowed HTTP request headers."""

    allowed_methods: List[Literal["GET", "POST", "HEAD", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE", "PATCH"]]
    """Allowed HTTP request methods."""

    allowed_origins: Iterable[object]
    """Allowed origins."""

    max_age: float
    """The maximum number of seconds the results of a preflight request can be cached."""


class Variant3(TypedDict, total=False):
    account_or_zone: Required[str]

    domain: Required[str]
    """The primary hostname and path that Access will secure.

    If the app is visible in the App Launcher dashboard, this is the domain that
    will be displayed.
    """

    type: Required[str]
    """The application type."""

    allow_authenticate_via_warp: bool
    """
    When set to true, users can authenticate to this application using their WARP
    session. When set to false this application will always require direct IdP
    authentication. This setting always overrides the organization setting for WARP
    authentication.
    """

    allowed_idps: List[str]
    """The identity providers your users can select when connecting to this
    application.

    Defaults to all IdPs configured in your account.
    """

    app_launcher_visible: bool
    """Displays the application in the App Launcher."""

    auto_redirect_to_identity: bool
    """When set to `true`, users skip the identity provider selection step during
    login.

    You must specify only one identity provider in allowed_idps.
    """

    cors_headers: Variant3CorsHeaders

    custom_deny_message: str
    """
    The custom error message shown to a user when they are denied access to the
    application.
    """

    custom_deny_url: str
    """
    The custom URL a user is redirected to when they are denied access to the
    application when failing identity-based rules.
    """

    custom_non_identity_deny_url: str
    """
    The custom URL a user is redirected to when they are denied access to the
    application when failing non-identity rules.
    """

    custom_pages: List[str]
    """The custom pages that will be displayed when applicable for this application"""

    enable_binding_cookie: bool
    """
    Enables the binding cookie, which increases security against compromised
    authorization tokens and CSRF attacks.
    """

    http_only_cookie_attribute: bool
    """
    Enables the HttpOnly cookie attribute, which increases security against XSS
    attacks.
    """

    logo_url: str
    """The image URL for the logo shown in the App Launcher dashboard."""

    name: str
    """The name of the application."""

    path_cookie_attribute: bool
    """Enables cookie paths to scope an application's JWT to the application path.

    If disabled, the JWT will scope to the hostname by default
    """

    same_site_cookie_attribute: str
    """
    Sets the SameSite cookie setting, which provides increased security against CSRF
    attacks.
    """

    self_hosted_domains: List[str]
    """List of domains that Access will secure."""

    service_auth_401_redirect: bool
    """Returns a 401 status code when the request is blocked by a Service Auth policy."""

    session_duration: str
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """

    skip_interstitial: bool
    """Enables automatic authentication through cloudflared."""

    tags: List[str]
    """The tags you want assigned to an application.

    Tags are used to filter applications in the App Launcher dashboard.
    """


class Variant3CorsHeaders(TypedDict, total=False):
    allow_all_headers: bool
    """Allows all HTTP request headers."""

    allow_all_methods: bool
    """Allows all HTTP request methods."""

    allow_all_origins: bool
    """Allows all origins."""

    allow_credentials: bool
    """
    When set to `true`, includes credentials (cookies, authorization headers, or TLS
    client certificates) with requests.
    """

    allowed_headers: Iterable[object]
    """Allowed HTTP request headers."""

    allowed_methods: List[Literal["GET", "POST", "HEAD", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE", "PATCH"]]
    """Allowed HTTP request methods."""

    allowed_origins: Iterable[object]
    """Allowed origins."""

    max_age: float
    """The maximum number of seconds the results of a preflight request can be cached."""


class Variant4(TypedDict, total=False):
    account_or_zone: Required[str]

    type: Required[Literal["self_hosted", "saas", "ssh", "vnc", "app_launcher", "warp", "biso", "bookmark", "dash_sso"]]
    """The application type."""

    allowed_idps: List[str]
    """The identity providers your users can select when connecting to this
    application.

    Defaults to all IdPs configured in your account.
    """

    auto_redirect_to_identity: bool
    """When set to `true`, users skip the identity provider selection step during
    login.

    You must specify only one identity provider in allowed_idps.
    """

    session_duration: str
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """


class Variant5(TypedDict, total=False):
    account_or_zone: Required[str]

    type: Required[Literal["self_hosted", "saas", "ssh", "vnc", "app_launcher", "warp", "biso", "bookmark", "dash_sso"]]
    """The application type."""

    allowed_idps: List[str]
    """The identity providers your users can select when connecting to this
    application.

    Defaults to all IdPs configured in your account.
    """

    auto_redirect_to_identity: bool
    """When set to `true`, users skip the identity provider selection step during
    login.

    You must specify only one identity provider in allowed_idps.
    """

    session_duration: str
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """


class Variant6(TypedDict, total=False):
    account_or_zone: Required[str]

    type: Required[Literal["self_hosted", "saas", "ssh", "vnc", "app_launcher", "warp", "biso", "bookmark", "dash_sso"]]
    """The application type."""

    allowed_idps: List[str]
    """The identity providers your users can select when connecting to this
    application.

    Defaults to all IdPs configured in your account.
    """

    auto_redirect_to_identity: bool
    """When set to `true`, users skip the identity provider selection step during
    login.

    You must specify only one identity provider in allowed_idps.
    """

    session_duration: str
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """


class Variant7(TypedDict, total=False):
    account_or_zone: Required[str]

    app_launcher_visible: object

    domain: object
    """The URL or domain of the bookmark."""

    logo_url: str
    """The image URL for the logo shown in the App Launcher dashboard."""

    name: str
    """The name of the application."""

    tags: List[str]
    """The tags you want assigned to an application.

    Tags are used to filter applications in the App Launcher dashboard.
    """

    type: str
    """The application type."""


AppCreateParams = Union[Variant0, Variant1, Variant2, Variant3, Variant4, Variant5, Variant6, Variant7]
