/*******************************************************************************
 * Size: 16 px
 * Bpp: 1
 * Opts: --bpp 1 --size 16 --font F:/ESP32/squareline/assets/Formula1-Regular.otf -o F:/ESP32/squareline/assets\ui_font_F1R16.c --format lvgl -r 0x20-0x7f --no-compress --no-prefilter
 ******************************************************************************/

#include "../ui.h"

#ifndef UI_FONT_F1R16
#define UI_FONT_F1R16 1
#endif

#if UI_FONT_F1R16

/*-----------------
 *    BITMAPS
 *----------------*/

/*Store the image of the glyphs*/
static LV_ATTRIBUTE_LARGE_CONST const uint8_t glyph_bitmap[] = {
    /* U+0020 " " */
    0x0,

    /* U+0021 "!" */
    0xff, 0xff, 0xc3,

    /* U+0022 "\"" */
    0xde, 0xf7, 0x20,

    /* U+0023 "#" */
    0x4, 0x40, 0xcc, 0xc, 0xc7, 0xff, 0x19, 0x81,
    0x98, 0x19, 0x8f, 0xfe, 0x33, 0x3, 0x30, 0x33,
    0x2, 0x20,

    /* U+0024 "$" */
    0xc, 0x3, 0x7, 0xff, 0x30, 0xcc, 0x33, 0xf,
    0xc1, 0xf8, 0xf, 0x83, 0x70, 0xcc, 0x33, 0xc,
    0xbf, 0xc0, 0xc0,

    /* U+0025 "%" */
    0x78, 0x66, 0x63, 0x33, 0x31, 0x9b, 0x7, 0xb8,
    0x0, 0x0, 0x37, 0xc3, 0x63, 0x1b, 0x19, 0x98,
    0xcc, 0xc6, 0xc3, 0xe0,

    /* U+0026 "&" */
    0xf, 0xe0, 0xc0, 0x6, 0x0, 0x38, 0x0, 0xe0,
    0x3f, 0x1f, 0xd, 0xd8, 0x3c, 0xc1, 0xc6, 0xe,
    0x30, 0x78, 0xfe, 0x60,

    /* U+0027 "'" */
    0xfe,

    /* U+0028 "(" */
    0x7c, 0xcc, 0xcc, 0xcc, 0xcc, 0xcc, 0xc7,

    /* U+0029 ")" */
    0xe3, 0x33, 0x33, 0x33, 0x33, 0x33, 0x3e,

    /* U+002A "*" */
    0x1, 0x23, 0x3f, 0x31, 0x20, 0x0,

    /* U+002B "+" */
    0x18, 0x30, 0x67, 0xf1, 0x83, 0x6, 0x0,

    /* U+002C "," */
    0x6d, 0xa0,

    /* U+002D "-" */
    0xf0,

    /* U+002E "." */
    0xc0,

    /* U+002F "/" */
    0x18, 0xc6, 0x23, 0x18, 0xc4, 0x63, 0x18, 0x84,
    0x60,

    /* U+0030 "0" */
    0x1f, 0xc, 0x1b, 0x1, 0x60, 0x3c, 0x7, 0x80,
    0xf0, 0x1e, 0x3, 0xc0, 0x78, 0x9, 0x83, 0xf,
    0x80,

    /* U+0031 "1" */
    0xf8, 0x6, 0x3, 0x1, 0x80, 0xc0, 0x60, 0x30,
    0x18, 0xc, 0x6, 0x3, 0x1f, 0xf0,

    /* U+0032 "2" */
    0xff, 0x80, 0x30, 0xc, 0x7, 0x7, 0xc3, 0xe3,
    0xe1, 0xe0, 0xe0, 0x30, 0xc, 0x3, 0xff,

    /* U+0033 "3" */
    0xff, 0xc0, 0xe0, 0x70, 0x78, 0x38, 0xf, 0xe0,
    0x1c, 0x3, 0x0, 0xc0, 0x30, 0xf, 0xfe,

    /* U+0034 "4" */
    0x3, 0x80, 0x6c, 0xc, 0xc1, 0x8c, 0x30, 0xc7,
    0xc, 0xe0, 0xcc, 0xc, 0x7f, 0xf0, 0xc, 0x0,
    0xc0, 0xc,

    /* U+0035 "5" */
    0xff, 0xe0, 0x30, 0x18, 0xc, 0x7, 0xf8, 0x6,
    0x3, 0x1, 0x80, 0xc0, 0x7f, 0xe0,

    /* U+0036 "6" */
    0x3f, 0xd8, 0xc, 0x3, 0x0, 0xc0, 0x3f, 0xec,
    0xf, 0x3, 0xc0, 0xf0, 0x36, 0xc, 0xfe,

    /* U+0037 "7" */
    0xff, 0xc0, 0x30, 0xc, 0x6, 0x3, 0x80, 0xc0,
    0x60, 0x18, 0xc, 0x7, 0x1, 0x80, 0xc0,

    /* U+0038 "8" */
    0x7f, 0xb0, 0x3c, 0xf, 0x3, 0xc0, 0xcf, 0xce,
    0x1b, 0x3, 0xc0, 0xf0, 0x3e, 0x1d, 0xfe,

    /* U+0039 "9" */
    0x7f, 0x30, 0x6c, 0xf, 0x3, 0xc0, 0xf0, 0x37,
    0xfc, 0x3, 0x0, 0xc0, 0x30, 0x1b, 0xfc,

    /* U+003A ":" */
    0xc0, 0x0, 0x30,

    /* U+003B ";" */
    0xc0, 0x0, 0xfe,

    /* U+003C "<" */
    0x8, 0xdd, 0x8e, 0x1c, 0x60,

    /* U+003D "=" */
    0xfe, 0x0, 0x0, 0xf, 0xe0,

    /* U+003E ">" */
    0x86, 0x1c, 0x33, 0xf3, 0x0,

    /* U+003F "?" */
    0xfe, 0x1, 0x80, 0x60, 0x30, 0x18, 0x18, 0xf8,
    0x0, 0x0, 0x0, 0x0, 0x6, 0x0,

    /* U+0040 "@" */
    0xff, 0xc0, 0x6, 0x0, 0x37, 0xf3, 0xc3, 0x3c,
    0x33, 0xc3, 0x3c, 0x33, 0xc3, 0x3c, 0x33, 0x7f,
    0xf0,

    /* U+0041 "A" */
    0x3, 0x0, 0x1e, 0x0, 0xc8, 0x3, 0x30, 0x8,
    0xc0, 0x61, 0x81, 0x6, 0xf, 0xfc, 0x20, 0x31,
    0x80, 0x66, 0x1, 0xb0, 0x6,

    /* U+0042 "B" */
    0xff, 0xb0, 0x3c, 0xf, 0x3, 0xc0, 0xff, 0xcc,
    0x1f, 0x3, 0xc0, 0xf0, 0x3c, 0xf, 0xfc,

    /* U+0043 "C" */
    0x1f, 0xec, 0x1, 0x0, 0x60, 0xc, 0x1, 0x80,
    0x30, 0x6, 0x0, 0xc0, 0x8, 0x1, 0x80, 0x1f,
    0xf0,

    /* U+0044 "D" */
    0xff, 0x18, 0x1b, 0x1, 0x60, 0x3c, 0x7, 0x80,
    0xf0, 0x1e, 0x3, 0xc0, 0x78, 0xb, 0x3, 0x7f,
    0x80,

    /* U+0045 "E" */
    0xff, 0xf0, 0xc, 0x3, 0x0, 0xc0, 0x3f, 0xfc,
    0x3, 0x0, 0xc0, 0x30, 0xc, 0x3, 0xff,

    /* U+0046 "F" */
    0xff, 0xf0, 0xc, 0x3, 0x0, 0xc0, 0x3f, 0xfc,
    0x3, 0x0, 0xc0, 0x30, 0xc, 0x3, 0x0,

    /* U+0047 "G" */
    0x1f, 0xe6, 0x0, 0x40, 0xc, 0x0, 0xc0, 0xc,
    0x3f, 0xc0, 0x3c, 0x3, 0xc0, 0x34, 0x3, 0x60,
    0x71, 0xfc,

    /* U+0048 "H" */
    0xc0, 0x78, 0xf, 0x1, 0xe0, 0x3c, 0x7, 0xff,
    0xf0, 0x1e, 0x3, 0xc0, 0x78, 0xf, 0x1, 0xe0,
    0x30,

    /* U+0049 "I" */
    0xff, 0xff, 0xff,

    /* U+004A "J" */
    0x3, 0x3, 0x3, 0x3, 0x3, 0x3, 0x3, 0x3,
    0x3, 0x3, 0x6, 0xfc,

    /* U+004B "K" */
    0xc0, 0xd8, 0x33, 0xc, 0x63, 0x8c, 0x61, 0xf8,
    0x33, 0x86, 0x30, 0xc3, 0x18, 0x33, 0x3, 0x60,
    0x70,

    /* U+004C "L" */
    0xc0, 0x60, 0x30, 0x18, 0xc, 0x6, 0x3, 0x1,
    0x80, 0xc0, 0x60, 0x30, 0x1f, 0xf0,

    /* U+004D "M" */
    0x38, 0x1c, 0x1e, 0xf, 0x1b, 0xd, 0x8d, 0x86,
    0xc6, 0x43, 0x63, 0x31, 0x31, 0x99, 0x8c, 0x8c,
    0xc6, 0xc2, 0x63, 0x61, 0xa1, 0xb0, 0xf0, 0xd8,
    0x38, 0x60,

    /* U+004E "N" */
    0x70, 0x1e, 0xc0, 0xf2, 0x7, 0x98, 0x3c, 0x61,
    0xe3, 0xf, 0xc, 0x78, 0x23, 0xc1, 0x9e, 0x6,
    0xf0, 0x17, 0x80, 0xe0,

    /* U+004F "O" */
    0x1f, 0x86, 0x6, 0xc0, 0x2c, 0x3, 0xc0, 0x3c,
    0x3, 0xc0, 0x3c, 0x3, 0xc0, 0x3c, 0x2, 0x60,
    0x61, 0xf8,

    /* U+0050 "P" */
    0xff, 0x98, 0x1f, 0x1, 0xe0, 0x3c, 0x7, 0x81,
    0xff, 0xe6, 0x0, 0xc0, 0x18, 0x3, 0x0, 0x60,
    0x0,

    /* U+0051 "Q" */
    0x1f, 0x86, 0x6, 0xc0, 0x2c, 0x3, 0xc0, 0x3c,
    0x3, 0xc0, 0x3c, 0x3, 0xc0, 0x3c, 0x2, 0x60,
    0x61, 0xfc, 0x3, 0x0, 0x18,

    /* U+0052 "R" */
    0xff, 0xd8, 0xf, 0x1, 0xe0, 0x3c, 0x7, 0xbf,
    0xb7, 0x6, 0x70, 0xc7, 0x18, 0x73, 0x7, 0x60,
    0x60,

    /* U+0053 "S" */
    0x3f, 0xf0, 0xc, 0x3, 0x0, 0xf8, 0x1f, 0xc1,
    0xf8, 0xf, 0x0, 0xc0, 0x30, 0xb, 0xfc,

    /* U+0054 "T" */
    0xff, 0xe0, 0xc0, 0x18, 0x3, 0x0, 0x60, 0xc,
    0x1, 0x80, 0x30, 0x6, 0x0, 0xc0, 0x18, 0x3,
    0x0,

    /* U+0055 "U" */
    0xc0, 0x78, 0xf, 0x1, 0xe0, 0x3c, 0x7, 0x80,
    0xf0, 0x1e, 0x3, 0xc0, 0x78, 0xd, 0x83, 0x1f,
    0xc0,

    /* U+0056 "V" */
    0x60, 0x36, 0x3, 0x70, 0x33, 0x6, 0x30, 0x61,
    0x8c, 0x18, 0xc1, 0x8c, 0xd, 0x80, 0xd8, 0xf,
    0x0, 0x70,

    /* U+0057 "W" */
    0xc0, 0xc0, 0xf0, 0x78, 0x3c, 0x16, 0x9, 0xd,
    0x86, 0x63, 0x31, 0x98, 0xcc, 0x66, 0x33, 0x30,
    0xd8, 0xcc, 0x36, 0x1b, 0xd, 0x86, 0x81, 0xe1,
    0xe0, 0x70, 0x30,

    /* U+0058 "X" */
    0x60, 0x33, 0x83, 0xc, 0x18, 0x31, 0x80, 0xd8,
    0x3, 0x80, 0x36, 0x3, 0x18, 0x18, 0xc1, 0x83,
    0x18, 0xc, 0xc0, 0x60,

    /* U+0059 "Y" */
    0xc0, 0x36, 0x6, 0x70, 0xe3, 0xc, 0x19, 0x81,
    0xd8, 0xf, 0x0, 0x60, 0x6, 0x0, 0x60, 0x6,
    0x0, 0x60,

    /* U+005A "Z" */
    0xff, 0x80, 0x30, 0xc, 0x7, 0x7, 0x83, 0xc1,
    0xc0, 0xe0, 0x70, 0x38, 0xc, 0x1, 0xff,

    /* U+005B "[" */
    0xfc, 0xcc, 0xcc, 0xcc, 0xcc, 0xcc, 0xcf,

    /* U+005C "\\" */
    0xc6, 0x18, 0xc6, 0x30, 0x86, 0x31, 0x84, 0x31,
    0x8c,

    /* U+005D "]" */
    0xf3, 0x33, 0x33, 0x33, 0x33, 0x33, 0x3f,

    /* U+005E "^" */
    0x33, 0xb6,

    /* U+005F "_" */
    0xfc,

    /* U+0060 "`" */
    0xd9, 0x0,

    /* U+0061 "a" */
    0xfe, 0x3, 0x83, 0xe3, 0xb3, 0x9b, 0x8f, 0x87,
    0x83, 0xc1, 0xbf, 0xc0,

    /* U+0062 "b" */
    0xc0, 0x60, 0x3f, 0x98, 0x6c, 0x1e, 0xf, 0x7,
    0x83, 0xc1, 0xe0, 0xf0, 0xdf, 0xc0,

    /* U+0063 "c" */
    0x3f, 0xb0, 0x30, 0x18, 0xc, 0x6, 0x3, 0x1,
    0x80, 0x60, 0x1f, 0xc0,

    /* U+0064 "d" */
    0x1, 0x80, 0xcf, 0xec, 0x3c, 0x1e, 0xf, 0x7,
    0x83, 0xc1, 0xe0, 0xd8, 0x67, 0xf0,

    /* U+0065 "e" */
    0x3e, 0x30, 0xf0, 0x78, 0x3f, 0xfe, 0x3, 0x1,
    0x80, 0x60, 0x1f, 0xc0,

    /* U+0066 "f" */
    0x3e, 0xc3, 0xfb, 0x6, 0xc, 0x18, 0x30, 0x60,
    0xc1, 0x83, 0x0,

    /* U+0067 "g" */
    0x3f, 0xa0, 0xf0, 0x78, 0x3c, 0x1e, 0xf, 0x6,
    0xff, 0x1, 0x80, 0xc0, 0x6f, 0xe0,

    /* U+0068 "h" */
    0xc0, 0x60, 0x3f, 0xd8, 0x3c, 0x1e, 0xf, 0x7,
    0x83, 0xc1, 0xe0, 0xf0, 0x78, 0x30,

    /* U+0069 "i" */
    0xcf, 0xff, 0xff,

    /* U+006A "j" */
    0x30, 0x33, 0x33, 0x33, 0x33, 0x33, 0x3e,

    /* U+006B "k" */
    0xc0, 0x30, 0xc, 0x1b, 0xc, 0xc3, 0x31, 0x8c,
    0xc3, 0xe0, 0xcc, 0x31, 0x8c, 0x33, 0x6,

    /* U+006C "l" */
    0xff, 0xff, 0xff,

    /* U+006D "m" */
    0xff, 0xfb, 0xc, 0x3c, 0x30, 0xf0, 0xc3, 0xc3,
    0xf, 0xc, 0x3c, 0x30, 0xf0, 0xc3, 0xc3, 0xf,
    0xc, 0x30,

    /* U+006E "n" */
    0xff, 0x60, 0xf0, 0x78, 0x3c, 0x1e, 0xf, 0x7,
    0x83, 0xc1, 0xe0, 0xc0,

    /* U+006F "o" */
    0x3f, 0x18, 0x6c, 0xf, 0x3, 0xc0, 0xf0, 0x3c,
    0xf, 0x3, 0x61, 0x8f, 0xc0,

    /* U+0070 "p" */
    0xfe, 0x61, 0xb0, 0x78, 0x3c, 0x1e, 0xf, 0x7,
    0x83, 0xc3, 0x7f, 0x30, 0x18, 0x0,

    /* U+0071 "q" */
    0x3f, 0xb0, 0xf0, 0x78, 0x3c, 0x1e, 0xf, 0x7,
    0x83, 0x61, 0x9f, 0xc0, 0x60, 0x30,

    /* U+0072 "r" */
    0x7f, 0xc, 0x30, 0xc3, 0xc, 0x30, 0xc3, 0x0,

    /* U+0073 "s" */
    0x7f, 0x60, 0x30, 0x1c, 0xf, 0xe1, 0xf8, 0x1c,
    0x2, 0x1, 0x7f, 0x0,

    /* U+0074 "t" */
    0x60, 0xc3, 0xfb, 0x6, 0xc, 0x18, 0x30, 0x60,
    0xc1, 0x81, 0xf0,

    /* U+0075 "u" */
    0xc1, 0xe0, 0xf0, 0x78, 0x3c, 0x1e, 0xf, 0x7,
    0x83, 0xc1, 0xbf, 0xc0,

    /* U+0076 "v" */
    0x60, 0x6c, 0xd, 0x83, 0x18, 0x63, 0x18, 0x33,
    0x6, 0x40, 0x58, 0xf, 0x0, 0xc0,

    /* U+0077 "w" */
    0x41, 0x83, 0x63, 0xc2, 0x63, 0x46, 0x62, 0x46,
    0x22, 0x66, 0x26, 0x64, 0x36, 0x6c, 0x34, 0x2c,
    0x14, 0x2c, 0x1c, 0x38,

    /* U+0078 "x" */
    0x60, 0xcc, 0x18, 0xc6, 0x8, 0x81, 0xb0, 0x1c,
    0x6, 0xc1, 0x8c, 0x31, 0xcc, 0x18,

    /* U+0079 "y" */
    0xc0, 0x6c, 0x19, 0x83, 0x18, 0xc3, 0x18, 0x72,
    0x6, 0xc0, 0xd8, 0xe, 0x0, 0xc0, 0x10, 0x3c,
    0x0,

    /* U+007A "z" */
    0xff, 0x0, 0xc0, 0xe1, 0xe1, 0xe1, 0xe1, 0xc1,
    0xc0, 0xc0, 0x3f, 0xc0,

    /* U+007B "{" */
    0x1c, 0xc3, 0xc, 0x30, 0xce, 0xc, 0x30, 0xc3,
    0xc, 0x30, 0x70,

    /* U+007C "|" */
    0xff, 0xff, 0xff, 0xf0,

    /* U+007D "}" */
    0xe1, 0x8c, 0x63, 0x18, 0xe6, 0x31, 0x8c, 0x63,
    0x70,

    /* U+007E "~" */
    0xcf, 0xbd, 0xc0
};


