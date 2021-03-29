import json
import os

# from flask import url_for
# from flask import redirect
# from flask import flash
# from flask import request
from flask import Blueprint
from flask import render_template

#
# from shopyo.api.html import notify_success
# from shopyo.api.forms import flash_errors
# from shopyo.api.enhance import get_active_theme_dir
# from shopyo.api.enhance import get_setting

# from modules.box__ecommerce.shop.helpers import get_cart_data


from modules.box__default.settings.helpers import get_setting

dirpath = os.path.dirname(os.path.abspath(__file__))
module_info = {}

with open(dirpath + "/info.json") as f:
    module_info = json.load(f)


globals()["{}_blueprint".format(module_info["module_name"])] = Blueprint(
    "{}".format(module_info["module_name"]),
    __name__,
    template_folder="",
    url_prefix=module_info["url_prefix"],
)


module_blueprint = globals()["{}_blueprint".format(module_info["module_name"])]


@module_blueprint.route("/")
def index():
    return render_template("mysitetheme/index.html")


@module_blueprint.route("/about")
def about():
    return render_template("mysitetheme/templates/info/about.html")


@module_blueprint.route("/contact")
def contact():
    return render_template("mysitetheme/templates/info/contact.html")

@module_blueprint.route("/privacy-policy")
def privacy_policy():
    return render_template("mysitetheme/templates/info/privacy_policy.html")
