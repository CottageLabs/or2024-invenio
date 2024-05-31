"""JS/CSS Webpack bundles for OR2024 Demo Instance by Cottage Labs."""

from invenio_assets.webpack import WebpackThemeBundle

theme = WebpackThemeBundle(
    __name__,
    "assets",
    default="semantic-ui",
    themes={
        "semantic-ui": dict(
            entry={
                # Add your webpack entrypoints
            },
        ),
    },
)