/*---------------------
 *  GLYPH DESCRIPTION
 *--------------------*/

static const lv_font_fmt_txt_glyph_dsc_t glyph_dsc[] = {
    {.bitmap_index = 0, .adv_w = 0, .box_w = 0, .box_h = 0, .ofs_x = 0, .ofs_y = 0} /* id = 0 reserved */,
    {.bitmap_index = 0, .adv_w = 67, .box_w = 1, .box_h = 1, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 1, .adv_w = 68, .box_w = 2, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 4, .adv_w = 115, .box_w = 5, .box_h = 4, .ofs_x = 1, .ofs_y = 8},
    {.bitmap_index = 7, .adv_w = 213, .box_w = 12, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 25, .adv_w = 185, .box_w = 10, .box_h = 15, .ofs_x = 1, .ofs_y = -1},
    {.bitmap_index = 44, .adv_w = 220, .box_w = 13, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 64, .adv_w = 220, .box_w = 13, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 84, .adv_w = 67, .box_w = 2, .box_h = 4, .ofs_x = 1, .ofs_y = 8},
    {.bitmap_index = 85, .adv_w = 94, .box_w = 4, .box_h = 14, .ofs_x = 1, .ofs_y = -2},
    {.bitmap_index = 92, .adv_w = 94, .box_w = 4, .box_h = 14, .ofs_x = 0, .ofs_y = -2},
    {.bitmap_index = 99, .adv_w = 134, .box_w = 6, .box_h = 7, .ofs_x = 1, .ofs_y = 6},
    {.bitmap_index = 105, .adv_w = 140, .box_w = 7, .box_h = 7, .ofs_x = 1, .ofs_y = 3},
    {.bitmap_index = 112, .adv_w = 71, .box_w = 3, .box_h = 4, .ofs_x = 0, .ofs_y = -2},
    {.bitmap_index = 114, .adv_w = 86, .box_w = 4, .box_h = 1, .ofs_x = 1, .ofs_y = 4},
    {.bitmap_index = 115, .adv_w = 68, .box_w = 2, .box_h = 1, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 116, .adv_w = 84, .box_w = 5, .box_h = 14, .ofs_x = 0, .ofs_y = -2},
    {.bitmap_index = 125, .adv_w = 205, .box_w = 11, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 142, .adv_w = 161, .box_w = 9, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 156, .adv_w = 186, .box_w = 10, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 171, .adv_w = 182, .box_w = 10, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 186, .adv_w = 204, .box_w = 12, .box_h = 12, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 204, .adv_w = 183, .box_w = 9, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 218, .adv_w = 190, .box_w = 10, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 233, .adv_w = 177, .box_w = 10, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 248, .adv_w = 193, .box_w = 10, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 263, .adv_w = 190, .box_w = 10, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 278, .adv_w = 68, .box_w = 2, .box_h = 10, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 281, .adv_w = 72, .box_w = 2, .box_h = 12, .ofs_x = 1, .ofs_y = -2},
    {.bitmap_index = 284, .adv_w = 118, .box_w = 5, .box_h = 8, .ofs_x = 1, .ofs_y = 2},
    {.bitmap_index = 289, .adv_w = 130, .box_w = 7, .box_h = 5, .ofs_x = 1, .ofs_y = 4},
    {.bitmap_index = 294, .adv_w = 118, .box_w = 5, .box_h = 8, .ofs_x = 1, .ofs_y = 2},
    {.bitmap_index = 299, .adv_w = 160, .box_w = 9, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 313, .adv_w = 229, .box_w = 12, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 330, .adv_w = 220, .box_w = 14, .box_h = 12, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 351, .adv_w = 200, .box_w = 10, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 366, .adv_w = 194, .box_w = 11, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 383, .adv_w = 209, .box_w = 11, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 400, .adv_w = 194, .box_w = 10, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 415, .adv_w = 189, .box_w = 10, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 430, .adv_w = 212, .box_w = 12, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 448, .adv_w = 227, .box_w = 11, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 465, .adv_w = 81, .box_w = 2, .box_h = 12, .ofs_x = 2, .ofs_y = 0},
    {.bitmap_index = 468, .adv_w = 161, .box_w = 8, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 480, .adv_w = 201, .box_w = 11, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 497, .adv_w = 172, .box_w = 9, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 511, .adv_w = 292, .box_w = 17, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 537, .adv_w = 248, .box_w = 13, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 557, .adv_w = 223, .box_w = 12, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 575, .adv_w = 201, .box_w = 11, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 592, .adv_w = 218, .box_w = 12, .box_h = 14, .ofs_x = 1, .ofs_y = -2},
    {.bitmap_index = 613, .adv_w = 206, .box_w = 11, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 630, .adv_w = 185, .box_w = 10, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 645, .adv_w = 191, .box_w = 11, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 662, .adv_w = 225, .box_w = 11, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 679, .adv_w = 207, .box_w = 12, .box_h = 12, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 697, .adv_w = 315, .box_w = 18, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 724, .adv_w = 207, .box_w = 13, .box_h = 12, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 744, .adv_w = 200, .box_w = 12, .box_h = 12, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 762, .adv_w = 180, .box_w = 10, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 777, .adv_w = 94, .box_w = 4, .box_h = 14, .ofs_x = 1, .ofs_y = -2},
    {.bitmap_index = 784, .adv_w = 84, .box_w = 5, .box_h = 14, .ofs_x = 0, .ofs_y = -2},
    {.bitmap_index = 793, .adv_w = 94, .box_w = 4, .box_h = 14, .ofs_x = 0, .ofs_y = -2},
    {.bitmap_index = 800, .adv_w = 181, .box_w = 5, .box_h = 3, .ofs_x = 3, .ofs_y = 5},
    {.bitmap_index = 802, .adv_w = 99, .box_w = 6, .box_h = 1, .ofs_x = 0, .ofs_y = -1},
    {.bitmap_index = 803, .adv_w = 181, .box_w = 3, .box_h = 3, .ofs_x = 4, .ofs_y = 11},
    {.bitmap_index = 805, .adv_w = 175, .box_w = 9, .box_h = 10, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 817, .adv_w = 186, .box_w = 9, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 831, .adv_w = 164, .box_w = 9, .box_h = 10, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 843, .adv_w = 186, .box_w = 9, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 857, .adv_w = 181, .box_w = 9, .box_h = 10, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 869, .adv_w = 119, .box_w = 7, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 880, .adv_w = 181, .box_w = 9, .box_h = 12, .ofs_x = 1, .ofs_y = -2},
    {.bitmap_index = 894, .adv_w = 183, .box_w = 9, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 908, .adv_w = 74, .box_w = 2, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 911, .adv_w = 74, .box_w = 4, .box_h = 14, .ofs_x = 0, .ofs_y = -2},
    {.bitmap_index = 918, .adv_w = 179, .box_w = 10, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 933, .adv_w = 74, .box_w = 2, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 936, .adv_w = 274, .box_w = 14, .box_h = 10, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 954, .adv_w = 183, .box_w = 9, .box_h = 10, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 966, .adv_w = 191, .box_w = 10, .box_h = 10, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 979, .adv_w = 189, .box_w = 9, .box_h = 12, .ofs_x = 1, .ofs_y = -2},
    {.bitmap_index = 993, .adv_w = 186, .box_w = 9, .box_h = 12, .ofs_x = 1, .ofs_y = -2},
    {.bitmap_index = 1007, .adv_w = 122, .box_w = 6, .box_h = 10, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 1015, .adv_w = 161, .box_w = 9, .box_h = 10, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 1027, .adv_w = 125, .box_w = 7, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 1038, .adv_w = 183, .box_w = 9, .box_h = 10, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 1050, .adv_w = 185, .box_w = 11, .box_h = 10, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 1064, .adv_w = 259, .box_w = 16, .box_h = 10, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 1084, .adv_w = 177, .box_w = 11, .box_h = 10, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 1098, .adv_w = 172, .box_w = 11, .box_h = 12, .ofs_x = 0, .ofs_y = -2},
    {.bitmap_index = 1115, .adv_w = 166, .box_w = 9, .box_h = 10, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 1127, .adv_w = 93, .box_w = 6, .box_h = 14, .ofs_x = 0, .ofs_y = -2},
    {.bitmap_index = 1138, .adv_w = 79, .box_w = 2, .box_h = 14, .ofs_x = 2, .ofs_y = -2},
    {.bitmap_index = 1142, .adv_w = 93, .box_w = 5, .box_h = 14, .ofs_x = 0, .ofs_y = -2},
    {.bitmap_index = 1151, .adv_w = 220, .box_w = 6, .box_h = 3, .ofs_x = 4, .ofs_y = 5}
};

