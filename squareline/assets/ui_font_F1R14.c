/*******************************************************************************
 * Size: 14 px
 * Bpp: 1
 * Opts: --bpp 1 --size 14 --font F:/ESP32/squareline/assets/Formula1-Regular.otf -o F:/ESP32/squareline/assets\ui_font_F1R14.c --format lvgl -r 0x20-0x7f --no-compress --no-prefilter
 ******************************************************************************/

#include "../ui.h"

#ifndef UI_FONT_F1R14
#define UI_FONT_F1R14 1
#endif

#if UI_FONT_F1R14

/*-----------------
 *    BITMAPS
 *----------------*/

/*Store the image of the glyphs*/
static LV_ATTRIBUTE_LARGE_CONST const uint8_t glyph_bitmap[] = {
    /* U+0020 " " */
    0x0,

    /* U+0021 "!" */
    0xff, 0xff, 0x3c,

    /* U+0022 "\"" */
    0xfb, 0xbb,

    /* U+0023 "#" */
    0x9, 0x82, 0x41, 0x91, 0xff, 0x13, 0x4, 0x81,
    0x23, 0xfe, 0x26, 0x9, 0x2, 0x40,

    /* U+0024 "$" */
    0xc, 0x6, 0x1f, 0xf9, 0x8c, 0xc6, 0x61, 0xf0,
    0x7e, 0xf, 0x86, 0xc3, 0x61, 0xbf, 0xf0, 0x60,

    /* U+0025 "%" */
    0x78, 0xd9, 0x93, 0x34, 0x66, 0x87, 0xa0, 0x0,
    0x3, 0x70, 0xd3, 0x12, 0x66, 0x4d, 0x87, 0x0,

    /* U+0026 "&" */
    0x1f, 0x82, 0x0, 0xc0, 0xc, 0x1, 0xc0, 0xf8,
    0xf1, 0xb6, 0x1c, 0xc1, 0x98, 0x79, 0xfb, 0x80,

    /* U+0027 "'" */
    0xea,

    /* U+0028 "(" */
    0x7b, 0x6d, 0xb6, 0xdb, 0x66,

    /* U+0029 ")" */
    0xe3, 0x33, 0x33, 0x33, 0x33, 0x33, 0xe0,

    /* U+002A "*" */
    0x48, 0xcf, 0xcc, 0x48,

    /* U+002B "+" */
    0x30, 0xcf, 0xcc, 0x30, 0xc0,

    /* U+002C "," */
    0x6d, 0xa0,

    /* U+002D "-" */
    0xe0,

    /* U+002E "." */
    0xf0,

    /* U+002F "/" */
    0x11, 0x33, 0x22, 0x66, 0x64, 0x4c, 0xc0,

    /* U+0030 "0" */
    0x3f, 0x18, 0x6c, 0xf, 0x3, 0xc0, 0xf0, 0x3c,
    0xf, 0x3, 0xc0, 0xd8, 0x63, 0xf0,

    /* U+0031 "1" */
    0xf8, 0x18, 0x18, 0x18, 0x18, 0x18, 0x18, 0x18,
    0x18, 0x18, 0xff,

    /* U+0032 "2" */
    0xff, 0x0, 0x80, 0x60, 0x60, 0xf0, 0xf1, 0xe1,
    0xe0, 0xc0, 0x60, 0x3f, 0xc0,

    /* U+0033 "3" */
    0xff, 0x83, 0x83, 0x83, 0x83, 0x83, 0xf8, 0x6,
    0x3, 0x1, 0x80, 0xff, 0xc0,

    /* U+0034 "4" */
    0x7, 0x1, 0xb0, 0x26, 0xc, 0xc3, 0x18, 0xc3,
    0x30, 0x66, 0xc, 0xff, 0xe0, 0x30, 0x6, 0x0,

    /* U+0035 "5" */
    0xff, 0xc0, 0xc0, 0xc0, 0xc0, 0xfe, 0x3, 0x3,
    0x3, 0x3, 0xfe,

    /* U+0036 "6" */
    0x3f, 0xb0, 0x30, 0x18, 0xc, 0x7, 0xfb, 0x7,
    0x83, 0xc1, 0xb0, 0xcf, 0xc0,

    /* U+0037 "7" */
    0xff, 0x80, 0xc0, 0x60, 0x60, 0x30, 0x30, 0x30,
    0x18, 0x18, 0xc, 0xc, 0x0,

    /* U+0038 "8" */
    0x7f, 0x60, 0xf0, 0x78, 0x3c, 0x19, 0xf3, 0x7,
    0x83, 0xc1, 0xe0, 0xdf, 0xc0,

    /* U+0039 "9" */
    0x7e, 0x61, 0xb0, 0x78, 0x3c, 0x1b, 0xfc, 0x6,
    0x3, 0x1, 0x81, 0xbf, 0x80,

    /* U+003A ":" */
    0xf0, 0x3, 0xc0,

    /* U+003B ";" */
    0xf0, 0x3, 0xf8,

    /* U+003C "<" */
    0x13, 0xe8, 0xe3, 0x10,

    /* U+003D "=" */
    0xfc, 0x0, 0x3f,

    /* U+003E ">" */
    0x8c, 0x71, 0x7c, 0x80,

    /* U+003F "?" */
    0xfc, 0x6, 0x3, 0x3, 0x3, 0x6, 0x3c, 0x0,
    0x0, 0x30, 0x30,

    /* U+0040 "@" */
    0xff, 0x0, 0x60, 0xd, 0xfb, 0xc6, 0xf1, 0xbc,
    0x6f, 0x1b, 0xc6, 0xdf, 0xf0,

    /* U+0041 "A" */
    0x6, 0x0, 0xf0, 0x9, 0x1, 0x98, 0x19, 0x83,
    0xc, 0x30, 0xc3, 0xfc, 0x60, 0x64, 0x2, 0xc0,
    0x30,

    /* U+0042 "B" */
    0xff, 0x60, 0xf0, 0x78, 0x3c, 0x1f, 0xf3, 0x7,
    0x83, 0xc1, 0xe0, 0xff, 0xc0,

    /* U+0043 "C" */
    0x3f, 0xb0, 0x30, 0x18, 0xc, 0x6, 0x3, 0x1,
    0x80, 0xc0, 0x30, 0xf, 0xe0,

    /* U+0044 "D" */
    0xff, 0x30, 0x6c, 0xf, 0x3, 0xc0, 0xf0, 0x3c,
    0xf, 0x3, 0xc0, 0xf0, 0x6f, 0xf0,

    /* U+0045 "E" */
    0xff, 0xe0, 0x30, 0x18, 0xc, 0x7, 0xff, 0x1,
    0x80, 0xc0, 0x60, 0x3f, 0xe0,

    /* U+0046 "F" */
    0xff, 0xe0, 0x30, 0x18, 0xc, 0x7, 0xff, 0x1,
    0x80, 0xc0, 0x60, 0x30, 0x0,

    /* U+0047 "G" */
    0x3f, 0x98, 0xc, 0x3, 0x0, 0xc0, 0x31, 0xfc,
    0xf, 0x3, 0xc0, 0xd8, 0x33, 0xf8,

    /* U+0048 "H" */
    0xc0, 0xf0, 0x3c, 0xf, 0x3, 0xc0, 0xff, 0xfc,
    0xf, 0x3, 0xc0, 0xf0, 0x3c, 0xc,

    /* U+0049 "I" */
    0xff, 0xff, 0xfc,

    /* U+004A "J" */
    0x6, 0xc, 0x18, 0x30, 0x60, 0xc1, 0x83, 0x6,
    0x1b, 0xe0,

    /* U+004B "K" */
    0xc1, 0xb0, 0x6c, 0x33, 0x18, 0xcc, 0x3e, 0xc,
    0xc3, 0x18, 0xc3, 0x30, 0x6c, 0x1c,

    /* U+004C "L" */
    0xc0, 0xc0, 0xc0, 0xc0, 0xc0, 0xc0, 0xc0, 0xc0,
    0xc0, 0xc0, 0xff,

    /* U+004D "M" */
    0x30, 0x31, 0xe1, 0xe6, 0x85, 0x92, 0x16, 0x4c,
    0xc9, 0x33, 0x2c, 0xc8, 0xf1, 0x23, 0xc5, 0x8f,
    0x1e, 0x38, 0x30, 0x40,

    /* U+004E "N" */
    0x60, 0x7a, 0xf, 0x41, 0xe4, 0x3c, 0xc7, 0x88,
    0xf0, 0x9e, 0x13, 0xc1, 0x78, 0x2f, 0x3, 0x0,

    /* U+004F "O" */
    0x3f, 0x8c, 0x1b, 0x1, 0xe0, 0x3c, 0x7, 0x80,
    0xf0, 0x1e, 0x3, 0xc0, 0x6c, 0x18, 0xfe, 0x0,

    /* U+0050 "P" */
    0xff, 0x60, 0xf0, 0x78, 0x3c, 0x1f, 0xfb, 0x1,
    0x80, 0xc0, 0x60, 0x30, 0x0,

    /* U+0051 "Q" */
    0x3f, 0x8c, 0x1b, 0x1, 0xe0, 0x3c, 0x7, 0x80,
    0xf0, 0x1e, 0x3, 0xc0, 0x6c, 0x18, 0xfe, 0x1,
    0x0, 0x30,

    /* U+0052 "R" */
    0xff, 0x60, 0xf0, 0x78, 0x3c, 0x1f, 0xfb, 0xe1,
    0xb8, 0xce, 0x63, 0xb0, 0xc0,

    /* U+0053 "S" */
    0x7f, 0xe0, 0x30, 0x1c, 0xf, 0xc1, 0xf8, 0x3e,
    0x3, 0x1, 0x80, 0xff, 0xc0,

    /* U+0054 "T" */
    0xff, 0xc3, 0x0, 0xc0, 0x30, 0xc, 0x3, 0x0,
    0xc0, 0x30, 0xc, 0x3, 0x0, 0xc0,

    /* U+0055 "U" */
    0xc0, 0xf0, 0x3c, 0xf, 0x3, 0xc0, 0xf0, 0x3c,
    0xf, 0x3, 0xc0, 0xf0, 0x77, 0xf8,

    /* U+0056 "V" */
    0x40, 0x6c, 0x9, 0x83, 0x10, 0x63, 0x8, 0x63,
    0x4, 0x60, 0xc8, 0x1b, 0x1, 0xc0, 0x38, 0x0,

    /* U+0057 "W" */
    0x41, 0xc1, 0xb0, 0xe0, 0x98, 0x58, 0xcc, 0x6c,
    0x62, 0x36, 0x31, 0x99, 0x10, 0xc8, 0xd8, 0x24,
    0x6c, 0x16, 0x34, 0xf, 0xe, 0x3, 0x7, 0x0,

    /* U+0058 "X" */
    0x60, 0x6c, 0x18, 0xc2, 0x8, 0xc1, 0xb0, 0x1c,
    0x6, 0xc0, 0x8c, 0x30, 0x8c, 0x19, 0x81, 0x80,

    /* U+0059 "Y" */
    0x60, 0x66, 0x6, 0x30, 0xc1, 0x8, 0x19, 0x80,
    0xf0, 0xf, 0x0, 0x60, 0x6, 0x0, 0x60, 0x6,
    0x0,

    /* U+005A "Z" */
    0xff, 0x0, 0xc0, 0xe0, 0xf0, 0xe0, 0xe0, 0xe0,
    0xe0, 0xe0, 0x60, 0x1f, 0xe0,

    /* U+005B "[" */
    0xfc, 0xcc, 0xcc, 0xcc, 0xcc, 0xcc, 0xf0,

    /* U+005C "\\" */
    0xcc, 0x44, 0x66, 0x22, 0x33, 0x31, 0x10,

    /* U+005D "]" */
    0xf3, 0x33, 0x33, 0x33, 0x33, 0x33, 0xf0,

    /* U+005E "^" */
    0x33, 0x92,

    /* U+005F "_" */
    0xf8,

    /* U+0060 "`" */
    0xc9, 0x80,

    /* U+0061 "a" */
    0xfe, 0x7, 0xf, 0x3b, 0x73, 0xe3, 0xc3, 0x83,
    0x7f,

    /* U+0062 "b" */
    0xc0, 0xc0, 0xfe, 0xc3, 0xc3, 0xc3, 0xc3, 0xc3,
    0xc3, 0xc2, 0xfe,

    /* U+0063 "c" */
    0x3f, 0x60, 0xc0, 0xc0, 0xc0, 0xc0, 0xc0, 0x40,
    0x3f,

    /* U+0064 "d" */
    0x3, 0x3, 0x7f, 0xc3, 0xc3, 0xc3, 0xc3, 0xc3,
    0xc3, 0x43, 0x7f,

    /* U+0065 "e" */
    0x3e, 0x63, 0xc3, 0xc3, 0xff, 0xc0, 0xc0, 0xe0,
    0x3f,

    /* U+0066 "f" */
    0x3d, 0x8f, 0xd8, 0x61, 0x86, 0x18, 0x61, 0x86,
    0x0,

    /* U+0067 "g" */
    0x7f, 0xc3, 0xc3, 0xc3, 0xc3, 0xc3, 0xc3, 0x7f,
    0x3, 0x3, 0x7e,

    /* U+0068 "h" */
    0xc0, 0xc0, 0xfe, 0xc3, 0xc3, 0xc3, 0xc3, 0xc3,
    0xc3, 0xc3, 0xc3,

    /* U+0069 "i" */
    0xcf, 0xff, 0xfc,

    /* U+006A "j" */
    0x30, 0x33, 0x33, 0x33, 0x33, 0x33, 0xe0,

    /* U+006B "k" */
    0xc0, 0x60, 0x30, 0x58, 0x4c, 0x66, 0x63, 0xe1,
    0x98, 0xc6, 0x61, 0xb0, 0x40,

    /* U+006C "l" */
    0xff, 0xff, 0xfc,

    /* U+006D "m" */
    0xff, 0xec, 0x63, 0xc6, 0x3c, 0x63, 0xc6, 0x3c,
    0x63, 0xc6, 0x3c, 0x63, 0xc6, 0x30,

    /* U+006E "n" */
    0xfe, 0xc3, 0xc3, 0xc3, 0xc3, 0xc3, 0xc3, 0xc3,
    0xc3,

    /* U+006F "o" */
    0x3e, 0x31, 0xb0, 0x78, 0x3c, 0x1e, 0xf, 0x6,
    0xc6, 0x3e, 0x0,

    /* U+0070 "p" */
    0xfe, 0xc2, 0xc3, 0xc3, 0xc3, 0xc3, 0xc3, 0xc3,
    0xfe, 0xc0, 0xc0,

    /* U+0071 "q" */
    0x7f, 0x43, 0xc3, 0xc3, 0xc3, 0xc3, 0xc3, 0xc3,
    0x7f, 0x3, 0x3,

    /* U+0072 "r" */
    0x7f, 0xc, 0x30, 0xc3, 0xc, 0x30, 0xc0,

    /* U+0073 "s" */
    0x7e, 0x80, 0x80, 0xf0, 0x7e, 0x1e, 0x2, 0x2,
    0xfc,

    /* U+0074 "t" */
    0x61, 0x8f, 0xd8, 0x61, 0x86, 0x18, 0x61, 0x83,
    0xc0,

    /* U+0075 "u" */
    0xc3, 0xc3, 0xc3, 0xc3, 0xc3, 0xc3, 0xc3, 0xc3,
    0x7f,

    /* U+0076 "v" */
    0xc0, 0xd8, 0x26, 0x18, 0x84, 0x33, 0x4, 0xc1,
    0xa0, 0x78, 0xc, 0x0,

    /* U+0077 "w" */
    0xc3, 0xd, 0x1e, 0x26, 0x78, 0x99, 0x26, 0x64,
    0x98, 0x93, 0x42, 0xcd, 0xe, 0x14, 0x18, 0x60,

    /* U+0078 "x" */
    0x41, 0xb0, 0x8c, 0xc2, 0xc1, 0xc0, 0xe0, 0xd8,
    0xc6, 0x61, 0x80,

    /* U+0079 "y" */
    0xc0, 0xb0, 0xd8, 0x44, 0x63, 0x31, 0x90, 0x78,
    0x38, 0x4, 0x6, 0x1e, 0x0,

    /* U+007A "z" */
    0x7f, 0x3, 0x7, 0xe, 0x1c, 0x78, 0xe0, 0xc0,
    0xff,

    /* U+007B "{" */
    0x36, 0x66, 0x66, 0xc6, 0x66, 0x66, 0x30,

    /* U+007C "|" */
    0xff, 0xff, 0xff,

    /* U+007D "}" */
    0xe1, 0x8c, 0x63, 0x18, 0x66, 0x31, 0x8c, 0x6e,
    0x0,

    /* U+007E "~" */
    0xcf, 0x6e
};


