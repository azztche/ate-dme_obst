"""
ate-dme.obst - Python SDK for Domainesia/Neva Objects S3-compatible storage
"""

from .client import ObjectsClient
from .exceptions import ObjectsError, UploadError, DownloadError, ListError

__version__ = "0.1.0"
__all__ = ["ObjectsClient", "ObjectsError", "UploadError", "DownloadError", "ListError"]