/*******************************************************************************
 * Size: 8 px
 * Bpp: 4
 * Opts: --bpp 4 --size 8 --font F:/ESP32/squareline/assets/SFPRODISPLAYREGULAR.OTF -o F:/ESP32/squareline/assets\ui_font_DISPLAYR8.c --format lvgl -r 0x20-0x7f --no-compress --no-prefilter
 ******************************************************************************/

#include "../ui.h"

#ifndef UI_FONT_DISPLAYR8
#define UI_FONT_DISPLAYR8 1
#endif

#if UI_FONT_DISPLAYR8

/*-----------------
 *    BITMAPS
 *----------------*/

/*Store the image of the glyphs*/
static LV_ATTRIBUTE_LARGE_CONST const uint8_t glyph_bitmap[] = {
    /* U+0020 " " */

    /* U+0021 "!" */
    0x46, 0x46, 0x46, 0x23, 0x23,

    /* U+0022 "\"" */
    0x72, 0x96, 0x29,

    /* U+0023 "#" */
    0x6, 0x28, 0x5, 0xc8, 0xc6, 0x8, 0x8, 0x8,
    0xc9, 0xb3, 0x44, 0x61, 0x0,

    /* U+0024 "$" */
    0x0, 0x40, 0x1, 0x9c, 0x90, 0x55, 0x83, 0x11,
    0x9c, 0x30, 0x0, 0x89, 0x45, 0x68, 0x73, 0x4,
    0xc3, 0x0,

    /* U+0025 "%" */
    0x78, 0x50, 0x91, 0x57, 0x38, 0x20, 0x0, 0x67,
    0x82, 0x4, 0x69, 0x9, 0x28, 0x5, 0x74,

    /* U+0026 "&" */
    0x9, 0x87, 0x0, 0x7, 0x6, 0x0, 0x39, 0x91,
    0xa0, 0x91, 0x1a, 0x90, 0x38, 0x89, 0xb1,

    /* U+0027 "'" */
    0x72, 0x62,

    /* U+0028 "(" */
    0x6, 0x20, 0xa0, 0x28, 0x2, 0x80, 0xa, 0x0,
    0x62,

    /* U+0029 ")" */
    0x71, 0x28, 0xb, 0xb, 0x28, 0x71,

    /* U+002A "*" */
    0x14, 0x31, 0x2d, 0xc1, 0x26, 0x51,

    /* U+002B "+" */
    0x0, 0x0, 0x0, 0x9, 0x0, 0x59, 0xd9, 0x30,
    0x9, 0x0, 0x0, 0x90, 0x0,

    /* U+002C "," */
    0x54, 0x80,

    /* U+002D "-" */
    0x59, 0x90,

    /* U+002E "." */
    0x23,

    /* U+002F "/" */
    0x2, 0x60, 0x71, 0x9, 0x2, 0x60, 0x71, 0x9,
    0x0,

    /* U+0030 "0" */
    0xa, 0x99, 0x7, 0x50, 0x75, 0x92, 0x4, 0x77,
    0x50, 0x75, 0x1a, 0x99, 0x0,

    /* U+0031 "1" */
    0x2a, 0x94, 0x29, 0x1, 0x90, 0x19, 0x1, 0x90,

    /* U+0032 "2" */
    0x29, 0x98, 0x4, 0x20, 0xb0, 0x0, 0x56, 0x0,
    0x66, 0x0, 0x6d, 0x99, 0x10,

    /* U+0033 "3" */
    0x19, 0x98, 0x2, 0x10, 0xb0, 0x3, 0xb8, 0x2,
    0x0, 0x83, 0x29, 0x99, 0x0,

    /* U+0034 "4" */
    0x0, 0x9b, 0x0, 0x64, 0xa0, 0x37, 0xa, 0x8,
    0x99, 0xd5, 0x0, 0xa, 0x0,

    /* U+0035 "5" */
    0x3c, 0x99, 0x5, 0xaa, 0x70, 0x23, 0x8, 0x44,
    0x30, 0x75, 0x19, 0xa9, 0x0,

    /* U+0036 "6" */
    0xa, 0x99, 0x17, 0x9a, 0x80, 0x97, 0x7, 0x57,
    0x60, 0x66, 0xa, 0xaa, 0x0,

    /* U+0037 "7" */
    0x69, 0x9e, 0x0, 0x3, 0x80, 0x0, 0xa0, 0x0,
    0x56, 0x0, 0xa, 0x0, 0x0,

    /* U+0038 "8" */
    0x19, 0x99, 0x5, 0x60, 0xa1, 0x1c, 0xba, 0x8,
    0x30, 0x75, 0x39, 0x99, 0x10,

    /* U+0039 "9" */
    0x3a, 0x98, 0xa, 0x20, 0x93, 0x29, 0x99, 0x64,
    0x20, 0x83, 0x1a, 0x98, 0x0,

    /* U+003A ":" */
    0x23, 0x0, 0x0, 0x23,

    /* U+003B ";" */
    0x23, 0x0, 0x0, 0x54, 0x80,

    /* U+003C "<" */
    0x0, 0x1, 0x0, 0x7, 0x90, 0x2a, 0x30, 0x0,
    0x88, 0x10, 0x0, 0x19, 0x10,

    /* U+003D "=" */
    0x48, 0x88, 0x24, 0x99, 0x93,

    /* U+003E ">" */
    0x10, 0x0, 0x1, 0xa5, 0x0, 0x0, 0x4a, 0x10,
    0x29, 0x70, 0x38, 0x10, 0x0,

    /* U+003F "?" */
    0x49, 0xa3, 0x40, 0x47, 0x4, 0x80, 0x3, 0x0,
    0x5, 0x0,

    /* U+0040 "@" */
    0x4, 0x87, 0x77, 0x3, 0x67, 0x6b, 0x17, 0x80,
    0x90, 0xb0, 0x87, 0x15, 0x87, 0x82, 0x19, 0x0,
    0x0, 0x0, 0x17, 0x77, 0x0,

    /* U+0041 "A" */
    0x1, 0xe1, 0x0, 0x76, 0x70, 0xb, 0xb, 0x4,
    0xc8, 0xc5, 0xa1, 0x1, 0xb0,

    /* U+0042 "B" */
    0x7b, 0x9a, 0x7, 0x30, 0x82, 0x7a, 0xab, 0x7,
    0x30, 0x47, 0x7b, 0x9a, 0x30,

    /* U+0043 "C" */
    0x9, 0xa9, 0x60, 0x76, 0x0, 0x70, 0xa2, 0x0,
    0x0, 0x76, 0x0, 0x50, 0x9, 0xa9, 0x60,

    /* U+0044 "D" */
    0x7b, 0xab, 0x30, 0x73, 0x0, 0xb0, 0x73, 0x0,
    0xa1, 0x73, 0x0, 0xb0, 0x7b, 0xab, 0x30,

    /* U+0045 "E" */
    0x7b, 0x99, 0x7, 0x30, 0x0, 0x7b, 0x98, 0x7,
    0x30, 0x0, 0x7b, 0x99, 0x0,

    /* U+0046 "F" */
    0x7b, 0x99, 0x73, 0x0, 0x7b, 0x97, 0x73, 0x0,
    0x73, 0x0,

    /* U+0047 "G" */
    0x9, 0xb9, 0x60, 0x76, 0x0, 0x50, 0xa2, 0x9,
    0xa3, 0x76, 0x0, 0xa2, 0x9, 0xab, 0x70,

    /* U+0048 "H" */
    0x73, 0x0, 0xa0, 0x73, 0x0, 0xa0, 0x7b, 0x99,
    0xd0, 0x73, 0x0, 0xa0, 0x73, 0x0, 0xa0,

    /* U+0049 "I" */
    0x73, 0x73, 0x73, 0x73, 0x73,

    /* U+004A "J" */
    0x0, 0x46, 0x0, 0x46, 0x0, 0x46, 0x40, 0x56,
    0x5a, 0xa1,

    /* U+004B "K" */
    0x73, 0xa, 0x37, 0x4a, 0x20, 0x7c, 0xa0, 0x7,
    0x46, 0x80, 0x73, 0x7, 0x60,

    /* U+004C "L" */
    0x73, 0x0, 0x73, 0x0, 0x73, 0x0, 0x73, 0x0,
    0x7b, 0x99,

    /* U+004D "M" */
    0x79, 0x0, 0xe, 0x17, 0xc1, 0x6, 0xc1, 0x75,
    0x80, 0xa8, 0x17, 0x39, 0x65, 0x81, 0x73, 0x3d,
    0x8, 0x10,

    /* U+004E "N" */
    0x79, 0x0, 0xa0, 0x7a, 0x60, 0xa0, 0x74, 0x93,
    0xa0, 0x73, 0xa, 0xb0, 0x73, 0x1, 0xe0,

    /* U+004F "O" */
    0x9, 0xaa, 0x80, 0x75, 0x0, 0x84, 0xa1, 0x0,
    0x37, 0x75, 0x0, 0x74, 0x9, 0xaa, 0x80,

    /* U+0050 "P" */
    0x7b, 0x99, 0x7, 0x30, 0x84, 0x7b, 0x97, 0x7,
    0x30, 0x0, 0x73, 0x0, 0x0,

    /* U+0051 "Q" */
    0x9, 0xab, 0x80, 0x75, 0x0, 0x84, 0xa1, 0x0,
    0x47, 0x75, 0x7, 0x84, 0x9, 0xac, 0xb0, 0x0,
    0x0, 0x50,

    /* U+0052 "R" */
    0x7b, 0x9a, 0x17, 0x30, 0x65, 0x7b, 0xaa, 0x7,
    0x31, 0xb0, 0x73, 0x7, 0x50,

    /* U+0053 "S" */
    0x2a, 0x99, 0x17, 0x50, 0x32, 0x6, 0x87, 0x4,
    0x10, 0x66, 0x3a, 0x9a, 0x10,

    /* U+0054 "T" */
    0x7a, 0xe9, 0x40, 0xa, 0x0, 0x0, 0xa0, 0x0,
    0xa, 0x0, 0x0, 0xa0, 0x0,

    /* U+0055 "U" */
    0x73, 0x0, 0xa0, 0x73, 0x0, 0xa0, 0x73, 0x0,
    0xa0, 0x66, 0x0, 0xc0, 0xa, 0xab, 0x50,

    /* U+0056 "V" */
    0xa1, 0x0, 0xa4, 0x60, 0x65, 0xb, 0xa, 0x0,
    0x76, 0x70, 0x1, 0xe1, 0x0,

    /* U+0057 "W" */
    0xa0, 0xc, 0x30, 0xa1, 0x55, 0x17, 0x70, 0xa0,
    0x19, 0x61, 0x93, 0x70, 0xa, 0x90, 0x6a, 0x20,
    0x6, 0x80, 0x2d, 0x0,

    /* U+0058 "X" */
    0x66, 0x4, 0x80, 0x94, 0xa0, 0x1, 0xf2, 0x0,
    0xa5, 0xa0, 0x75, 0x5, 0x70,

    /* U+0059 "Y" */
    0x84, 0x5, 0x70, 0xb2, 0xa0, 0x2, 0xd1, 0x0,
    0xb, 0x0, 0x0, 0xb0, 0x0,

    /* U+005A "Z" */
    0x49, 0x9d, 0x60, 0x2, 0x90, 0x1, 0xa0, 0x0,
    0xa1, 0x0, 0x7c, 0x99, 0x50,

    /* U+005B "[" */
    0x2b, 0x42, 0x70, 0x27, 0x2, 0x70, 0x27, 0x2,
    0xb3,

    /* U+005C "\\" */
    0x90, 0x7, 0x10, 0x26, 0x0, 0x90, 0x7, 0x10,
    0x26,

    /* U+005D "]" */
    0x7b, 0xa, 0xa, 0xa, 0xa, 0x7b,

    /* U+005E "^" */
    0x5, 0x10, 0x1a, 0x80, 0x82, 0x91,

    /* U+005F "_" */
    0x17, 0x77, 0x30,

    /* U+0060 "`" */
    0x55,

    /* U+0061 "a" */
    0x39, 0x93, 0x28, 0x89, 0x91, 0x39, 0x49, 0x89,

    /* U+0062 "b" */
    0x82, 0x0, 0x8, 0x9a, 0x80, 0x85, 0x9, 0x8,
    0x50, 0x90, 0x89, 0xa8, 0x0,

    /* U+0063 "c" */
    0x3b, 0x94, 0xa1, 0x3, 0xa1, 0x3, 0x3b, 0x94,

    /* U+0064 "d" */
    0x0, 0xa, 0x2b, 0x9c, 0x91, 0xd, 0x91, 0xd,
    0x2b, 0x9c,

    /* U+0065 "e" */
    0x29, 0x84, 0x98, 0x89, 0x92, 0x4, 0x2b, 0x94,

    /* U+0066 "f" */
    0x3a, 0x1a, 0xb1, 0x55, 0x5, 0x50, 0x55, 0x0,

    /* U+0067 "g" */
    0x3a, 0x8c, 0x91, 0xd, 0x91, 0xd, 0x3b, 0x9c,
    0x38, 0x86,

    /* U+0068 "h" */
    0x82, 0x0, 0x89, 0xa6, 0x83, 0xb, 0x82, 0xa,
    0x82, 0xa,

    /* U+0069 "i" */
    0x40, 0x82, 0x82, 0x82, 0x82,

    /* U+006A "j" */
    0x4, 0x0, 0x82, 0x8, 0x20, 0x82, 0x8, 0x22,
    0xa0,

    /* U+006B "k" */
    0x82, 0x0, 0x82, 0x84, 0x8b, 0x50, 0x87, 0x90,
    0x82, 0x56,

    /* U+006C "l" */
    0x82, 0x82, 0x82, 0x82, 0x82,

    /* U+006D "m" */
    0x89, 0xb7, 0x98, 0x82, 0x29, 0xb, 0x81, 0x18,
    0xa, 0x81, 0x18, 0xa,

    /* U+006E "n" */
    0x89, 0xa5, 0x83, 0xb, 0x81, 0xa, 0x81, 0xa,

    /* U+006F "o" */
    0x3b, 0xa5, 0xa1, 0xc, 0xa1, 0xc, 0x3b, 0xa5,

    /* U+0070 "p" */
    0x89, 0xa7, 0x8, 0x40, 0xa0, 0x84, 0xa, 0x8,
    0x9a, 0x70, 0x81, 0x0, 0x0,

    /* U+0071 "q" */
    0x3b, 0x9c, 0x91, 0xd, 0x91, 0xd, 0x3b, 0x9c,
    0x0, 0xa,

    /* U+0072 "r" */
    0x89, 0x38, 0x20, 0x81, 0x8, 0x10,

    /* U+0073 "s" */
    0x49, 0x91, 0x67, 0x20, 0x12, 0x94, 0x58, 0x92,

    /* U+0074 "t" */
    0x55, 0xa, 0xb1, 0x55, 0x5, 0x50, 0x2b, 0x10,

    /* U+0075 "u" */
    0x91, 0xa, 0x91, 0xa, 0x82, 0xb, 0x3a, 0x8b,

    /* U+0076 "v" */
    0xa0, 0x19, 0x55, 0x73, 0x9, 0xa0, 0x9, 0x70,

    /* U+0077 "w" */
    0xa0, 0x95, 0x27, 0x72, 0x98, 0x62, 0x29, 0x68,
    0x90, 0xd, 0x15, 0x90,

    /* U+0078 "x" */
    0x73, 0x74, 0xa, 0x80, 0xa, 0x90, 0x83, 0x74,

    /* U+0079 "y" */
    0xa0, 0x19, 0x45, 0x72, 0x9, 0xa0, 0x8, 0x50,
    0x49, 0x0,

    /* U+007A "z" */
    0x58, 0xc4, 0x2, 0x80, 0xa, 0x0, 0x8a, 0x83,

    /* U+007B "{" */
    0xa, 0x41, 0x90, 0xc3, 0x2, 0x80, 0x9, 0x0,
    0x84,

    /* U+007C "|" */
    0x99, 0x99, 0x99,

    /* U+007D "}" */
    0x86, 0x0, 0xa0, 0x9, 0x60, 0xa0, 0x9, 0x8,
    0x40,

    /* U+007E "~" */
    0x2a, 0x52, 0x23, 0x17, 0x91
};


