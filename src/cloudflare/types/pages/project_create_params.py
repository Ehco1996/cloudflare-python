# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "ProjectCreateParams",
    "BuildConfig",
    "CanonicalDeployment",
    "DeploymentConfigs",
    "DeploymentConfigsPreview",
    "DeploymentConfigsPreviewAIBindings",
    "DeploymentConfigsPreviewAIBindingsAIBinding",
    "DeploymentConfigsPreviewAnalyticsEngineDatasets",
    "DeploymentConfigsPreviewAnalyticsEngineDatasetsAnalyticsEngineBinding",
    "DeploymentConfigsPreviewD1Databases",
    "DeploymentConfigsPreviewD1DatabasesD1Binding",
    "DeploymentConfigsPreviewDurableObjectNamespaces",
    "DeploymentConfigsPreviewDurableObjectNamespacesDoBinding",
    "DeploymentConfigsPreviewEnvVars",
    "DeploymentConfigsPreviewEnvVarsEnvironmentVariable",
    "DeploymentConfigsPreviewKvNamespaces",
    "DeploymentConfigsPreviewKvNamespacesKvBinding",
    "DeploymentConfigsPreviewPlacement",
    "DeploymentConfigsPreviewQueueProducers",
    "DeploymentConfigsPreviewQueueProducersQueueProducerBinding",
    "DeploymentConfigsPreviewR2Buckets",
    "DeploymentConfigsPreviewR2BucketsR2Binding",
    "DeploymentConfigsPreviewServiceBindings",
    "DeploymentConfigsPreviewServiceBindingsServiceBinding",
    "DeploymentConfigsProduction",
    "DeploymentConfigsProductionAIBindings",
    "DeploymentConfigsProductionAIBindingsAIBinding",
    "DeploymentConfigsProductionAnalyticsEngineDatasets",
    "DeploymentConfigsProductionAnalyticsEngineDatasetsAnalyticsEngineBinding",
    "DeploymentConfigsProductionD1Databases",
    "DeploymentConfigsProductionD1DatabasesD1Binding",
    "DeploymentConfigsProductionDurableObjectNamespaces",
    "DeploymentConfigsProductionDurableObjectNamespacesDoBinding",
    "DeploymentConfigsProductionEnvVars",
    "DeploymentConfigsProductionEnvVarsEnvironmentVariable",
    "DeploymentConfigsProductionKvNamespaces",
    "DeploymentConfigsProductionKvNamespacesKvBinding",
    "DeploymentConfigsProductionPlacement",
    "DeploymentConfigsProductionQueueProducers",
    "DeploymentConfigsProductionQueueProducersQueueProducerBinding",
    "DeploymentConfigsProductionR2Buckets",
    "DeploymentConfigsProductionR2BucketsR2Binding",
    "DeploymentConfigsProductionServiceBindings",
    "DeploymentConfigsProductionServiceBindingsServiceBinding",
    "LatestDeployment",
]


class ProjectCreateParams(TypedDict, total=False):
    build_config: BuildConfig
    """Configs for the project build process."""

    canonical_deployment: CanonicalDeployment

    deployment_configs: DeploymentConfigs
    """Configs for deployments in a project."""

    latest_deployment: LatestDeployment

    name: str
    """Name of the project."""

    production_branch: str
    """Production branch of the project. Used to identify production deployments."""


class BuildConfig(TypedDict, total=False):
    build_caching: Optional[bool]
    """Enable build caching for the project."""

    build_command: Optional[str]
    """Command used to build project."""

    destination_dir: Optional[str]
    """Output directory of the build."""

    root_dir: Optional[str]
    """Directory to run the command."""

    web_analytics_tag: Optional[str]
    """The classifying tag for analytics."""

    web_analytics_token: Optional[str]
    """The auth token for analytics."""


class CanonicalDeployment(TypedDict, total=False):
    pass


class DeploymentConfigsPreviewAIBindingsAIBinding(TypedDict, total=False):
    project_id: object


class DeploymentConfigsPreviewAIBindings(TypedDict, total=False):
    ai_binding: Annotated[DeploymentConfigsPreviewAIBindingsAIBinding, PropertyInfo(alias="AI_BINDING")]
    """AI binding."""


class DeploymentConfigsPreviewAnalyticsEngineDatasetsAnalyticsEngineBinding(TypedDict, total=False):
    dataset: str
    """Name of the dataset."""


class DeploymentConfigsPreviewAnalyticsEngineDatasets(TypedDict, total=False):
    analytics_engine_binding: Annotated[
        DeploymentConfigsPreviewAnalyticsEngineDatasetsAnalyticsEngineBinding,
        PropertyInfo(alias="ANALYTICS_ENGINE_BINDING"),
    ]
    """Analytics Engine binding."""


class DeploymentConfigsPreviewD1DatabasesD1Binding(TypedDict, total=False):
    id: str
    """UUID of the D1 database."""


class DeploymentConfigsPreviewD1Databases(TypedDict, total=False):
    d1_binding: Annotated[DeploymentConfigsPreviewD1DatabasesD1Binding, PropertyInfo(alias="D1_BINDING")]
    """D1 binding."""