/*---------------------
 *  GLYPH DESCRIPTION
 *--------------------*/

static const lv_font_fmt_txt_glyph_dsc_t glyph_dsc[] = {
    {.bitmap_index = 0, .adv_w = 0, .box_w = 0, .box_h = 0, .ofs_x = 0, .ofs_y = 0} /* id = 0 reserved */,
    {.bitmap_index = 0, .adv_w = 58, .box_w = 1, .box_h = 1, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 1, .adv_w = 60, .box_w = 2, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 4, .adv_w = 101, .box_w = 4, .box_h = 4, .ofs_x = 1, .ofs_y = 7},
    {.bitmap_index = 6, .adv_w = 187, .box_w = 10, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 20, .adv_w = 162, .box_w = 9, .box_h = 14, .ofs_x = 1, .ofs_y = -1},
    {.bitmap_index = 36, .adv_w = 192, .box_w = 11, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 52, .adv_w = 192, .box_w = 11, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 68, .adv_w = 58, .box_w = 2, .box_h = 4, .ofs_x = 1, .ofs_y = 7},
    {.bitmap_index = 69, .adv_w = 82, .box_w = 3, .box_h = 13, .ofs_x = 1, .ofs_y = -2},
    {.bitmap_index = 74, .adv_w = 82, .box_w = 4, .box_h = 13, .ofs_x = 0, .ofs_y = -2},
    {.bitmap_index = 81, .adv_w = 117, .box_w = 6, .box_h = 5, .ofs_x = 1, .ofs_y = 6},
    {.bitmap_index = 85, .adv_w = 122, .box_w = 6, .box_h = 6, .ofs_x = 1, .ofs_y = 3},
    {.bitmap_index = 90, .adv_w = 62, .box_w = 3, .box_h = 4, .ofs_x = 0, .ofs_y = -2},
    {.bitmap_index = 92, .adv_w = 75, .box_w = 3, .box_h = 1, .ofs_x = 1, .ofs_y = 4},
    {.bitmap_index = 93, .adv_w = 59, .box_w = 2, .box_h = 2, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 94, .adv_w = 74, .box_w = 4, .box_h = 13, .ofs_x = 0, .ofs_y = -2},
    {.bitmap_index = 101, .adv_w = 179, .box_w = 10, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 115, .adv_w = 140, .box_w = 8, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 126, .adv_w = 163, .box_w = 9, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 139, .adv_w = 159, .box_w = 9, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 152, .adv_w = 179, .box_w = 11, .box_h = 11, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 168, .adv_w = 160, .box_w = 8, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 179, .adv_w = 166, .box_w = 9, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 192, .adv_w = 155, .box_w = 9, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 205, .adv_w = 169, .box_w = 9, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 218, .adv_w = 166, .box_w = 9, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 231, .adv_w = 59, .box_w = 2, .box_h = 9, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 234, .adv_w = 63, .box_w = 2, .box_h = 11, .ofs_x = 1, .ofs_y = -2},
    {.bitmap_index = 237, .adv_w = 103, .box_w = 4, .box_h = 7, .ofs_x = 1, .ofs_y = 2},
    {.bitmap_index = 241, .adv_w = 113, .box_w = 6, .box_h = 4, .ofs_x = 1, .ofs_y = 4},
    {.bitmap_index = 244, .adv_w = 103, .box_w = 4, .box_h = 7, .ofs_x = 1, .ofs_y = 2},
    {.bitmap_index = 248, .adv_w = 140, .box_w = 8, .box_h = 11, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 259, .adv_w = 200, .box_w = 10, .box_h = 10, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 272, .adv_w = 193, .box_w = 12, .box_h = 11, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 289, .adv_w = 175, .box_w = 9, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 302, .adv_w = 169, .box_w = 9, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 315, .adv_w = 183, .box_w = 10, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 329, .adv_w = 170, .box_w = 9, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 342, .adv_w = 165, .box_w = 9, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 355, .adv_w = 186, .box_w = 10, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 369, .adv_w = 198, .box_w = 10, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 383, .adv_w = 71, .box_w = 2, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 386, .adv_w = 141, .box_w = 7, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 396, .adv_w = 176, .box_w = 10, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 410, .adv_w = 150, .box_w = 8, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 421, .adv_w = 256, .box_w = 14, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 441, .adv_w = 217, .box_w = 11, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 457, .adv_w = 195, .box_w = 11, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 473, .adv_w = 176, .box_w = 9, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 486, .adv_w = 190, .box_w = 11, .box_h = 13, .ofs_x = 1, .ofs_y = -2},
    {.bitmap_index = 504, .adv_w = 180, .box_w = 9, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 517, .adv_w = 162, .box_w = 9, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 530, .adv_w = 167, .box_w = 10, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 544, .adv_w = 197, .box_w = 10, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 558, .adv_w = 181, .box_w = 11, .box_h = 11, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 574, .adv_w = 276, .box_w = 17, .box_h = 11, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 598, .adv_w = 181, .box_w = 11, .box_h = 11, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 614, .adv_w = 175, .box_w = 12, .box_h = 11, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 631, .adv_w = 158, .box_w = 9, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 644, .adv_w = 82, .box_w = 4, .box_h = 13, .ofs_x = 1, .ofs_y = -2},
    {.bitmap_index = 651, .adv_w = 74, .box_w = 4, .box_h = 13, .ofs_x = 0, .ofs_y = -2},
    {.bitmap_index = 658, .adv_w = 82, .box_w = 4, .box_h = 13, .ofs_x = 0, .ofs_y = -2},
    {.bitmap_index = 665, .adv_w = 158, .box_w = 5, .box_h = 3, .ofs_x = 2, .ofs_y = 5},
    {.bitmap_index = 667, .adv_w = 86, .box_w = 5, .box_h = 1, .ofs_x = 0, .ofs_y = -1},
    {.bitmap_index = 668, .adv_w = 158, .box_w = 3, .box_h = 3, .ofs_x = 3, .ofs_y = 10},
    {.bitmap_index = 670, .adv_w = 153, .box_w = 8, .box_h = 9, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 679, .adv_w = 163, .box_w = 8, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 690, .adv_w = 144, .box_w = 8, .box_h = 9, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 699, .adv_w = 163, .box_w = 8, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 710, .adv_w = 158, .box_w = 8, .box_h = 9, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 719, .adv_w = 104, .box_w = 6, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 728, .adv_w = 158, .box_w = 8, .box_h = 11, .ofs_x = 1, .ofs_y = -2},
    {.bitmap_index = 739, .adv_w = 160, .box_w = 8, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 750, .adv_w = 65, .box_w = 2, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 753, .adv_w = 65, .box_w = 4, .box_h = 13, .ofs_x = -1, .ofs_y = -2},
    {.bitmap_index = 760, .adv_w = 157, .box_w = 9, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 773, .adv_w = 65, .box_w = 2, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 776, .adv_w = 240, .box_w = 12, .box_h = 9, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 790, .adv_w = 160, .box_w = 8, .box_h = 9, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 799, .adv_w = 167, .box_w = 9, .box_h = 9, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 810, .adv_w = 165, .box_w = 8, .box_h = 11, .ofs_x = 1, .ofs_y = -2},
    {.bitmap_index = 821, .adv_w = 163, .box_w = 8, .box_h = 11, .ofs_x = 1, .ofs_y = -2},
    {.bitmap_index = 832, .adv_w = 107, .box_w = 6, .box_h = 9, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 839, .adv_w = 140, .box_w = 8, .box_h = 9, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 848, .adv_w = 110, .box_w = 6, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 857, .adv_w = 160, .box_w = 8, .box_h = 9, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 866, .adv_w = 162, .box_w = 10, .box_h = 9, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 878, .adv_w = 226, .box_w = 14, .box_h = 9, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 894, .adv_w = 155, .box_w = 9, .box_h = 9, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 905, .adv_w = 151, .box_w = 9, .box_h = 11, .ofs_x = 0, .ofs_y = -2},
    {.bitmap_index = 918, .adv_w = 145, .box_w = 8, .box_h = 9, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 927, .adv_w = 82, .box_w = 4, .box_h = 13, .ofs_x = 1, .ofs_y = -2},
    {.bitmap_index = 934, .adv_w = 69, .box_w = 2, .box_h = 12, .ofs_x = 1, .ofs_y = -1},
    {.bitmap_index = 937, .adv_w = 82, .box_w = 5, .box_h = 13, .ofs_x = 0, .ofs_y = -2},
    {.bitmap_index = 946, .adv_w = 193, .box_w = 5, .box_h = 3, .ofs_x = 3, .ofs_y = 5}
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
    0, 0, -16, 0, 0, 0, 0, 0,
    0, -20, -34, -7, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, -7, 0,
    0, -4, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, -4, 0, 0, 0, 0,
    0, 0, -4, -4, -4, 0, 0, -4,
    0, 0, 0, 0, 0, 0, 0, -13,
    -4, -4, 0, 0, -13, 0, 0, 0,
    0, -4, -4, 0, 0, 0, -13, 0,
    -9, -7, -4, -18, -4, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -9,
    -4, -7, -4, -4, 0, 0, 0, 0,
    0, 0, -7, 0, 0, 0, -13, -4,
    -18, -7, -4, 0, 0, 0, 0, 0,
    0, 0, -20, 0, -29, -20, 0, -34,
    0, 0, 0, -4, 0, 0, 0, 0,
    0, 0, 0, -22, -9, 0, -7, 0,
    0, 0, 0, -9, 0, 0, -4, 0,
    0, 0, -4, 0, 0, -4, 0, 0,
    0, -9, -9, -7, -4, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -2,
    0, -2, 0, -4, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, -2, 0,
    -7, -4, 0, 0, -9, -2, 0, 0,
    -13, 0, 0, 0, 0, -4, -9, 0,
    0, 0, -4, 0, -4, -4, -4, -9,
    -2, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, -2, 0, -2, 0, -2,
    -22, 0, 0, -7, 0, 0, -7, 0,
    0, 0, -11, 0, -16, 0, 0, 0,
    0, 0, 0, 0, 0, 0, -20, 0,
    -20, -16, 0, -22, 0, -16, 0, 0,
    0, 0, 0, 0, 0, 0, -2, 0,
    -11, 0, 0, 0, 0, 0, 0, -4,
    -2, 0, -7, 0, 0, 0, -11, 0,
    -4, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, -4, 0, -7, -4, 0, 0,
    0, 0, 0, 0, -9, 0, 0, -4,
    0, -2, 0, 0, 0, 0, -4, 0,
    -9, -9, -4, -9, 0, -2, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, -4, -2, 0, -9, 0, 0, 0,
    -4, 0, 0, 0, 0, -4, 0, 0,
    -16, 0, -4, -4, 0, 0, -4, 0,
    0, 0, -9, 0, -9, -9, 0, -9,
    0, -4, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, -4, 0, 0, 0,
    0, 0, 0, 0, -4, -4, 0, 0,
    0, 0, 0, 0, -7, 0, 0, -4,
    0, 0, -4, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    -2, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, -13, -38, -11, -4, 0,
    -4, 0, -20, 0, 0, -4, 0, 0,
    0, -27, -22, -11, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -9,
    0, -9, 0, -7, -4, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, -4, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -4,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, -4, 0, 0, 0, 0, -16, 0,
    0, -11, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, -7, 0, -7, -4, -4, -4,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    -20, 0, 0, -4, 0, 0, -4, 0,
    0, 0, -7, 0, -13, -2, 0, 0,
    -4, 0, 0, 0, 0, 0, -25, -7,
    -25, -22, 0, -31, 0, -13, 0, -2,
    -2, -2, 0, 0, 0, -4, -2, -16,
    -11, 0, -4, 0, 0, 0, 0, -7,
    0, 0, -7, 0, 0, 0, -11, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, -2, 0, -4, 0, 0,
    0, 0, 0, -9, -9, 0, -4, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -7,
    -4, -4, -2, 0, 0, -4, 0, 0,
    -27, -7, -4, 0, 0, 0, -4, 0,
    -9, 0, 0, 0, 0, -20, -56, 0,
    -9, 0, 0, 0, 0, 0, 0, 0,
    0, 0, -4, -2, 0, -2, 0, -2,
    -2, 0, 0, 0, 0, -4, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, -2, -2, 0, 0, 0, -4, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -4,
    0, -2, -4, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, -7, 0, -2,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, -9, 0,
    0, 0, -13, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -7,
    -4, -7, 0, 0, 0, 0, -9, -9,
    -9, 0, -7, -2, -43, 0, 0, -9,
    0, 0, -7, 0, 0, 0, -9, 0,
    -22, 0, 0, 0, 0, 0, 0, 0,
    0, 0, -36, -7, -31, -27, 0, -40,
    0, -7, 0, -4, -4, -4, 0, 0,
    0, -7, -4, -29, -20, 0, -11, 0,
    -7, 0, 0, 0, 0, 0, -2, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, -13, 0,
    -13, -13, 0, -18, 0, -4, 0, -2,
    0, 0, 0, 0, 0, 0, -2, 0,
    -4, 0, 0, 0, 0, 0, 0, 0,
    0, -4, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, -2, -4, 0,
    0, 0, -4, 0, -7, -4, 0, -7,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, -2, 0, 0,
    0, 0, 0, -9, -27, -16, 0, 0,
    0, 0, -9, 0, 0, -4, 0, 0,
    0, -22, -56, -11, 0, -2, 0, 0,
    -4, -4, -9, -7, -9, 0, 0, -7,
    0, -4, 0, -4, -2, 0, 0, 0,
    0, -4, 0, 0, 0, 0, 0, -4,
    0, 0, -2, 0, 0, 0, -7, 0,
    0, 0, 0, 0, 0, 0, -9, 0,
    0, 0, 0, 0, -4, -7, 0, -7,
    0, 0, 0, -3, 0, -4, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, -2, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, -2, -2, 0, 0, 0, -9, 0,
    0, 0, 0, 0, -2, 0, 0, 0,
    0, 0, 0, 0, -4, 0, 0, -7,
    -4, -2, -4, 0, 0, 0, 0, -16,
    -20, -13, -4, 0, 0, 0, -27, 0,
    0, -4, 0, 0, -16, -25, -40, -13,
    -4, -2, 0, 0, 0, 0, 0, 0,
    0, 0, -7, -18, 0, -16, -16, -18,
    -13, 0, -16, -11, -2, -4, -4, -13,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, -7, -7, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -9,
    -29, -11, -4, 0, 0, 0, -11, 0,
    0, -7, 0, 0, 0, -25, -36, -13,
    -7, -2, 0, 0, 0, 0, 0, 0,
    -4, 0, -7, -13, -2, -13, -11, -11,
    -11, 0, -4, 0, 0, -7, 0, -9,
    0, 0, 0, -7, -20, -11, -4, 0,
    0, -4, -16, 0, 0, -4, 0, 0,
    -11, -22, -29, -13, -4, -4, 0, 0,
    0, 0, 0, 0, -2, 0, -7, -11,
    -2, -11, -7, -11, -9, 0, -4, 0,
    0, -4, 0, -7, 0, 0, 0, -4,
    0, 0, -4, 0, 0, 0, -4, 0,
    0, -4, 0, 0, 0, 0, 0, 0,
    -2, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, -7, 0, -9, 0, -2,
    0, 0, 0, -9, -4, 0, -2, 0,
    0, 0, 0, -18, -34, -13, -9, 0,
    0, 0, -22, 0, 0, -7, 0, -4,
    0, -29, -40, -18, -7, -4, 0, 0,
    0, 0, 0, 0, 0, 0, -7, -20,
    -4, -18, -11, -20, -16, 0, -9, -7,
    -4, -7, -4, -11, 0, 0, 0, -4,
    0, 0, -2, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, -2, 0, 0, -2, 0, 0, -2,
    0, 0, 0, -4, 0, -4, 0, 0,
    -4, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, -4, 0,
    0, -4, -4, 0, -11, -2, 0, 0,
    0, 0, 0, 0, 0, 0, -4, 0,
    -16, -11, 0, -13, 0, 0, 0, 0,
    0, -2, 0, 0, 0, 0, 0, -11,
    -4, 0, 0, 0, -4, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, -18, 0, -16, -11, 0, -18,
    0, -4, 0, 0, 0, 0, 0, 0,
    0, 0, 0, -9, -7, 0, -7, 0,
    -2, 0, -4, 0, -4, -2, 0, 0,
    0, 0, 0, 0, -9, 0, 0, 0,
    0, -2, -4, 0, 0, 0, -18, 0,
    -13, -9, -7, -18, -4, -4, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -2,
    -2, -4, -4, -4, 0, 0, 0, 0,
    0, 0, -2, 0, 0, 0, -7, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, -4, 0, -2, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, -7, 0, 0,
    0, 0, -9, 0, 0, 0, 0, 0,
    0, -13, -29, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -4,
    0, -2, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -9,
    0, 0, -4, 0, 0, 0, -9, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, -9, 0, -9, -7, 0, -7,
    0, 0, 0, -9, 0, -7, 0, 0,
    -7, 0, 0, 0, 0, 0, 0, -4,
    0, 0, 0, 0, -20, 0, 0, 0,
    0, 0, -9, 0, 0, 0, 0, 0,
    0, -16, -29, 0, 0, 0, -9, 0,
    0, 0, 0, -4, 0, 0, 0, -4,
    4, -2, 0, 0, 0, 4, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, -9, 0, -7, -9, 0, -9,
    -2, 0, 0, 0, 0, -2, 0, 0,
    -3, 0, 0, -2, 0, 0, 0, -2,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, -4, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -4,
    0, -2, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -9,
    -22, -4, -2, 0, 0, 0, -4, 0,
    0, 0, 0, 0, 0, -11, -22, 0,
    0, 0, -11, 0, 0, 0, -9, 0,
    -9, 0, 0, -2, 0, -2, 0, -7,
    -7, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, -4, -9, -4, 0, 0,
    0, 0, -7, 0, 0, 0, 0, 0,
    0, -11, -20, 0, 0, 0, -2, 0,
    0, 0, -4, 0, -4, 0, 0, -2,
    0, -2, 0, -2, -4, 0, 0, 0,
    0, 0, 0, -2, 0, 0, 0, -7,
    0, 0, -2, 0, 0, 0, -7, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, -4, 0, -7, -4, 0, -7,
    0, 0, 0, -4, 0, -2, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, -4, -13, -4, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, -11, -11, 0, 0, 0, -4, 0,
    0, 0, -2, 0, -4, 0, 0, -4,
    0, -2, 0, -4, -2, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -4,
    0, 0, -2, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, -13, 0, -16, -7, 0, -11,
    0, -7, 0, -7, 0, -4, 0, 0,
    -2, 0, 0, -4, -4, 0, -2, 0
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
const lv_font_t ui_font_F1R14 = {
#else
lv_font_t ui_font_F1R14 = {
#endif
    .get_glyph_dsc = lv_font_get_glyph_dsc_fmt_txt,    /*Function pointer to get glyph's data*/
    .get_glyph_bitmap = lv_font_get_bitmap_fmt_txt,    /*Function pointer to get glyph's bitmap*/
    .line_height = 15,          /*The maximum line height required by the font*/
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



#endif /*#if UI_FONT_F1R14*/

