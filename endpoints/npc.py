from io import BytesIO

from PIL import Image, ImageDraw
from flask import send_file

from utils.endpoint import Endpoint, setup
from utils.textutils import render_text_with_emoji, wrap

@setup
class Npc(Endpoint):
    params = ['text']

    def generate(self, avatars, text, usernames, kwargs):
        base = Image.open(self.assets.get('assets/npc/npc.bmp'))
        font = self.assets.get_font('assets/fonts/sans.ttf', size=40)

        canv = ImageDraw.Draw(base)

        if len(text) >= 115:
            text = text[:115] + "..."

        text = wrap(font, text, 810)
        render_text_with_emoji(base, canv, (175, 130), text, font=font, fill='Black')

        base = base.convert('RGB')
        b = BytesIO()
        base.save(b, format='jpeg')
        b.seek(0)
        return send_file(b, mimetype='image/jpeg')