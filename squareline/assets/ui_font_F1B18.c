/*******************************************************************************
 * Size: 18 px
 * Bpp: 1
 * Opts: --bpp 1 --size 18 --font F:/ESP32/squareline/assets/Formula1-Bold.otf -o F:/ESP32/squareline/assets\ui_font_F1B18.c --format lvgl -r 0x20-0x7f --no-compress --no-prefilter
 ******************************************************************************/

#include "../ui.h"

#ifndef UI_FONT_F1B18
#define UI_FONT_F1B18 1
#endif

#if UI_FONT_F1B18

/*-----------------
 *    BITMAPS
 *----------------*/

/*Store the image of the glyphs*/
static LV_ATTRIBUTE_LARGE_CONST const uint8_t glyph_bitmap[] = {
    /* U+0020 " " */
    0x0,

    /* U+0021 "!" */
    0xff, 0xff, 0xff, 0xff, 0x0, 0xff, 0xff,

    /* U+0022 "\"" */
    0xef, 0xdf, 0xbe, 0x7c, 0xc0,

    /* U+0023 "#" */
    0xe, 0x70, 0x73, 0x83, 0x98, 0xff, 0xf7, 0xff,
    0x8e, 0x60, 0x63, 0x3, 0x38, 0xff, 0xf7, 0xff,
    0x8c, 0x60, 0x67, 0x7, 0x38, 0x39, 0xc0,

    /* U+0024 "$" */
    0x6, 0x3, 0xff, 0x7f, 0xff, 0x60, 0xf6, 0xf,
    0xe0, 0xff, 0x7, 0xfc, 0x3f, 0xe0, 0x7f, 0x7,
    0xf0, 0x6f, 0x6, 0xff, 0xfe, 0xff, 0x80, 0x60,
    0x6, 0x0,

    /* U+0025 "%" */
    0x7c, 0x1b, 0xf8, 0xec, 0x63, 0xb1, 0x9c, 0xc6,
    0x73, 0xfb, 0x87, 0xc0, 0x0, 0x3e, 0x1d, 0xfc,
    0xe6, 0x33, 0x98, 0xdc, 0x63, 0x71, 0xfd, 0x83,
    0xe0,

    /* U+0026 "&" */
    0xf, 0xe0, 0x7f, 0x83, 0x80, 0xe, 0x0, 0x3c,
    0x0, 0xf8, 0x3, 0xe3, 0x9f, 0xde, 0xff, 0xf3,
    0x9f, 0x8e, 0x3c, 0x38, 0xf8, 0xff, 0xf1, 0xfd,
    0xe0,

    /* U+0027 "'" */
    0xff, 0xfc,

    /* U+0028 "(" */
    0x3d, 0xff, 0x3c, 0xf3, 0xcf, 0x3c, 0xf3, 0xcf,
    0x3c, 0xf3, 0xcf, 0x1f, 0x3c,

    /* U+0029 ")" */
    0xf3, 0xe3, 0xcf, 0x3c, 0xf3, 0xcf, 0x3c, 0xf3,
    0xcf, 0x3c, 0xf3, 0xfe, 0xf0,

    /* U+002A "*" */
    0x0, 0xd8, 0xe7, 0xf3, 0x8d, 0x80, 0x0,

    /* U+002B "+" */
    0x1c, 0xe, 0x7, 0x1f, 0xff, 0xf8, 0xe0, 0x70,
    0x38, 0x1c, 0x0,

    /* U+002C "," */
    0x7b, 0xde, 0xf7, 0xf8,

    /* U+002D "-" */
    0xff,

    /* U+002E "." */
    0xff, 0xff,

    /* U+002F "/" */
    0xe, 0x38, 0x70, 0xe1, 0xc3, 0x8e, 0x1c, 0x38,
    0x71, 0xc3, 0x87, 0xe, 0x38, 0x70,

    /* U+0030 "0" */
    0x1f, 0xc1, 0xff, 0x1e, 0x3d, 0xe0, 0xff, 0x7,
    0xf8, 0x3f, 0xc1, 0xfe, 0xf, 0xf0, 0x7f, 0x83,
    0xfc, 0x1e, 0xf1, 0xe3, 0xfe, 0xf, 0xe0,

    /* U+0031 "1" */
    0xf8, 0x3f, 0x1, 0xe0, 0x78, 0x1e, 0x7, 0x81,
    0xe0, 0x78, 0x1e, 0x7, 0x81, 0xe0, 0x78, 0xff,
    0xff, 0xf0,

    /* U+0032 "2" */
    0xff, 0x9f, 0xf8, 0x3, 0x80, 0xf0, 0x3e, 0x1f,
    0xc7, 0xf1, 0xfc, 0x7e, 0x1f, 0x83, 0xc0, 0x78,
    0xf, 0xff, 0xff, 0xc0,

    /* U+0033 "3" */
    0xff, 0xff, 0xff, 0x3, 0xe0, 0x7c, 0xf, 0x81,
    0xf0, 0x3f, 0xc3, 0xff, 0x0, 0xf0, 0xf, 0x0,
    0xf0, 0xf, 0xff, 0xef, 0xfc,

    /* U+0034 "4" */
    0x1, 0xf0, 0x7, 0xf0, 0x1f, 0xe0, 0x7f, 0xc0,
    0xf7, 0x83, 0xcf, 0xf, 0x1e, 0x3e, 0x3c, 0x78,
    0x78, 0xe0, 0xf1, 0xff, 0xf9, 0xff, 0xf0, 0x7,
    0x80, 0xf, 0x0,

    /* U+0035 "5" */
    0xff, 0xff, 0xff, 0x80, 0x70, 0xe, 0x1, 0xc0,
    0x3f, 0xe7, 0xfe, 0x1, 0xe0, 0x3c, 0x7, 0x80,
    0xff, 0xfd, 0xff, 0x0,

    /* U+0036 "6" */
    0x1f, 0xe3, 0xfe, 0x78, 0xf, 0x0, 0xf0, 0xf,
    0x0, 0xff, 0xcf, 0xfe, 0xf0, 0xff, 0xf, 0xf0,
    0xf7, 0xf, 0x7f, 0xe1, 0xfc,

    /* U+0037 "7" */
    0xff, 0xdf, 0xfc, 0x7, 0x80, 0xf0, 0x3c, 0x7,
    0x81, 0xe0, 0x3c, 0xf, 0x1, 0xe0, 0x78, 0xf,
    0x3, 0xc0, 0x78, 0x0,

    /* U+0038 "8" */
    0x3f, 0xc3, 0xff, 0x3c, 0x3d, 0xe1, 0xef, 0xf,
    0x78, 0x79, 0xff, 0x8f, 0xfc, 0xf0, 0x7f, 0x83,
    0xfc, 0x1f, 0xe0, 0xf7, 0xff, 0x1f, 0xf0,

    /* U+0039 "9" */
    0x3f, 0x87, 0xfe, 0xf1, 0xef, 0xf, 0xf0, 0xff,
    0xf, 0xf0, 0xf7, 0xff, 0x3f, 0xf0, 0xf, 0x0,
    0xf0, 0x1e, 0x7f, 0xc7, 0xf8,

    /* U+003A ":" */
    0xff, 0xff,

    /* U+003B ";" */
    0x7b, 0xde, 0xf7, 0xf8,

    /* U+003C "<" */
    0xc, 0x77, 0xfc, 0xf1, 0xe3, 0xc3, 0x4,

    /* U+003D "=" */
    0xff, 0xff, 0x0, 0x0, 0xff, 0xff,

    /* U+003E ">" */
    0xc3, 0x8f, 0x8f, 0x3d, 0xef, 0x30, 0x80,

    /* U+003F "?" */
    0xff, 0x3f, 0xe0, 0x3c, 0xf, 0x3, 0xc0, 0xf3,
    0xf8, 0xfc, 0x0, 0x0, 0x3, 0xc0, 0xf0, 0x3c,
    0xf, 0x0,

    /* U+0040 "@" */
    0xff, 0xc7, 0xff, 0x80, 0x1c, 0x0, 0x73, 0xf3,
    0xff, 0x9f, 0x9c, 0xfc, 0xe7, 0xe7, 0x3f, 0x39,
    0xff, 0xfe, 0x7f, 0xf0,

    /* U+0041 "A" */
    0x3, 0xc0, 0x7, 0xe0, 0x7, 0xe0, 0xf, 0xf0,
    0xe, 0x70, 0xe, 0x78, 0x1e, 0x78, 0x1c, 0x38,
    0x3c, 0x3c, 0x3f, 0xfc, 0x7f, 0xfe, 0x78, 0x1e,
    0x70, 0xe, 0xf0, 0xf,

    /* U+0042 "B" */
    0xff, 0xc7, 0xff, 0x3c, 0x3d, 0xe1, 0xef, 0xf,
    0x78, 0x7b, 0xff, 0x9f, 0xfc, 0xf0, 0x7f, 0x83,
    0xfc, 0x1f, 0xe0, 0xff, 0xff, 0x7f, 0xf0,

    /* U+0043 "C" */
    0x1f, 0xf3, 0xff, 0x78, 0xf, 0x0, 0xf0, 0xf,
    0x0, 0xf0, 0xf, 0x0, 0xf0, 0xf, 0x0, 0xf0,
    0x7, 0x80, 0x3f, 0xf1, 0xff,

    /* U+0044 "D" */
    0xff, 0xc3, 0xff, 0xcf, 0x7, 0xbc, 0xf, 0xf0,
    0x3f, 0xc0, 0xff, 0x3, 0xfc, 0xf, 0xf0, 0x3f,
    0xc0, 0xff, 0x3, 0xfc, 0x1e, 0xff, 0xf3, 0xff,
    0x80,

    /* U+0045 "E" */
    0xff, 0xff, 0xff, 0xf0, 0xf, 0x0, 0xf0, 0xf,
    0x0, 0xff, 0xff, 0xff, 0xf0, 0xf, 0x0, 0xf0,
    0xf, 0x0, 0xff, 0xff, 0xff,

    /* U+0046 "F" */
    0xff, 0xff, 0xff, 0xc0, 0x78, 0xf, 0x1, 0xe0,
    0x3f, 0xff, 0xff, 0xf0, 0x1e, 0x3, 0xc0, 0x78,
    0xf, 0x1, 0xe0, 0x0,

    /* U+0047 "G" */
    0xf, 0xfc, 0xff, 0xf7, 0x80, 0x3c, 0x0, 0xf0,
    0x3, 0xc0, 0xf, 0x1f, 0xfc, 0x7f, 0xf0, 0x1f,
    0xc0, 0x7f, 0x1, 0xde, 0x7, 0x3f, 0xf8, 0x3f,
    0xc0,

    /* U+0048 "H" */
    0xf0, 0x3f, 0xc0, 0xff, 0x3, 0xfc, 0xf, 0xf0,
    0x3f, 0xc0, 0xff, 0xff, 0xff, 0xff, 0xf0, 0x3f,
    0xc0, 0xff, 0x3, 0xfc, 0xf, 0xf0, 0x3f, 0xc0,
    0xf0,

    /* U+0049 "I" */
    0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,

    /* U+004A "J" */
    0x3, 0xc0, 0xf0, 0x3c, 0xf, 0x3, 0xc0, 0xf0,
    0x3c, 0xf, 0x3, 0xc0, 0xf0, 0x3c, 0x1e, 0xff,
    0xbf, 0x80,

    /* U+004B "K" */
    0xf0, 0x7b, 0xc3, 0xcf, 0xf, 0x3c, 0x78, 0xf1,
    0xc3, 0xce, 0xf, 0xf8, 0x3f, 0xe0, 0xf3, 0xc3,
    0xc7, 0xf, 0x1e, 0x3c, 0x3c, 0xf0, 0xfb, 0xc1,
    0xe0,

    /* U+004C "L" */
    0xf0, 0x1e, 0x3, 0xc0, 0x78, 0xf, 0x1, 0xe0,
    0x3c, 0x7, 0x80, 0xf0, 0x1e, 0x3, 0xc0, 0x78,
    0xf, 0xff, 0xff, 0xc0,

    /* U+004D "M" */
    0x1e, 0x7, 0x83, 0xf0, 0xfc, 0x7f, 0xf, 0xe7,
    0x78, 0xee, 0x77, 0x9e, 0xe7, 0x79, 0xee, 0x73,
    0x9c, 0xe7, 0x39, 0xce, 0x73, 0x9c, 0xe7, 0x3d,
    0xce, 0xf3, 0xfc, 0xff, 0x1f, 0xcf, 0xf1, 0xf8,
    0xff, 0xf, 0xf,

    /* U+004E "N" */
    0x38, 0x1e, 0xfc, 0x3f, 0xf8, 0x7f, 0xb8, 0xff,
    0x71, 0xfe, 0xe3, 0xfc, 0xe7, 0xf9, 0xcf, 0xf1,
    0xdf, 0xe3, 0xbf, 0xc7, 0x7f, 0x87, 0xff, 0xf,
    0xde, 0xf, 0x0,

    /* U+004F "O" */
    0x1f, 0xe0, 0xff, 0xc7, 0x87, 0xbc, 0xf, 0xf0,
    0x3f, 0xc0, 0xff, 0x3, 0xfc, 0xf, 0xf0, 0x3f,
    0xc0, 0xff, 0x3, 0xde, 0x1e, 0x3f, 0xf0, 0x7f,
    0x80,

    /* U+0050 "P" */
    0xff, 0xcf, 0xfe, 0xf0, 0xff, 0xf, 0xf0, 0xff,
    0xf, 0xf0, 0xff, 0xfe, 0xff, 0xcf, 0x0, 0xf0,
    0xf, 0x0, 0xf0, 0xf, 0x0,

    /* U+0051 "Q" */
    0x1f, 0xe0, 0xff, 0xc7, 0x87, 0xbc, 0xf, 0xf0,
    0x3f, 0xc0, 0xff, 0x3, 0xfc, 0xf, 0xf0, 0x3f,
    0xc0, 0xff, 0x3, 0xde, 0x1e, 0x3f, 0xf0, 0x7f,
    0x80, 0x1c, 0x0, 0x78, 0x0, 0xe0,

    /* U+0052 "R" */
    0xff, 0xe7, 0xff, 0xbc, 0x1f, 0xe0, 0xff, 0x7,
    0xf8, 0x3f, 0xdf, 0xde, 0xfc, 0xf7, 0x7, 0xbc,
    0x3c, 0xf1, 0xe3, 0xcf, 0x1f, 0x78, 0x7c,

    /* U+0053 "S" */
    0x3f, 0xf7, 0xff, 0xf0, 0xf, 0x0, 0xfe, 0xf,
    0xf8, 0x7f, 0xe3, 0xff, 0xf, 0xf0, 0x1f, 0x0,
    0xf0, 0xf, 0xff, 0xef, 0xf8,

    /* U+0054 "T" */
    0xff, 0xff, 0xff, 0xf0, 0x78, 0x1, 0xe0, 0x7,
    0x80, 0x1e, 0x0, 0x78, 0x1, 0xe0, 0x7, 0x80,
    0x1e, 0x0, 0x78, 0x1, 0xe0, 0x7, 0x80, 0x1e,
    0x0,

    /* U+0055 "U" */
    0xf0, 0x7f, 0x83, 0xfc, 0x1f, 0xe0, 0xff, 0x7,
    0xf8, 0x3f, 0xc1, 0xfe, 0xf, 0xf0, 0x7f, 0x83,
    0xfc, 0x1e, 0xe0, 0xf7, 0xff, 0xf, 0xe0,

    /* U+0056 "V" */
    0xf0, 0x1d, 0xe0, 0xf7, 0x83, 0xde, 0xe, 0x38,
    0x78, 0xf1, 0xe3, 0xc7, 0x7, 0x1c, 0x1c, 0xf0,
    0x7b, 0x80, 0xee, 0x3, 0xf8, 0xf, 0xc0, 0x1e,
    0x0,

    /* U+0057 "W" */
    0xf0, 0x78, 0x3d, 0xc3, 0xf0, 0xe7, 0xf, 0xc3,
    0x9c, 0x7f, 0x8e, 0x71, 0xde, 0x79, 0xe7, 0x39,
    0xe7, 0x9c, 0xe7, 0x8e, 0x73, 0x9c, 0x39, 0xce,
    0x70, 0xef, 0x3d, 0xc3, 0xb8, 0xf7, 0xe, 0xe1,
    0xdc, 0x1f, 0x87, 0xe0, 0x3c, 0xf, 0x0,

    /* U+0058 "X" */
    0x78, 0x3e, 0xf0, 0x78, 0xf1, 0xe0, 0xf7, 0x81,
    0xff, 0x1, 0xfc, 0x1, 0xf0, 0x3, 0xe0, 0xf,
    0xe0, 0x3d, 0xe0, 0x79, 0xe1, 0xe3, 0xc7, 0x83,
    0xcf, 0x3, 0xc0,

    /* U+0059 "Y" */
    0xf0, 0x3d, 0xe0, 0xe7, 0x87, 0x8f, 0x1c, 0x3c,
    0xf0, 0x7b, 0x81, 0xfe, 0x3, 0xf0, 0xf, 0xc0,
    0x1e, 0x0, 0x78, 0x1, 0xe0, 0x7, 0x80, 0x1e,
    0x0,

    /* U+005A "Z" */
    0xff, 0xef, 0xff, 0x0, 0xf0, 0x1f, 0x3, 0xf0,
    0xfe, 0x1f, 0xc7, 0xf8, 0x7f, 0xf, 0xc0, 0xf8,
    0xf, 0x0, 0x7f, 0xf3, 0xff,

    /* U+005B "[" */
    0xff, 0xf9, 0xce, 0x73, 0x9c, 0xe7, 0x39, 0xce,
    0x73, 0x9f, 0xf8,

    /* U+005C "\\" */
    0xe0, 0xe1, 0xc3, 0x87, 0xf, 0xe, 0x1c, 0x38,
    0x70, 0x70, 0xe1, 0xc3, 0x83, 0x87,

    /* U+005D "]" */
    0xff, 0xce, 0x73, 0x9c, 0xe7, 0x39, 0xce, 0x73,
    0x9c, 0xff, 0xf8,

    /* U+005E "^" */
    0x0, 0x71, 0xf7, 0x60,

    /* U+005F "_" */
    0xff, 0xff,

    /* U+0060 "`" */
    0xe6,

    /* U+0061 "a" */
    0x7f, 0xf, 0xf8, 0xf, 0x87, 0xf1, 0xfe, 0x7d,
    0xdf, 0x3b, 0xc7, 0xf0, 0xef, 0xfc, 0xff, 0x80,

    /* U+0062 "b" */
    0xf0, 0xf, 0x0, 0xf0, 0xf, 0xfc, 0xff, 0xef,
    0xf, 0xf0, 0xff, 0xf, 0xf0, 0xff, 0xf, 0xf0,
    0xff, 0xf, 0xff, 0xef, 0xfc,

    /* U+0063 "c" */
    0x3f, 0xdf, 0xff, 0x83, 0xc0, 0xf0, 0x3c, 0xf,
    0x3, 0xc0, 0xf0, 0x1f, 0xf3, 0xfc,

    /* U+0064 "d" */
    0x0, 0xf0, 0xf, 0x0, 0xf3, 0xff, 0x7f, 0xff,
    0xf, 0xf0, 0xff, 0xf, 0xf0, 0xff, 0xf, 0xf0,
    0xff, 0xf, 0x7f, 0xf3, 0xff,

    /* U+0065 "e" */
    0x3f, 0x8f, 0xfb, 0xc3, 0xf8, 0x7f, 0xff, 0xff,
    0xfc, 0x7, 0x80, 0xf8, 0xf, 0xfc, 0x7f, 0x80,

    /* U+0066 "f" */
    0x3f, 0x7f, 0x78, 0xff, 0xff, 0x78, 0x78, 0x78,
    0x78, 0x78, 0x78, 0x78, 0x78, 0x78,

    /* U+0067 "g" */
    0x3f, 0xf7, 0xff, 0xf0, 0xff, 0xf, 0xf0, 0xff,
    0xf, 0xf0, 0xff, 0xf, 0x7f, 0xf3, 0xff, 0x0,
    0xf0, 0xf, 0x7f, 0xe7, 0xfc,

    /* U+0068 "h" */
    0xf0, 0x1e, 0x3, 0xc0, 0x7f, 0xcf, 0xfd, 0xe3,
    0xfc, 0x7f, 0x8f, 0xf1, 0xfe, 0x3f, 0xc7, 0xf8,
    0xff, 0x1f, 0xe3, 0xc0,

    /* U+0069 "i" */
    0xff, 0xf, 0xff, 0xff, 0xff, 0xff, 0xff,

    /* U+006A "j" */
    0x3c, 0xf0, 0xf, 0x3c, 0xf3, 0xcf, 0x3c, 0xf3,
    0xcf, 0x3c, 0xf3, 0xfe, 0xf0,

    /* U+006B "k" */
    0xf0, 0xf, 0x0, 0xf0, 0xf, 0xf, 0xf1, 0xef,
    0x3c, 0xf3, 0x8f, 0xf0, 0xff, 0xf, 0x78, 0xf3,
    0xcf, 0x1c, 0xf1, 0xef, 0xf,

    /* U+006C "l" */
    0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,

    /* U+006D "m" */
    0xff, 0xff, 0x3f, 0xff, 0xef, 0x1e, 0x3f, 0xc7,
    0x8f, 0xf1, 0xe3, 0xfc, 0x78, 0xff, 0x1e, 0x3f,
    0xc7, 0x8f, 0xf1, 0xe3, 0xfc, 0x78, 0xff, 0x1e,
    0x3c,

    /* U+006E "n" */
    0xff, 0x9f, 0xfb, 0xc7, 0xf8, 0xff, 0x1f, 0xe3,
    0xfc, 0x7f, 0x8f, 0xf1, 0xfe, 0x3f, 0xc7, 0x80,

    /* U+006F "o" */
    0x1f, 0x87, 0xfe, 0x70, 0xef, 0xf, 0xf0, 0xff,
    0xf, 0xf0, 0xff, 0xf, 0x70, 0xe7, 0xfe, 0x1f,
    0x80,

    /* U+0070 "p" */
    0xff, 0xcf, 0xfe, 0xf0, 0xff, 0xf, 0xf0, 0xff,
    0xf, 0xf0, 0xff, 0xf, 0xf0, 0xff, 0xfe, 0xff,
    0xcf, 0x0, 0xf0, 0xf, 0x0,

    /* U+0071 "q" */
    0x3f, 0xf7, 0xff, 0xf0, 0xff, 0xf, 0xf0, 0xff,
    0xf, 0xf0, 0xff, 0xf, 0xf0, 0xf7, 0xff, 0x3f,
    0xf0, 0xf, 0x0, 0xf0, 0xf,

    /* U+0072 "r" */
    0x3f, 0x7f, 0xf0, 0xf0, 0xf0, 0xf0, 0xf0, 0xf0,
    0xf0, 0xf0, 0xf0,

    /* U+0073 "s" */
    0x3f, 0xdf, 0xfe, 0x3, 0xe0, 0xff, 0x1f, 0xe3,
    0xfc, 0x1f, 0x1, 0xff, 0xef, 0xf0,

    /* U+0074 "t" */
    0x78, 0x3c, 0x3f, 0xff, 0xf7, 0x83, 0xc1, 0xe0,
    0xf0, 0x78, 0x3c, 0x1e, 0x7, 0xf1, 0xf8,

    /* U+0075 "u" */
    0xf1, 0xfe, 0x3f, 0xc7, 0xf8, 0xff, 0x1f, 0xe3,
    0xfc, 0x7f, 0x8f, 0xf1, 0xef, 0xfc, 0xff, 0x80,

    /* U+0076 "v" */
    0xf0, 0x7b, 0x83, 0x9e, 0x1c, 0xf1, 0xe3, 0x8e,
    0x1c, 0x70, 0xf7, 0x83, 0xb8, 0x1f, 0xc0, 0x7c,
    0x1, 0xc0,

    /* U+0077 "w" */
    0xf0, 0xf0, 0xee, 0x3f, 0x1d, 0xcf, 0xe7, 0xb9,
    0xdc, 0xe7, 0x3b, 0x9c, 0xf7, 0x73, 0x8e, 0xef,
    0x71, 0xdc, 0xee, 0x3b, 0x9d, 0xc7, 0xe3, 0xf0,
    0x78, 0x3c, 0x0,

    /* U+0078 "x" */
    0x70, 0x73, 0xc7, 0x8f, 0x38, 0x3b, 0xc1, 0xfc,
    0x7, 0xc0, 0x3f, 0x3, 0xf8, 0x1d, 0xe1, 0xc7,
    0x9e, 0x1e,

    /* U+0079 "y" */
    0xf0, 0x73, 0x87, 0x9e, 0x3c, 0xf1, 0xc3, 0x9e,
    0x1e, 0xf0, 0xf7, 0x3, 0xf8, 0x1f, 0xc0, 0x7c,
    0x0, 0xe0, 0xe, 0x7, 0xf0, 0x3e, 0x0,

    /* U+007A "z" */
    0xff, 0xbf, 0xf0, 0x1c, 0x1f, 0x3f, 0xdf, 0xef,
    0xf3, 0xe0, 0xe0, 0x3f, 0xf7, 0xfc,

    /* U+007B "{" */
    0x1e, 0x7c, 0xe1, 0xc3, 0x87, 0xe, 0x1c, 0xf1,
    0xf0, 0xe1, 0xc3, 0x87, 0xe, 0x1f, 0x1e,

    /* U+007C "|" */
    0xff, 0xff, 0xff, 0xff, 0xff, 0xf8,

    /* U+007D "}" */
    0xf1, 0xf0, 0xe1, 0xc3, 0x87, 0xe, 0x1c, 0x1e,
    0x7c, 0xe1, 0xc3, 0x87, 0xe, 0x7c, 0xf0,

    /* U+007E "~" */
    0xf7, 0xbc
};


