"""Template filters for showing values."""


def bhd(fils):
    """12900 -> "12.900 BHD". Used in templates as {{ order["total_fils"]|bhd }}."""
    return "{:.3f} BHD".format(fils / 1000)


def register(app):
    app.add_template_filter(bhd, "bhd")
