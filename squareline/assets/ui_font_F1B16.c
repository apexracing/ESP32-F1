/*******************************************************************************
 * Size: 16 px
 * Bpp: 1
 * Opts: --bpp 1 --size 16 --font F:/ESP32/squareline/assets/Formula1-Bold.otf -o F:/ESP32/squareline/assets\ui_font_F1B16.c --format lvgl -r 0x20-0x7f --no-compress --no-prefilter
 ******************************************************************************/

#include "../ui.h"

#ifndef UI_FONT_F1B16
#define UI_FONT_F1B16 1
#endif

#if UI_FONT_F1B16

/*-----------------
 *    BITMAPS
 *----------------*/

/*Store the image of the glyphs*/
static LV_ATTRIBUTE_LARGE_CONST const uint8_t glyph_bitmap[] = {
    /* U+0020 " " */
    0x0,

    /* U+0021 "!" */
    0xff, 0xff, 0xf8, 0x1f, 0xf0,

    /* U+0022 "\"" */
    0xff, 0x7d, 0xf7,

    /* U+0023 "#" */
    0xe, 0xe0, 0xcc, 0x7f, 0xf7, 0xff, 0x19, 0xc1,
    0x98, 0x39, 0x8f, 0xfe, 0xff, 0xe3, 0x30, 0x73,
    0x7, 0x70,

    /* U+0024 "$" */
    0x6, 0x0, 0xc0, 0xff, 0xbf, 0xf7, 0x61, 0xec,
    0x1f, 0x83, 0xfc, 0x1f, 0xe0, 0xfc, 0x1b, 0x83,
    0x77, 0xfc, 0xff, 0x1, 0x80,

    /* U+0025 "%" */
    0x78, 0x6f, 0xce, 0xcc, 0xef, 0xdc, 0x79, 0xc0,
    0x0, 0x1, 0xe3, 0xbf, 0x3b, 0x37, 0x33, 0x73,
    0xf6, 0x1e,

    /* U+0026 "&" */
    0x1f, 0xc3, 0xfc, 0x38, 0x3, 0x80, 0x3c, 0x3,
    0xe7, 0xfe, 0xef, 0x7c, 0xe3, 0xce, 0x3c, 0xff,
    0xe7, 0xef,

    /* U+0027 "'" */
    0xfb, 0x60,

    /* U+0028 "(" */
    0x3f, 0xf9, 0xce, 0x73, 0x9c, 0xe7, 0x39, 0xcf,
    0x9c,

    /* U+0029 ")" */
    0xf7, 0xce, 0x73, 0x9c, 0xe7, 0x39, 0xce, 0x7f,
    0xf8,

    /* U+002A "*" */
    0x49, 0xef, 0xff, 0x79, 0x20,

    /* U+002B "+" */
    0x38, 0x38, 0x38, 0xff, 0xff, 0x38, 0x38, 0x38,

    /* U+002C "," */
    0x77, 0x77, 0x60,

    /* U+002D "-" */
    0xff, 0xf0,

    /* U+002E "." */
    0xff, 0x80,

    /* U+002F "/" */
    0x1c, 0x71, 0xc6, 0x38, 0xe3, 0x8c, 0x71, 0xc7,
    0x18, 0x63, 0x80,

    /* U+0030 "0" */
    0x1f, 0x87, 0xfe, 0x70, 0xee, 0x7, 0xe0, 0x7e,
    0x7, 0xe0, 0x7e, 0x7, 0xe0, 0x77, 0xe, 0x7f,
    0xe1, 0xf8,

    /* U+0031 "1" */
    0xf8, 0x7e, 0x7, 0x3, 0x81, 0xc0, 0xe0, 0x70,
    0x38, 0x1c, 0xe, 0x3f, 0xff, 0xf0,

    /* U+0032 "2" */
    0xff, 0x3f, 0xf0, 0x1c, 0xf, 0x7, 0xc7, 0xe7,
    0xf1, 0xf0, 0xf0, 0x38, 0xf, 0xff, 0xff,

    /* U+0033 "3" */
    0xff, 0xff, 0xf0, 0x78, 0x3c, 0x1e, 0xf, 0xe3,
    0xfc, 0x7, 0x1, 0xc0, 0x7f, 0xff, 0xfc,

    /* U+0034 "4" */
    0x3, 0xc0, 0x3f, 0x3, 0xf8, 0x3d, 0xc3, 0xce,
    0x1e, 0x71, 0xe3, 0x8e, 0x1c, 0x7f, 0xfb, 0xff,
    0xc0, 0x38, 0x1, 0xc0,

    /* U+0035 "5" */
    0xff, 0xff, 0xfe, 0x3, 0x80, 0xff, 0x3f, 0xf0,
    0x1c, 0x7, 0x1, 0xc0, 0x7f, 0xfb, 0xfc,

    /* U+0036 "6" */
    0x1f, 0xef, 0xfd, 0xc0, 0x70, 0xe, 0x1, 0xff,
    0x3f, 0xff, 0x7, 0xe0, 0xfc, 0x1d, 0xff, 0x1f,
    0xc0,

    /* U+0037 "7" */
    0xff, 0xbf, 0xf0, 0x1c, 0xf, 0x3, 0x81, 0xe0,
    0xf0, 0x38, 0x1e, 0x7, 0x3, 0xc0, 0xe0,

    /* U+0038 "8" */
    0x3f, 0x9f, 0xff, 0x83, 0xf0, 0x7e, 0xe, 0xff,
    0x9f, 0xf7, 0x7, 0xe0, 0xfc, 0x1f, 0xff, 0x9f,
    0xc0,

    /* U+0039 "9" */
    0x3f, 0xf, 0xfb, 0x83, 0xf0, 0x7e, 0xf, 0xff,
    0xcf, 0xf8, 0x7, 0x0, 0xe0, 0x3b, 0xff, 0x7f,
    0x80,

    /* U+003A ":" */
    0xff, 0x80,

    /* U+003B ";" */
    0x77, 0x77, 0x60,

    /* U+003C "<" */
    0xc, 0xf7, 0xb8, 0xf1, 0xf1, 0xc3,

    /* U+003D "=" */
    0xff, 0xfc, 0x0, 0xf, 0xff, 0xc0,

    /* U+003E ">" */
    0xc3, 0x8f, 0x8e, 0x7b, 0xce, 0x20,

    /* U+003F "?" */
    0xfe, 0x7f, 0x80, 0xe0, 0x70, 0x39, 0xf8, 0xf8,
    0x0, 0x0, 0x1c, 0xe, 0x7, 0x0,

    /* U+0040 "@" */
    0xff, 0x8f, 0xfe, 0x0, 0xf0, 0x7, 0x7f, 0x7f,
    0xf7, 0xe7, 0x7e, 0x77, 0xe7, 0x7f, 0xff, 0x7f,
    0xf0,

    /* U+0041 "A" */
    0x7, 0x80, 0x1f, 0x0, 0xfc, 0x3, 0xb8, 0x1c,
    0xe0, 0x73, 0x83, 0x87, 0xf, 0xfc, 0x3f, 0xf9,
    0xc0, 0xe7, 0x3, 0xf8, 0x7,

    /* U+0042 "B" */
    0xff, 0x9f, 0xff, 0x83, 0xf0, 0x7e, 0xf, 0xff,
    0xbf, 0xf7, 0x7, 0xe0, 0xfc, 0x1f, 0xff, 0xff,
    0xe0,

    /* U+0043 "C" */
    0x1f, 0xef, 0xfd, 0xc0, 0x70, 0xe, 0x1, 0xc0,
    0x38, 0x7, 0x0, 0xe0, 0xe, 0x1, 0xff, 0x8f,
    0xf0,

    /* U+0044 "D" */
    0xff, 0x8f, 0xfe, 0xe0, 0xee, 0x7, 0xe0, 0x7e,
    0x7, 0xe0, 0x7e, 0x7, 0xe0, 0x7e, 0xe, 0xff,
    0xef, 0xf8,

    /* U+0045 "E" */
    0xff, 0xff, 0xfe, 0x3, 0x80, 0xe0, 0x3f, 0xff,
    0xff, 0x80, 0xe0, 0x38, 0xf, 0xff, 0xff,

    /* U+0046 "F" */
    0xff, 0xff, 0xfe, 0x3, 0x80, 0xe0, 0x3f, 0xff,
    0xff, 0x80, 0xe0, 0x38, 0xe, 0x3, 0x80,

    /* U+0047 "G" */
    0x1f, 0xf7, 0xff, 0x70, 0xe, 0x0, 0xe0, 0xe,
    0x3f, 0xe3, 0xfe, 0x7, 0xe0, 0x77, 0x7, 0x7f,
    0xe1, 0xfc,

    /* U+0048 "H" */
    0xe0, 0x7e, 0x7, 0xe0, 0x7e, 0x7, 0xff, 0xff,
    0xff, 0xff, 0xfe, 0x7, 0xe0, 0x7e, 0x7, 0xe0,
    0x7e, 0x7,

    /* U+0049 "I" */
    0xff, 0xff, 0xff, 0xff, 0xf0,

    /* U+004A "J" */
    0x7, 0x7, 0x7, 0x7, 0x7, 0x7, 0x7, 0x7,
    0x7, 0x7, 0xfe, 0xfc,

    /* U+004B "K" */
    0xe1, 0xee, 0x1c, 0xe3, 0x8e, 0x70, 0xff, 0xf,
    0xe0, 0xff, 0xe, 0x70, 0xe7, 0x8e, 0x3c, 0xe1,
    0xee, 0xe,

    /* U+004C "L" */
    0xe0, 0x38, 0xe, 0x3, 0x80, 0xe0, 0x38, 0xe,
    0x3, 0x80, 0xe0, 0x38, 0xf, 0xff, 0xff,

    /* U+004D "M" */
    0x38, 0x1e, 0x3e, 0x1f, 0xbf, 0x8f, 0xdd, 0xc7,
    0xee, 0xe7, 0x77, 0x73, 0xbb, 0x9d, 0xdd, 0xce,
    0xef, 0xe7, 0x77, 0xf3, 0xf3, 0xf9, 0xf9, 0xfc,
    0x78, 0xf0,

    /* U+004E "N" */
    0x78, 0x3f, 0xe1, 0xff, 0x8f, 0xdc, 0x7e, 0xf3,
    0xf3, 0x9f, 0x9c, 0xfc, 0xf7, 0xe3, 0xbf, 0x1f,
    0xf8, 0x7f, 0xc1, 0xe0,

    /* U+004F "O" */
    0x1f, 0xc3, 0xff, 0x9c, 0x1d, 0xc0, 0x7e, 0x3,
    0xf0, 0x1f, 0x80, 0xfc, 0x7, 0xe0, 0x3b, 0x83,
    0x9f, 0xfc, 0x3f, 0x80,

    /* U+0050 "P" */
    0xff, 0x9f, 0xfb, 0x83, 0xf0, 0x7e, 0xf, 0xc1,
    0xff, 0xff, 0xfc, 0xe0, 0x1c, 0x3, 0x80, 0x70,
    0x0,

    /* U+0051 "Q" */
    0x1f, 0xc3, 0xff, 0x9c, 0x1d, 0xc0, 0x7e, 0x3,
    0xf0, 0x1f, 0x80, 0xfc, 0x7, 0xe0, 0x3b, 0x83,
    0x9f, 0xfc, 0x3f, 0x80, 0x3c, 0x0, 0xf0,

    /* U+0052 "R" */
    0xff, 0xdf, 0xff, 0x83, 0xf0, 0x7e, 0xf, 0xdf,
    0xfb, 0xe7, 0x70, 0xe7, 0x1c, 0xf3, 0x8f, 0x70,
    0xf0,

    /* U+0053 "S" */
    0x3f, 0xcf, 0xfb, 0x80, 0x78, 0xf, 0xe0, 0xff,
    0xf, 0xf0, 0x3e, 0x1, 0xc0, 0x1b, 0xff, 0x7f,
    0x80,

    /* U+0054 "T" */
    0xff, 0xff, 0xff, 0x7, 0x0, 0x70, 0x7, 0x0,
    0x70, 0x7, 0x0, 0x70, 0x7, 0x0, 0x70, 0x7,
    0x0, 0x70,

    /* U+0055 "U" */
    0xe0, 0x7e, 0x7, 0xe0, 0x7e, 0x7, 0xe0, 0x7e,
    0x7, 0xe0, 0x7e, 0x7, 0xe0, 0x7e, 0x7, 0x7f,
    0xe3, 0xfc,

    /* U+0056 "V" */
    0xf0, 0x7b, 0x83, 0x9c, 0x1c, 0xf0, 0xe3, 0x8e,
    0x1c, 0x70, 0xf3, 0x83, 0xb8, 0x1d, 0xc0, 0xfe,
    0x3, 0xe0, 0xe, 0x0,

    /* U+0057 "W" */
    0xf0, 0xf0, 0xfe, 0x3e, 0x1d, 0xc7, 0xe3, 0xb9,
    0xdc, 0x77, 0x3b, 0x9c, 0xe7, 0x73, 0x9c, 0xe7,
    0x71, 0xdc, 0xee, 0x3b, 0x9d, 0xc7, 0xe3, 0xb8,
    0xfc, 0x3e, 0xf, 0x7, 0x80,

    /* U+0058 "X" */
    0x70, 0x7b, 0xc3, 0x8f, 0x38, 0x3b, 0xc1, 0xfc,
    0x7, 0xc0, 0x3e, 0x1, 0xf8, 0x1d, 0xe1, 0xe7,
    0x1e, 0x1c, 0xe0, 0xf0,

    /* U+0059 "Y" */
    0x70, 0x73, 0xc7, 0x8e, 0x38, 0x7b, 0xc1, 0xfc,
    0x7, 0xc0, 0x3e, 0x0, 0xe0, 0x7, 0x0, 0x38,
    0x1, 0xc0, 0xe, 0x0,

    /* U+005A "Z" */
    0xff, 0x9f, 0xf8, 0x3, 0x1, 0xe0, 0xfc, 0x3f,
    0x1f, 0xc7, 0xe0, 0xf0, 0x1c, 0x3, 0xff, 0xbf,
    0xf0,

    /* U+005B "[" */
    0xff, 0xf9, 0xce, 0x73, 0x9c, 0xe7, 0x39, 0xcf,
    0xfc,

    /* U+005C "\\" */
    0xe3, 0x86, 0x1c, 0x71, 0xc3, 0xe, 0x38, 0xe1,
    0x87, 0x1c, 0x70,

    /* U+005D "]" */
    0xff, 0xce, 0x73, 0x9c, 0xe7, 0x39, 0xce, 0x7f,
    0xfc,

    /* U+005E "^" */
    0x71, 0xed, 0x80,

    /* U+005F "_" */
    0xff, 0xff, 0xf8,

    /* U+0060 "`" */
    0x66, 0x70,

    /* U+0061 "a" */
    0xff, 0x3f, 0xe0, 0x7c, 0x3f, 0x3f, 0xdf, 0x77,
    0x1f, 0xc7, 0x7f, 0xcf, 0xf0,

    /* U+0062 "b" */
    0xe0, 0x1c, 0x3, 0xfe, 0x7f, 0xee, 0xf, 0xc1,
    0xf8, 0x3f, 0x7, 0xe0, 0xfc, 0x1f, 0xff, 0x7f,
    0xc0,

    /* U+0063 "c" */
    0x3f, 0xbf, 0xf8, 0x1c, 0xe, 0x7, 0x3, 0x81,
    0xc0, 0x7f, 0x9f, 0xc0,

    /* U+0064 "d" */
    0x0, 0xe0, 0x1c, 0xff, 0xbf, 0xfe, 0xf, 0xc1,
    0xf8, 0x3f, 0x7, 0xe0, 0xfc, 0x1d, 0xff, 0x9f,
    0xf0,

    /* U+0065 "e" */
    0x3f, 0x1f, 0xee, 0x1f, 0x87, 0xff, 0xff, 0xfe,
    0x3, 0x80, 0x7f, 0xcf, 0xf0,

    /* U+0066 "f" */
    0x1e, 0x7c, 0xe7, 0xff, 0xe7, 0xe, 0x1c, 0x38,
    0x70, 0xe1, 0xc3, 0x80,

    /* U+0067 "g" */
    0x3f, 0xdf, 0xfe, 0x1f, 0x87, 0xe1, 0xf8, 0x77,
    0xfc, 0xff, 0x1, 0xc0, 0x77, 0xf9, 0xfc,

    /* U+0068 "h" */
    0xe0, 0x38, 0xf, 0xf3, 0xfe, 0xe1, 0xf8, 0x7e,
    0x1f, 0x87, 0xe1, 0xf8, 0x7e, 0x1f, 0x87,

    /* U+0069 "i" */
    0xff, 0xff, 0xff, 0xff, 0xf0,

    /* U+006A "j" */
    0x39, 0xce, 0x73, 0x9c, 0xe7, 0x39, 0xce, 0x7f,
    0xf8,

    /* U+006B "k" */
    0xe0, 0x38, 0xe, 0x3f, 0x8e, 0xe7, 0x3b, 0xcf,
    0xe3, 0xf8, 0xef, 0x39, 0xce, 0x3b, 0x8f,

    /* U+006C "l" */
    0xff, 0xff, 0xff, 0xff, 0xf0,

    /* U+006D "m" */
    0xff, 0xf9, 0xff, 0xfb, 0x8e, 0x3f, 0x1c, 0x7e,
    0x38, 0xfc, 0x71, 0xf8, 0xe3, 0xf1, 0xc7, 0xe3,
    0x8f, 0xc7, 0x1c,

    /* U+006E "n" */
    0xff, 0x3f, 0xee, 0x1f, 0x87, 0xe1, 0xf8, 0x7e,
    0x1f, 0x87, 0xe1, 0xf8, 0x70,

    /* U+006F "o" */
    0x3f, 0x1f, 0xee, 0x1f, 0x87, 0xe1, 0xf8, 0x7e,
    0x1f, 0x87, 0x7f, 0x8f, 0xc0,

    /* U+0070 "p" */
    0xff, 0x9f, 0xfb, 0x83, 0xf0, 0x7e, 0xf, 0xc1,
    0xf8, 0x3f, 0xf, 0xff, 0xdf, 0xf3, 0x80, 0x70,
    0x0,

    /* U+0071 "q" */
    0x3f, 0xef, 0xff, 0x83, 0xf0, 0x7e, 0xf, 0xc1,
    0xf8, 0x3f, 0x7, 0x7f, 0xe7, 0xfc, 0x3, 0x80,
    0x70,

    /* U+0072 "r" */
    0x3e, 0xff, 0x87, 0xe, 0x1c, 0x38, 0x70, 0xe1,
    0xc0,

    /* U+0073 "s" */
    0x7f, 0xff, 0xf8, 0x1f, 0xf, 0xf3, 0xfc, 0x3e,
    0x3, 0xff, 0xff, 0x80,

    /* U+0074 "t" */
    0x70, 0x70, 0xff, 0xff, 0x70, 0x70, 0x70, 0x70,
    0x70, 0x70, 0x7f, 0x3f,

    /* U+0075 "u" */
    0xe1, 0xf8, 0x7e, 0x1f, 0x87, 0xe1, 0xf8, 0x7e,
    0x1f, 0x87, 0x7f, 0xcf, 0xf0,

    /* U+0076 "v" */
    0xe0, 0xee, 0x1d, 0xc3, 0xb8, 0xe3, 0x9c, 0x73,
    0xe, 0xe0, 0xfc, 0x1f, 0x1, 0xe0,

    /* U+0077 "w" */
    0xe1, 0xc3, 0xb9, 0xf1, 0xdc, 0xfc, 0xce, 0x6e,
    0x67, 0x77, 0x73, 0xbb, 0xb9, 0xdd, 0xdc, 0x6e,
    0x6e, 0x3e, 0x3e, 0xe, 0xf, 0x0,

    /* U+0078 "x" */
    0x70, 0xe7, 0x9c, 0x3b, 0xc1, 0xf8, 0xf, 0x0,
    0xf0, 0x1f, 0x83, 0xbc, 0x39, 0xc7, 0xe,

    /* U+0079 "y" */
    0xf0, 0xee, 0x1d, 0xc7, 0x3c, 0xe3, 0x9c, 0x77,
    0x7, 0xe0, 0xfc, 0x7, 0x0, 0xe1, 0xf8, 0x3e,
    0x0,

    /* U+007A "z" */
    0xff, 0x7f, 0xc0, 0xe1, 0xf7, 0xff, 0xfb, 0xe1,
    0xc0, 0xff, 0xbf, 0xc0,

    /* U+007B "{" */
    0x1e, 0x7c, 0xe1, 0xc3, 0x9f, 0x3e, 0x1c, 0x38,
    0x70, 0xe1, 0xc3, 0xe3, 0xc0,

    /* U+007C "|" */
    0xff, 0xff, 0xff, 0xff, 0xff, 0xc0,

    /* U+007D "}" */
    0xf3, 0xe3, 0x8e, 0x38, 0xf3, 0xce, 0x38, 0xe3,
    0x8e, 0xfb, 0xc0,

    /* U+007E "~" */
    0xe7, 0xff, 0x38
};