/*---------------------
 *  GLYPH DESCRIPTION
 *--------------------*/

static const lv_font_fmt_txt_glyph_dsc_t glyph_dsc[] = {
    {.bitmap_index = 0, .adv_w = 0, .box_w = 0, .box_h = 0, .ofs_x = 0, .ofs_y = 0} /* id = 0 reserved */,
    {.bitmap_index = 0, .adv_w = 26, .box_w = 0, .box_h = 0, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 0, .adv_w = 34, .box_w = 2, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 5, .adv_w = 50, .box_w = 3, .box_h = 2, .ofs_x = 0, .ofs_y = 3},
    {.bitmap_index = 8, .adv_w = 77, .box_w = 5, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 21, .adv_w = 77, .box_w = 5, .box_h = 7, .ofs_x = 0, .ofs_y = -1},
    {.bitmap_index = 39, .adv_w = 94, .box_w = 6, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 54, .adv_w = 86, .box_w = 6, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 69, .adv_w = 27, .box_w = 2, .box_h = 2, .ofs_x = 0, .ofs_y = 3},
    {.bitmap_index = 71, .adv_w = 41, .box_w = 3, .box_h = 6, .ofs_x = 0, .ofs_y = -1},
    {.bitmap_index = 80, .adv_w = 41, .box_w = 2, .box_h = 6, .ofs_x = 0, .ofs_y = -1},
    {.bitmap_index = 86, .adv_w = 62, .box_w = 4, .box_h = 3, .ofs_x = 0, .ofs_y = 3},
    {.bitmap_index = 92, .adv_w = 77, .box_w = 5, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 105, .adv_w = 33, .box_w = 2, .box_h = 2, .ofs_x = 0, .ofs_y = -1},
    {.bitmap_index = 107, .adv_w = 55, .box_w = 3, .box_h = 1, .ofs_x = 0, .ofs_y = 2},
    {.bitmap_index = 109, .adv_w = 33, .box_w = 2, .box_h = 1, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 110, .adv_w = 41, .box_w = 3, .box_h = 6, .ofs_x = 0, .ofs_y = -1},
    {.bitmap_index = 119, .adv_w = 78, .box_w = 5, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 132, .adv_w = 57, .box_w = 3, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 140, .adv_w = 72, .box_w = 5, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 153, .adv_w = 76, .box_w = 5, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 166, .adv_w = 77, .box_w = 5, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 179, .adv_w = 75, .box_w = 5, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 192, .adv_w = 77, .box_w = 5, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 205, .adv_w = 70, .box_w = 5, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 218, .adv_w = 77, .box_w = 5, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 231, .adv_w = 77, .box_w = 5, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 244, .adv_w = 33, .box_w = 2, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 248, .adv_w = 33, .box_w = 2, .box_h = 5, .ofs_x = 0, .ofs_y = -1},
    {.bitmap_index = 253, .adv_w = 77, .box_w = 5, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 266, .adv_w = 77, .box_w = 5, .box_h = 2, .ofs_x = 0, .ofs_y = 1},
    {.bitmap_index = 271, .adv_w = 77, .box_w = 5, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 284, .adv_w = 63, .box_w = 4, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 294, .adv_w = 112, .box_w = 7, .box_h = 6, .ofs_x = 0, .ofs_y = -1},
    {.bitmap_index = 315, .adv_w = 81, .box_w = 5, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 328, .adv_w = 77, .box_w = 5, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 341, .adv_w = 88, .box_w = 6, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 356, .adv_w = 87, .box_w = 6, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 371, .adv_w = 71, .box_w = 5, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 384, .adv_w = 68, .box_w = 4, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 394, .adv_w = 90, .box_w = 6, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 409, .adv_w = 90, .box_w = 6, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 424, .adv_w = 29, .box_w = 2, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 429, .adv_w = 63, .box_w = 4, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 439, .adv_w = 79, .box_w = 5, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 452, .adv_w = 67, .box_w = 4, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 462, .adv_w = 106, .box_w = 7, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 480, .adv_w = 90, .box_w = 6, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 495, .adv_w = 94, .box_w = 6, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 510, .adv_w = 74, .box_w = 5, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 523, .adv_w = 94, .box_w = 6, .box_h = 6, .ofs_x = 0, .ofs_y = -1},
    {.bitmap_index = 541, .adv_w = 77, .box_w = 5, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 554, .adv_w = 76, .box_w = 5, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 567, .adv_w = 74, .box_w = 5, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 580, .adv_w = 89, .box_w = 6, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 595, .adv_w = 81, .box_w = 5, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 608, .adv_w = 118, .box_w = 8, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 628, .adv_w = 81, .box_w = 5, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 641, .adv_w = 78, .box_w = 5, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 654, .adv_w = 79, .box_w = 5, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 667, .adv_w = 41, .box_w = 3, .box_h = 6, .ofs_x = 0, .ofs_y = -1},
    {.bitmap_index = 676, .adv_w = 41, .box_w = 3, .box_h = 6, .ofs_x = 0, .ofs_y = -1},
    {.bitmap_index = 685, .adv_w = 41, .box_w = 2, .box_h = 6, .ofs_x = 0, .ofs_y = -1},
    {.bitmap_index = 691, .adv_w = 56, .box_w = 4, .box_h = 3, .ofs_x = 0, .ofs_y = 3},
    {.bitmap_index = 697, .adv_w = 52, .box_w = 5, .box_h = 1, .ofs_x = -1, .ofs_y = -1},
    {.bitmap_index = 700, .adv_w = 63, .box_w = 2, .box_h = 1, .ofs_x = 1, .ofs_y = 5},
    {.bitmap_index = 701, .adv_w = 64, .box_w = 4, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 709, .adv_w = 71, .box_w = 5, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 722, .adv_w = 64, .box_w = 4, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 730, .adv_w = 71, .box_w = 4, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 740, .adv_w = 66, .box_w = 4, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 748, .adv_w = 39, .box_w = 3, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 756, .adv_w = 70, .box_w = 4, .box_h = 5, .ofs_x = 0, .ofs_y = -1},
    {.bitmap_index = 766, .adv_w = 69, .box_w = 4, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 776, .adv_w = 26, .box_w = 2, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 781, .adv_w = 26, .box_w = 3, .box_h = 6, .ofs_x = -1, .ofs_y = -1},
    {.bitmap_index = 790, .adv_w = 62, .box_w = 4, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 800, .adv_w = 26, .box_w = 2, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 805, .adv_w = 103, .box_w = 6, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 817, .adv_w = 67, .box_w = 4, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 825, .adv_w = 68, .box_w = 4, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 833, .adv_w = 70, .box_w = 5, .box_h = 5, .ofs_x = 0, .ofs_y = -1},
    {.bitmap_index = 846, .adv_w = 70, .box_w = 4, .box_h = 5, .ofs_x = 0, .ofs_y = -1},
    {.bitmap_index = 856, .adv_w = 39, .box_w = 3, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 862, .adv_w = 60, .box_w = 4, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 870, .adv_w = 39, .box_w = 3, .box_h = 5, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 878, .adv_w = 67, .box_w = 4, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 886, .adv_w = 62, .box_w = 4, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 894, .adv_w = 92, .box_w = 6, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 906, .adv_w = 60, .box_w = 4, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 914, .adv_w = 62, .box_w = 4, .box_h = 5, .ofs_x = 0, .ofs_y = -1},
    {.bitmap_index = 924, .adv_w = 60, .box_w = 4, .box_h = 4, .ofs_x = 0, .ofs_y = 0},
    {.bitmap_index = 932, .adv_w = 41, .box_w = 3, .box_h = 6, .ofs_x = 0, .ofs_y = -1},
    {.bitmap_index = 941, .adv_w = 41, .box_w = 1, .box_h = 6, .ofs_x = 1, .ofs_y = -1},
    {.bitmap_index = 944, .adv_w = 41, .box_w = 3, .box_h = 6, .ofs_x = 0, .ofs_y = -1},
    {.bitmap_index = 953, .adv_w = 77, .box_w = 5, .box_h = 2, .ofs_x = 0, .ofs_y = 2}
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
    .kern_dsc = NULL,
    .kern_scale = 0,
    .cmap_num = 1,
    .bpp = 4,
    .kern_classes = 0,
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
const lv_font_t ui_font_DISPLAYR8 = {
#else
lv_font_t ui_font_DISPLAYR8 = {
#endif
    .get_glyph_dsc = lv_font_get_glyph_dsc_fmt_txt,    /*Function pointer to get glyph's data*/
    .get_glyph_bitmap = lv_font_get_bitmap_fmt_txt,    /*Function pointer to get glyph's bitmap*/
    .line_height = 7,          /*The maximum line height required by the font*/
    .base_line = 1,             /*Baseline measured from the bottom of the line*/
#if !(LVGL_VERSION_MAJOR == 6 && LVGL_VERSION_MINOR == 0)
    .subpx = LV_FONT_SUBPX_NONE,
#endif
#if LV_VERSION_CHECK(7, 4, 0) || LVGL_VERSION_MAJOR >= 8
    .underline_position = -1,
    .underline_thickness = 0,
#endif
    .dsc = &font_dsc           /*The custom font data. Will be accessed by `get_glyph_bitmap/dsc` */
};



#endif /*#if UI_FONT_DISPLAYR8*/

