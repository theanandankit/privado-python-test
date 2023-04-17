from logging.config import fileConfig
from os import getenv

from sqlalchemy import engine_from_config, pool

from alembic import context

config.set_main_option(
    "sqlalchemy.url",
    f"redshift+psycopg2://"
    f'{getenv("BI_REDSHIFT_USER")}:'
    f'{getenv("BI_REDSHIFT_PASSWORD")}@'
    f'{getenv("BI_REDSHIFT_HOST")}:'
    f'{getenv("BI_REDSHIFT_PORT")}/'
    f'{getenv("BI_REDSHIFT_DBNAME")}',
)

def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()