/*---------------------
 *  GLYPH DESCRIPTION
 *--------------------*/

static const lv_font_fmt_txt_glyph_dsc_t glyph_dsc[] = {
    {.bitmap_index = 0, .adv_w = 0, .box_w = 0, .box_h = 0, .ofs_x = 0, .ofs_y = 0} /* id = 0 reserved */,
    {.bitmap_index = 0, .adv_w = 69, .box_w = 1, .box_h = 1, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 1, .adv_w = 97, .box_w = 4, .box_h = 14, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 8, .adv_w = 156, .box_w = 7, .box_h = 5, .ofs_x = 1, .ofs_y = 9},
    {.bitmap_index = 13, .adv_w = 240, .box_w = 13, .box_h = 14, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 36, .adv_w = 217, .box_w = 12, .box_h = 17, .ofs_x = 1, .ofs_y = -2},
    {.bitmap_index = 62, .adv_w = 244, .box_w = 14, .box_h = 14, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 87, .adv_w = 234, .box_w = 14, .box_h = 14, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 112, .adv_w = 89, .box_w = 3, .box_h = 5, .ofs_x = 1, .ofs_y = 9},
    {.bitmap_index = 114, .adv_w = 129, .box_w = 6, .box_h = 17, .ofs_x = 2, .ofs_y = -3},
    {.bitmap_index = 127, .adv_w = 129, .box_w = 6, .box_h = 17, .ofs_x = 1, .ofs_y = -3},
    {.bitmap_index = 140, .adv_w = 151, .box_w = 7, .box_h = 7, .ofs_x = 1, .ofs_y = 7},
    {.bitmap_index = 147, .adv_w = 169, .box_w = 9, .box_h = 9, .ofs_x = 1, .ofs_y = 2},
    {.bitmap_index = 158, .adv_w = 82, .box_w = 5, .box_h = 6, .ofs_x = 0, .ofs_y = -3},
    {.bitmap_index = 162, .adv_w = 105, .box_w = 4, .box_h = 2, .ofs_x = 1, .ofs_y = 4},
    {.bitmap_index = 163, .adv_w = 95, .box_w = 4, .box_h = 4, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 165, .adv_w = 112, .box_w = 7, .box_h = 16, .ofs_x = 0, .ofs_y = -2},
    {.bitmap_index = 179, .adv_w = 243, .box_w = 13, .box_h = 14, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 202, .adv_w = 182, .box_w = 10, .box_h = 14, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 220, .adv_w = 199, .box_w = 11, .box_h = 14, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 240, .adv_w = 206, .box_w = 12, .box_h = 14, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 261, .adv_w = 235, .box_w = 15, .box_h = 14, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 288, .adv_w = 204, .box_w = 11, .box_h = 14, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 308, .adv_w = 220, .box_w = 12, .box_h = 14, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 329, .adv_w = 198, .box_w = 11, .box_h = 14, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 349, .adv_w = 216, .box_w = 13, .box_h = 14, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 372, .adv_w = 220, .box_w = 12, .box_h = 14, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 393, .adv_w = 95, .box_w = 4, .box_h = 4, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 395, .adv_w = 86, .box_w = 5, .box_h = 6, .ofs_x = 0, .ofs_y = -3},
    {.bitmap_index = 399, .adv_w = 136, .box_w = 6, .box_h = 9, .ofs_x = 1, .ofs_y = 2},
    {.bitmap_index = 406, .adv_w = 151, .box_w = 8, .box_h = 6, .ofs_x = 1, .ofs_y = 5},
    {.bitmap_index = 412, .adv_w = 136, .box_w = 6, .box_h = 9, .ofs_x = 1, .ofs_y = 2},
    {.bitmap_index = 419, .adv_w = 180, .box_w = 10, .box_h = 14, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 437, .adv_w = 241, .box_w = 13, .box_h = 12, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 457, .adv_w = 256, .box_w = 16, .box_h = 14, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 485, .adv_w = 230, .box_w = 13, .box_h = 14, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 508, .adv_w = 208, .box_w = 12, .box_h = 14, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 529, .adv_w = 245, .box_w = 14, .box_h = 14, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 554, .adv_w = 215, .box_w = 12, .box_h = 14, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 575, .adv_w = 206, .box_w = 11, .box_h = 14, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 595, .adv_w = 246, .box_w = 14, .box_h = 14, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 620, .adv_w = 255, .box_w = 14, .box_h = 14, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 645, .adv_w = 98, .box_w = 4, .box_h = 14, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 652, .adv_w = 182, .box_w = 10, .box_h = 14, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 670, .adv_w = 232, .box_w = 14, .box_h = 14, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 695, .adv_w = 195, .box_w = 11, .box_h = 14, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 715, .adv_w = 334, .box_w = 20, .box_h = 14, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 750, .adv_w = 280, .box_w = 15, .box_h = 14, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 777, .adv_w = 252, .box_w = 14, .box_h = 14, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 802, .adv_w = 224, .box_w = 12, .box_h = 14, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 823, .adv_w = 252, .box_w = 14, .box_h = 17, .ofs_x = 1, .ofs_y = -3},
    {.bitmap_index = 853, .adv_w = 233, .box_w = 13, .box_h = 14, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 876, .adv_w = 217, .box_w = 12, .box_h = 14, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 897, .adv_w = 236, .box_w = 14, .box_h = 14, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 922, .adv_w = 245, .box_w = 13, .box_h = 14, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 945, .adv_w = 233, .box_w = 14, .box_h = 14, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 970, .adv_w = 351, .box_w = 22, .box_h = 14, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 1009, .adv_w = 243, .box_w = 15, .box_h = 14, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 1036, .adv_w = 230, .box_w = 14, .box_h = 14, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 1061, .adv_w = 207, .box_w = 12, .box_h = 14, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 1082, .adv_w = 126, .box_w = 5, .box_h = 17, .ofs_x = 2, .ofs_y = -3},
    {.bitmap_index = 1093, .adv_w = 112, .box_w = 7, .box_h = 16, .ofs_x = 0, .ofs_y = -2},
    {.bitmap_index = 1107, .adv_w = 126, .box_w = 5, .box_h = 17, .ofs_x = 1, .ofs_y = -3},
    {.bitmap_index = 1118, .adv_w = 204, .box_w = 7, .box_h = 4, .ofs_x = 3, .ofs_y = 6},
    {.bitmap_index = 1122, .adv_w = 128, .box_w = 8, .box_h = 2, .ofs_x = 0, .ofs_y = -3},
    {.bitmap_index = 1124, .adv_w = 204, .box_w = 4, .box_h = 2, .ofs_x = 4, .ofs_y = 12},
    {.bitmap_index = 1125, .adv_w = 197, .box_w = 11, .box_h = 11, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 1141, .adv_w = 218, .box_w = 12, .box_h = 14, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 1162, .adv_w = 179, .box_w = 10, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 1176, .adv_w = 218, .box_w = 12, .box_h = 14, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 1197, .adv_w = 201, .box_w = 11, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 1213, .adv_w = 142, .box_w = 8, .box_h = 14, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 1227, .adv_w = 213, .box_w = 12, .box_h = 14, .ofs_x = 1, .ofs_y = -3},
    {.bitmap_index = 1248, .adv_w = 212, .box_w = 11, .box_h = 14, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 1268, .adv_w = 95, .box_w = 4, .box_h = 14, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 1275, .adv_w = 91, .box_w = 6, .box_h = 17, .ofs_x = -1, .ofs_y = -3},
    {.bitmap_index = 1288, .adv_w = 205, .box_w = 12, .box_h = 14, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 1309, .adv_w = 95, .box_w = 4, .box_h = 14, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 1316, .adv_w = 313, .box_w = 18, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 1341, .adv_w = 212, .box_w = 11, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 1357, .adv_w = 209, .box_w = 12, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 1374, .adv_w = 218, .box_w = 12, .box_h = 14, .ofs_x = 1, .ofs_y = -3},
    {.bitmap_index = 1395, .adv_w = 218, .box_w = 12, .box_h = 14, .ofs_x = 1, .ofs_y = -3},
    {.bitmap_index = 1416, .adv_w = 139, .box_w = 8, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 1427, .adv_w = 183, .box_w = 10, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 1441, .adv_w = 156, .box_w = 9, .box_h = 13, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 1456, .adv_w = 212, .box_w = 11, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 1472, .adv_w = 208, .box_w = 13, .box_h = 11, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 1490, .adv_w = 308, .box_w = 19, .box_h = 11, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 1517, .adv_w = 213, .box_w = 13, .box_h = 11, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 1535, .adv_w = 207, .box_w = 13, .box_h = 14, .ofs_x = 0, .ofs_y = -3},
    {.bitmap_index = 1558, .adv_w = 193, .box_w = 10, .box_h = 11, .ofs_x = 1, .ofs_y = 0},
    {.bitmap_index = 1572, .adv_w = 117, .box_w = 7, .box_h = 17, .ofs_x = 0, .ofs_y = -3},
    {.bitmap_index = 1587, .adv_w = 89, .box_w = 3, .box_h = 15, .ofs_x = 1, .ofs_y = -1},
    {.bitmap_index = 1593, .adv_w = 117, .box_w = 7, .box_h = 17, .ofs_x = 1, .ofs_y = -3},
    {.bitmap_index = 1608, .adv_w = 248, .box_w = 7, .box_h = 2, .ofs_x = 4, .ofs_y = 6}
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
    0, 0, -20, 0, 0, 0, 0, 0,
    0, -32, -43, -9, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, -9, 0,
    0, -6, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, -6, 0, 0, 0, 0,
    0, 0, -6, -6, -6, 0, 0, -6,
    0, 0, 0, 0, 0, 0, 0, -17,
    -6, -6, 0, 0, -17, 0, 0, 0,
    0, -9, -6, 0, 0, 0, -17, 0,
    -12, -9, -6, -23, -6, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -12,
    -6, -9, -6, -6, 0, 0, 0, 0,
    0, 0, -9, 0, 0, 0, -17, -6,
    -23, -9, -6, 0, 0, 0, 0, 0,
    0, 0, -26, 0, -37, -12, 0, -43,
    0, 0, 0, -6, 0, 0, 0, 0,
    0, 0, 0, -29, -12, 0, -9, 0,
    0, 0, 0, -12, 0, 0, -6, 0,
    0, 0, -6, 0, 0, -6, 0, 0,
    0, -12, -12, -9, -6, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -9,
    0, -3, 0, -6, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, -3, 0,
    -9, -6, 0, -3, -6, -14, 0, 0,
    -17, 0, -6, 0, 0, -14, -12, 0,
    0, -9, -12, 0, -6, -3, -14, -20,
    -3, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, -3, 0, -6, 0, -3,
    -29, 0, 0, -9, 0, 0, -9, 0,
    0, 0, -14, 0, -20, 0, 0, 0,
    0, 0, 0, 0, 0, 0, -26, 0,
    -26, -20, 0, -29, 0, -20, 0, 0,
    0, 0, 0, 0, 0, 0, -3, 0,
    -14, 0, 0, 0, 0, 0, 0, -6,
    -3, 0, -3, 0, 0, -3, -12, 0,
    -6, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, -6, 0, -9, -6, 0, 0,
    0, 0, 0, 0, -12, 0, 0, -6,
    0, -3, 0, 0, 0, -6, -6, 0,
    -9, -3, -12, -12, 3, -3, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, -6, -3, 0, -12, 0, 0, 0,
    -6, 0, 0, 0, 0, -6, 0, 0,
    -20, 0, -6, -6, 0, 0, -6, 0,
    0, 0, -12, 0, -12, -12, 0, -12,
    0, -6, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, -6, 0, 0, 0,
    0, 0, 0, 0, -6, -6, 0, 0,
    0, 0, 0, 0, -9, 0, 0, -6,
    0, 0, -6, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    -3, 0, -6, 0, 0, 0, 0, 0,
    -12, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, -17, -49, -14, -9, 0,
    -6, 0, -26, 0, 0, -6, -3, 0,
    0, -35, -29, -14, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -12,
    0, -12, 0, -9, -6, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, -6, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -6,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, -6, 0, 0, 0, 0, -20, 0,
    0, -14, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, -9, 0, -9, -6, -6, -6,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    -32, 0, 0, -9, 0, 0, -14, 0,
    0, 0, -9, 0, -17, -3, 0, 0,
    -6, 0, 0, 0, 0, 0, -40, -12,
    -37, -23, 0, -52, 0, -17, 0, -9,
    -14, -6, 0, 0, 0, -17, -9, -29,
    -17, 0, -12, -6, 0, 0, 0, -9,
    0, 0, -9, 0, 0, 0, -14, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, -3, 0, -6, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -9,
    -6, -6, -3, 0, 0, -6, 0, 0,
    -35, -9, -6, 0, 0, 0, -6, 0,
    -12, 0, 0, 0, 0, -35, -72, 0,
    -12, 0, 0, 0, 0, 0, 0, 0,
    0, 0, -6, -3, 0, -3, 0, -3,
    -9, 0, 0, 0, 0, -6, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, -9, -3, 0, 0, 0, -6, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -6,
    0, -9, -6, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, -9, 0, -3,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, -23, 0,
    0, 0, -17, 0, 0, 0, 0, 0,
    0, 0, 0, -3, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -9,
    -6, -9, 0, 0, 0, 0, -12, -12,
    -12, 0, -9, -3, -55, 0, 0, -12,
    0, 0, -12, 0, 0, 0, -12, 0,
    -29, 0, 0, 0, 0, 0, 0, 0,
    0, -9, -66, -12, -46, -26, 0, -58,
    0, -9, 0, -6, -23, -6, 0, 0,
    0, -20, -12, -37, -20, 0, -14, -6,
    -9, 0, 0, 0, 0, 0, -3, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, -17, 0,
    -23, -14, 0, -23, 0, -6, 0, -3,
    0, 0, 0, 0, 0, 0, -3, 0,
    -6, 0, 0, 0, 0, 0, 0, 0,
    0, -6, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, -9, -9, 0,
    0, -6, -6, 0, -6, -3, 0, -20,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, -3, 0, 0,
    0, 0, 0, -12, -35, -20, -3, 0,
    0, 0, -12, 0, 0, -6, 0, 0,
    0, -35, -66, -12, 0, -3, 0, 0,
    -6, 0, -12, -9, -6, 0, 0, -3,
    0, -6, 0, -6, -3, 0, 0, 0,
    0, -6, 0, 0, 0, 0, 0, -6,
    0, 0, -3, 0, 0, 0, -9, 0,
    0, 0, 0, 0, 0, 0, -12, 0,
    0, 0, 0, 0, 0, 0, 0, -6,
    0, 0, 0, -4, 0, -6, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, -3, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, -12, -3, 0, 0, -12, -12, 0,
    0, 0, -9, 0, -3, 0, 0, 0,
    0, 0, 0, 0, -3, 0, 0, -9,
    -6, -3, -6, 0, 0, 0, 0, -20,
    -26, -17, -12, 0, 0, 0, -35, 0,
    0, -6, 0, 0, -20, -40, -52, -17,
    -6, -9, 0, 0, 0, 0, 0, 0,
    0, 0, -3, -20, 0, -20, -6, -23,
    -17, 0, -20, -9, -6, -6, -6, -17,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, -12, -9, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -12,
    -37, -14, -6, 0, 0, 0, -14, 0,
    0, -9, 0, 0, 0, -37, -37, -17,
    -12, -9, 0, 0, 0, 0, 0, 0,
    0, 0, -6, -17, -3, -17, -9, -14,
    -14, 0, -6, 0, 0, -9, 0, -12,
    0, 0, 0, -9, -3, -6, -3, 0,
    0, 0, -3, 0, 0, 0, 0, 0,
    -14, -23, -14, -14, -6, -6, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -6,
    0, -6, 0, -3, -6, 0, -6, 0,
    0, -6, 0, -9, 0, 0, 0, -6,
    0, 0, -14, 0, 0, 0, -12, 0,
    0, -6, 0, 0, 0, 0, 0, 0,
    -3, -9, 0, 0, 0, 0, 0, 0,
    0, 0, 0, -14, 0, -12, 0, -3,
    0, 0, 0, -12, -6, 0, -3, 0,
    0, 0, 0, -23, -43, -17, -17, 0,
    0, 0, -29, 0, 0, -9, 0, -6,
    0, -43, -55, -23, -20, -14, 0, 0,
    0, 0, 0, 0, 0, 0, -9, -32,
    -12, -32, -14, -32, -29, -9, -17, -12,
    -9, -14, -6, -23, 0, 0, 0, -6,
    0, 0, -3, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, -3, 0, 0, -3, 0, 0, -3,
    0, 0, 0, -6, 0, -6, 0, 0,
    -6, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, -6, 0,
    0, -6, -6, 0, -14, -3, 0, 0,
    0, 0, 0, 0, 0, 0, -6, 0,
    -20, -14, 0, -17, 0, 0, 0, 0,
    0, -3, 0, 0, 0, 0, 0, -14,
    -6, 0, 0, 0, -6, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, -23, 0, -20, -9, 0, -23,
    0, -6, 0, 0, 0, 0, 0, 0,
    0, 0, 0, -12, -9, 0, -9, 0,
    -3, 0, -6, 0, -6, -9, 0, 0,
    0, 0, 0, 0, -12, 0, 0, 0,
    0, -9, -6, 0, 0, 0, -29, 0,
    -17, -12, -14, -29, 0, -6, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -9,
    -6, -17, -9, -6, 0, 0, 0, 0,
    0, 0, -3, 0, 0, 0, -9, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, -6, 0, -3, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, -9, 0, 0,
    0, 0, -12, 0, 0, 0, 0, 0,
    0, -23, -37, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -12,
    0, 0, -3, 0, 0, 0, -12, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, -9, 0, -9, -3, 0, -9,
    0, 0, 0, -9, 0, -9, 0, 0,
    -9, 0, 0, 0, 0, 0, 0, -6,
    0, 0, 0, 0, -26, 0, 0, 0,
    0, 0, -12, 0, 0, 0, 0, 0,
    0, -23, -37, 0, 0, 0, -12, 0,
    0, 0, 0, -6, 0, 0, 0, -6,
    6, -3, 0, 0, 0, 6, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, -3, 0, 0,
    0, 0, -12, 0, -9, -6, 0, -12,
    -3, 0, 0, -3, 0, -3, 0, 0,
    -4, 0, 0, -3, 0, 0, 0, -3,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, -6, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -6,
    0, -3, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -12,
    -29, -6, -3, 0, 0, 0, -6, 0,
    0, 0, 0, 0, 0, -29, -29, 0,
    0, 0, -9, 0, 0, 0, -12, 0,
    -12, 0, 0, -9, 0, -6, 0, -9,
    -9, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, -6, -12, -6, 0, 0,
    0, 0, -9, 0, 0, 0, 0, 0,
    0, -17, -17, 0, 0, 0, 0, 0,
    0, 0, -6, 0, 0, 0, 0, -3,
    0, -3, 0, -3, -6, 0, 0, 0,
    0, 0, 0, -3, 0, 0, 0, -9,
    0, 0, -6, 0, 0, 0, -9, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, -6, 0, -9, -6, 0, -14,
    0, 0, 0, -17, 0, -3, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, -6, -17, -6, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, -29, -32, 0, 0, 0, -6, 0,
    0, 0, -3, 0, -6, 0, 0, -9,
    0, -6, 0, -9, -6, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, -6,
    0, 0, -3, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, -20, 0, -20, -3, 0, -26,
    0, -9, 0, -3, 0, -6, 0, 0,
    -3, 0, 0, -6, -6, 0, -3, 0
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
const lv_font_t ui_font_F1B18 = {
#else
lv_font_t ui_font_F1B18 = {
#endif
    .get_glyph_dsc = lv_font_get_glyph_dsc_fmt_txt,    /*Function pointer to get glyph's data*/
    .get_glyph_bitmap = lv_font_get_bitmap_fmt_txt,    /*Function pointer to get glyph's bitmap*/
    .line_height = 18,          /*The maximum line height required by the font*/
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



#endif /*#if UI_FONT_F1B18*/