/*---------------------
 *  CHARACTER MAPPING
 *--------------------*/



/*Collect the unicode lists and glyph_id offsets*/
static const lv_font_fmt_txt_cmap_t cmaps[] =
{
    {
        .range_start = 32, .range_length = 95, .glyph_id_start = 1,
        .unicode_list = NULL, .glyph_id_ofs_list = NULL, .list_length = 0, .type = LV_FONT_FMT_TXT_CMAP_FORMAT0_TINY
    }
};

/*-----------------
 *    KERNING
 *----------------*/


/*Map glyph_ids to kern left classes*/
static const uint8_t kern_left_class_mapping[] =
{
    0, 0, 0, 1, 0, 0, 0, 0,
    1, 2, 0, 1, 3, 4, 3, 4,
    5, 6, 7, 8, 9, 10, 11, 12,
    13, 9, 6, 14, 14, 0, 3, 15,
    0, 16, 17, 9, 18, 6, 19, 20,
    21, 0, 0, 22, 23, 24, 25, 26,
    6, 27, 6, 28, 29, 30, 31, 32,
    33, 34, 35, 36, 2, 37, 0, 0,
    4, 0, 38, 39, 40, 0, 0, 41,
    0, 38, 0, 0, 42, 0, 38, 38,
    39, 39, 0, 43, 44, 45, 0, 46,
    47, 48, 49, 50, 2, 0, 0, 0
};