class DeploymentConfigsPreviewDurableObjectNamespacesDoBinding(TypedDict, total=False):
    namespace_id: str
    """ID of the Durabble Object namespace."""


class DeploymentConfigsPreviewDurableObjectNamespaces(TypedDict, total=False):
    do_binding: Annotated[DeploymentConfigsPreviewDurableObjectNamespacesDoBinding, PropertyInfo(alias="DO_BINDING")]
    """Durabble Object binding."""


class DeploymentConfigsPreviewEnvVarsEnvironmentVariable(TypedDict, total=False):
    type: Literal["plain_text", "secret_text"]
    """The type of environment variable (plain text or secret)"""

    value: str
    """Environment variable value."""


class DeploymentConfigsPreviewEnvVars(TypedDict, total=False):
    environment_variable: Annotated[
        DeploymentConfigsPreviewEnvVarsEnvironmentVariable, PropertyInfo(alias="ENVIRONMENT_VARIABLE")
    ]
    """Environment variable."""


class DeploymentConfigsPreviewKvNamespacesKvBinding(TypedDict, total=False):
    namespace_id: str
    """ID of the KV namespace."""


class DeploymentConfigsPreviewKvNamespaces(TypedDict, total=False):
    kv_binding: Annotated[DeploymentConfigsPreviewKvNamespacesKvBinding, PropertyInfo(alias="KV_BINDING")]
    """KV binding."""


class DeploymentConfigsPreviewPlacement(TypedDict, total=False):
    mode: str
    """Placement mode."""


class DeploymentConfigsPreviewQueueProducersQueueProducerBinding(TypedDict, total=False):
    name: str
    """Name of the Queue."""


class DeploymentConfigsPreviewQueueProducers(TypedDict, total=False):
    queue_producer_binding: Annotated[
        DeploymentConfigsPreviewQueueProducersQueueProducerBinding, PropertyInfo(alias="QUEUE_PRODUCER_BINDING")
    ]
    """Queue Producer binding."""


class DeploymentConfigsPreviewR2BucketsR2Binding(TypedDict, total=False):
    name: str
    """Name of the R2 bucket."""


class DeploymentConfigsPreviewR2Buckets(TypedDict, total=False):
    r2_binding: Annotated[DeploymentConfigsPreviewR2BucketsR2Binding, PropertyInfo(alias="R2_BINDING")]
    """R2 binding."""


class DeploymentConfigsPreviewServiceBindingsServiceBinding(TypedDict, total=False):
    environment: str
    """The Service environment."""

    service: str
    """The Service name."""


class DeploymentConfigsPreviewServiceBindings(TypedDict, total=False):
    service_binding: Annotated[
        DeploymentConfigsPreviewServiceBindingsServiceBinding, PropertyInfo(alias="SERVICE_BINDING")
    ]
    """Service binding."""


class DeploymentConfigsPreview(TypedDict, total=False):
    ai_bindings: Optional[DeploymentConfigsPreviewAIBindings]
    """Constellation bindings used for Pages Functions."""

    analytics_engine_datasets: Optional[DeploymentConfigsPreviewAnalyticsEngineDatasets]
    """Analytics Engine bindings used for Pages Functions."""

    compatibility_date: str
    """Compatibility date used for Pages Functions."""

    compatibility_flags: Iterable[object]
    """Compatibility flags used for Pages Functions."""

    d1_databases: Optional[DeploymentConfigsPreviewD1Databases]
    """D1 databases used for Pages Functions."""

    durable_object_namespaces: Optional[DeploymentConfigsPreviewDurableObjectNamespaces]
    """Durabble Object namespaces used for Pages Functions."""

    env_vars: Optional[DeploymentConfigsPreviewEnvVars]
    """Environment variables for build configs."""

    kv_namespaces: DeploymentConfigsPreviewKvNamespaces
    """KV namespaces used for Pages Functions."""

    placement: Optional[DeploymentConfigsPreviewPlacement]
    """Placement setting used for Pages Functions."""

    queue_producers: Optional[DeploymentConfigsPreviewQueueProducers]
    """Queue Producer bindings used for Pages Functions."""

    r2_buckets: Optional[DeploymentConfigsPreviewR2Buckets]
    """R2 buckets used for Pages Functions."""

    service_bindings: Optional[DeploymentConfigsPreviewServiceBindings]
    """Services used for Pages Functions."""


class DeploymentConfigsProductionAIBindingsAIBinding(TypedDict, total=False):
    project_id: object


class DeploymentConfigsProductionAIBindings(TypedDict, total=False):
    ai_binding: Annotated[DeploymentConfigsProductionAIBindingsAIBinding, PropertyInfo(alias="AI_BINDING")]
    """AI binding."""


class DeploymentConfigsProductionAnalyticsEngineDatasetsAnalyticsEngineBinding(TypedDict, total=False):
    dataset: str
    """Name of the dataset."""


class DeploymentConfigsProductionAnalyticsEngineDatasets(TypedDict, total=False):
    analytics_engine_binding: Annotated[
        DeploymentConfigsProductionAnalyticsEngineDatasetsAnalyticsEngineBinding,
        PropertyInfo(alias="ANALYTICS_ENGINE_BINDING"),
    ]
    """Analytics Engine binding."""


