from io import BytesIO

from PIL import Image, ImageDraw
from flask import send_file

from utils.endpoint import Endpoint, setup
from utils.textutils import render_text_with_emoji, wrap

@setup
class Bernie(Endpoint):
    params = ['text']

    def generate(self, avatars, text, usernames, kwargs):
        base = Image.open(self.assets.get('assets/bernie/bernie.bmp'))
        font = self.assets.get_font('assets/fonts/truenobd.otf', size=40)

        canv = ImageDraw.Draw(base)

        if len(text) >= 30:
            text = text[:30] + "..."

        w = canv.textsize(text, font)[0]

        text = wrap(font, text, 810)
        render_text_with_emoji(base, canv, ((750 - w) / 2, 660), text, font=font, fill='White')

        base = base.convert('RGB')
        b = BytesIO()
        base.save(b, format='jpeg')
        b.seek(0)
        return send_file(b, mimetype='image/jpeg')