/*Map glyph_ids to kern right classes*/
static const uint8_t kern_right_class_mapping[] =
{
    0, 0, 0, 1, 0, 0, 0, 2,
    1, 0, 3, 1, 4, 5, 4, 5,
    6, 7, 8, 9, 10, 11, 12, 7,
    13, 14, 15, 16, 16, 17, 4, 0,
    0, 0, 18, 0, 7, 0, 0, 0,
    7, 0, 0, 19, 0, 0, 20, 21,
    7, 0, 7, 0, 22, 23, 24, 25,
    26, 27, 28, 29, 0, 30, 3, 0,
    5, 0, 31, 0, 32, 32, 32, 33,
    34, 0, 0, 0, 0, 0, 35, 35,
    32, 35, 32, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 0, 0, 3, 0
};

/*Kern values between classes*/
static const int8_t kern_class_values[] =
{
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, -18, 0, 0, 0, 0, 0,
    0, -23, -38, -8, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, -8, 0,
    0, -5, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, -5, 0, 0, 0, 0,
    0, 0, -5, -5, -5, 0, 0, -5,
    0, 0, 0, 0, 0, 0, 0, -15,
    -5, -5, 0, 0, -15, 0, 0, 0,
    0, -5, -5, 0, 0, 0, -15, 0,
    -10, -8, -5, -20, -5, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -10,
    -5, -8, -5, -5, 0, 0, 0, 0,
    0, 0, -8, 0, 0, 0, -15, -5,
    -20, -8, -5, 0, 0, 0, 0, 0,
    0, 0, -23, 0, -33, -23, 0, -38,
    0, 0, 0, -5, 0, 0, 0, 0,
    0, 0, 0, -26, -10, 0, -8, 0,
    0, 0, 0, -10, 0, 0, -5, 0,
    0, 0, -5, 0, 0, -5, 0, 0,
    0, -10, -10, -8, -5, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -3,
    0, -3, 0, -5, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, -3, 0,
    -8, -5, 0, 0, -10, -3, 0, 0,
    -15, 0, 0, 0, 0, -5, -10, 0,
    0, 0, -5, 0, -5, -5, -5, -10,
    -3, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, -3, 0, -3, 0, -3,
    -26, 0, 0, -8, 0, 0, -8, 0,
    0, 0, -13, 0, -18, 0, 0, 0,
    0, 0, 0, 0, 0, 0, -23, 0,
    -23, -18, 0, -26, 0, -18, 0, 0,
    0, 0, 0, 0, 0, 0, -3, 0,
    -13, 0, 0, 0, 0, 0, 0, -5,
    -3, 0, -8, 0, 0, 0, -13, 0,
    -5, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, -5, 0, -8, -5, 0, 0,
    0, 0, 0, 0, -10, 0, 0, -5,
    0, -3, 0, 0, 0, 0, -5, 0,
    -10, -10, -5, -10, 0, -3, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, -5, -3, 0, -10, 0, 0, 0,
    -5, 0, 0, 0, 0, -5, 0, 0,
    -18, 0, -5, -5, 0, 0, -5, 0,
    0, 0, -10, 0, -10, -10, 0, -10,
    0, -5, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, -5, 0, 0, 0,
    0, 0, 0, 0, -5, -5, 0, 0,
    0, 0, 0, 0, -8, 0, 0, -5,
    0, 0, -5, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    -3, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, -15, -44, -13, -5, 0,
    -5, 0, -23, 0, 0, -5, 0, 0,
    0, -31, -26, -13, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -10,
    0, -10, 0, -8, -5, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, -5, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -5,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, -5, 0, 0, 0, 0, -18, 0,
    0, -13, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, -8, 0, -8, -5, -5, -5,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    -23, 0, 0, -5, 0, 0, -5, 0,
    0, 0, -8, 0, -15, -3, 0, 0,
    -5, 0, 0, 0, 0, 0, -28, -8,
    -28, -26, 0, -36, 0, -15, 0, -3,
    -3, -3, 0, 0, 0, -5, -3, -18,
    -13, 0, -5, 0, 0, 0, 0, -8,
    0, 0, -8, 0, 0, 0, -13, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, -3, 0, -5, 0, 0,
    0, 0, 0, -10, -10, 0, -5, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -8,
    -5, -5, -3, 0, 0, -5, 0, 0,
    -31, -8, -5, 0, 0, 0, -5, 0,
    -10, 0, 0, 0, 0, -23, -64, 0,
    -10, 0, 0, 0, 0, 0, 0, 0,
    0, 0, -5, -3, 0, -3, 0, -3,
    -3, 0, 0, 0, 0, -5, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, -3, -3, 0, 0, 0, -5, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -5,
    0, -3, -5, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, -8, 0, -3,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, -10, 0,
    0, 0, -15, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -8,
    -5, -8, 0, 0, 0, 0, -10, -10,
    -10, 0, -8, -3, -49, 0, 0, -10,
    0, 0, -8, 0, 0, 0, -10, 0,
    -26, 0, 0, 0, 0, 0, 0, 0,
    0, 0, -41, -8, -36, -31, 0, -46,
    0, -8, 0, -5, -5, -5, 0, 0,
    0, -8, -5, -33, -23, 0, -13, 0,
    -8, 0, 0, 0, 0, 0, -3, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, -15, 0,
    -15, -15, 0, -20, 0, -5, 0, -3,
    0, 0, 0, 0, 0, 0, -3, 0,
    -5, 0, 0, 0, 0, 0, 0, 0,
    0, -5, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, -3, -5, 0,
    0, 0, -5, 0, -8, -5, 0, -8,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, -3, 0, 0,
    0, 0, 0, -10, -31, -18, 0, 0,
    0, 0, -10, 0, 0, -5, 0, 0,
    0, -26, -64, -13, 0, -3, 0, 0,
    -5, -5, -10, -8, -10, 0, 0, -8,
    0, -5, 0, -5, -3, 0, 0, 0,
    0, -5, 0, 0, 0, 0, 0, -5,
    0, 0, -3, 0, 0, 0, -8, 0,
    0, 0, 0, 0, 0, 0, -10, 0,
    0, 0, 0, 0, -5, -8, 0, -8,
    0, 0, 0, -4, 0, -5, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, -3, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, -3, -3, 0, 0, 0, -10, 0,
    0, 0, 0, 0, -3, 0, 0, 0,
    0, 0, 0, 0, -5, 0, 0, -8,
    -5, -3, -5, 0, 0, 0, 0, -18,
    -23, -15, -5, 0, 0, 0, -31, 0,
    0, -5, 0, 0, -18, -28, -46, -15,
    -5, -3, 0, 0, 0, 0, 0, 0,
    0, 0, -8, -20, 0, -18, -18, -20,
    -15, 0, -18, -13, -3, -5, -5, -15,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, -8, -8, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -10,
    -33, -13, -5, 0, 0, 0, -13, 0,
    0, -8, 0, 0, 0, -28, -41, -15,
    -8, -3, 0, 0, 0, 0, 0, 0,
    -5, 0, -8, -15, -3, -15, -13, -13,
    -13, 0, -5, 0, 0, -8, 0, -10,
    0, 0, 0, -8, -23, -13, -5, 0,
    0, -5, -18, 0, 0, -5, 0, 0,
    -13, -26, -33, -15, -5, -5, 0, 0,
    0, 0, 0, 0, -3, 0, -8, -13,
    -3, -13, -8, -13, -10, 0, -5, 0,
    0, -5, 0, -8, 0, 0, 0, -5,
    0, 0, -5, 0, 0, 0, -5, 0,
    0, -5, 0, 0, 0, 0, 0, 0,
    -3, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, -8, 0, -10, 0, -3,
    0, 0, 0, -10, -5, 0, -3, 0,
    0, 0, 0, -20, -38, -15, -10, 0,
    0, 0, -26, 0, 0, -8, 0, -5,
    0, -33, -46, -20, -8, -5, 0, 0,
    0, 0, 0, 0, 0, 0, -8, -23,
    -5, -20, -13, -23, -18, 0, -10, -8,
    -5, -8, -5, -13, 0, 0, 0, -5,
    0, 0, -3, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, -3, 0, 0, -3, 0, 0, -3,
    0, 0, 0, -5, 0, -5, 0, 0,
    -5, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, -5, 0,
    0, -5, -5, 0, -13, -3, 0, 0,
    0, 0, 0, 0, 0, 0, -5, 0,
    -18, -13, 0, -15, 0, 0, 0, 0,
    0, -3, 0, 0, 0, 0, 0, -13,
    -5, 0, 0, 0, -5, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, -20, 0, -18, -13, 0, -20,
    0, -5, 0, 0, 0, 0, 0, 0,
    0, 0, 0, -10, -8, 0, -8, 0,
    -3, 0, -5, 0, -5, -3, 0, 0,
    0, 0, 0, 0, -10, 0, 0, 0,
    0, -3, -5, 0, 0, 0, -20, 0,
    -15, -10, -8, -20, -5, -5, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -3,
    -3, -5, -5, -5, 0, 0, 0, 0,
    0, 0, -3, 0, 0, 0, -8, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, -5, 0, -3, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, -8, 0, 0,
    0, 0, -10, 0, 0, 0, 0, 0,
    0, -15, -33, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -5,
    0, -3, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -10,
    0, 0, -5, 0, 0, 0, -10, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, -10, 0, -10, -8, 0, -8,
    0, 0, 0, -10, 0, -8, 0, 0,
    -8, 0, 0, 0, 0, 0, 0, -5,
    0, 0, 0, 0, -23, 0, 0, 0,
    0, 0, -10, 0, 0, 0, 0, 0,
    0, -18, -33, 0, 0, 0, -10, 0,
    0, 0, 0, -5, 0, 0, 0, -5,
    5, -3, 0, 0, 0, 5, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, -10, 0, -8, -10, 0, -10,
    -3, 0, 0, 0, 0, -3, 0, 0,
    -4, 0, 0, -3, 0, 0, 0, -3,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, -5, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -5,
    0, -3, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -10,
    -26, -5, -3, 0, 0, 0, -5, 0,
    0, 0, 0, 0, 0, -13, -26, 0,
    0, 0, -13, 0, 0, 0, -10, 0,
    -10, 0, 0, -3, 0, -3, 0, -8,
    -8, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, -5, -10, -5, 0, 0,
    0, 0, -8, 0, 0, 0, 0, 0,
    0, -13, -23, 0, 0, 0, -3, 0,
    0, 0, -5, 0, -5, 0, 0, -3,
    0, -3, 0, -3, -5, 0, 0, 0,
    0, 0, 0, -3, 0, 0, 0, -8,
    0, 0, -3, 0, 0, 0, -8, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, -5, 0, -8, -5, 0, -8,
    0, 0, 0, -5, 0, -3, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, -5, -15, -5, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, -13, -13, 0, 0, 0, -5, 0,
    0, 0, -3, 0, -5, 0, 0, -5,
    0, -3, 0, -5, -3, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -5,
    0, 0, -3, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, -15, 0, -18, -8, 0, -13,
    0, -8, 0, -8, 0, -5, 0, 0,
    -3, 0, 0, -5, -5, 0, -3, 0
};