/*---------------------
 *  GLYPH DESCRIPTION
 *--------------------*/

static const lv_font_fmt_txt_glyph_dsc_t glyph_dsc[] = {
    {.bitmap_index = 0, .adv_w = 0, .box_w = 0, .box_h = 0, .ofs_x = 0, .ofs_y = 0} /* id = 0 reserved */,
    {.bitmap_index = 0, .adv_w = 61, .box_w = 1, .box_h = 1, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 1, .adv_w = 86, .box_w = 3, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 6, .adv_w = 138, .box_w = 6, .box_h = 4, .ofs_x = 1, .ofs_y = 8},
    {.bitmap_index = 9, .adv_w = 213, .box_w = 12, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 27, .adv_w = 193, .box_w = 11, .box_h = 15, .ofs_x = 0, .ofs_y = -1},
    {.bitmap_index = 48, .adv_w = 217, .box_w = 12, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 66, .adv_w = 208, .box_w = 12, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 84, .adv_w = 79, .box_w = 3, .box_h = 4, .ofs_x = 1, .ofs_y = 8},
    {.bitmap_index = 86, .adv_w = 114, .box_w = 5, .box_h = 14, .ofs_x = 1, .ofs_y = -2},
    {.bitmap_index = 95, .adv_w = 114, .box_w = 5, .box_h = 14, .ofs_x = 0, .ofs_y = -2},
    {.bitmap_index = 104, .adv_w = 134, .box_w = 6, .box_h = 6, .ofs_x = 1, .ofs_y = 6},
    {.bitmap_index = 109, .adv_w = 150, .box_w = 8, .box_h = 8, .ofs_x = 1, .ofs_y = 2},
    {.bitmap_index = 117, .adv_w = 73, .box_w = 4, .box_h = 5, .ofs_x = 0, .ofs_y = -2},
    {.bitmap_index = 120, .adv_w = 94, .box_w = 4, .box_h = 3, .ofs_x = 1, .ofs_y = 3},
    {.bitmap_index = 122, .adv_w = 84, .box_w = 3, .box_h = 3, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 124, .adv_w = 100, .box_w = 6, .box_h = 14, .ofs_x = 0, .ofs_y = -2},
    {.bitmap_index = 135, .adv_w = 216, .box_w = 12, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 153, .adv_w = 162, .box_w = 9, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 167, .adv_w = 177, .box_w = 10, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 182, .adv_w = 183, .box_w = 10, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 197, .adv_w = 209, .box_w = 13, .box_h = 12, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 217, .adv_w = 182, .box_w = 10, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 232, .adv_w = 196, .box_w = 11, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 249, .adv_w = 176, .box_w = 10, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 264, .adv_w = 192, .box_w = 11, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 281, .adv_w = 196, .box_w = 11, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 298, .adv_w = 84, .box_w = 3, .box_h = 3, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 300, .adv_w = 76, .box_w = 4, .box_h = 5, .ofs_x = 0, .ofs_y = -2},
    {.bitmap_index = 303, .adv_w = 121, .box_w = 6, .box_h = 8, .ofs_x = 1, .ofs_y = 2},
    {.bitmap_index = 309, .adv_w = 135, .box_w = 7, .box_h = 6, .ofs_x = 1, .ofs_y = 4},
    {.bitmap_index = 315, .adv_w = 121, .box_w = 6, .box_h = 8, .ofs_x = 1, .ofs_y = 2},
    {.bitmap_index = 321, .adv_w = 160, .box_w = 9, .box_h = 12, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 335, .adv_w = 215, .box_w = 12, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 352, .adv_w = 228, .box_w = 14, .box_h = 12, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 373, .adv_w = 204, .box_w = 11, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 390, .adv_w = 185, .box_w = 11, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 407, .adv_w = 218, .box_w = 12, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 425, .adv_w = 191, .box_w = 10, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 440, .adv_w = 183, .box_w = 10, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 455, .adv_w = 219, .box_w = 12, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 473, .adv_w = 227, .box_w = 12, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 491, .adv_w = 87, .box_w = 3, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 496, .adv_w = 162, .box_w = 8, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 508, .adv_w = 206, .box_w = 12, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 526, .adv_w = 173, .box_w = 10, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 541, .adv_w = 297, .box_w = 17, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 567, .adv_w = 249, .box_w = 13, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 587, .adv_w = 224, .box_w = 13, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 607, .adv_w = 199, .box_w = 11, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 624, .adv_w = 224, .box_w = 13, .box_h = 14, .ofs_x = 1, .ofs_y = -2},
    {.bitmap_index = 647, .adv_w = 207, .box_w = 11, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 664, .adv_w = 193, .box_w = 11, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 681, .adv_w = 210, .box_w = 12, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 699, .adv_w = 218, .box_w = 12, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 717, .adv_w = 207, .box_w = 13, .box_h = 12, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 737, .adv_w = 312, .box_w = 19, .box_h = 12, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 766, .adv_w = 216, .box_w = 13, .box_h = 12, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 786, .adv_w = 205, .box_w = 13, .box_h = 12, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 806, .adv_w = 184, .box_w = 11, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 823, .adv_w = 112, .box_w = 5, .box_h = 14, .ofs_x = 1, .ofs_y = -2},
    {.bitmap_index = 832, .adv_w = 100, .box_w = 6, .box_h = 14, .ofs_x = 0, .ofs_y = -2},
    {.bitmap_index = 843, .adv_w = 112, .box_w = 5, .box_h = 14, .ofs_x = 0, .ofs_y = -2},
    {.bitmap_index = 852, .adv_w = 181, .box_w = 6, .box_h = 3, .ofs_x = 3, .ofs_y = 5},
    {.bitmap_index = 855, .adv_w = 114, .box_w = 7, .box_h = 3, .ofs_x = 0, .ofs_y = -3},
    {.bitmap_index = 858, .adv_w = 181, .box_w = 4, .box_h = 3, .ofs_x = 3, .ofs_y = 11},
    {.bitmap_index = 860, .adv_w = 175, .box_w = 10, .box_h = 10, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 873, .adv_w = 194, .box_w = 11, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 890, .adv_w = 159, .box_w = 9, .box_h = 10, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 902, .adv_w = 194, .box_w = 11, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 919, .adv_w = 179, .box_w = 10, .box_h = 10, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 932, .adv_w = 126, .box_w = 7, .box_h = 13, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 944, .adv_w = 189, .box_w = 10, .box_h = 12, .ofs_x = 1, .ofs_y = -2},
    {.bitmap_index = 959, .adv_w = 189, .box_w = 10, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 974, .adv_w = 84, .box_w = 3, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 979, .adv_w = 81, .box_w = 5, .box_h = 14, .ofs_x = -1, .ofs_y = -2},
    {.bitmap_index = 988, .adv_w = 183, .box_w = 10, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 1003, .adv_w = 84, .box_w = 3, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 1008, .adv_w = 279, .box_w = 15, .box_h = 10, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 1027, .adv_w = 189, .box_w = 10, .box_h = 10, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 1040, .adv_w = 186, .box_w = 10, .box_h = 10, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 1053, .adv_w = 194, .box_w = 11, .box_h = 12, .ofs_x = 1, .ofs_y = -2},
    {.bitmap_index = 1070, .adv_w = 194, .box_w = 11, .box_h = 12, .ofs_x = 1, .ofs_y = -2},
    {.bitmap_index = 1087, .adv_w = 123, .box_w = 7, .box_h = 10, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 1096, .adv_w = 163, .box_w = 9, .box_h = 10, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 1108, .adv_w = 139, .box_w = 8, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 1120, .adv_w = 189, .box_w = 10, .box_h = 10, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 1133, .adv_w = 185, .box_w = 11, .box_h = 10, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 1147, .adv_w = 274, .box_w = 17, .box_h = 10, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 1169, .adv_w = 189, .box_w = 12, .box_h = 10, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 1184, .adv_w = 184, .box_w = 11, .box_h = 12, .ofs_x = 0, .ofs_y = -2},
    {.bitmap_index = 1201, .adv_w = 171, .box_w = 9, .box_h = 10, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 1213, .adv_w = 104, .box_w = 7, .box_h = 14, .ofs_x = 0, .ofs_y = -2},
    {.bitmap_index = 1226, .adv_w = 79, .box_w = 3, .box_h = 14, .ofs_x = 1, .ofs_y = -2},
    {.bitmap_index = 1232, .adv_w = 104, .box_w = 6, .box_h = 14, .ofs_x = 0, .ofs_y = -2},
    {.bitmap_index = 1243, .adv_w = 220, .box_w = 7, .box_h = 3, .ofs_x = 4, .ofs_y = 5}
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
    0, -28, -38, -8, 0, 0, 0, 0,
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
    0, -8, -5, 0, 0, 0, -15, 0,
    -10, -8, -5, -20, -5, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -10,
    -5, -8, -5, -5, 0, 0, 0, 0,
    0, 0, -8, 0, 0, 0, -15, -5,
    -20, -8, -5, 0, 0, 0, 0, 0,
    0, 0, -23, 0, -33, -10, 0, -38,
    0, 0, 0, -5, 0, 0, 0, 0,
    0, 0, 0, -26, -10, 0, -8, 0,
    0, 0, 0, -10, 0, 0, -5, 0,
    0, 0, -5, 0, 0, -5, 0, 0,
    0, -10, -10, -8, -5, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -8,
    0, -3, 0, -5, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, -3, 0,
    -8, -5, 0, -3, -5, -13, 0, 0,
    -15, 0, -5, 0, 0, -13, -10, 0,
    0, -8, -10, 0, -5, -3, -13, -18,
    -3, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, -3, 0, -5, 0, -3,
    -26, 0, 0, -8, 0, 0, -8, 0,
    0, 0, -13, 0, -18, 0, 0, 0,
    0, 0, 0, 0, 0, 0, -23, 0,
    -23, -18, 0, -26, 0, -18, 0, 0,
    0, 0, 0, 0, 0, 0, -3, 0,
    -13, 0, 0, 0, 0, 0, 0, -5,
    -3, 0, -3, 0, 0, -3, -10, 0,
    -5, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, -5, 0, -8, -5, 0, 0,
    0, 0, 0, 0, -10, 0, 0, -5,
    0, -3, 0, 0, 0, -5, -5, 0,
    -8, -3, -10, -10, 3, -3, 0, 0,
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
    -3, 0, -5, 0, 0, 0, 0, 0,
    -10, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, -15, -44, -13, -8, 0,
    -5, 0, -23, 0, 0, -5, -3, 0,
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
    -28, 0, 0, -8, 0, 0, -13, 0,
    0, 0, -8, 0, -15, -3, 0, 0,
    -5, 0, 0, 0, 0, 0, -36, -10,
    -33, -20, 0, -46, 0, -15, 0, -8,
    -13, -5, 0, 0, 0, -15, -8, -26,
    -15, 0, -10, -5, 0, 0, 0, -8,
    0, 0, -8, 0, 0, 0, -13, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, -3, 0, -5, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -8,
    -5, -5, -3, 0, 0, -5, 0, 0,
    -31, -8, -5, 0, 0, 0, -5, 0,
    -10, 0, 0, 0, 0, -31, -64, 0,
    -10, 0, 0, 0, 0, 0, 0, 0,
    0, 0, -5, -3, 0, -3, 0, -3,
    -8, 0, 0, 0, 0, -5, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, -8, -3, 0, 0, 0, -5, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -5,
    0, -8, -5, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, -8, 0, -3,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, -20, 0,
    0, 0, -15, 0, 0, 0, 0, 0,
    0, 0, 0, -3, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -8,
    -5, -8, 0, 0, 0, 0, -10, -10,
    -10, 0, -8, -3, -49, 0, 0, -10,
    0, 0, -10, 0, 0, 0, -10, 0,
    -26, 0, 0, 0, 0, 0, 0, 0,
    0, -8, -59, -10, -41, -23, 0, -51,
    0, -8, 0, -5, -20, -5, 0, 0,
    0, -18, -10, -33, -18, 0, -13, -5,
    -8, 0, 0, 0, 0, 0, -3, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, -15, 0,
    -20, -13, 0, -20, 0, -5, 0, -3,
    0, 0, 0, 0, 0, 0, -3, 0,
    -5, 0, 0, 0, 0, 0, 0, 0,
    0, -5, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, -8, -8, 0,
    0, -5, -5, 0, -5, -3, 0, -18,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, -3, 0, 0,
    0, 0, 0, -10, -31, -18, -3, 0,
    0, 0, -10, 0, 0, -5, 0, 0,
    0, -31, -59, -10, 0, -3, 0, 0,
    -5, 0, -10, -8, -5, 0, 0, -3,
    0, -5, 0, -5, -3, 0, 0, 0,
    0, -5, 0, 0, 0, 0, 0, -5,
    0, 0, -3, 0, 0, 0, -8, 0,
    0, 0, 0, 0, 0, 0, -10, 0,
    0, 0, 0, 0, 0, 0, 0, -5,
    0, 0, 0, -4, 0, -5, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, -3, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, -10, -3, 0, 0, -10, -10, 0,
    0, 0, -8, 0, -3, 0, 0, 0,
    0, 0, 0, 0, -3, 0, 0, -8,
    -5, -3, -5, 0, 0, 0, 0, -18,
    -23, -15, -10, 0, 0, 0, -31, 0,
    0, -5, 0, 0, -18, -36, -46, -15,
    -5, -8, 0, 0, 0, 0, 0, 0,
    0, 0, -3, -18, 0, -18, -5, -20,
    -15, 0, -18, -8, -5, -5, -5, -15,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, -10, -8, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -10,
    -33, -13, -5, 0, 0, 0, -13, 0,
    0, -8, 0, 0, 0, -33, -33, -15,
    -10, -8, 0, 0, 0, 0, 0, 0,
    0, 0, -5, -15, -3, -15, -8, -13,
    -13, 0, -5, 0, 0, -8, 0, -10,
    0, 0, 0, -8, -3, -5, -3, 0,
    0, 0, -3, 0, 0, 0, 0, 0,
    -13, -20, -13, -13, -5, -5, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -5,
    0, -5, 0, -3, -5, 0, -5, 0,
    0, -5, 0, -8, 0, 0, 0, -5,
    0, 0, -13, 0, 0, 0, -10, 0,
    0, -5, 0, 0, 0, 0, 0, 0,
    -3, -8, 0, 0, 0, 0, 0, 0,
    0, 0, 0, -13, 0, -10, 0, -3,
    0, 0, 0, -10, -5, 0, -3, 0,
    0, 0, 0, -20, -38, -15, -15, 0,
    0, 0, -26, 0, 0, -8, 0, -5,
    0, -38, -49, -20, -18, -13, 0, 0,
    0, 0, 0, 0, 0, 0, -8, -28,
    -10, -28, -13, -28, -26, -8, -15, -10,
    -8, -13, -5, -20, 0, 0, 0, -5,
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
    0, 0, -20, 0, -18, -8, 0, -20,
    0, -5, 0, 0, 0, 0, 0, 0,
    0, 0, 0, -10, -8, 0, -8, 0,
    -3, 0, -5, 0, -5, -8, 0, 0,
    0, 0, 0, 0, -10, 0, 0, 0,
    0, -8, -5, 0, 0, 0, -26, 0,
    -15, -10, -13, -26, 0, -5, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -8,
    -5, -15, -8, -5, 0, 0, 0, 0,
    0, 0, -3, 0, 0, 0, -8, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, -5, 0, -3, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, -8, 0, 0,
    0, 0, -10, 0, 0, 0, 0, 0,
    0, -20, -33, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -10,
    0, 0, -3, 0, 0, 0, -10, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, -8, 0, -8, -3, 0, -8,
    0, 0, 0, -8, 0, -8, 0, 0,
    -8, 0, 0, 0, 0, 0, 0, -5,
    0, 0, 0, 0, -23, 0, 0, 0,
    0, 0, -10, 0, 0, 0, 0, 0,
    0, -20, -33, 0, 0, 0, -10, 0,
    0, 0, 0, -5, 0, 0, 0, -5,
    5, -3, 0, 0, 0, 5, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, -3, 0, 0,
    0, 0, -10, 0, -8, -5, 0, -10,
    -3, 0, 0, -3, 0, -3, 0, 0,
    -4, 0, 0, -3, 0, 0, 0, -3,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, -5, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -5,
    0, -3, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -10,
    -26, -5, -3, 0, 0, 0, -5, 0,
    0, 0, 0, 0, 0, -26, -26, 0,
    0, 0, -8, 0, 0, 0, -10, 0,
    -10, 0, 0, -8, 0, -5, 0, -8,
    -8, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, -5, -10, -5, 0, 0,
    0, 0, -8, 0, 0, 0, 0, 0,
    0, -15, -15, 0, 0, 0, 0, 0,
    0, 0, -5, 0, 0, 0, 0, -3,
    0, -3, 0, -3, -5, 0, 0, 0,
    0, 0, 0, -3, 0, 0, 0, -8,
    0, 0, -5, 0, 0, 0, -8, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, -5, 0, -8, -5, 0, -13,
    0, 0, 0, -15, 0, -3, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, -5, -15, -5, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, -26, -28, 0, 0, 0, -5, 0,
    0, 0, -3, 0, -5, 0, 0, -8,
    0, -5, 0, -8, -5, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -5,
    0, 0, -3, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, -18, 0, -18, -3, 0, -23,
    0, -8, 0, -3, 0, -5, 0, 0,
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
const lv_font_t ui_font_F1B16 = {
#else
lv_font_t ui_font_F1B16 = {
#endif
    .get_glyph_dsc = lv_font_get_glyph_dsc_fmt_txt,    /*Function pointer to get glyph's data*/
    .get_glyph_bitmap = lv_font_get_bitmap_fmt_txt,    /*Function pointer to get glyph's bitmap*/
    .line_height = 17,          /*The maximum line height required by the font*/
    .base_line = 3,             /*Baseline measured from the bottom of the line*/
#if !(LVGL_VERSION_MAJOR == 6 && LVGL_VERSION_MINOR == 0)
    .subpx = LV_FONT_SUBPX_NONE,
#endif
#if LV_VERSION_CHECK(7, 4, 0) || LVGL_VERSION_MAJOR >= 8
    .underline_position = 0,
    .underline_thickness = 0,
#endif
    .dsc = &font_dsc           /*The custom font data. Will be accessed by `get_glyph_bitmap/dsc` */
};



#endif /*#if UI_FONT_F1B16*/