class DeploymentConfigsProductionD1DatabasesD1Binding(TypedDict, total=False):
    id: str
    """UUID of the D1 database."""


class DeploymentConfigsProductionD1Databases(TypedDict, total=False):
    d1_binding: Annotated[DeploymentConfigsProductionD1DatabasesD1Binding, PropertyInfo(alias="D1_BINDING")]
    """D1 binding."""


class DeploymentConfigsProductionDurableObjectNamespacesDoBinding(TypedDict, total=False):
    namespace_id: str
    """ID of the Durabble Object namespace."""


class DeploymentConfigsProductionDurableObjectNamespaces(TypedDict, total=False):
    do_binding: Annotated[DeploymentConfigsProductionDurableObjectNamespacesDoBinding, PropertyInfo(alias="DO_BINDING")]
    """Durabble Object binding."""


class DeploymentConfigsProductionEnvVarsEnvironmentVariable(TypedDict, total=False):
    type: Literal["plain_text", "secret_text"]
    """The type of environment variable (plain text or secret)"""

    value: str
    """Environment variable value."""


class DeploymentConfigsProductionEnvVars(TypedDict, total=False):
    environment_variable: Annotated[
        DeploymentConfigsProductionEnvVarsEnvironmentVariable, PropertyInfo(alias="ENVIRONMENT_VARIABLE")
    ]
    """Environment variable."""


class DeploymentConfigsProductionKvNamespacesKvBinding(TypedDict, total=False):
    namespace_id: str
    """ID of the KV namespace."""


class DeploymentConfigsProductionKvNamespaces(TypedDict, total=False):
    kv_binding: Annotated[DeploymentConfigsProductionKvNamespacesKvBinding, PropertyInfo(alias="KV_BINDING")]
    """KV binding."""


class DeploymentConfigsProductionPlacement(TypedDict, total=False):
    mode: str
    """Placement mode."""


class DeploymentConfigsProductionQueueProducersQueueProducerBinding(TypedDict, total=False):
    name: str
    """Name of the Queue."""


class DeploymentConfigsProductionQueueProducers(TypedDict, total=False):
    queue_producer_binding: Annotated[
        DeploymentConfigsProductionQueueProducersQueueProducerBinding, PropertyInfo(alias="QUEUE_PRODUCER_BINDING")
    ]
    """Queue Producer binding."""


class DeploymentConfigsProductionR2BucketsR2Binding(TypedDict, total=False):
    name: str
    """Name of the R2 bucket."""


class DeploymentConfigsProductionR2Buckets(TypedDict, total=False):
    r2_binding: Annotated[DeploymentConfigsProductionR2BucketsR2Binding, PropertyInfo(alias="R2_BINDING")]
    """R2 binding."""


class DeploymentConfigsProductionServiceBindingsServiceBinding(TypedDict, total=False):
    environment: str
    """The Service environment."""

    service: str
    """The Service name."""


class DeploymentConfigsProductionServiceBindings(TypedDict, total=False):
    service_binding: Annotated[
        DeploymentConfigsProductionServiceBindingsServiceBinding, PropertyInfo(alias="SERVICE_BINDING")
    ]
    """Service binding."""


class DeploymentConfigsProduction(TypedDict, total=False):
    ai_bindings: Optional[DeploymentConfigsProductionAIBindings]
    """Constellation bindings used for Pages Functions."""

    analytics_engine_datasets: Optional[DeploymentConfigsProductionAnalyticsEngineDatasets]
    """Analytics Engine bindings used for Pages Functions."""

    compatibility_date: str
    """Compatibility date used for Pages Functions."""

    compatibility_flags: Iterable[object]
    """Compatibility flags used for Pages Functions."""

    d1_databases: Optional[DeploymentConfigsProductionD1Databases]
    """D1 databases used for Pages Functions."""

    durable_object_namespaces: Optional[DeploymentConfigsProductionDurableObjectNamespaces]
    """Durabble Object namespaces used for Pages Functions."""

    env_vars: Optional[DeploymentConfigsProductionEnvVars]
    """Environment variables for build configs."""

    kv_namespaces: DeploymentConfigsProductionKvNamespaces
    """KV namespaces used for Pages Functions."""

    placement: Optional[DeploymentConfigsProductionPlacement]
    """Placement setting used for Pages Functions."""

    queue_producers: Optional[DeploymentConfigsProductionQueueProducers]
    """Queue Producer bindings used for Pages Functions."""

    r2_buckets: Optional[DeploymentConfigsProductionR2Buckets]
    """R2 buckets used for Pages Functions."""

    service_bindings: Optional[DeploymentConfigsProductionServiceBindings]
    """Services used for Pages Functions."""


class DeploymentConfigs(TypedDict, total=False):
    preview: DeploymentConfigsPreview
    """Configs for preview deploys."""

    production: DeploymentConfigsProduction
    """Configs for production deploys."""


class LatestDeployment(TypedDict, total=False):
    pass