/*Collect the kern class' data in one place*/
static const lv_font_fmt_txt_kern_classes_t kern_classes =
{
    .class_pair_values   = kern_class_values,
    .left_class_mapping  = kern_left_class_mapping,
    .right_class_mapping = kern_right_class_mapping,
    .left_class_cnt      = 50,
    .right_class_cnt     = 44,
};

/*--------------------
 *  ALL CUSTOM DATA
 *--------------------*/

#if LV_VERSION_CHECK(8, 0, 0)
/*Store all the custom data of the font*/
static  lv_font_fmt_txt_glyph_cache_t cache;
static const lv_font_fmt_txt_dsc_t font_dsc = {
#else
static lv_font_fmt_txt_dsc_t font_dsc = {
#endif
    .glyph_bitmap = glyph_bitmap,
    .glyph_dsc = glyph_dsc,
    .cmaps = cmaps,
    .kern_dsc = &kern_classes,
    .kern_scale = 16,
    .cmap_num = 1,
    .bpp = 1,
    .kern_classes = 1,
    .bitmap_format = 0,
#if LV_VERSION_CHECK(8, 0, 0)
    .cache = &cache
#endif
};


/*-----------------
 *  PUBLIC FONT
 *----------------*/

/*Initialize a public general font descriptor*/
#if LV_VERSION_CHECK(8, 0, 0)
const lv_font_t ui_font_F1R16 = {
#else
lv_font_t ui_font_F1R16 = {
#endif
    .get_glyph_dsc = lv_font_get_glyph_dsc_fmt_txt,    /*Function pointer to get glyph's data*/
    .get_glyph_bitmap = lv_font_get_bitmap_fmt_txt,    /*Function pointer to get glyph's bitmap*/
    .line_height = 16,          /*The maximum line height required by the font*/
    .base_line = 2,             /*Baseline measured from the bottom of the line*/
#if !(LVGL_VERSION_MAJOR == 6 && LVGL_VERSION_MINOR == 0)
    .subpx = LV_FONT_SUBPX_NONE,
#endif
#if LV_VERSION_CHECK(7, 4, 0) || LVGL_VERSION_MAJOR >= 8
    .underline_position = 0,
    .underline_thickness = 0,
#endif
    .dsc = &font_dsc           /*The custom font data. Will be accessed by `get_glyph_bitmap/dsc` */
};



#endif /*#if UI_FONT_F1R16*/

