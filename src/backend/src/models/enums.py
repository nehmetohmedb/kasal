from enum import Enum

# Legacy role enum - keeping for backward compatibility
class UserRole(str, Enum):
    ADMIN = "admin"
    TECHNICAL = "technical"
    REGULAR = "regular"

class UserStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"

# Group enums (formerly tenant enums)
class GroupStatus(str, Enum):
    ACTIVE = "active"
    SUSPENDED = "suspended"
    ARCHIVED = "archived"

class GroupUserRole(str, Enum):
    ADMIN = "admin"           # Full control within group
    MANAGER = "manager"       # Can manage users and workflows
    USER = "user"            # Can execute workflows
    VIEWER = "viewer"        # Read-only access

class GroupUserStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"

# Legacy tenant enums for backward compatibility during migration
class TenantStatus(str, Enum):
    ACTIVE = "active"
    SUSPENDED = "suspended"
    ARCHIVED = "archived"

class TenantUserRole(str, Enum):
    ADMIN = "admin"           # Full control within tenant
    MANAGER = "manager"       # Can manage users and workflows
    USER = "user"            # Can execute workflows
    VIEWER = "viewer"        # Read-only access

class TenantUserStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"

class IdentityProviderType(str, Enum):
    LOCAL = "local"
    OAUTH = "oauth"
    OIDC = "oidc"
    SAML = "saml"
    CUSTOM = "custom" 