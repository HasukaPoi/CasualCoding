from bdflib import reader
from bdflib import writer
import fontforge


def OpenBDF(path):
    with open(path, "rb") as handle:
        return reader.read_bdf(handle)


def Start():
    bdf_font = OpenBDF(r"D:\Downloads\Zfull-GB\script\Zfull-GB-10.bdf")  # 手动设定
    sfd_font = fontforge.font()
    sfd_font.encoding = "unicode"  # 手动指定
    sfd_font.ascent = bdf_font.properties[b'FONT_ASCENT']*100
    sfd_font.descent = bdf_font.properties[b'FONT_DESCENT']*100
    print(bdf_font.properties)
    for bdf_glyph in bdf_font.glyphs:
        x = 0
        y = bdf_glyph.bbH + bdf_glyph.bbY - 1
        print(bdf_glyph.codepoint)
        glyph = sfd_font.createMappedChar(bdf_glyph.codepoint)
        if bdf_glyph.advance > 0:
            w = bdf_glyph.advance * 100
        else:
            w = 1000  # 不知为何获取不到全局定义，故手动指定
        vw = bdf_glyph.bbH * 100
        pen = glyph.glyphPen()
        for ch in bdf_glyph.__str__():
            if ch == '\n':
                y = y - 1
                x = -1
                print("")
            elif ch == '#':
                pen.moveTo((100 * x, 100 * y))
                pen.lineTo((100 * x, 100 * y + 100))
                pen.lineTo((100 * x + 100, 100 * y + 100))
                pen.lineTo((100 * x + 100, 100 * y))
                pen.closePath()
                print("#", end="")
            else:
                print(".", end="")
            x = x + 1
        pen = None
        print()
        glyph.width = w  # 在绘制完后指定才有效
        glyph.vwidth = vw  # 在绘制完后指定才有效
        glyph.removeOverlap()

    # sdf_font.autoWidth()
    sfd_font.save(r"converted.sfd")  # 手动设定


Start()
