from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-+*=qsag1-o7+p(63p_d9t6gz-9*=w$1^77!ek%n^a+f6s)x2y6'

# --- Debug & Allowed Hosts ---
DEBUG = False  # Set to False for production
ALLOWED_HOSTS = ['yourdomain.com', '127.0.0.1']  # Change to your actual domain

# LibraryProject/settings.py

if not DEBUG:  # Only enforce HTTPS in production
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

# --- Installed Apps ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf',
    'relationship_app',
    'django_extensions',
]

AUTH_USER_MODEL = 'bookshelf.CustomUser'

# --- Middleware ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    # Our custom Content Security Policy middleware
    'LibraryProject.middleware.ContentSecurityPolicyMiddleware',
]

ROOT_URLCONF = 'LibraryProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'LibraryProject.wsgi.application'

# --- Database ---
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# --- Password Validators ---
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --- Internationalization ---
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# --- Static Files ---
STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- Security Headers ---
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# --- Cookie Security (for HTTPS only) ---
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# --- Content Security Policy (CSP) Rules ---
CSP_DEFAULT_SRC = "'self'"
CSP_STYLE_SRC = "'self' https://fonts.googleapis.com"
CSP_SCRIPT_SRC = "'self'"


# -------------------------
# HTTPS and Secure Redirects
# -------------------------

# Redirect all HTTP requests to HTTPS
SECURE_SSL_REDIRECT = True  

# HTTP Strict Transport Security (HSTS)
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  
SECURE_HSTS_PRELOAD = True  

# Secure Cookies
SESSION_COOKIE_SECURE = True  
CSRF_COOKIE_SECURE = True  

# Security Headers
X_FRAME_OPTIONS = "DENY"  # Prevent Clickjacking
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevent MIME-type sniffing
SECURE_BROWSER_XSS_FILTER = True  # Enable browser XSS filter

# -------------------------
# Notes:
# - Ensure your server has valid SSL/TLS certificates (Let's Encrypt or similar).
# - In production, ALLOWED_HOSTS must include your domain name.
# -------------------------


# --- Force HTTPS ---
SECURE_SSL_REDIRECT = True   # Redirect all HTTP requests to HTTPS

# --- HSTS (HTTP Strict Transport Security) ---
SECURE_HSTS_SECONDS = 31536000       # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True           # Allow HSTS preloading

# --- Cookies over HTTPS only ---
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# --- Security Headers ---
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'


# --- Recognize HTTPS when behind a proxy ---
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
